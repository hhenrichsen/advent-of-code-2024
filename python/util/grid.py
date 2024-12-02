from typing import Callable, Generic, List, Set, Tuple, TypeVar, Union


A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")

AGrid = List[List[A]]
BGrid = List[List[B]]
CGrid = List[List[C]]
Coord = Tuple[int, int]


def _curry_filter(filter):
    return (
        lambda x: all([f(x) for f in filter]) if isinstance(filter, list) else filter(x)
    )


class Grid(Generic[A]):
    class GridItem(Generic[A]):
        def __init__(self, parent: "Grid[A]", data: A, x: int, y: int):
            self.parent = parent
            self.data = data
            self.x = x
            self.y = y

        def __repr__(self):
            return f"GridItem({repr(self.data)}, {self.x}, {self.y})"

        def __str__(self):
            return f"GridItem({repr(self.data)}, {self.x}, {self.y})"

        def __eq__(self, other):
            return (
                isinstance(other, Grid.GridItem)
                and self.parent == other.parent
                and self.data == other.data
                and self.x == other.x
                and self.y == other.y
            )

        def __hash__(self):
            return hash((self.data, self.x, self.y))

        def clone(self, parent=None, item=None, x=None, y=None):
            return Grid.GridItem(
                parent if parent is not None else self.parent,
                item if item is not None else self.data,
                x if x is not None else self.x,
                y if y is not None else self.y,
            )

        def neighbors(
            self,
            horizontal: bool = True,
            vertical: bool = True,
            diagonal: bool = False,
        ) -> List["Grid.GridItem[A]"]:
            """
            Get a list of valid neighbor coordinates
            """
            res = []
            sx, sy = self.parent.size()

            if vertical:
                if self.y - 1 >= 0:
                    res.append(self.parent[self.x, self.y - 1])

            if horizontal:
                if self.y < sy and self.x - 1 >= 0:
                    res.append(self.parent[self.x - 1, self.y])
                if self.y < sy and self.x + 1 < sx:
                    res.append(self.parent[self.x + 1, self.y])

            if vertical:
                if self.y + 1 < sy and self.x < sx:
                    res.append(self.parent[self.x, self.y + 1])

            if diagonal:
                if self.y + 1 < sy and self.x + 1 < sx:
                    res.append(self.parent[self.x + 1, self.y + 1])
                if self.y + 1 < sy and self.x - 1 >= 0:
                    res.append(self.parent[self.x - 1, self.y + 1])
                if self.y - 1 >= 0 and self.x + 1 < sx:
                    res.append(self.parent[self.x + 1, self.y - 1])
                if self.y - 1 >= 0 and self.x - 1 >= 0:
                    res.append(self.parent[self.x - 1, self.y - 1])
            return res

        def neighbor_data(
            self,
            horizontal: bool = True,
            vertical: bool = True,
            diagonal: bool = False,
        ) -> List[A]:
            """
            Get the data from neighboring items.
            """
            return self.neighbors(horizontal, vertical, diagonal).map(
                lambda item: item.item
            )

        def filter_neighbors(
            self,
            filter: Union[
                Callable[["Grid.GridItem[A]"], bool],
                List[Callable[["Grid.GridItem[A]"], bool]],
            ],
            horizontal: bool = True,
            vertical: bool = True,
            diagonal: bool = False,
        ) -> List["Grid.GridItem[A]"]:
            """
            Get the neighboring items that match a given filter, based on the
            full grid item. Returns the full grid item.

            Accepts a single filter or a list of filters.

            Example:
            ```
            grid.filter_neighbors(lambda a: a.data.isnumeric() and a.data != ".")
            ```
            """
            results = []
            neighbors = self.neighbors(horizontal, vertical, diagonal)
            _filter = _curry_filter(filter)
            for neighbor in neighbors:
                if _filter(neighbor):
                    results.append(neighbor)
            return results

        def filter_neighbor_data(
            self,
            filter: Union[Callable[[A], bool], List[Callable[[A], bool]]],
            horizontal: bool = True,
            vertical: bool = True,
            diagonal: bool = False,
        ) -> List["Grid.GridItem[A]"]:
            """
            Get the neighboring items that match a given filter, based on the
            data in the grid item. Returns the full grid item.

            Accepts a single filter or a list of filters.

            Examples:
            ```
            grid.filter_neighbor_data(lambda a: a.isnumeric() and a != ".")
            grid.filter_neighbor_data([str.isnumeric, ne(".")])
            ```
            """
            results = []
            neighbors = self.neighbors(horizontal, vertical, diagonal)
            _filter = _curry_filter(filter)
            for neighbor in neighbors:
                if _filter(neighbor()):
                    results.append(neighbor)
            return results

        def count_neighbors(
            self,
            filter: Union[
                Callable[["Grid.GridItem[A]"], bool],
                List[Callable[["Grid.GridItem[A]"], bool]],
            ],
            horizontal: bool = True,
            vertical: bool = True,
            diagonal: bool = False,
        ) -> int:
            """
            Count the number of neighboring items that match a given filter,
            based on the full grid item.

            Accepts a single filter or a list of filters.

            Example:
            ```
            grid.count_neighbors(lambda a: a.data.isnumeric() and a.data != ".")
            ```
            """
            count = 0
            neighbors = self.neighbors(horizontal, vertical, diagonal)
            _filter = _curry_filter(filter)
            for neighbor in neighbors:
                if _filter(neighbor):
                    count += 1
            return count

        def count_neighbor_data(
            self,
            filter: Union[Callable[[A], bool], List[Callable[[A], bool]]],
            horizontal: bool = True,
            vertical: bool = True,
            diagonal: bool = False,
        ) -> int:
            """
            Count the number of neighboring items that match a given filter,
            based on the data in the grid item.

            Accepts a single filter or a list of filters.

            Examples:
            ```
            grid.count_neighbor_data(lambda a: a.isnumeric() and a != ".")
            grid.count_neighbor_data([str.isnumeric, ne(".")])
            ```
            """
            count = 0
            neighbors = self.neighbors(horizontal, vertical, diagonal)
            _filter = _curry_filter(filter)
            for neighbor in neighbors:
                if _filter(neighbor()):
                    count += 1
            return count

        def __call__(self) -> A:
            return self.data

    def __init__(self, data: List[List[A]]):
        self.__data = []
        for y, row in enumerate(data):
            self.__data.append([])
            for x, item in enumerate(row):
                self.__data[-1].append(Grid.GridItem(self, item, x, y))

    @staticmethod
    def read(
        filename: str,
        item_parser: Callable[[A, int, int], B] = lambda c, x, y: c,
        line_splitter: Callable[[List[str]], List[A]] = lambda line: list(line),
    ) -> "Grid[B]":
        """
        Parses a text file into a grid using the given item parser. Defaults to
        splitting lines character-wise.
        """
        with open(filename) as f:
            inp = list(map(str.strip, f.readlines()))
            data = []
            for y, line in enumerate(map(line_splitter, inp)):
                data.append([])
                for x, item in enumerate(line):
                    data[-1].append(item_parser(item, x, y))
            return Grid(data)

    def filter(self, filter: Callable[[GridItem[A]], bool]) -> List[GridItem[A]]:
        """
        Finds coordinates where a given filter returns true in a grid.
        """
        results = []
        for row in self.__data:
            for item in row:
                if filter(item):
                    results.append(item)
        return results

    def map(self, map: Callable[[GridItem[A]], B]) -> "Grid[B]":
        """
        Transforms each item in a grid to something else.
        """
        grid = Grid()
        for y, row in enumerate(grid):
            grid.__data.append([])
            for x, item in enumerate(row):
                grid.__data[-1].append(Grid.GridItem(grid, map(item), x, y))
        return grid

    def flood(
        self,
        start: Union[Tuple[int, int], GridItem[A]],
        is_valid: Callable[[GridItem[A]], bool],
        get_next: Callable[
            [GridItem[A]], List[GridItem[A]]
        ] = lambda item: item.neighbors(),
    ) -> Tuple[int, Set[GridItem[A]]]:
        """
        Floods a grid starting at the given coordinates, returning the number of
        valid items and a set of valid items.
        """
        count = 0
        to_visit = [start if isinstance(start, tuple) else (start.x, start.y)]
        valid = set()
        visited = set()
        while len(to_visit) > 0:
            check = to_visit.pop(0)
            visited.add(check)
            item = self[*check]
            if is_valid(item):
                count += 1
                valid.add(check)
                neighbors = get_next(item)
                n = [neighbor for neighbor in neighbors if neighbor not in visited]
                to_visit.extend(n)
                visited.update(n)
        return count, valid

    def __getitem__(self, key: Coord) -> GridItem[A]:
        """
        Index into the grid using a tuple (x, y).
        """
        return self.__data[key[1]][key[0]]

    def __len__(self) -> int:
        """
        Get the total number of items in the grid.

        Assumes that the grid is not jagged.
        """
        return len(self.__data) * len(self.__data[0]) if len(self.__data) > 0 else 0

    def size(self) -> Tuple[int, int]:
        """
        Get the size of the grid as a tuple (width, height).

        Assumes that the grid is not jagged.
        """
        return (len(self.__data[0]), len(self.__data))


def compare_x(a: Grid.GridItem[A], b: Grid.GridItem[B]) -> int:
    return a.x - b.x


def compare_y(a: Grid.GridItem[A], b: Grid.GridItem[B]) -> int:
    return a.y - b.y
