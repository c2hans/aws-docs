---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_data_classification_identify_data.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC07-BP01 Identify the data within your workload
<a name="sec_data_classification_identify_data"></a>

 You need to understand the type and classification of data your workload is processing, the associated business processes, data owner, applicable legal and compliance requirements, where it’s stored, and the resulting controls that are needed to be enforced. This may include classifications to indicate if the data is intended to be publicly available, if the data is internal use only such as customer personally identifiable information (PII), or if the data is for more restricted access such as intellectual property, legally privileged or marked sensitive, and more. By carefully managing an appropriate data classification system, along with each workload’s level of protection requirements, you can map the controls and level of access or protection appropriate for the data. For example, public content is available for anyone to access, but important content is encrypted and stored in a protected manner that requires authorized access to a key for decrypting the content.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Consider discovering data using Amazon Macie: Macie recognizes sensitive data such as personally identifiable information (PII) or intellectual property.
  +  [Amazon Macie](https://aws.amazon.com/macie/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon Macie](https://aws.amazon.com/macie/)
+  [Data Classification Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html)
+  [Getting started with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html)

 **Related videos:**
+  [Introducing the New Amazon Macie](https://youtu.be/I-ewoQekdXE)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
