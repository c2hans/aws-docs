---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/data-protection.html
---

# Data protection
<a name="data-protection"></a>

| AOSSEC03: How do you protect your data, indices, and documents? |
| --- |
|   |

 To protect the security and integrity of your data, indices, and documents on OpenSearch Service, it's essential to implement robust security measures. Fine-grained access control in OpenSearch Service provides additional control over data access. For instance, you can tailor search results based on the requester, displaying results from specific indexes or concealing certain fields in documents.

**Topics**
+ [AOSSEC03-BP01 Implement fine-grained access control to manage access to your data on Amazon OpenSearch Service](aossec03-bp01.md)
+ [AOSSEC03-BP02 Secure your indices, documents, and fields using fine-grained access control](aossec03-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
