from .account_holder import AccountHolder

def pay_out(recipient: AccountHolder, salary: float):
    target = recipient.get_account_details()
    print(f"Pay {salary:2f} to {recipient} at {target}")
