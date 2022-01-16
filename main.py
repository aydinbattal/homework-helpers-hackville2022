import streamlit as st
from config import auth_key
import pyrebase

config = {
    "apiKey": "AIzaSyCiJOaByMSGWio3hW72IGnpsCFf9Y2PdVw",
    "authDomain": "homework-helpers-be9f9.firebaseapp.com",
    "projectId": "homework-helpers-be9f9",
    "storageBucket": "homework-helpers-be9f9.appspot.com",
    "messagingSenderId": "799751403520",
    "appId": "1:799751403520:web:4b8afe99d489f1792c80e5",
    "databaseURL": "https://homework-helpers-be9f9.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

st.title('Homework Helpers')

file_to_upload = st.file_uploader("Upload a video")
url = ""

if file_to_upload is not None:
    path_on_cloud = "images/" + file_to_upload.name
    storage.child(path_on_cloud).put(file_to_upload)
    url = storage.child(path_on_cloud).get_url('idToken')

if url != "":
    st.video(url)

