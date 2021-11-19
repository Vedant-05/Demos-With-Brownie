from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_Storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_Storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_Storage = SimpleStorage.deploy({"from": account})
    # act
    expected = 15
    simple_Storage.store(expected, {"from": account})
    # assert
    assert expected == simple_Storage.retrieve()
