---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-api.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Managing admin controls and guardrails using APIs
<a name="guardrails-api"></a>

Amazon Q Business supports admin controls and guardrails configuration through both the console and the APIs.

| API action | API description | Relevant User Guide topic |
| --- | --- | --- |
| [UpdateChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateChatControlsConfiguration.html) | Updates an set of chat controls configured for an existing Amazon Q Business application | +  [Customizing global controls](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html#guardrails-global-controls-customizing) <br />+  [Creating topic controls](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-topic-controls.html#guardrails-topic-controls-customizing)  |
| [DeleteChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteChatControlsConfiguration.html) | Deletes chat controls configured for an existing Amazon Q Business application | [Deleting topic controls](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-management.html) |
| [GetChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatControlsConfiguration.html) | Gets information about chat controls configured for an existing Amazon Q Business application. |  [Getting topic control properties](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-management.html#topic-control-properties) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
