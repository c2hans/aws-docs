---
source_url: https://docs.aws.amazon.com/chime/latest/ug/lock-actions.html
---

# Locking a meeting
<a name="lock-actions"></a>

Hosts, moderators, and delegates can lock meetings. When you lock a meeting, removed attendees can't rejoin the meeting. Also, uninvited and unauthenticated users can't join a locked meeting.

**To lock a meeting**

1. In the left control bar, choose the **More options** menu (![An icon of a horizontal ellipsis.](http://docs.aws.amazon.com/chime/latest/ug/images/left-control-6.png)).

1. Choose **Lock meeting**

The following rules apply to your meeting when you lock the meeting:
+ If an attendee doesn't have an Amazon Chime account, or wasn't invited to the meeting, they receive a message that the meeting is locked if they try to join.
+ If an invited attendee signs into their Amazon Chime account, they can join the locked meeting. They can also drop and reconnect after you lock the meeting.
+ An attendee can join a locked meeting from an in-room conference system, or with the **Dial-in** or **Switch to dial-in** options. However, they must enter the 13-digit meeting ID from the Amazon Chime desktop or mobile client, or from the Amazon Chime web app.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
