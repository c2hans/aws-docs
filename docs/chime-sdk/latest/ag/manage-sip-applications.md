---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html
---

# Managing SIP media applications
<a name="manage-sip-applications"></a>

**Note**
Amazon Chime SDK SIP media applications will no longer be open to new customers starting October 29, 2026. If you would like to use SIP media applications, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [SIP media applications service change](sip-applications-service-change.md).

You can use the Amazon Chime SDK console to create Session Initiation Protocol (SIP) media applications. SIP media applications make it easier and faster for you to create custom signaling and media instructions that you would normally build on your private branch telephone exchange (PBX).

You also use the console to create SIP rules. SIP rules specify how a SIP media application can connect to an Amazon Chime SDK meeting. Calls can go to and from public DID or toll-free phone numbers that are provisioned from your Amazon Chime SDK inventory, or to and from a Request URI hostname, the name assigned to an Amazon Chime SDK Voice Connector. The Amazon Chime SDK runs the SIP rules when a user places or receives a call. For information about using SIP rules, refer to [Managing SIP rules](use-sip-rules.md).

You must be an AWS Lambda user before you can create SIP media applications. The SIP media applications use Lambda functions for the following reasons:
+ You can write complex logic that involves decision-making. For example, a caller can use a touchtone phone to dial in to a meeting. In turn, that phone number triggers Lambda functions that ask for a meeting PIN and route the caller to the correct meeting.
+ You can deploy Lambda functions without a server infrastructure.

For more information about AWS Lambda, see [Getting started with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html).

**Note**
Amazon Chime SDK SIP media applications have outbound international calling restrictions. For more information, refer to [Outbound calling restrictions](outbound-call-restrictions.md).

**Topics**
+ [Understanding SIP applications and rules](understand-sip-data-models.md)
+ [SIP media applications service change](sip-applications-service-change.md)
+ [Using SIP media applications](use-sip-apps.md)
