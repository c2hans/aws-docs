---
source_url: https://docs.aws.amazon.com/chime/latest/ug/reschedule-meeting.html
---

# Rescheduling a meeting when the host leaves
<a name="reschedule-meeting"></a>

When meeting hosts leave their organizations, an administrator or a system such as Active Directory suspends their accounts and their meetings become inactive.

When that happens, auto-call stops working. However, recurring and individual meetings scheduled by that host may still appear in your calendar.

You can't create another meeting bridge ID for those inactive meetings, or use the former host's meeting ID. You must reschedule the meeting.

**To reschedule a meeting**

1. If the former host made you a delegate for the meeting, use your calendar app to cancel the meeting. If you aren't a delegate, go to step 2.

1. Create and schedule a new meeting, and invite the attendees from the old meeting. You can host the meeting, or ask someone else to host.

 For more information about canceling meetings, see [Canceling meetings](cancel-meeting.md). For more information about scheduling meetings, see the topics in [Scheduling meetings using Amazon Chime](chime-schedule-meetings.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
