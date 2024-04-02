import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt

#C:\Users\rghlr\Desktop\PYTHON\CSV FILE\file1.csv
# Streamlit part

st.set_page_config(layout= "wide")
st.title("AIRBNB DATA ANALYSIS")
st.write("")

def datafr():
    df= pd.read_csv(r"C:\\Users\\rghlr\\Desktop\\PYTHON\\CSV FILE\\file1.csv")
    return df

df= datafr()

with st.sidebar:
    select= option_menu("Main Menu", ["PRICE ANALYSIS", "AVAILABILITY ANALYSIS",
                                      "LOCATION BASED","GEOSPATIAL VISUALIZATION","AVERAGE COMPARE"])


if select == "PRICE ANALYSIS":
    
    st.title("**PRICE DIFFERENCE**")
    col1,col2= st.columns(2)

    with col1:
        
        
        country= st.selectbox("Select the Country",df["country"].unique())

        df1= df[df["country"] == country]
        df1.reset_index(drop= True, inplace= True)

        room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique())
        
        df2= df1[df1["room_type"] == room_ty]
        df2.reset_index(drop= True, inplace= True)

        df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
        df_bar.reset_index(inplace= True)

        fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",
                        hover_data=["number_of_reviews","review_scores"],
                        color_discrete_sequence = px.colors.qualitative.G10, width=600, height=500)
        st.plotly_chart(fig_bar)

    
    with col2:
        
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    
        proper_ty= st.selectbox("Select the Property type",df2["property_type"].unique())

        df4= df2[df2["property_type"] == proper_ty]
        df4.reset_index(drop= True, inplace= True)

        df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
        df_pie.reset_index(inplace= True)

        fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                        hover_data=["bedrooms"],
                        color_discrete_sequence= px.colors.qualitative.G10,
                        title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                        width= 600, height= 500)
        st.plotly_chart(fig_pi)

    col1,col2= st.columns(2)

    with col1:

        
        hostresponsetime= st.selectbox("Select the host_response_time",df4["host_response_time"].unique())

        df5= df4[df4["host_response_time"] == hostresponsetime]

        df_do_bar= pd.DataFrame(df4.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
        df_do_bar.reset_index(inplace= True)

        fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
        title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data=["price"],
        barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width=600, height=500)
        

        st.plotly_chart(fig_do_bar)

    with col2:

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
        df_do_bar_2.reset_index(inplace= True)

        fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
        title='BEDROOMS AND BEDS ACCOMMODATES',hover_data=["price"],
        barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)
        
        st.plotly_chart(fig_do_bar_2)
        
    # Assuming df is your DataFrame containing the data
    # Disable the warning globally
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Distribution of Price
    st.write("## Distribution of Price")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], kde=True)
    plt.title('Distribution of Price')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    st.pyplot()

    # Relationship between Price and other variables (Accomodates)
    st.write("## Price vs. Accomodates")
    plt.figure(figsize=(12, 6))
    sns.scatterplot(df, x='accommodates', y='price')
    plt.title('Price vs. Accomodates')
    plt.xlabel('Accomodates')
    plt.ylabel('Price')
    st.pyplot()

    # Boxplot of Price vs. Room type
    st.write("## Price vs. Room Type")
    plt.figure(figsize=(10, 6))                                                                                 
    sns.boxplot(data=df, x='room_type', y='price')
    plt.title('Price vs. Room Type')
    plt.xlabel('Room Type')
    plt.ylabel('Price')
    st.pyplot()

if select == "AVAILABILITY ANALYSIS":

    def datafr():
        df_a= pd.read_csv(r"C:\\Users\\rghlr\\Desktop\\PYTHON\\CSV FILE\\file1.csv")
        return df_a

    df_a= datafr()

    st.title("**AVAILABILITY ANALYSIS**")
    col1,col2= st.columns(2)

    with col1:
        
        
        country_a= st.selectbox("Select the Country_a",df_a["country"].unique())

        df1_a= df[df["country"] == country_a]
        df1_a.reset_index(drop= True, inplace= True)

        property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())
        
        df2_a= df1_a[df1_a["property_type"] == property_ty_a]
        df2_a.reset_index(drop= True, inplace= True)

        df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30 Days",color_discrete_sequence=px.colors.sequential.Rainbow_r)
        st.plotly_chart(df_a_sunb_30)
    
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        

        df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60 Days",color_discrete_sequence=px.colors.sequential.Brwnyl_r)
        st.plotly_chart(df_a_sunb_60)

    col1,col2= st.columns(2)

    with col1:
        
        df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90 Days",color_discrete_sequence=px.colors.sequential.Darkmint_r)
        st.plotly_chart(df_a_sunb_90)

    with col2:

        df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365 Days",color_discrete_sequence=px.colors.sequential.Electric_r)
        st.plotly_chart(df_a_sunb_365)
    
if select == "LOCATION BASED":

    

    st.title("LOCATION ANALYSIS")
    st.write("")

    def datafr():
        df= pd.read_csv(r"C:\\Users\\rghlr\\Desktop\\PYTHON\\CSV FILE\\file1.csv")
        return df

    df_l= datafr()

    country_l= st.selectbox("Select the Country_l",df_l["country"].unique())

    df1_l= df_l[df_l["country"] == country_l]
    df1_l.reset_index(drop= True, inplace= True)

    proper_ty_l= st.selectbox("Select the Property_type_l",df1_l["property_type"].unique())

    df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
    df2_l.reset_index(drop= True, inplace= True)

    st.write("")

    def select_the_df(sel_val):
        if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

            df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
            df_val_30.reset_index(drop= True, inplace= True)
            return df_val_30

        elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
        
            df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
            df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
            df_val_60_1.reset_index(drop= True, inplace= True)
            return df_val_60_1
        
        elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

            df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
            df_val_100.reset_index(drop= True, inplace= True)
            return df_val_100
        
    differ_max_min= df2_l['price'].max()-df2_l['price'].min()

    val_sel= st.radio("Select the Price Range",[str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                
                                                str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                        
    df_val_sel= select_the_df(val_sel)

    st.dataframe(df_val_sel)

    # checking the correlation

    df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                        "room_type", "bed_type","cancellation_policy",
                                        "images","host_url","host_name", "host_location",                   
                                        "host_response_time", "host_thumbnail_url",            
                                        "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                        "host_picture_url","host_neighbourhood",
                                        "host_identity_verified","host_verifications",
                                        "street", "suburb", "government_area", "market",                        
                                        "country", "country_code","location_type","is_location_exact",
                                        "amenities"]).corr()
    
    st.dataframe(df_val_sel_corr)

    df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
    df_val_sel_gr.reset_index(inplace= True)

    fig_1 = px.bar(df_val_sel_gr, x="accommodates", y=["cleaning_fee", "bedrooms", "beds"],
            title="ACCOMMODATES", hover_data=["extra_people"], barmode='group',
            color_discrete_sequence=px.colors.sequential.Oryel_r, width=1000)

    st.plotly_chart(fig_1)
    
    room_ty_l= st.selectbox("Select the Room_Type_l", df_val_sel["room_type"].unique())

    df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

    fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Greens_r,width=1000)
    st.plotly_chart(fig_2)

    fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Greens_r,width=1000)
    st.plotly_chart(fig_3)

if select == "GEOSPATIAL VISUALIZATION":
    
    st.title("GEOSPATIAL VISUALIZATION")
    st.write("")

    fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                    color_discrete_sequence= ["fuchsia"],hover_name='name',range_color=(0,49000), mapbox_style="open-street-map",
                    zoom=1)
    fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
    
    fig_4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_4)

if select == "AVERAGE COMPARE":
    

    country_t= st.selectbox("SELECT THE COUNTRY",df["country"].unique())

    df1_t= df[df["country"] == country_t]

    property_ty_t= st.selectbox("SELECT THE PROPERTY TYPE",df1_t["property_type"].unique())

    df2_t= df1_t[df1_t["property_type"] == property_ty_t]
    df2_t.reset_index(drop= True, inplace= True)

    df2_t_sorted= df2_t.sort_values(by="price")
    df2_t_sorted.reset_index(drop= True, inplace= True)


    df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
    df_price.reset_index(inplace= True)
    df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
    
    fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                        title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
    st.plotly_chart(fig_price_2)

    df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
    df_price_1.reset_index(inplace= True)
    df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
    
    fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                        width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Teal_r,
                        title= "AVERAGE PRICE BASED ON HOST_LOCATION")
    st.plotly_chart(fig_price_4)


    room_type_t= st.selectbox("Select the Room Type",df2_t_sorted["room_type"].unique())

    df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

    df3_t_sorted_price= df3_t.sort_values(by= "price")

    df3_t_sorted_price.reset_index(drop= True, inplace = True)

    df3_top_50_price= df3_t_sorted_price.head(100)

    fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                color_continuous_scale= "rainbow",
                            range_color=(0,df3_top_50_price["price"].max()),
                            title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                            width=1200, height= 800,
                            hover_data= ["minimum_nights","maximum_nights","accommodates"])
    
    st.plotly_chart(fig_top_50_price_1)

    fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                color_continuous_scale= "greens",
                                title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                            range_color=(0,df3_top_50_price["price"].max()),
                            width=1200, height= 800,
                            hover_data= ["accommodates","bedrooms","beds","bed_type"])

    st.plotly_chart(fig_top_50_price_2)
