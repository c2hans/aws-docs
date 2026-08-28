---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-1-how-is-māori-data-protected.html
---

# MD\_SEC 1: How is Māori data protected?
<a name="md_sec-1-how-is-māori-data-protected"></a>

 Systems designed to capture, store, or process Māori data should follow the same best practice as any other cloud solution in that they should be designed, built, and operated with security in mind. The Security Pillar of the Well-Architected Framework provides in-depth, best practice guidance for architecting secure workloads. The [Data protection](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-dataprot.html) best practice area in the Security Pillar provides best practices relating to data classification, protecting data at rest, and protecting data in transit. Data protection is just one aspect of securing your cloud architectures. Security should be applied at all layers through multiple controls using a defence-in-depth approach. In addition to the best practices contained in the Security Pillar, the following considerations may also apply:
+  **MD\_SEC01-BP01: Design storage systems to handle data with different Māori data classifications.** If the data is considered tapu and that is feedback you have received from your customers, then it may be appropriate to apply additional controls and procedures. These may be required to support specific tikanga related to the handling of certain data. You may choose to store certain data separately from other data with different security requirements for access and processing. It is possible, for example, to store data in separate virtual private clouds (VPC), separate databases, or separate object storage buckets. This separation of datasets means you can apply independent security controls, such as different access permissions, different logging and auditing levels, and different backup approaches.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
