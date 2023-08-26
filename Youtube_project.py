from googleapiclient.discovery import build
import streamlit as st
import pymongo
import pandas as pd
import requests
import seaborn as sns
import json

# Defining  API key and the channel ID
api_key = "AIzaSyBRGIe2p5MXP7ZfLoas5ghA1kfBbai_9R0"
channel_id = "7lCDEYXw3mM"

# Defining the base URL for YouTube Data API
base_url = "https://www.googleapis.com/youtube/v3/"

# Defining parameters for channel request
channel_params = {
    "part": "snippet,statistics",
    "id": channel_id,
    "key": api_key
}

# Make channel request & get response
channel_response = requests.get(base_url + "channels", params=channel_params)
channel_data = channel_response.json()

# Extracting the channel details
channel_name = channel_data["items"][0]["snippet"]["title"]
channel_description = channel_data["items"][0]["snippet"]["description"]
subscription_count = channel_data["items"][0]["statistics"]["subscriberCount"]
channel_views = channel_data["items"][0]["statistics"]["viewCount"]
playlist_id = channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

# Defining parameters for playlist request
playlist_params = {
    "part": "snippet",
    "playlistId": playlist_id,
    "key": api_key,
    "maxResults": 70
}

# Making the playlist request & getting  response
playlist_response = requests.get(base_url + "playlistItems", params=playlist_params)
playlist_data = playlist_response.json()

# Initializing an empty dictionary for store video details
video_info = {}

# Looping throughout the playlist items & extracting video details
for item in playlist_data["items"]:
    # Getting video ID & title
    video_id = item["snippet"]["resourceId"]["videoId"]
    video_name = item["snippet"]["title"]

    # Defining parameters for video request
    video_params = {
        "part": "snippet,statistics,contentDetails",
        "id": video_id,
        "key": api_key
    }

    # Making video request & get the response
    video_response = requests.get(base_url + "videos", params=video_params)
    video_data = video_response.json()

    # Extracting video details
    video_description = video_data["items"][0]["snippet"]["description"]
    tags = video_data["items"][0]["snippet"]["tags"]
    published_at = video_data["items"][0]["snippet"]["publishedAt"]
    view_count = video_data["items"][0]["statistics"]["viewCount"]
    like_count = video_data["items"][0]["statistics"]["likeCount"]
    dislike_count = video_data["items"][0]["statistics"]["dislikeCount"]
    favorite_count = video_data["items"][0]["statistics"]["favoriteCount"]
    comment_count = video_data["items"][0]["statistics"]["commentCount"]
    duration = video_data["items"][0]["contentDetails"]["duration"]
    thumbnail = video_data["items"][0]["snippet"]["thumbnails"]["default"]["url"]
    caption_status = video_data["items"][0]["contentDetails"]["caption"]

    # Defining parameters for the comment request
    comment_params = {
        "part": "snippet",
        "videoId": video_id,
        "key": api_key,
        "maxResults": 70
    }

    # for comment request & get response
    comment_response = requests.get(base_url + "commentThreads", params=comment_params)
    comment_data = comment_response.json()

    # start an empty dictionary for storing comments
    comments = {}

    # for Looping throughout the comment items & extracting comments
    for comment in comment_data["items"]:
        # Get the comment ID and text
        comment_id = comment["id"]
        comment_text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

        # to get comment author & published date
        comment_author = comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        comment_published_at = comment["snippet"]["topLevelComment"]["snippet"]["publishedAt"]

        # Storing comment information in a dictionary
        comments[comment_id] = {
            "Comment_Id": comment_id,
            "Comment_Text": comment_text,
            "Comment_Author": comment_author,
            "Comment_PublishedAt": comment_published_at
        }

    
    # Store the video information in a dictionary with video ID as key
    video_info[video_id] = {
        "Video_Id": video_id,
        "Video_Name": video_name,
        "Video_Description": video_description,
        "Tags": tags,
        "PublishedAt": published_at,
        "View_Count": view_count,
        "Like_Count": like_count,
        "Dislike_Count": dislike_count,
        "Favorite_Count": favorite_count,
        "Comment_Count": comment_count,
        "Duration": duration,
        "Thumbnail": thumbnail,
        "Caption_Status": caption_status,
        "Comments": comments
    }

# Store the channel information in a dictionary with channel name as key
channel_info = {
    channel_name: {
        "Channel_Name": channel_name,
        "Channel_Id": channel_id,
        "Subscription_Count": subscription_count,
        "Channel_Views": channel_views,
        "Channel_Description": channel_description,
        "Playlist_Id": playlist_id
    }
}

# Merge the channel and video information into one dictionary
youtube_data = {**channel_info, **video_info}

# Convert the dictionary to JSON format and print it
youtube_json = json.dumps(youtube_data, indent=4)
print(youtube_json)


# Define the API key and the channel ID
api_key = "AIzaSyA79XBlkzuMdQsoA74g4TmjdQwnTRmWdxA"
channel_id = "UC1234567890"

# Define the base URL for the YouTube Data API
base_url = "https://www.googleapis.com/youtube/v3/"

# Define the parameters for the channel request
channel_params = {
    "part": "snippet,statistics",
    "id": channel_id,
    "key": api_key
}

# Make the channel request and get the response
channel_response = requests.get(base_url + "channels", params=channel_params)
channel_data = channel_response.json()

# Extract the channel information
channel_name = channel_data["items"][0]["snippet"]["title"]
channel_description = channel_data["items"][0]["snippet"]["description"]
subscription_count = channel_data["items"][0]["statistics"]["subscriberCount"]
channel_views = channel_data["items"][0]["statistics"]["viewCount"]
playlist_id = channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

# Define the parameters for the playlist request
playlist_params = {
    "part": "snippet",
    "playlistId": playlist_id,
    "key": api_key,
    "maxResults": 50 # Change this as per your need
}

# Make the playlist request and get the response
playlist_response = requests.get(base_url + "playlistItems", params=playlist_params)
playlist_data = playlist_response.json()

# Initialize an empty dictionary to store the video information
video_info = {}

# Loop through the playlist items and extract the video information
for item in playlist_data["items"]:
    # Get the video ID and title
    video_id = item["snippet"]["resourceId"]["videoId"]
    video_name = item["snippet"]["title"]

    # Define the parameters for the video request
    video_params = {
        "part": "snippet,statistics,contentDetails",
        "id": video_id,
        "key": api_key
    }

    # Make the video request and get the response
    video_response = requests.get(base_url + "videos", params=video_params)
    video_data = video_response.json()

    # Extract the video information
    video_description = video_data["items"][0]["snippet"]["description"]
    tags = video_data["items"][0]["snippet"]["tags"]
    published_at = video_data["items"][0]["snippet"]["publishedAt"]
    view_count = video_data["items"][0]["statistics"]["viewCount"]
    like_count = video_data["items"][0]["statistics"]["likeCount"]
    dislike_count = video_data["items"][0]["statistics"]["dislikeCount"]
    favorite_count = video_data["items"][0]["statistics"]["favoriteCount"]
    comment_count = video_data["items"][0]["statistics"]["commentCount"]
    duration = video_data["items"][0]["contentDetails"]["duration"]
    thumbnail = video_data["items"][0]["snippet"]["thumbnails"]["default"]["url"]
    caption_status = video_data["items"][0]["contentDetails"]["caption"]

    # Define the parameters for the comment request
    comment_params = {
        "part": "snippet",
        "videoId": video_id,
        "key": api_key,
        "maxResults": 50 # Change this as per your need
    }

    # Make the comment request and get the response
    comment_response = requests.get(base_url + "commentThreads", params=comment_params)
    comment_data = comment_response.json()

    # Initialize an empty dictionary to store the comments
    comments = {}

    # Loop through the comment items and extract the comments
    for comment in comment_data["items"]:
        # Get the comment ID and text
        comment_id = comment["id"]
        comment_text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

        # Get the comment author and published date
        comment_author = comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        comment_published_at = comment["snippet"]["topLevelComment"]["snippet"]["publishedAt"]

        # Store the comment information in a dictionary with comment ID as key
        comments[comment_id] = {
            "Comment_Id": comment_id,
            "Comment_Text": comment_text,
            "Comment_Author": comment_author,
            "Comment_PublishedAt": comment_published_at
        }

    
    # Store the video information in a dictionary with video ID as key
    video_info[video_id] = {
        "Video_Id": video_id,
        "Video_Name": video_name,
        "Video_Description": video_description,
        "Tags": tags,
        "PublishedAt": published_at,
        "View_Count": view_count,
        "Like_Count": like_count,
        "Dislike_Count": dislike_count,
        "Favorite_Count": favorite_count,
        "Comment_Count": comment_count,
        "Duration": duration,
        "Thumbnail": thumbnail,
        "Caption_Status": caption_status,
        "Comments": comments
    }

# Store the channel information in a dictionary with channel name as key
channel_info = {
    channel_name: {
        "Channel_Name": channel_name,
        "Channel_Id": channel_id,
        "Subscription_Count": subscription_count,
        "Channel_Views": channel_views,
        "Channel_Description": channel_description,
        "Playlist_Id": playlist_id
    }
}

# Merge the channel and video information into one dictionary
youtube_data = {**channel_info, **video_info}

# Convert the dictionary to JSON format and print it
youtube_json = json.dumps(youtube_data, indent=4)
print(youtube_json)



# Import Streamlit and other modules
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from JSON file
with open('data.json') as f:
    data = pd.read_json(f)

# Display the title and some text
st.title('youtube_data')


# Display the data as a dataframe and a table
st.subheader('Dataframe')
st.dataframe(data)
st.subheader('Table')
st.table(data)

# Display a metric with a delta indicator
st.subheader('Metric')
st.metric('Average Rating', np.mean(data['rating']), 0.1)

# Display the JSON data
st.subheader('JSON')
st.json(data.to_dict())

# Display a line chart using matplotlib
st.subheader('Line Chart')
fig, ax = plt.subplots()
ax.plot(data['rating'], label='Rating')
ax.set_xlabel('Index')
ax.set_ylabel('Rating')
ax.legend()
st.pyplot(fig)

# Display a bar chart using Streamlit
st.subheader('Bar Chart')
st.bar_chart(data['rating'])

# Display a map using Streamlit
st.subheader('Map')
st.map(data[['lat', 'lon']])

# Create a sidebar with widgets for user input
st.sidebar.title('Options')
site = st.sidebar.selectbox('Select a site', ['site1', 'site2'])
is_vip = st.sidebar.checkbox('Show only VIP customers')

# Filter the data based on user input and display it as a table
st.subheader(f'Filtered Data for {site}')
filtered_data = data[(data['site'] == site) & (data['is_vip'] == is_vip)]
st.table(filtered_data)