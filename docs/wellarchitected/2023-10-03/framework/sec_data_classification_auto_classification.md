---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_data_classification_auto_classification.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC07-BP03 Automate identification and classification
<a name="sec_data_classification_auto_classification"></a>

 Automating the identification and classification of data can help you implement the correct controls. Using automation for this instead of direct access from a person reduces the risk of human error and exposure. You should evaluate using a tool, such as [Amazon Macie](https://aws.amazon.com/macie/), that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. Amazon Macie recognizes sensitive data, such as personally identifiable information (PII) or intellectual property, and provides you with dashboards and alerts that give visibility into how this data is being accessed or moved.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use Amazon Simple Storage Service (Amazon S3) Inventory: Amazon S3 inventory is one of the tools you can use to audit and report on the replication and encryption status of your objects.
  +  [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html)
+  Consider Amazon Macie: Amazon Macie uses machine learning to automatically discover and classify data stored in Amazon S3.
  +  [Amazon Macie](https://aws.amazon.com/macie/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon Macie](https://aws.amazon.com/macie/)
+  [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html)
+  [Data Classification Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html)
+  [Getting started with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html)

 **Related videos:**
+  [Introducing the New Amazon Macie](https://youtu.be/I-ewoQekdXE)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
