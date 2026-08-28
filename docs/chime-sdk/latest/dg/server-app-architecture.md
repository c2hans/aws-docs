---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/server-app-architecture.html
---

# Understanding server application architecture for the Amazon Chime SDK
<a name="server-app-architecture"></a>

When a server receives a request from a client, it first ensures that the user is authorized to start or join a meeting. The server uses the embedded AWS SDK in the language of choice to make [chime:CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html) and [chime:CreateAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html) API calls to the global media control plane. It does that to create the meeting and attendees in one of the supported AWS Regions. To make these requests, the service needs the appropriate IAM user or role. In turn, IAM users and roles need the [ AmazonChimeSDK ](https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_id-based-policy-examples.html) policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
