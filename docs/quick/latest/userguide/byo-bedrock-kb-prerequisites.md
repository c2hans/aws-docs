---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/byo-bedrock-kb-prerequisites.html
---

# Prerequisites
<a name="byo-bedrock-kb-prerequisites"></a>
+ A Amazon Bedrock managed knowledge base that has been created and configured. For more information, see [Build a managed knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-build-managed.html) in the *Amazon Bedrock User Guide*.
+ The managed knowledge base and the Amazon Quick instance are in the same AWS Region.
+ Administrator-level permissions in Amazon Quick to manage AWS resource integrations.
+ For cross-account setups: the ability to attach a resource policy to the knowledge base, or coordination with the knowledge base owner to attach the policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
