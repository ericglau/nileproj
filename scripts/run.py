
import asyncio

def run(nre):
    print('from run')

    # classhash = nre.declare("contract", alias="contract")
    # print(classhash)

    nre.deploy_proxy(["contract"])




    # address, abi = nre.declare("contract", alias="my_contract")
    # print(abi, address)

    #print(f'result ${nre.greet(["1", "2"])}')

    # loop = asyncio.get_event_loop()
    # coroutine = nre.greet(["contract"])
    # loop.run_until_complete(coroutine)
    
    print('done')

    #nre = NileRuntimeEnvironment()
    #ret = nre.greet(["1", "2"])
    # ret is equal to 3