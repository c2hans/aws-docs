---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech-bp-sysrole.html
---

# System role adaptation
<a name="prompting-speech-bp-sysrole"></a>

**Note**
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Speech-to-Speech prompt engineering guide, visit [Voice conversation prompts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html).

Amazon Nova text models benefit from [clear role definitions](https://docs.aws.amazon.com/nova/latest/userguide/prompting-system-role.html). For Amazon Nova Sonic applications, consider the following:
+ Define roles that sound natural when speaking (such as, "friendly advisor" rather than "information retrieval system").
+ Use role descriptions that emphasize conversational attributes (warm, patient, concise) rather than text-oriented attributes (detailed, comprehensive, systematic).
+ Consider how the chosen voice might influence the perceived personality. Test the voices to chose the best voice for your use case. Review the [System prompt authoring guidelines and examples](prompting-speech-speech.md) section for techniques on how to indirectly influence the model's natural prosody.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
