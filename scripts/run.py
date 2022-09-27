
from nile.core.account import Account

def run(nre):
    account = Account('PKEY1', nre.network)

    addr = nre.deploy_proxy(["contract", account.alias, '0'])

    account.send(addr, "increase_balance", calldata=['1'], max_fee=0)
    print(f"balance from v1: {nre.call(addr, 'get_balance')}")

    nre.upgrade_proxy([addr, "contract_v2", account.alias, '0'])
    print(f"balance from v2: {nre.call(addr, 'get_balance')}")

    account.send(addr, "reset_balance", calldata=[], max_fee=0)
    print(f"balance after reset from v2: {nre.call(addr, 'get_balance')}")
