#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "qiskit",
# ]
# ///
"""Encode and decode strings in quantum circuits using amplitude encoding.

References
----------
- https://qiskit.qotlabs.org/learning/courses/quantum-machine-learning/data-encoding#amplitude-encoding
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import qiskit
from qiskit import qpy


def get_power_of_two_exponent(string: str) -> int:
    """Return the smallest number n such that 2**n >= len(string)."""
    len_ = len(string)
    if len_ == 0:
        return 0
    return (len_ - 1).bit_length()


def subcommand_encode(args: argparse.Namespace) -> None:
    """Encode string into a quantum circuit."""
    n_qubits = get_power_of_two_exponent(args.string)

    nums = [ord(x) for x in args.string]
    nums += [0] * (2**n_qubits - len(nums))

    normalization_constant = np.sqrt(np.sum(np.square(nums)))
    desired_state = nums / normalization_constant

    circuit = qiskit.QuantumCircuit(n_qubits)
    circuit.initialize(desired_state)

    with args.circuit_path.open("wb") as fp:
        qpy.dump(circuit, fp)

    print("Key:", normalization_constant)


def subcommand_decode(args: argparse.Namespace) -> None:
    """Decode string from quantum circuit."""
    with args.circuit_path.open("rb") as fp:
        circuit = qpy.load(fp)[0]

    state = qiskit.quantum_info.Statevector(circuit)
    nums = state * args.key
    string = "".join(chr(int(x.real)) for x in nums)
    string.strip("\x00")

    print(string)


def main() -> None:
    """Parse command line and dispatch subcommand."""
    module_docstring_first_line = sys.modules[__name__].__doc__.partition("\n")[0]
    parser = argparse.ArgumentParser(description=module_docstring_first_line)
    subparsers = parser.add_subparsers(required=True)

    parser_encode = subparsers.add_parser(
        "encode", description=subcommand_encode.__doc__
    )
    parser_encode.set_defaults(subcommand=subcommand_encode)
    parser_encode.add_argument("string", type=str, help="String to encode.")
    parser_encode.add_argument(
        "circuit_path", type=Path, help="Path where the circuit shall be saved to."
    )

    parser_decode = subparsers.add_parser(
        "decode", description=subcommand_decode.__doc__
    )
    parser_decode.set_defaults(subcommand=subcommand_decode)
    parser_decode.add_argument(
        "circuit_path", type=Path, help="Path to the circuit file."
    )
    parser_decode.add_argument(
        "key", type=float, help="Normalization constant used during encoding."
    )

    args = parser.parse_args()
    args.subcommand(args)


if __name__ == "__main__":
    main()
