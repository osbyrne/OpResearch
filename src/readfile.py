def readfile(url):
    try:
        with open(f"Data\{url}", 'r') as file:
    
            data=[]
            provision=[]
            order=[]
            lines=file.readlines()
            height=1
            length=1
            for i in range(len(lines)):
                if i==0:
                    temp=lines[i].split()
                    height=int(temp[0])
                    length=int(temp[1])
                elif i<height+1:
                    temp=[]
                    d=lines[i].split()
                    for j in range(length):
                        temp.append(int(d[j]))
                    data.append(temp)
                    provision.append(int(d[length]))
                else:
                    d=lines[i].split()
                    for i in d:
                        order.append(int(i))
            for i in range(len(provision)):
                provision[i]=int(provision[i])                
            return (data,order,provision)
    except FileNotFoundError:
        print(f"The file {url} hasn't been found.")
        return None