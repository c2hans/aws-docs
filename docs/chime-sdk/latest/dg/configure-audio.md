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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
