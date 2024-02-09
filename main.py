def sum_of_products(series1, series2):
    if len(series1) != len(series2):
        return "Error: Lists must be the same length."
    result = sum(a * b for a, b in zip(series1, series2))

    return result

if __name__ == "__main__":
    try:
        series1 = list(map(int, input().split()))
        series2 = list(map(int, input().split()))
        result = sum_of_products(series1, series2)
        print(result)
    except ValueError:
        print("Error: Please enter valid integers.")
