---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/cleanup.html
---

# Archive table cleanup
<a name="cleanup"></a>

The final stage in the archive process is to clean up the tables in your archive schema. You can do this after you confirm that your archive data is safely archived in Amazon S3. To avoid any impact to your application, we recommend dropping the archive schema tables during a scheduled downtime or maintenance window or during a very low traffic window in your application. These tables are not actively queried by your application and shouldn't be cause for alarm for their impact to ongoing transactions. Still, it is a best practice to run DDLs during a downtime.

After the storage for large archive schema tables is freed up, Amazon Aurora uses [dynamic resizing ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Performance.html)to help you save on storage costs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
