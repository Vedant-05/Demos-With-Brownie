from brownie import SimpleStorage, config, accounts


def read_contract():
    simple_Storage = SimpleStorage[
        0
    ]  # -1 to get recently added transaction and 0 to get first transaction
    print(simple_Storage.retrieve())


def main():
    read_contract()
