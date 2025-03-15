from qiskit_ibm_provider import IBMProvider

# Load your saved IBM Quantum account
provider = IBMProvider()

# List available backends
print(provider.backends())
