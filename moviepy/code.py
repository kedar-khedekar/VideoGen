from moviepy.editor import *
clip = VideoFileClip("video1.mkv")

data = {
    "id": 1,
  "title": "Erdogan Says Saudis Planned Khashoggi\u2019s Killing in Turkey",
  "date": "2018-10-23",
  "authors": [
   "Carlotta Gall",
   "Richard P\u00e9rez-Pe\u00f1a"
  ],
  "keywords": [
   "saudis",
   "killing",
   "president",
   "murder",
   "turkey",
   "mr",
   "khashoggis",
   "istanbul",
   "erdogan",
   "saudi",
   "officials",
   "planned",
   "truth"
  ],
  "summary": "ISTANBUL \u2014 President Recep Tayyip Erdogan of Turkey on Tuesday raised the stakes in his dispute with Saudi Arabia over what he called the \u201cpremeditated murder\u201d of the Saudi journalist Jamal Khashoggi, demanding that Riyadh supply more answers and hand over the Saudi suspects.",
  "image_url": "https://static01.nyt.com/images/2018/10/23/world/24TURKEY-promo/24TURKEY-promo-facebookJumbo-v2.jpg",
  "video_url": [],
  "time": "09:35:34"
}
date_clip = TextClip(data["date"],fontsize=20,color='white',bg_color="black").margin(6,color=(0,0,0)).margin(left=20,color=(0,0,0)).margin(left=0,top=20,opacity=0).set_pos(("left","top")).set_start(3).set_end(21)
title_clip = TextClip(data["title"],fontsize=70,color='white',bg_color="black").set_pos("center").margin(10,color=(0,0,0)).set_start(4).set_end(10)
summary_clip = TextClip(data["summary"],fontsize=50,color='white',bg_color="black").set_pos(("right","bottom")).margin(6,color=(0,0,0)).margin(right=0,bottom=20,opacity=0).set_start(10).set_end(20)



video = CompositeVideoClip([clip, date_clip])
video = CompositeVideoClip([video, title_clip])
video = CompositeVideoClip([video, summary_clip])
video.write_videofile("output2.mp4")
