---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.disabling.html
---

# Disabling RDS for SQL Server integration with S3
<a name="Appendix.SQLServer.Options.S3-integration.disabling"></a>

Following, you can find how to disable Amazon S3 integration with Amazon RDS for SQL Server. Files in `D:\S3\` aren't deleted when disabling S3 integration.

**Note**
To remove an IAM role from a DB instance, the status of the DB instance must be `available`.

## Console
<a name="Appendix.SQLServer.Options.S3-integration.disabling.console"></a>

**To disassociate your IAM role from your DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose the RDS for SQL Server DB instance name to display its details.

1. On the **Connectivity & security** tab, in the **Manage IAM roles** section, choose the IAM role to remove.

1. Choose **Delete**.

## AWS CLI
<a name="Appendix.SQLServer.Options.S3-integration.disabling.cli"></a>

**To remove the IAM role from the RDS for SQL Server DB instance**
+ The following AWS CLI command removes the IAM role from a RDS for SQL Server DB instance named `{{mydbinstance}}`.
**Example**

  For Linux, macOS, or Unix:

  ```
  aws rds remove-role-from-db-instance \
  	   --db-instance-identifier {{mydbinstance}} \
  	   --feature-name S3_INTEGRATION \
  	   --role-arn {{your-role-arn}}
  ```

  For Windows:

  ```
  aws rds remove-role-from-db-instance ^
  	   --db-instance-identifier {{mydbinstance}} ^
  	   --feature-name S3_INTEGRATION ^
  	   --role-arn {{your-role-arn}}
  ```

  Replace `{{your-role-arn}}` with the appropriate IAM role ARN for the `--feature-name` option.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
