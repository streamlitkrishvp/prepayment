import streamlit as st
st.header("Streamlit Machine Learning App")
EMI_amount = st.number_input(label='EMI Amount Per month', min_value=None, max_value=None, value=100, step=100)
Total_oustanding  = st.number_input(label='Total Outstanding Amount', min_value=None, max_value=None, value=100, step=100)
#import streamlit as st
interest_rate  = st.number_input(label='Interest rate per month', min_value=0, max_value=100, value=8, step=0.25)
prepayment_amt  = st.number_input(label='Prepayment ', min_value=None, max_value=None, value=100, step=100)


#Emi_amount = st.nummber_input(label ='Enter Per month EMI amount', min_value=0, max_value=10000000000000000000000000000,value=100)
#Total_oustanding = st.nummber_input(label ='Enter total Outstandling loan', min_value=0, max_value=1000000000000000000000000000000,value=100)
#interest_rate = st.nummber_input(label ='Enter Annual Interest rate', min_value=0, max_value=100,value=.25)
prepayment_amt = st.nummber_input(label ='Enter Prepayment Amount', min_value=0, max_value=100000000000000000000000000000000000,value=100)
#Emi_amount = 50000
#Total_oustanding = 5000000
#interest_rate = 7
#prepayment_amt = 100000
total_sum = 0
Monthly_interest = interest_rate / (1200)
Total_amount = 0
Total_amount1 =0 
Total_amount2 = 0
k=0
emi_stop = 0



for i in range(0,1200):
    if i==1:
        prepayment_value = prepayment_amt
    else:
        prepayment_value = 0
    
    MonthlyInt_amount = (Total_oustanding - prepayment_value) * Monthly_interest
    principal_amt = min(Total_oustanding, Emi_amount) - MonthlyInt_amount
    outsanding_after_emi = max(Total_oustanding - principal_amt, 0) - prepayment_value
    Total_amount = MonthlyInt_amount + principal_amt + prepayment_value
    Total_amount1 = Total_amount + Total_amount1
    Total_oustanding = outsanding_after_emi
    emi_stop = Total_oustanding - Emi_amount
    if k == 1:
        n1 =i+1
        break
    
    if emi_stop < 0:
        k = 1
    
#Emi_amount = 50000
#Total_oustanding = 5000000
#interest_rate = 7
#prepayment_amt = 100000
total_sum = 0
Monthly_interest = interest_rate / (1200)
Total_amount = 0
Total_amount2 = 0
m=0
emi_stop = 0

for j in range(0,1200):
    if j==1:
        prepayment_value = 0
    else:
        prepayment_value = 0
    
    MonthlyInt_amount = (Total_oustanding - prepayment_value) * Monthly_interest
    principal_amt = min(Total_oustanding, Emi_amount) - MonthlyInt_amount
    outsanding_after_emi = max(Total_oustanding - principal_amt, 0) - prepayment_value
    Total_amount = MonthlyInt_amount + principal_amt + prepayment_value
    Total_amount2 = Total_amount + Total_amount2
    Total_oustanding = outsanding_after_emi
    emi_stop = Total_oustanding - Emi_amount
    if m == 1:
        n2 =j+1
        break
    
    if emi_stop < 0:
        m = 1
print(Total_amount1)  
print(Total_amount2)
print(Total_amount2-Total_amount1)
print(n2-n1)

amount_saved = st.text_input(label= 'amount saved', value= (Total_amount2-Total_amount1))


