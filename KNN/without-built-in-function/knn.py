import math as mt

def main():
    data_points = [
        [40, 20, 'RED'],   # P1
        [50, 50, 'BLUE'],  # P2
        [60, 90, 'BLUE'],  # P3
        [10, 25, 'RED'],   # P4
        [70, 70, 'BLUE'],  # P5
        [60, 10, 'RED'],   # P6
        [25, 80, 'BLUE']   # P7
    ]
    new_point = [20, 35]
    frequency = {}
    maxi = 0
    color = ''
    k = 5
    
    for arr in data_points:
        x, y, c = arr
        p, q = new_point
        
        arr.append(mt.sqrt((x-p)*(x-p) + (y-q)*(y-q)));
        
    sorted_data = sorted(data_points, key=lambda x: x[3])
    # for arr in sorted_data:
    #     print(arr)
    
    for arr in sorted_data:
        k -= 1
        if arr[2] in frequency:
            frequency[arr[2]] += 1
        else:
            frequency[arr[2]] = 1
            
        if frequency[arr[2]] > maxi:
            maxi = frequency[arr[2]]
            color = arr[2]
        
        if not k:
            break
    
    # print(frequency)
    print('Result = ', color)
    
        

if __name__=="__main__":
    main()