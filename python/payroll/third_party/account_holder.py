from typing import Protocol


class AccountHolder(Protocol):
    def get_account_details(self) -> str:
        raise NotImplementedError()
