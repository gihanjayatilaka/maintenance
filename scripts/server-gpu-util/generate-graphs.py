import os
import pandas as pd
import matplotlib.pyplot as plt
import json


SERVERS = ["turing","kepler","ai4covid"]
LOGS_DIRECTORY = '../../reports/server-gpu-util/logs/'
JSON_FILE = "./gpu-info.json"
OUT_FOLDER = "../../reports/server-gpu-util/plots/"


if __name__=="__main__":
    data = {}
    JSON = json.load(open(JSON_FILE))
    
    # iterate over files in
    # that directory
    for filename in os.listdir(LOGS_DIRECTORY):
        f = os.path.join(LOGS_DIRECTORY, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)

            s = f.split("/")[-1].split("-")[0]
            if s not in data:
                data[s] = pd.read_csv(f)
            else:
                data[s] = data[s].append(pd.read_csv(f))
            
            
            

            # data[s].set_index(keys=['gpuid'], drop=False,inplace=True)

    
    for s in SERVERS:
        print(s)
        data[s] = data[s].rename(columns=lambda x: x.strip())
        
        data[s] = data[s][data[s]["gpuid"].apply(lambda x: str(x).isdigit())] #Keep only rows where GPUID \in int 


        data[s]["timestamp"] = data[s]["timestamp"].apply(pd.to_datetime)
        data[s]["power.draw [W]"] = data[s]["power.draw [W]"].apply(lambda x: float(x.replace(" W","")))
        data[s]["utilization.gpu [%]"] = data[s]["utilization.gpu [%]"].apply(lambda x: float(x.replace(" %","")))
        data[s]["memory.used [MiB]"] = data[s]["memory.used [MiB]"].apply(lambda x: float(x.replace(" MiB","")))

        for i in [0,1]:
            if str(i) in JSON[s]:
                if bool(JSON[s][str(i)]["active"]):#==True: 
                    data[s+"-"+str(i)] = data[s][:][data[s].gpuid == i]
        del data[s]



    for s in data:
        data[s].head()
        data[s] = data[s].groupby(data[s].timestamp.dt.floor("D")).mean()


    for s in data:
        print(s+"------------------")
        # print(data[s])
        ax = data[s].plot(y=["utilization.gpu [%]","memory.used [MiB]"],secondary_y = ["memory.used [MiB]"],ylim=(0,100),marker="*",\
                          style={"utilization.gpu [%]":"*-r","memory.used [MiB]":"*-b"})
        ax.set_ylabel("utilization.gpu [%]",color="r")
        ax.right_ax.set_ylabel("memory.used [MiB]",color="b")
        ax.right_ax.set_ylim(0,JSON[s.split("-")[0]][s.split("-")[1]]["memory"])
        ax.get_legend().remove()

        plt.savefig(OUT_FOLDER+"/"+"plot{}.jpeg".format(s),bbox_inches='tight')
            


