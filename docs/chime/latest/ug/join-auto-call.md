---
source_url: https://docs.aws.amazon.com/chime/latest/ug/join-auto-call.html
---

# Joining an auto-call meeting
<a name="join-auto-call"></a>

You can use the desktop client and web app to join an auto-call meeting.

Meeting organizers create auto-call meetings by adding **meet@chime.aws** to the list of meeting attendees. When a meeting is set to auto-call, attendees receive a prompt just before meeting time to join or decline the meeting.

**To join an auto-call meeting**

1. When Amazon Chime calls you, choose **Join**.

1. (Optional) In the **Device preview** dialog box, use the options under **Video settings** and **Audio settings** to change your video and audio sources. For more information choosing video and audio settings, see [Setting video and audio sources](set-video-audio.md).

1. Choose an option for joining the meeting:
   + **Join** – Adds you to the meeting with just audio.
   + **Join with video** – Adds you to the meeting with audio and video.
   + **Use a conference room for audio** – Uses a conference room audio system that's compatible with Amazon Chime to add the room to the meeting.
   + **Use a phone for audio** – Call into the meeting from a cell phone, landline phone, or from a conference room audio system that isn't compatible with Amazon Chime.

**Note**
Moderated meetings only start when a moderator or a delegate joins the meeting. If you have the moderator passcode, choose **Enter moderator passcode** to join as a moderator and start the meeting. For more information, see [Scheduling moderated meetings](moderate-meeting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
