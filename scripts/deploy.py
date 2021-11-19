from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()  # for deploying from ganache local serving account
    print(account)
    # account = accounts.load("learning")   for deploying from brownie accounts saved lists.
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])      for deploying  from .env and saving it in config
    # print(account)
    simple_Storage = SimpleStorage.deploy({"from": account})
    print(simple_Storage)
    stored_value = simple_Storage.retrieve()
    print(stored_value)
    transaction = simple_Storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_Storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "dvelopment":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
