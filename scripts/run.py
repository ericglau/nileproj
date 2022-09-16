
def run(nre):
    print('Testing deploy proxy:')

    addr = nre.deploy_proxy(["contract"])

    nre.invoke(addr, "increase_balance", params=['1'], abi='artifacts/abis/contract.json')
    print(f"balance: {nre.call(addr, 'get_balance', abi='artifacts/abis/contract.json')}")

    print('Testing upgrade proxy:')

    nre.upgrade_proxy([addr, "contract_v2"])

    print(f"balance: {nre.call(addr, 'get_balance', abi='artifacts/abis/contract_v2.json')}")
    nre.invoke(addr, "reset_balance", abi='artifacts/abis/contract_v2.json')
    print(f"balance: {nre.call(addr, 'get_balance', abi='artifacts/abis/contract_v2.json')}")
    
    print('Done test')
