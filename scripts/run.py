from time import sleep
from nile.core.account import Account

async def run(nre):
    print(f"before account")

    signer = "PKEY1"
    account = await Account(signer, nre.network)

    print(f"after account, before proxy")

    proxy = await nre.deploy_proxy(nre, signer, "contract", [account.address, 523])

    print(f"proxy {proxy}")

    await account.send(proxy, "increase_balance", calldata=['1'], watch_mode="track")
    print(f"balance from v1: {await nre.call(proxy, 'get_balance')}")
    print(f"bal2 from v1: {await nre.call(proxy, 'get_balance2')}")

    tx = await nre.upgrade_proxy(nre, signer, proxy, "contract_v2")
    # tx = await nre.upgrade_proxy(nre, signer, proxy, "contract_v2", call="increase_balance", args=[5])
    # tx = await nre.upgrade_proxy(nre, signer, proxy, "contract_v2", call="reset_balance")

    print(f"upgrade tx: {tx}")
    print(f"balance from v2: {await nre.call(proxy, 'get_balance')}")

    await account.send(proxy, "reset_balance", calldata=[], watch_mode="track")
    print(f"balance after reset from v2: {await nre.call(proxy, 'get_balance')}")
