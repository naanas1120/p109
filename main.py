import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
math_score=df["math score"].to_list()

mean=statistics.mean(math_score)
median=statistics.median(math_score)
mode=statistics.mode(math_score)
sd=statistics.stdev(math_score)
print(mean,median,mode,sd)

sd1_start,sd1_end=mean-sd,mean+sd
sd2_start,sd2_end=mean-(2*sd),mean+(2*sd)
sd3_start,sd3_end=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([math_score],["dice distribution"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.16],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1_start,sd1_start],y=[0,0.16],mode="lines",name="sd1 start"))
fig.add_trace(go.Scatter(x=[sd1_end,sd1_end],y=[0,0.16],mode="lines",name="sd1 end"))

fig.add_trace(go.Scatter(x=[sd2_start,sd2_start],y=[0,0.16],mode="lines",name="sd2 start"))
fig.add_trace(go.Scatter(x=[sd2_end,sd2_end],y=[0,0.16],mode="lines",name="sd2 end"))

fig.add_trace(go.Scatter(x=[sd3_start,sd3_start],y=[0,0.16],mode="lines",name="sd3 start"))
fig.add_trace(go.Scatter(x=[sd3_end,sd3_end],y=[0,0.16],mode="lines",name="sd3 end"))

list_of_data_within_sd1=[i for i in math_score if i > sd1_start and i < sd1_end]

list_of_data_within_sd2=[i for i in math_score if i > sd2_start and i < sd2_end]

list_of_data_within_sd3=[i for i in math_score if i > sd3_start and i < sd3_end]

print(len(list_of_data_within_sd1)* 100/len(math_score))
print(len(list_of_data_within_sd2)* 100/len(math_score))
print(len(list_of_data_within_sd3)* 100/len(math_score))