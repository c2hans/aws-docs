---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/data-security-and-risk-management.html
---

# Data security and risk management
<a name="data-security-and-risk-management"></a>

Within an AWS environment, you will probably have accounts with differing compliance and security requirements. For example, you might have a developer sandbox, and an account hosting the production environment for a highly regulated workload, such as processing payments. By isolating them into different accounts, you can [apply distinct security controls](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html#apply-distinct-security-controls-by-environment), [constrain access to sensitive data](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html#constrain-access-to-sensitive-data), and reduce the scope of audit for regulated workloads.

 Adopting a single standard for all workloads can lead to challenges. While many controls apply equally across an environment, some controls are excessive or irrelevant for accounts that don't need to meet specific regulatory frameworks, and accounts where no personal identifiable data will ever be present (for example, a developer sandbox, or workload development accounts). This typically leads to false positive security findings that must be triaged and closed with no action, which takes effort away from findings that should be investigated.

 *Table 11 – Example data security and risk management tags*

|  Use case  |  Tag Key  |  Rationale  |  Example Values  |
| --- | --- | --- | --- |
| Incident management  | example-inc:incident- management:escalationlog |  The system in use by the supporting team to log incidents  |  jira, servicenow, zendesk  |
| Incident management  | example-inc:incident- management:escalationpath |  Path of escalation  | ops-center, dev-ops, app-team  |
| Data classification  | example-inc:data:classification |  Classify data for compliance and governance  | Public, Private, Confidential, Restricted  |
| Compliance  | example-inc:compliance:framework |  Identifies the compliance framework the workload is subject to  | PCI-DSS, HIPAA  |

 Manually managing different controls across an AWS environment is both time consuming and error prone. The next step is to automate the deployment of appropriate security controls, and configure inspection of resources, based on the classification of that account. By applying tags to the accounts and the resources within them, the deployment of controls can be automated and configured appropriately for the workload.

**Example: **

 A workload includes an Amazon S3 bucket with the tag `example-inc:data:classification` with the value `Private`. The security tooling automation deploys AWS Config rule `s3-bucket-public-read-prohibited`, which checks the Amazon S3 bucket’s Block Public Access settings, the bucket policy, and the bucket access control list (ACL), confirming the bucket’s configuration is appropriate for its data classification. To ensure the content of the bucket is consistent with the classification, [Amazon Macie can be configured to check for personal identifiable information (PII)](https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-macie-supports-criteria-based-bucket-selection-sensitive-data-discovery-jobs/). The blog [Using Amazon Macie to Validate S3 Bucket Data Classification](https://aws.amazon.com/blogs/architecture/using-amazon-macie-to-validate-s3-bucket-data-classification/) explores this pattern in greater depth.

 Certain regulatory environments, such as insurance and healthcare, might be subject to mandatory data retention policies. Data retention using tags, combined with Amazon S3 Lifecycle policies, can be an effective and simple way to scope object transitions to a different storage tier. Amazon S3 Lifecycle rules can also be used to expire objects for data deletion after the mandatory hold period expires. Refer to [Simplify your data lifecycle by using object tags with Amazon S3 Lifecycle](https://aws.amazon.com/blogs/storage/simplify-your-data-lifecycle-by-using-object-tags-with-amazon-s3-lifecycle/) for an in-depth guide to this process.

 Additionally, when triaging or addressing security finding, tags can provide the investigator with important context that helps qualify the risk, and aids in engaging the appropriate teams to investigate or mitigate the finding.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
