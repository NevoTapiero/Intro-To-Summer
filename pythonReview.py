def create_youtube_video(title, description):
	IshowSpeed = {"title": title, "description": description, "likes": 0, "dislikes": 0, comments:{}}
	return IshowSpeed
title = input("What is your title? ")
description = input("what is your youtube video description? ")
new_youtube_video = create_youtube_video(title, description)