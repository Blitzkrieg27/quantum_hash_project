# quantum_hash/input_encoder.py

def encode_input_to_params(input_data: bytes, params: list) -> dict:
    """
    Maps input bytes cyclically to circuit parameters, scaled to [0, 2π].

    Args:
        input_data (bytes): Input byte array.
        params (list): List of circuit Parameters.

    Returns:
        dict: Mapping of parameters to float values.
    """
    param_dict = {}
    for i, param in enumerate(params):
        byte_val = input_data[i % len(input_data)]
        param_dict[param] = (byte_val / 255) * 2 * 3.14159  # 0 to 2π
    return param_dict
