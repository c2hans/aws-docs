---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/maintenance.html
---

# Patching and upgrading
<a name="maintenance"></a>

One benefit of Amazon RDS for Oracle is the ease of maintenance. AWS does all the undifferentiated heavy lifting work behind the scenes so that your attention can be on applications and users. You can enable maintenance options during setup. Amazon RDS for Oracle will then automatically apply operating system (OS) patching, Oracle database patching, and minor database version upgrades in a predefined maintenance window.

With Amazon RDS Custom for Oracle, because you have database administrator privileges and operating system root access, you're responsible for patching and upgrade activities instead of AWS.

|
|
| Responsibility | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| Automatic OS patching | Yes | No |
| Automatic Oracle patching | Yes | No |
| Automatic minor Oracle version upgrades | Yes | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
