---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/byo-bedrock-kb-limitations.html
---

# Limitations
<a name="byo-bedrock-kb-limitations"></a>
+ This feature is available in the following AWS Regions: US East (N. Virginia), US West (Oregon), Europe (Ireland), and Asia Pacific (Sydney).
+ You can connect up to 2 managed knowledge bases per Amazon Quick instance.
+ The managed knowledge base and Amazon Quick instance must be in the same AWS Region.
+ Only Amazon Bedrock managed knowledge bases are supported. Custom knowledge bases with self-managed vector stores are not supported.
+ Cross-account access requires a resource policy on the knowledge base.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
