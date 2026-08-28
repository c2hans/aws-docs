---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connectors.html
---

# Managing Amazon Chime SDK Voice Connectors
<a name="voice-connectors"></a>

**What is an Amazon Chime SDK Voice Connector?**
An Amazon Chime SDK Voice Connector provides Session Initiation Protocol (SIP) trunking service for your existing phone system. You can manage your Voice Connectors from the Amazon Chime SDK console and access it over your internet connection, or you can use AWS Direct Connect. For more information, see [What is Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) in the *Direct Connect User Guide*.

**Important**
Voice Connectors do not support SMS.

**Voice Connector outbound and inbound calling**
After you create a Voice Connector, edit the termination and origination settings to allow outbound or inbound calls, or both. You then assign phone numbers to the Voice Connector. You can use the Amazon Chime SDK console to port in existing phone numbers or provision new phone numbers. For more information, see [Porting existing phone numbers](porting.md), [Provisioning phone numbers](provision-phone.md), and [Assigning and unassigning Amazon Chime SDK Voice Connector phone numbers](assign-voicecon.md).

**Note**
Amazon Chime SDK Voice Connectors have outbound international calling restrictions. For more information, refer to [Outbound calling restrictions](outbound-call-restrictions.md).
Voice Connectors support outbound calling in E.164 format and do not require an international dialing access code, such as 011. You pay a per-minute rate based on the destination country of the call. For a current list of supported countries, and the per-minute rate for each country, see [ https://aws.amazon.com/chime/voice-connector/pricing/](https://aws.amazon.com/chime/voice-connector/pricing/). Voice Connector PSTN calling does not support private numbering schemes such as 4, 5, or 6-digit extension numbers.

**Voice Connector groups**
You can also create an Voice Connector group and add Voice Connectors to it. You can use Voice Connectors created in different AWS Regions. This creates a fault-tolerant mechanism for fallback if availability events occur. For more information, see [Managing Amazon Chime SDK Voice Connector groups](voice-connector-groups.md).

**Logging and monitoring Voice Connector data**
Optionally, you can send logs from your Voice Connector to CloudWatch Logs, and turn on media streaming from your Amazon Chime SDK Voice Connector to Amazon Kinesis. For more information, see [CloudWatch logs for the Amazon Chime SDK](monitoring-cloudwatch.md#cw-logs) and [Streaming Amazon Chime SDK Voice Connector media to Kinesis](start-kinesis-vc.md).

**Topics**
+ [Before you begin](#vc-prereq)
+ [Creating an Amazon Chime SDK Voice Connector](create-voicecon.md)
+ [Using tags with Voice Connectors](use-tags-voice-con.md)
+ [Editing Amazon Chime SDK Voice Connector settings](edit-voicecon.md)
+ [Assigning and unassigning Amazon Chime SDK Voice Connector phone numbers](assign-voicecon.md)
+ [Deleting an Amazon Chime SDK Voice Connector](delete-voicecon.md)
+ [Configuring Voice Connectors to use call analytics](configure-voicecon.md)
+ [Managing Amazon Chime SDK Voice Connector groups](voice-connector-groups.md)
+ [Streaming Amazon Chime SDK Voice Connector media to Kinesis](start-kinesis-vc.md)
+ [Using Amazon Chime SDK Voice Connector configuration guides](config-guides.md)

## Before you begin
<a name="vc-prereq"></a>

To use an Amazon Chime SDK Voice Connector, you must have an IP Private Branch Exchange (PBX), Session Border Controller (SBC), or other voice infrastructure with internet access that supports Session Initiation Protocol (SIP). Make sure that you have enough bandwidth to support peak call volume. For information about bandwidth requirements, see [Bandwidth requirements](network-config.md#bandwidth).

To ensure security for calls sent from AWS to your on-premises phone system, we recommend configuring an SBC between AWS and your phone system. Allow list SIP traffic to the SBC from the Amazon Chime SDK Voice Connector signaling and media IP addresses. For more information, see the recommended ports and protocols for [Amazon Chime SDK Voice Connector](network-config.md#cvc).

Amazon Chime SDK Voice Connectors expect phone numbers to be in E.164 format.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
