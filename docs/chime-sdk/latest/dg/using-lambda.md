---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/using-lambda.html
---

# Understanding phone numbers, SIP rules, SIP media applications, and AWS Lambda functions for Amazon Chime SDK PSTN audio
<a name="using-lambda"></a>

Before you can use the PSTN audio service, an Amazon Chime SDK administrator must provision your phone numbers and create managed objects called SIP rules and SIP media applications. You can use the Amazon Chime SDK console or the AWS SDK to provision phone numbers, and to provision the SIP rule and SIP media application managed objects.

This image shows the relationship between the managed objects that comprise the PSTN audio service. Numbers in the image correspond to numbers in the text below the image.

![Managed objects in the Amazon Chime SDK PSTN audio service.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/pstn-diagram2.png)

You can only assign phone numbers and Amazon Chime SDK Voice Connectors (1) to SIP rules (2). Also, you must provision the phone number or Voice Connector in your PSTN audio service. Upon receiving an inbound call to a phone number, or an outbound call request from a Voice Connector, the SIP rule invokes a SIP media application and an associated AWS Lambda function (4). The AWS Lambda function runs a predefined set of actions, such as playing on-hold music or joining a meeting. To provide multi-region resiliency, SIP rules can specify alternate target SIP media applications in different AWS Regions (3) by order of priority for failover. If one target fails, the PSTN audio service tries the next one and so on. Note that each alternate target must reside in a different AWS Region.

In addition, multiple SIP media applications can invoke a given AWS Lambda function. Put another way, when you create an AWS Lambda function, any SIP media application can use that function.

For more information about provisioning SIP media applications and rules, see [Managing SIP media applications and rules](https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html) in the *Amazon Chime SDK Administrator Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
