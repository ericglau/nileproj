
def run(nre):
    addr = nre.deploy_proxy(["contract"])

    nre.invoke(addr, "increase_balance", params=['1'])
    print(f"balance from v1: {nre.call(addr, 'get_balance')}")

    nre.upgrade_proxy([addr, "contract_v2"])
    print(f"balance from v2: {nre.call(addr, 'get_balance')}")

    nre.invoke(addr, "reset_balance")
    print(f"balance after reset from v2: {nre.call(addr, 'get_balance')}")
