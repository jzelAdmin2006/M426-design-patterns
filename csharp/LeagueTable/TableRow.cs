namespace LeagueTable
{
    public class TableRow
    {
        public string TeamName { get; set; }
        public int Rank { get; set; }
        public int Wins { get; set; }
        public int Defeats { get; set; }
        public int Ties { get; set; }
        public int GoalsScored { get; set; }
        public int GoalsConceded { get; set; }
        public int GoalsDifference
        {
            get { return this.GoalsScored - this.GoalsConceded; }
        }
        public int Points
        {
            get { return this.Wins * 3 + this.Ties; }
        }

        private TableRow()
        {
            this.TeamName = string.Empty;
        }

        public override string ToString()
        {
            return $"{TeamName,20} {Rank,2} {Wins,2} {Defeats,2} {Ties,2} {GoalsScored,2} {GoalsConceded,2} {GoalsDifference,2} {Points,2}";
        }

        public class TableRowBuilder
        {
            private TableRow Row = new();

            public TableRowBuilder TeamName(string teamName) { Row.TeamName = teamName; return this; }
            public TableRowBuilder Rank(int rank) { Row.Rank = rank; return this; }
            public TableRowBuilder Wins(int wins) { Row.Wins = wins; return this; }
            public TableRowBuilder Defeats(int defeats) { Row.Defeats = defeats; return this; }
            public TableRowBuilder Ties(int ties) { Row.Ties = ties; return this; }
            public TableRowBuilder GoalsScored(int goalsScored) { Row.GoalsScored = goalsScored; return this; }
            public TableRowBuilder GoalsConceded(int goalsConceded) { Row.GoalsConceded = goalsConceded; return this; }

            public TableRow Build() { return Row; }
        }
    }
}
