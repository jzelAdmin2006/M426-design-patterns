class TableRow:
    def __init__(
        self,
        name: str,
        rank: int,
        wins: int,
        defeats: int,
        ties: int,
        goals_scored: int,
        goals_conceded: int,
    ):
        self.name = name
        self.rank = rank
        self.wins = wins
        self.defeats = defeats
        self.ties = ties
        self.goals_scored = goals_scored
        self.goals_conceded = goals_conceded
        self.goals_difference = goals_scored - goals_conceded

    def points(self) -> int:
        return self.wins * 3 + self.ties

    def __str__(self) -> str:
        return (
            f"{self.name:20s} {self.rank:2d} {self.wins:2d} {self.defeats:2d}"
            + f" {self.ties:2d} {self.goals_scored:2d} {self.goals_conceded:2d}"
            + f" {self.goals_difference:2d} {self.points():2d}"
        )
