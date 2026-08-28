---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompting-best-practices.html
---

# General best practices
<a name="prompting-best-practices"></a>

The following best practices mainly apply to the Amazon Nova text models, but you can apply them to other models, in addition to modality-specific best practices.

For more information on how to prompt multimodal inputs, refer to [Prompting multimodal inputs](prompting-multimodal.md). For information on how to prompt speech inputs, refer to [Voice conversation prompts](sonic-system-prompts.md).

## Understanding the roles
<a name="understanding-roles"></a>

Amazon Nova models allow you to structure prompts through the use of three distinct roles: system, user, and assistant.
+ **System (optional)** – Although not mandatory, it establishes the overall behavioral parameters of the assistant. It can also be utilized to provide additional instructions and guidelines that the user wishes the model to adhere to throughout the conversation.
+ **User** – Can optionally convey the context, tasks, instructions, and the desired outcome along with the user query.
+ **Assistant** – Aids in guiding the model towards the intended response.

**Topics**
+ [Understanding the roles](#understanding-roles)
+ [Create precise prompts](create-precise-prompts.md)
+ [Bring focus to sections of the prompt](prompting-bring-focus.md)
+ [Using the system role](prompting-system-role.md)
+ [Provide examples (few-shot prompting)](prompting-provide-examples.md)
+ [Tool calling systems](prompting-tools-function.md)
+ [Advanced prompting techniques](advanced-prompting-techniques.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
