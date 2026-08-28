---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/my-sql-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the MySQL connector
<a name="my-sql-limitations"></a>
+ Deleted database rows will not be tracked in when Amazon Q checks for updated content.
+ The size of field names and values in a row of your database can't exceed 400KB.
+ Column names should only contain alphanumeric characters and not spaces.
+ If you have a large amount of data in your database data source, and do not want Amazon Q to index all your database content after the first sync, you can choose to sync only new, modified, or deleted documents.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
