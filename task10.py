import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.header(":blue[PLOTS]")
st.subheader(":blue[ploting using matplotlib]")
if st.button(":blue[chart]"):
    df=pd.read_csv("tip.csv")
    fig ,axs=plt.subplots(2,2,figsize=(12,8))

    axs[0,0].hist(df["total_bill"],bins=20,color="skyblue",edgecolor="black")
    axs[0,0].set_title("Histogram of Total_Bill")
    axs[0,0].set_xlabel("totla_bill")
    axs[0,0].set_ylabel("frequency")

    axs[0,1].boxplot(df["tip"],vert=True,patch_artist=True)
    axs[0,1].set_title("Boxplot of Tips")
    axs[0,1].set_ylabel("tip amount")

    gender_counts = df["sex"].value_counts()
    axs[1,0].pie(gender_counts,labels=gender_counts.index, autopct='%1.1f%%', startangle=90,colors=['skyblue','pink'])
    axs[1, 0].axis('equal')
    axs[1, 0].set_title("Gender Distribution")

    avg_bill_by_day = df.groupby("day")["total_bill"].mean()
    axs[1, 1].bar(avg_bill_by_day.index, avg_bill_by_day.values, color='lightgreen')
    axs[1, 1].set_title("Average Total Bill by Day")
    axs[1, 1].set_xlabel("Day")
    axs[1, 1].set_ylabel("Average Total Bill")

    plt.tight_layout()
    st.pyplot(fig)
