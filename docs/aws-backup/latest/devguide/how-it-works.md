---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/how-it-works.html
---

# AWS Backup: How it works
<a name="how-it-works"></a>

AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backing up of data across AWS services. With AWS Backup, you can create backup policies called *backup plans*. You can use these plans to define your backup requirements, such as how frequently to back up your data and how long to retain those backups.

AWS Backup lets you apply backup plans to your AWS resources by simply tagging them. AWS Backup then automatically backs up your AWS resources according to the backup plan that you defined.

The following sections describe how AWS Backup works, its implementation details, and security considerations.

**Topics**
+ [How AWS Backup works with supported AWS services](working-with-supported-services.md)
+ [Metering, costs, and billing for AWS Backup](metering-and-billing.md)
+ [AWS Backup blogs, videos, tutorials, and other resources](blogs-videos.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
