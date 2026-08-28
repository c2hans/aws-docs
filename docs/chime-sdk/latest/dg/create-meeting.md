---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-meeting.html
---

# Creating a meeting for the Amazon Chime SDK
<a name="create-meeting"></a>

A [CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html) API call accepts a required parameter, the `ClientRequestToken`, that allows developers to pass in a uniqueness context. It also accepts optional parameters such as `MediaRegion`, which represents the media services data plane region to choose for the meeting, the `MeetingHostId` used to pass in an opaque identifier to represent the meeting host, if applicable, and the `NotificationsConfiguration` for receiving meeting lifecycle events. By default, Amazon EventBridge delivers the events. Optionally, you can also receive events by passing an SQS queue ARN or an SNS Topic ARN in `NotificationsConfiguration`. The API Returns a Meeting object that contains a unique `MeetingId`, plus the `MediaRegion` and the `MediaPlacement` object with a set of media URLs.

```
   meeting = await chime.createMeeting({
                ClientRequestToken: clientRequestToken,
                MediaRegion: mediaRegion,
                MeetingHostId: meetingHostId,
                NotificationsConfiguration: {
                   SqsQueueArn: sqsQueueArn,
                   SnsTopicArn: snsTopicArn
                }
            }).promise();
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
