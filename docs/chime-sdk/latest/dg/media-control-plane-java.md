---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/media-control-plane-java.html
---

# Understanding the Amazon Chime SDK media control plane
<a name="media-control-plane-java"></a>

The Amazon Chime SDK media control plane is global – hosted out of us-east-1 – and serves the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html) and [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html) APIs used to create and manage meeting and attendee resources across the data plane. It validates credentials and ensures the session is bootstrapped in the data plane in the requested region.

The control plane also triggers [ Amazon Chime SDK Events ](https://docs.aws.amazon.com/chime-sdk/latest/ag/automating-chime-with-cloudwatch-events.html) to the notification mechanisms such as Amazon EventBridge, Amazon Simple Queueing Service (SQS) or Amazon Simple Notification Service (SNS). AWS constantly monitors the services, and they scale automatically as load increases. The APIs are designed to only accept opaque user identifiers and not user data, so they adhere to data-sovereignty requirements.
