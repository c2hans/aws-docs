---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/disconnect-hang-up.html
---

# Flow block in Connect Customer: Disconnect / hang up
<a name="disconnect-hang-up"></a>

This topic defines the flow block for disconnecting a contact at the end of a call.

## Description
<a name="disconnect-hang-up-description"></a>
+ Disconnects the contact.

## Supported channels
<a name="disconnect-hang-up-channels"></a>

The following table lists how this block routes a contact that is using the specified channel.

| Channel | Supported? |
| --- | --- |
| Voice | Yes |
| Chat | Yes |
| Task | Yes |
| Email | Yes |

## Flow types
<a name="disconnect-hang-up-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ Inbound flow
+ Customer queue flow
+ Transfer to Agent flow
+ Transfer to Queue flow

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
