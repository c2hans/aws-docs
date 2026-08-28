---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/understand-sip-data-models.html
---

# Understanding SIP applications and rules
<a name="understand-sip-data-models"></a>

To use the Session Initiation Protocol (SIP) with the Amazon Chime SDK, you create SIP media applications and SIP rules. You create both in the Amazon Chime SDK console.

The following diagram shows how the applications and rules work. It shows how SIP rules can route calls from phone numbers and Request URI hostnames to different SIP applications.

Numbers in the image correspond to numbers in the text below the image.

![SIP rules triggering SIP media applications in priority order; SIP applications invoking Lambda functions in the Amazon Chime SDK PSTN Audio service.](http://docs.aws.amazon.com/chime-sdk/latest/ag/images/pstn-diagram2.png)

You can only assign phone numbers from your Chime inventory and Voice Connectors (1) to SIP rules (2). Also, you must provision a phone number or Amazon Chime SDK Voice Connector in your PSTN Audio service, and the steps in [Creating a SIP media application](create-sip-app.md) explain how to do that. Upon receiving a call to a phone number, the SIP rule invokes a SIP media application and its associated Lambda function (4). The Lambda function runs code that invokes actions, such as playing on-hold music or joining a meeting, or muting a call. To provide multi-region resiliency, SIP rules (2) can specify alternate target SIP media applications in different AWS regions (3) by order of priority for failover. If one target fails, the PSTN Audio service tries the next one. Note that each alternate target must reside in a different AWS Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
