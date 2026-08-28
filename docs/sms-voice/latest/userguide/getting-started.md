---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/getting-started.html
---

# Getting started with AWS End User Messaging SMS
<a name="getting-started"></a>

This topic shows you how to use the AWS End User Messaging SMS console to manage phone numbers, sender IDs, pools, and configuration sets, and then send test SMS messages. We recommend you use simulator phone numbers to test both sending and receiving an SMS message. The [workshop](https://catalog.workshops.aws/build-sms-program/en-US) is targeted for developers and technical individuals who are comfortable using the AWS Command Line Interface (AWS CLI) to run API commands. For more information about SMS, MMS, or origination identity pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

**Note**
When you set up a new AWS End User Messaging SMS account, it is placed in a sandbox for SMS, MMS, and voice message channels until you request production access. In the sandbox, you can access all of features of AWS End User Messaging SMS, with restrictions on your SMS, MMS, and voice messages.
For information about the SMS/MMS sandbox restrictions, see [The AWS End User Messaging SMS SMS/MMS sandbox](sandbox.md#sandbox-sms).
For information about the voice sandbox restrictions, see [AWS End User Messaging SMS Voice sandbox](sandbox.md#sandbox-voice).
When you're ready to move from the sandbox to production, create an AWS Support case for a **Service limit increase** request for each channel that you want to move.

**Tip**
If you want to send OTP or verification messages without managing phone numbers, you can use Notify. Notify lets you send templated messages using AWS-managed origination identities. For more information, see [What is AWS End User Messaging Notify?](notify.md).

**Tip**
To send rich, interactive messages over RCS (Rich Communication Services), including rich cards, carousels, media files, and interactive suggestions, set up an RCS agent and use the `SendRcsMessage` API action. For more information, see [Getting started with RCS](rcs-getting-started.md) and [Sending rich RCS messages](rcs-rich-messaging.md).

**Topics**
+ [First time user tutorial](getting-started-tutorial.md)
+ [Add a verified destination phone number](verify-destination-phone-number.md)
+ [SMS/MMS and Voice sandbox](sandbox.md)
+ [Message part preview](getting-started-mpp.md)
+ [Simulator phone numbers](test-phone-numbers.md)
+ [Set a spending limit](spend-limit.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
