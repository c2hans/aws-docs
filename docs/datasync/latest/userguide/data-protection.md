---
source_url: https://docs.aws.amazon.com/datasync/latest/userguide/data-protection.html
---

# Data protection in AWS DataSync
<a name="data-protection"></a>

AWS DataSync securely transfers data between self-managed storage systems and AWS storage services and also between AWS storage services. How your storage data is encrypted in transit depends in part on the locations involved in the transfer.

After the transfer completes, data is encrypted at rest by the system or service that's storing the data (not DataSync).

**Topics**
+ [AWS DataSync encryption in transit](encryption-in-transit.md)
+ [AWS DataSync encryption at rest](encrypting-data.md)
+ [Internetwork traffic privacy](internetwork-traffic-privacy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
