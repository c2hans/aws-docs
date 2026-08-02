---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-audio.html
---

# Configuring the audio folder for Amazon Chime SDK media capture pipelines
<a name="configure-audio"></a>

The audio folder contains 5-second MP4 files of the mixed audio stream, meaning they contain audio from all attendees, plus the active speaker’s video. The folder contains files for the entire meeting. As desired, you can configure the folder to contain just the audio artifacts. Each file name contains a *yyyy-mm-dd-hour-min-seconds-milleseconds* timestamp. The timestamp is in UTC, and it marks the start time. You can configure the folder to only contain audio artifacts.

```
"ArtifactsConfiguration": {
         "Audio": {
            "MuxType": "AudioOnly"
         },
         "Content": {
            "State": "Disabled"
         },
         "Video": {
            "State": "Disabled"
         }
      }
```
