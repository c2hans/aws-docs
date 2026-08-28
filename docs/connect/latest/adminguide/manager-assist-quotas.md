---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/manager-assist-quotas.html
---

# Service quotas
<a name="manager-assist-quotas"></a>

The following quotas apply during preview. These quotas might change as the capability matures, so check this page for updates.

## Quotas
<a name="manager-assist-quotas-list"></a>

| Quota | Default value | Scope | Adjustable |
| --- | --- | --- | --- |
| Maximum message length | 15,000 characters | Per message | No |
| Request rate | Subject to the Connect Customer agent assist `SendMessage` rate quota, which varies by AWS Region | Per account, per Region | Yes, through AWS Support |
| Chat context | Responses reflect the recent turns in a chat. In a very long chat, the earliest turns are no longer referenced. | Per chat | No |

## Behavior when a quota is reached
<a name="manager-assist-quotas-behavior"></a>

| Quota reached | Behavior |
| --- | --- |
| Message length (15,000 characters) | The message box shows a character count, and you cannot submit the message until you shorten it. |
| Request rate | Additional questions are throttled and return a rate limit error. Wait a moment, and then try again. |
| Chat context | Responses no longer reflect the earliest turns in the chat. Provide the relevant context in your next message. |

## Request a quota increase
<a name="manager-assist-quotas-increase"></a>

The request rate is the only adjustable quota. Because it is governed by the Connect Customer agent assist `SendMessage` service quota, request an increase through AWS Support rather than in the Service Quotas console. The maximum message length and chat context quotas are fixed application quotas during preview, and cannot be increased.

## Regional differences
<a name="manager-assist-quotas-regional"></a>

The request rate varies by AWS Region. The maximum message length and chat context behavior are the same in all Regions where manager assist is available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
