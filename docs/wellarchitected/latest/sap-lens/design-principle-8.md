---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-8.html
---

# 8 – Protect your SAP data at rest and in transit
<a name="design-principle-8"></a>

 **How do you protect your SAP data?** SAP systems often run the core functions within a business and store sensitive enterprise data. Best practice is to encrypt data at rest and in transit using at least one encryption mechanism to meet internal or external security requirements and controls. In addition to the controls listed in the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS provides multiple encryption solutions. Many AWS services have features which allow you to enable encryption with minimal effort and performance impact. There are encryption options available for the database and SAP application layer that you can consider.

| ID | Priority | Best Practice |
| --- | --- | --- |
| ☐ BP 8.1 | Highly Recommended | Encrypt data at rest |
| ☐ BP 8.2 | Highly Recommended | Encrypt data in transit |
| ☐ BP 8.3 | Highly Recommended | Secure your data recovery mechanisms to protect against threats |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
