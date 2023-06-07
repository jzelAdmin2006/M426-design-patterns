from league_table.table_row import TableRow

if __name__ == "__main__":
    liverpool = TableRow("Liverpool", 0, 0, 0, 0, 0, 0)
    arsenal = TableRow("Arsenal London", 2, 0, 1, 0, 0, 3)
    print(
        f"{'Team':20s} {'#':>2s} {'W':>2s} {'D':>2s} {'T':>2s} " 
        f"{'+':>2s} {'-':>2s} {'=':>2s} {'P':>2s}"
    )
    print(liverpool)
    print(arsenal)
