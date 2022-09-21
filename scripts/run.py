
def run(nre):
    print('Testing deploy proxy:')

    addr = nre.deploy_proxy(["contract"])

    nre.invoke(addr, "increase_balance", params=['1'])
    print(f"balance: {nre.call(addr, 'get_balance')}")

    print('Testing upgrade proxy:')

    nre.upgrade_proxy([addr, "contract_v2"])

    print(f"balance: {nre.call(addr, 'get_balance')}")
    nre.invoke(addr, "reset_balance", override_abi='artifacts/abis/contract_v2.json')
    print(f"balance: {nre.call(addr, 'get_balance')}")
    
    print('Done test')
