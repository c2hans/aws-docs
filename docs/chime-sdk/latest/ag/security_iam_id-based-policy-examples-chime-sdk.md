---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_id-based-policy-examples-chime-sdk.html
---

# AWS managed Amazon Chime SDK policy
<a name="security_iam_id-based-policy-examples-chime-sdk"></a>

You use the AWS managed `AmazonChimeVoiceConnectorServiceLinkedRolePolicy` to grant users access to Amazon Chime SDK actions. For more information, see [Example IAM roles](https://docs.aws.amazon.com/chime/latest/dg/iam-roles.html) in the *Amazon Chime SDK Developer Guide*, and [Actions, resources, and condition keys for Amazon Chime](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html) in the *Service Authorization Reference*.

```
// Policy ARN: arn:aws:iam::aws:policy/AmazonChimeSDK
// Description: Provides access to Amazon Chime SDK operations
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "chime:CreateMediaCapturePipeline",
                "chime:CreateMediaConcatenationPipeline",
                "chime:CreateMediaLiveConnectorPipeline",
                "chime:CreateMeeting",
                "chime:CreateMeetingWithAttendees",
                "chime:DeleteMediaCapturePipeline",
                "chime:DeleteMediaPipeline",
                "chime:DeleteMeeting",
                "chime:GetMeeting",
                "chime:ListMeetings",
                "chime:CreateAttendee",
                "chime:BatchCreateAttendee",
                "chime:DeleteAttendee",
                "chime:GetAttendee",
                "chime:GetMediaCapturePipeline",
                "chime:GetMediaPipeline",
                "chime:ListAttendees",
                "chime:ListAttendeeTags",
                "chime:ListMediaCapturePipelines",
                "chime:ListMediaPipelines",
                "chime:ListMeetingTags",
                "chime:ListTagsForResource",
                "chime:StartMeetingTranscription",
                "chime:StopMeetingTranscription",
                "chime:TagAttendee",
                "chime:TagMeeting",
                "chime:TagResource",
                "chime:UntagAttendee",
                "chime:UntagMeeting",
                "chime:UntagResource"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```
