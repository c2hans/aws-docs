---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-8.html
---

# Step 8: Configure a Data Migration
<a name="dm-postgresql-step-8"></a>

After you create the migration project with two PostgreSQL data providers, you can use this project for homogeneous data migrations.

 **To create a data migration**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. Choose your AWS Region.

1. Choose **Migration projects**. The **Migration projects** page opens.

1. Choose `dm-project`, and then choose **Data migrations**.

1. Choose **Create data migration**.

1. For **Name**, enter a unique name for your data migration. For example, enter `postgresql-replication`.

1. For **Replication type**, choose **Full load and change data capture (CDC)** to migrate your existing source data and replicate ongoing changes. For this replication type, AWS DMS deletes all data, tables, and other database objects on your target database. Make sure you create a backup of your target database before you start your data migration.

1. Select the check box for **Turn on CloudWatch logs** to store data migration logs in Amazon CloudWatch.

1. For **IAM service role**, choose the IAM role that you created in [Step 1](dm-postgresql-step-1.md).

1. For **Stop mode**, choose **Don’t stop CDC**.

1. Choose **Create data migration**.

 AWS DMS creates your data migration and sets its status to **Ready**. To migrate your data, you must start the data migration manually. For more information, see [Step 9](dm-postgresql-step-9.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
