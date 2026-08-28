---
source_url: https://docs.aws.amazon.com/chime/latest/ug/event-mode-changes.html
---

# How meetings change when you turn on Event Mode
<a name="event-mode-changes"></a>

When you turn on Event Mode, the meeting changes in the following ways:
+ Hosts, delegates, or moderators automatically receive presenter permissions when they join the meeting.
+ The system mutes any attendees already in the meeting.
+ The system mutes attendees who join the meeting after you turn on Event Mode unless they join from an in-room video conference system. Attendees who join from a conference system can use their video conference device to mute themselves. Other attendees can also mute them in the Amazon Chime client.
+ Only presenters can share their screens, turn on their video, or mute other presenters.
+ Notifications don't appear for the following roster changes:
  + Attendees who join the meeting.
  + Attendees who leave the meeting.
  + Attendees who drop from the meeting.
+ Attendees who try to perform a restricted task receive a message that the host turned off the chosen action.
+ If attendees join from an in-room conference system with Event Mode on, Amazon Chime blocks content sharing and video. Other attendees can view videos only from presenters or from in-room conference systems that join before you turn Event Mode on.

  To let new conference rooms join with video or present, turn off Event Mode before the new room joins. If a room joins before you turn off Event Mode and wants to share media or video, they must leave and rejoin the meeting after you turn off Event Mode.
**Note**
If attendees join from an in-room conference system before you turn on Event Mode, they can use the conference system to share media and video.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
