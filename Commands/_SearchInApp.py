from roku import Roku; 
import requests; 
import time; 

app='Netflix'; 
query='Stranger Things'; 
rokuIP='[replace]'; 

roku=Roku(rokuIP, '8060'); roku.poweron(); (roku[app]).launch(); time.sleep(8); 
if(app=='Netflix'): roku.select(); time.sleep(1.0); roku.left(); time.sleep(0.5); roku.up(); time.sleep(0.5); roku.select(); time.sleep(0.5); roku.literal(query); 