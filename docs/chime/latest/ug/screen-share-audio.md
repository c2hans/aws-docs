---
source_url: https://docs.aws.amazon.com/chime/latest/ug/screen-share-audio.html
---

# Playing videos while sharing your screen
<a name="screen-share-audio"></a>

When you play a video while sharing your screen, other meeting attendees can see the video, but they can't hear the audio. Why? By design, Amazon Chime only captures and distributes audio from microphones.

To include audio with a video, you can use the following tools to redirect the audio as a mic input to Amazon Chime.
+ OBS and a virtual camera: [https://streamlabs.com/streamlabs-obs](https://streamlabs.com/streamlabs-obs).
+ VB Cable: [https://vb-audio.com/Cable/index.htm](https://vb-audio.com/Cable/index.htm).
+ An HDMI to USB adapter cable. You route the signal out from HDMI and back in via USB.
+ Loopback: [https://rogueamoeba.com/loopback/](https://rogueamoeba.com/loopback/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
