def calculate_risk(service_name, error_rate):
    """Calculates if a service is safe to deploy."""
    print(f"--- Checking health for: {service_name} ---")
    
    if error_rate > 0.05:
        return "🔴 DANGER: High Error Rate. Block Deployment."
    return "🟢 SUCCESS: Low Error Rate. Safe to Deploy."

if __name__ == "__main__":
    # Simulate a check
    print(calculate_risk("PaymentGateway", 0.02))
