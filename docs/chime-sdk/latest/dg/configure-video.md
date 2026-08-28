---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-video.html
---

# Configuring the video folder for Amazon Chime SDK media capture pipelines
<a name="configure-video"></a>

The video folder contains 5-second MP4 files that contain video streams, plus content share streams if they’re specified in the API request. Each file name contain a <yyyy-mm-dd-hour-min-seconds-milleseconds>-<attendeeID> timestamp with an attendee ID. The content share video chunk is appended as <yyyy-mm-dd-hour-min-seconds-milleseconds>-<attendeeID>\#content.mp4. You can configure the folder to only contain video artifacts.

```
"ArtifactsConfiguration": {
         "Audio": {
            "MuxType": "AudioOnly"
         },
         "Content": {
            "State": "Disabled"
         },
         "Video": {
            "MuxType": "VideoOnly"
            "State": "Enabled"
         }
      }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
