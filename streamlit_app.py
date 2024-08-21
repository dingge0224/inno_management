import streamlit as st
from streamlit_option_menu import option_menu
from http import HTTPStatus
import os
import time
import numpy as np
#import graphviz
#from graphviz import Digraph
import matplotlib.pyplot as plt
import pandas as pd
import dashscope


def call_with_prompt(text1, text2, text3):
    response = dashscope.Generation.call(
        model='qwen-max',
        prompt = f"结合以下关键词进行头脑风暴:{text1}、{text2}。并将一下关键词作为头脑风暴的补充:{text3}。探讨这两个关键词如何结合以形成新产品，或者给出有哪些现有产品已经结合了这两个关键词。",
        result_format='message',
        enable_search=False,
        max_tokens=1500,
        temperature=0.85,
        repetition_penalty=1.0
    )
    #print(f"Response: {response}")  # 添加此行以调试
    if response.status_code == HTTPStatus.OK:
        content = response['output']['choices'][0]['message']['content']
        return content
    else:
        return f'Request id: {response.request_id}, Status code: {response.status_code}, error code: {response.code}, error message: {response.message}'


#定义网页标题    
st.set_page_config(
    page_icon='🐳',
    page_title='Innovation Management system',
    layout='wide'
)
#定义边栏导航
with st.sidebar:
    choose = option_menu('创新工作管理系统',['系统简介','管理系统使用说明','For PM','For Team Focal','For PoC Owner','For Patent Owner','PoC数据分析','Patent数据分析','创新数据可视化','灵感激发'],

                         icons=['house','book-half','','','','','book-half','book-half','book-half','book-half'])


#定义系统简介
if choose == '系统简介':
    # 定义页面标题
    st.title('欢迎使用创新工作管理系统')
    # 写入文本
    st.write('本系统用于处理DCBU相关创新工作，帮助大家提升日常的工作效率，欢迎大家随时提出修改意见。')
    st.write('本系统仅为试用版，正式版敬请期待。')    

#定义管理系统使用说明
if choose == '管理系统使用说明':
    st.title('管理系统使用说明')
    # 写入文本
    st.write('请大家按需求点击对应侧边栏提交内容或查看数据')
   
#定义PM使用说明
if choose == 'For PM':
    st.title('请PM输入需要查询的创新方向')
    
    option = st.selectbox(
    '请选择创新方向',
     ('ME', 'AI', 'camera','screen','audio'))
    st.write('您要查询的创新方向是', option)
    st.write('如下是该方向在历史数据库中的查询结果')
    st.markdown('---')


#定义各function流程
if choose == 'For Team Focal':
    st.title("请各team focal提交对应内容！")
    st.markdown('---')
#上传专利数据
    uploaded_file = st.file_uploader('请上传team内部专利达成情况', type=['txt', 'csv', 'xlsx'])
    if uploaded_file is not None:
                # 显示上传文件的名称
        st.write('你上传的文件名称:', uploaded_file.name)
        contents = uploaded_file.getvalue()
        #st.write(contents)
    else:
        st.write('请上传一个文件。')
    st.markdown('---')      
#上传PoC数据
    uploaded_file = st.file_uploader('请上传team内部PoC完成情况', type=['txt', 'csv', 'xlsx'])
    if uploaded_file is not None:
                # 显示上传文件的名称
        st.write('你上传的文件名称:', uploaded_file.name)
        contents = uploaded_file.getvalue()
        #st.write(contents)
    else:
        st.write('请上传一个文件。')    
    st.markdown('---')    
#模板下载 
    st.write('上传的文件时请使用标准模板填写，如下为对应模板下载链接')  



if choose == 'For PoC Owner':
    # 写入文本
    st.title("请PoC owner提交对应内容！")
    # 添加一个输入框
    PCRtext = st.text_input("请输入您的项目变更细节，请按照格式标准来写")
    # 添加一个按钮pip
    button = st.button("提交")
    # 在按钮被点击时执行的操作
    if button:
        st.text("您好，！内容已经成功提交！")
        # 文件上传器
    st.markdown('---')
   
   

if choose == 'For Patent Owner':
    st.title('请Patent owner提交对应内容')
   # 添加一个输入框
    PCRtext = st.text_input("请输入您的专利变更细节，请按照格式标准来写")
    # 添加一个按钮pip
    button = st.button("提交")
    # 在按钮被点击时执行的操作
    if button:
        st.text("您好，！内容已经成功提交！")
        # 文件上传器
    st.markdown('---')
   
    
  
   
    

if choose == 'PoC数据分析':
    st.title('PoC数据分析')
    # 写入文本
    st.write('请进行评估') 
    st.markdown('---')
    add_radio = st.radio(
        "请选择数据分析类型",
        ['技术方向','落地情况','项目周期','预算情况']
        )  
    if add_radio:    
        if add_radio == '技术方向':
             PCRtext = st.text_input("请输入您的评估结果")
             # 添加一个按钮pip
             button = st.button("提交")
             # 在按钮被点击时执行的操作
             if button:
                st.text("您好，！PCR评估结果已经成功提交！")
        if add_radio == '落地情况':
             PCRtext = st.text_input("请输入您的评估结果")
             # 添加一个按钮pip
             button = st.button("提交")
             # 在按钮被点击时执行的操作
             if button:
                st.text("您好，！PCR评估结果已经成功提交！")        
        if add_radio == '预算情况':
             PCRtext = st.text_input("请输入您的评估结果")
             # 添加一个按钮pip
             button = st.button("提交")
             # 在按钮被点击时执行的操作
             if button:
                st.text("您好，！PCR评估结果已经成功提交！")     
            
             
                    
       
             
if choose == 'Patent数据分析':
    st.title('Patent数据分析')
    st.markdown('---')
    add_radio = st.radio(
        "请选择生成report的方式",
        ("提交内容合成", "提交文档合成", "提交内容和文档合成")
        ) 
    button = st.button("提交")
    # 在按钮被点击时执行的操作
    if button:
        st.text("您好，！Report已经成功生成！")
        if add_radio:    
            if add_radio == '提交内容合成':
                st.title("提交内容合成")
                #labels = ['BB','MB','ME','Thermal','Cert','PA']
                st.write('提交内容合成')
                exit()       
            if add_radio == '提交文档合成':
                st.title("提交文档合成")
                #labels = ['BB','MB','ME','Thermal','Cert','PA']
                st.write('提交文档合成')
                exit() 
            if add_radio == '提交内容和文档合成':
                st.title("提交内容和文档合成")
                #labels = ['BB','MB','ME','Thermal','Cert','PA']
                st.write('提交内容和文档合成')
                exit()          


#定义历史数据分析
if choose == '创新数据可视化':
    # 定义一个输入框
    st.title('创新数据可视化')
    st.markdown('---')
    add_radio = st.radio(
        "请选择FY23-24历史数据分析关键词",
        ("词云", "各技术方向数量占比")
        )  
    st.markdown('---')
    if add_radio:    
        if add_radio == '词云':
            st.title("词云")
            labels = ['BB','MB','ME','Thermal','Cert','PA']
            sizes = [15,6,31,8,9,12]

            tab1, tab2 = st.tabs(["PoC", "Patent"])

            tab1.subheader("PoC词云")
            fig1 = plt.figure()
            plt.pie(sizes,  labels=labels)
            plt.title('PoC historical data analysis pie chart', fontdict={'size':15})
            plt.legend(loc="upper right",fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)#添加图例
            #st.pyplot(fig1)
            tab1.pyplot(fig1)
            tab2.subheader("Patent词云")
            #tab5.write(data)
            fig2 = plt.figure()
            plt.bar(x=labels, height=sizes)
            plt.title('Patent historical data analysis bar chart', fontdict={'size':15})           
            tab2.pyplot(fig2)                   
            exit()    
        if add_radio == '各技术方向数量占比':
            st.title("各技术方向数量占比")
            labels = ['BB','MB','ME','Thermal','Cert','PA']
            sizes = [12,8,25,6,41,19] 

            tab1, tab2 = st.tabs(["PoC", "Patent"])

            tab1.subheader("PoC")
            fig1 = plt.figure()
            plt.pie(sizes,  labels=labels)
            plt.title('PoC historical data analysis pie chart', fontdict={'size':15})
            #plt.legend(loc="upper right",fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)#添加图例
            #st.pyplot(fig1)
            tab1.pyplot(fig1)
            tab2.subheader("Patent")
            #tab5.write(data)
            fig2 = plt.figure()
            plt.bar(x=labels, height=sizes)
            plt.title('Patent historical data analysis bar chart', fontdict={'size':15})           
            tab2.pyplot(fig2)                   
            exit()    




#灵感激发
if choose == '灵感激发':
    # 定义页面标题
    st.title('欢迎使用灵感激发')
    st.write('本小程序主要用于发散思维。可以依次输入两个关键词。点击开始按钮，看两者可以碰撞出哪些灵感的火花') 
    # 添加一个输入框
    option1 = st.selectbox(
    '请选择您的第一个关键词',
     ('台式电脑', '散热系统', '创新机械结构', '先进材料', '麦克风','扬声器','Bios','驱动程序','电子工程','摄像头','显示器','天线','无线网络','User defined'))
    
    if option1 == 'User defined':
        option1 = st.text_input("请输入您的自定义关键词")
    st.write('您的第一个关键词是', option1)    
    st.markdown('---') 

    option2 = st.selectbox(
    '请选择您的第二个关键词',
    ('人工智能', '汽车领域', '万物互联','键盘','物联网','极致用户体验','高端品质','User defined'), key="option2")
    if option2 == 'User defined':
        option2 = st.text_input("请输入您的自定义关键词")
    st.write('您的第二个关键词是', option2)  
    st.markdown('---') 
    

    st.write('进一步补充（optional）') 
    option3 = st.selectbox(
    '请输入要补充的内容',
    ('无补充内容', 'User defined'), key="option3")
    if option3 == 'User defined':
        option3 = st.text_input("如果您还想加入其他备注或者导向词，请输入到下面文本框")
     
    st.markdown('---') 

  

    # 添加一个按钮pip
    button = st.button("开始灵感碰撞")
    dashscope.api_key='sk-2a94241b0582420cb3b14360a288e6b'
    # 在按钮被点击时执行的操作
    if button:
        result = call_with_prompt(option1, option2, option3)
        st.write('灵感激发结果如下') 
        st.markdown('---')
        st.write(result)  
        #response1 = get_response1(user_input1, access_token1)
        #st.text_area('文心一言回答:', response1)
        #response2 = get_response2(user_input2, access_token2)
        #st.text_area('DCBU回答:', response2)

    st.markdown('---')
    st.markdown('---')
    st.markdown('---')
    st.markdown('---')
    st.markdown('---')
    st.markdown('---')
    st.markdown('---')
    st.write('与你搜索关键词相关的专利信息如下，你可以找到对应发明人沟通或者合作')  
    st.markdown('---') 
    st.write('与你搜索关键词相关的PoC信息如下，你可以找到对应负责人沟通或者合作')  
    st.markdown('---')

    st.write('这里还是一个开放性的互助平台，你也可以在这里简单写下你的idea，其他同事可以匿名或实名点评你的idea')  
    st.write('可能会有研发同事给予你技术上的支持或评价，也可能有marketing同事基于市场需求给予你前端的中肯建议') 
               
    
         
