---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/byo-bedrock-kb-acl.html
---

# Access control list (ACL) support
<a name="byo-bedrock-kb-acl"></a>

Amazon Bedrock managed knowledge bases with ACL-enabled data source connectors support document-level access control. When a user queries the knowledge base, Amazon Quick automatically passes the user's identity to Amazon Bedrock. Amazon Bedrock then filters retrieval results so that users only see documents they are authorized to access in the original data source.

No additional configuration is required in Amazon Quick to enable ACL support. The access control rules are configured on the Amazon Bedrock managed knowledge base data source connectors. See [Connect a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-connect-ds.html) in the *Amazon Bedrock User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
