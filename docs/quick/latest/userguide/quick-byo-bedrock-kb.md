---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/quick-byo-bedrock-kb.html
---

# Bring your own Amazon Bedrock managed knowledge base
<a name="quick-byo-bedrock-kb"></a>

Amazon Quick can connect Amazon Bedrock managed knowledge bases as knowledge sources. After connection, a managed knowledge base is treated like any other knowledge base in Amazon Quick. You can add it to spaces and it is queried automatically during chat. You can connect up to 2 managed knowledge bases per Amazon Quick instance. The managed knowledge base can live in the same AWS account as Amazon Quick or in a different account.

**Topics**
+ [Prerequisites](byo-bedrock-kb-prerequisites.md)
+ [Setting up permissions](byo-bedrock-kb-permissions.md)
+ [Creating knowledge bases from Amazon Bedrock managed knowledge bases](byo-bedrock-kb-creating.md)
+ [Access control list (ACL) support](byo-bedrock-kb-acl.md)
+ [Billing](byo-bedrock-kb-billing.md)
+ [Limitations](byo-bedrock-kb-limitations.md)
+ [Security best practices](byo-bedrock-kb-security.md)
+ [Monitoring and observability](byo-bedrock-kb-monitoring.md)
+ [Troubleshooting](byo-bedrock-kb-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
