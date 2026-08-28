---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.createreplicationinstance.html
---

# Step 5: Create an AWS DMS Replication Instance
<a name="chap-sqlserver2aurora.steps.createreplicationinstance"></a>

After validating the schema structure between source and target databases, continue with the core part of this walkthrough, which is the data migration. The following illustration shows a high-level view of the migration process.

![Migration process diagram showing source and target databases](http://docs.aws.amazon.com/dms/latest/sbs/images/datarep-conceptual2.png)

An AWS DMS replication instance performs the actual data migration between source and target. The replication instance also caches the transaction logs during the migration. The amount of CPU and memory capacity a replication instance has influences the overall time that is required for the migration.

For information about best practices for using AWS DMS, see [AWS Database Migration Service Best Practices](https://d0.awsstatic.com/whitepapers/RDS/AWS_Database_Migration_Service_Best_Practices.pdf).

To create an AWS DMS replication instance, do the following:

1. Sign in to the AWS Management Console, and open the [AWS DMS console](https://console.aws.amazon.com/dms/v2).

1. In the console, choose **Create migration**. If you are signed in as an AWS Identity and Access Management (IAM) user, you must have the appropriate permissions to access AWS DMS. For more information about the permissions required, see [IAM Permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions).

1. On the Welcome page, choose **Next** to start a database migration.

1. On the **Create replication instance** page, specify your replication instance information.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.createreplicationinstance.html)

1. For the **Advanced** section, specify the following information.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.createreplicationinstance.html)

   For information about the KMS key, see [Setting an Encryption Key and Specifying KMS Permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.EncryptionKey.html).

1. Click **Next**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
