---
source_url: https://docs.aws.amazon.com/chime/latest/ug/record-meeting.html
---

# Recording a meeting
<a name="record-meeting"></a>

Meeting organizers, delegates, and moderators can record meetings. Recordings have the following limitations:
+ You can record audio and screen sharing for up to 12 hours.
+ Amazon Chime only records video when someone shares their screen. Any parts of a meeting without a screen share appear as blank during playback.
+ Amazon Chime doesn't record any attendee video tiles. That includes host, moderator, and delegate tiles.
+ You can only start to record a meeting after it begins.

**To record a meeting**

1. At the bottom of the left control bar, choose the **Record meeting** icon ( ![A rectangular icon showing REC.](http://docs.aws.amazon.com/chime/latest/ug/images/icon-record-meeting.png) ).

1. To stop recording, choose the **Record meeting** icon again.

Amazon Chime processes the recording as soon as you stop recording the meeting. By default, the system creates MP4 files for meetings with screen sharing, and MP4a files for meetings without screen sharing. The processing time varies based on the length of the recording. Once processing ends, Amazon Chime sends you a chat message in regular chat with a link to the recording. For security reasons, Amazon Chime packages the file as a download and places it in your device's downloads folder.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
