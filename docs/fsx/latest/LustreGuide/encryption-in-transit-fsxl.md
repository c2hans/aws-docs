---
source_url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-in-transit-fsxl.html
---

# Encrypting data in transit
<a name="encryption-in-transit-fsxl"></a>

Scratch 2 and persistent file systems can automatically encrypt data in transit when the file system is accessed from Amazon EC2 instances that support encryption in transit, and also for all communications between hosts within the file system. To learn which EC2 instances support encryption in transit, see [Encryption in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) in the *Amazon EC2 User Guide*.

For a list of AWS Regions in which Amazon FSx for Lustre is available, see [Deployment type availability](using-fsx-lustre.md#persistent-deployment-regions).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
