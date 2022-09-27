// Declare this file as a StarkNet contract.
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin
from openzeppelin.upgrades.library import Proxy

// Define a storage variable.
@storage_var
func balance() -> (res: felt) {
}

// Increases the balance by the given amount.
@external
func increase_balance{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    amount: felt
) {
    let (res) = balance.read();
    balance.write(res + amount);
    return ();
}

// Returns the current balance.
@view
func get_balance{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}() -> (res: felt) {
    let (res) = balance.read();
    return (res,);
}

@external
func upgrade{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
}(new_implementation: felt) -> () {
    // Proxy.assert_only_admin(); TODO
    Proxy._set_implementation_hash(new_implementation);
    return ();
}