from qiskit_ibm_runtime import QiskitRuntimeService

# Save your IBM Quantum account
QiskitRuntimeService.save_account(
    token="51d843421456b6ef179496703907f6319cf555dc54444bfa3e35bf4ba5e3a36280a6a1cc36fe307bdefc7192b0d1e778ebb7180277c50a6976573382efb8644a", 
    overwrite=True, 
    channel="ibm_quantum"  # Explicitly specifying the channel
)

# Load the saved account
service = QiskitRuntimeService()
print("Qiskit Runtime Service initialized successfully!")