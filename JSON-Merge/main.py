import os,sys
from pathlib import Path
import json

output={'employees':[]}

def read_files(inp_files,merged1,s):
    max_size=s
    for i in inp_files:
        d = json.load(open(i))
        size=json.dumps(d)
        for i in d:
            key=i
            obj=d[i]
            for o in obj:
                str_size=len(json.dumps(o).encode('utf-8'))
                output["employees"].append(o)
    print("Output:")
    print(output)
    print("\n")
    with open('merge1.json', 'w') as json_file:
        l=len(json.dumps(output))
        print("Size of the merged_data:")
        print(l)
        if l>max_size:
            print("Merged data size larger than maximum size given.")
        else:
            json.dump(output, json_file,indent=5)
            print("Merge successful")
  
def merge_files(fpath,inp,merge1,size):
    files=os.listdir(fpath)
    inp_files=[]
    for f in files:
        if f.startswith(inp) and f.endswith('.json'):
            inp_files.append(f)
    print("The input files are:")
    print(inp_files)
    print("\n")
    inp_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    read_files(inp_files,merge1,size)


merge_files("C:\Users\Vidhya\Desktop\JSON-Merge","data","merge1",1500)
