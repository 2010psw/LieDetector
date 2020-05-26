
import numpy as np
import tensorflow as tf
import pandas as pd

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DB import conn

##########################아이디 목록 가져오기#########################
id_list = conn.select_id()
print(id_list)
gsr_list = []
hrt_list = []
lb_list = []
####################################################################


for i in id_list :
    gsr_list.append(conn.select_gsr(i))
    print(gsr_list)