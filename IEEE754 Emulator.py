import struct
import sys

read_input = sys.stdin.read

# Helper functions for IEEE 754 float conversions
def hex_to_float(hex_value):
    """Converts a hexadecimal IEEE 754 representation to a Python float."""
    int_value = int(hex_value, 16)
    return struct.unpack('!f', struct.pack('!I', int_value))[0]

def float_to_hex(float_value):
    """Converts a Python float to a hexadecimal IEEE 754 representation."""
    int_value = struct.unpack('!I', struct.pack('!f', float_value))[0]
    return f"{int_value:08x}"

def extract_bits(value, start, length):
    """Extracts 'length' bits starting from 'start' from a 32-bit integer."""
    mask = (1 << length) - 1
    return (value >> start) & mask

# Read input
data = read_input().splitlines()
index = 0

T = int(data[index])  # Number of test cases
index += 1
results = []

for _ in range(T):
    # Initial value C[0]
    c0_hex = data[index]
    c0_value = int(c0_hex, 16)
    index += 1

    # Reading LUTs
    L = int(data[index])
    index += 1
    LUTs = []
    for _ in range(L):
        line = data[index].split()
        k = int(line[0])
        size = 1 << k  # 2^k
        LUTs.append([int(h, 16) for h in line[1:size + 1]])
        index += 1

    # Reading commands
    Q = int(data[index])
    index += 1
    values = [c0_value]

    for _ in range(Q):
        command = data[index].split()
        
        if command[0] == 'C':
            # Constant command: Store a constant value
            h = int(command[1], 16)
            values.append(h)
            
        elif command[0] == 'N':
            # NAND command: Bitwise NAND of values[i] and values[j]
            i, j = int(command[1]), int(command[2])
            if i < len(values) and j < len(values):
                nand_result = ~(values[i] & values[j]) & 0xFFFFFFFF
                values.append(nand_result)
            else:
                values.append(0)  # Out-of-bounds index handling
                
        elif command[0] == 'F':
            # FMA command: Fused Multiply-Add on floats
            i, j, k = int(command[1]), int(command[2]), int(command[3])
            if i < len(values) and j < len(values) and k < len(values):
                # Convert integers to IEEE 754 floats
                a = hex_to_float(f"{values[i]:08x}")
                b = hex_to_float(f"{values[j]:08x}")
                c = hex_to_float(f"{values[k]:08x}")

                # Check for special IEEE 754 values
                if any(val in [float('inf'), float('-inf'), float('nan')] for val in [a, b, c]):
                    fma_result = float('nan')
                else:
                    fma_result = a * b + c

                # Store as integer in hexadecimal format
                values.append(int(float_to_hex(fma_result), 16))
            else:
                values.append(0)  # Out-of-bounds index handling
                
        elif command[0] == 'L':
            # LUT command: Lookup in the LUT
            i, j, b = int(command[1]), int(command[2]), int(command[3])
            if i < len(LUTs):
                mask = extract_bits(values[0], j, b)
                if mask < len(LUTs[i]):
                    values.append(LUTs[i][mask])
                else:
                    values.append(0)  # Handle out-of-bounds index in LUT
            else:
                values.append(0)  # Handle out-of-bounds LUT index
                
        index += 1

    # Convert last command's result to hexadecimal for output
    final_value = values[-1]
    final_result_hex = f"{final_value:08x}"
    results.append(final_result_hex)

# Output results for all test cases
print("\n".join(results))
