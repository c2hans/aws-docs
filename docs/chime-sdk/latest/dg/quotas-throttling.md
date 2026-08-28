---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/quotas-throttling.html
---

# Verifying SDK quotas and API throttling for Amazon Chime SDK meetings
<a name="quotas-throttling"></a>

The [Amazon Chime SDK endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/chime-sdk.html) page lists the service quotas, API rates, and whether you can adjust them. Use the [AWS Console Service Quota](https://console.aws.amazon.com/servicequotas/home/services/chime/quotas) page to request quota adjustments.

**Fine tuning your API rates**
Applications that exceed their API rates receive HTTP Status Code 429 and `ThrottledClientException` messages. You can adjust your API rates, but before you do, check your application for bugs that may exhaust those rates. For example, you may create meetings in a loop, or create meetings and not clean up.

Depending on how you create meetings, you might need to modify your code. For example, you can replace `CreateMeeting` and `CreateAttendee` with:
+ [CreateMeetingWithAttendees](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeetingWithAttendees.html) – Creates up to 10 attendees per meeting.
+ [BatchCreateAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html) – Creates up to 100 attendees per meeting.

You can store created attendees in a database, pull attendee information as invitees join the meeting, and then associate them with the pre-created attendees.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
