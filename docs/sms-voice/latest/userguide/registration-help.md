---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/registration-help.html
---

# Registration support
<a name="registration-help"></a>

When you send A2P (application-to-person) SMS messages to US destinations through AWS End User Messaging SMS, your traffic must be registered with the appropriate number type. This guide helps you prepare and submit successful registrations, troubleshoot denials, and meet compliance requirements for your industry.

**Geographic scope**
The detailed guidance in this chapter is primarily written for US registration types (10DLC, Toll-Free, and Short Code) and the carrier compliance requirements that apply to US destinations. Canadian registrations follow very similar requirements. For other countries, the guidance on opt-in workflows, privacy policies, sample messages, and registration text fields is broadly applicable and helps ensure you provide complete, accurate information regardless of destination country.

## Registration types
<a name="registration-help-types"></a>

AWS End User Messaging SMS supports three US registration paths:
+ **US 10DLC** – Register a brand and campaign to send messages using standard 10-digit long codes. Required for most A2P messaging to US numbers.
+ **Toll-Free** – Register a toll-free number for messaging. Suitable for transactional and lower-volume use cases.
+ **Short Code** – Register a dedicated short code for high-volume messaging programs.

For general information about creating and managing registrations, see [Origination identity registration in AWS End User Messaging SMS](registrations.md).

## Before you begin
<a name="registration-help-before-you-begin"></a>

Before submitting a registration, ensure you have:

1. A clearly documented opt-in flow that captures explicit consumer consent for SMS messaging.

1. A privacy policy and terms of service published on your website.

1. Sample messages that accurately represent the content you will send.

1. A valid business website that matches your brand identity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
