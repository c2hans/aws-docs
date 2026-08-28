---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-iam-users-roles.html
---

# Creating IAM users or roles for the Amazon Chime SDK
<a name="create-iam-users-roles"></a>

You create users as IAM users, or in roles appropriate to your use case. You then assign the following policy to them. This ensures that you have the necessary permissions for the AWS SDK embedded in your server application. In turn, that allows you to perform lifecycle operations on the meeting and attendee resources.

```
   // Policy ARN:     arn:aws:iam::aws:policy/AmazonChimeSDK
    // Description:    Provides access to Amazon Chime SDK operations
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "chime:CreateMeeting",
                "chime:DeleteMeeting",
                "chime:GetMeeting",
                "chime:ListMeetings",
                "chime:CreateAttendee",
                "chime:BatchCreateAttendee",
                "chime:DeleteAttendee",
                "chime:GetAttendee",
                "chime:ListAttendees"
            ],
            "Effect": "Allow",
            "Resource": "*"
     }
 ]}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
