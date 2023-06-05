class AccountHolder:
    def GetAccountDetails():
        pass


def pay_out(recipient: AccountHolder, salary: float):
    target = recipient.get_account_details()
    print(f"Pay {salary:2f} to {recipient} at {target}")
