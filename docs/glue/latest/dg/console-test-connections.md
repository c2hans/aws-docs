---
source_url: https://docs.aws.amazon.com/glue/latest/dg/console-test-connections.html
---

# Testing an AWS Glue connection
<a name="console-test-connections"></a>

 As a best practice, before you use an AWS Glue connection in an ETL job, use the AWS Glue console to test the connection. AWS Glue uses the parameters in your connection to confirm that it can access your data store and reports any errors. For information about AWS Glue connections, see [Connecting to data](glue-connections.md).

**To test an AWS Glue connection**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1.  In the navigation pane, under **Data Catalog**, choose **Connections**. You can also choose **Data connections** above **Data Catalog** in the navigation pane.

1.  In **Connections**, select the check box next to the desired connection, and then choose **Actions**. In the drop-down menu, choose **Test connection**.

1.  In the **Test connection** dialog box, select a role or choose **Create IAM role** to go to the AWS Identity and Access Management (IAM) console to create a new role. The role must have permissions on the data store.

1. Choose **Confirm**.

   The test begins and can take several minutes to complete. If the test fails, choose **Troubleshoot** to view the steps to resolve the issue.

1.  Choose **Logs** to view the logs in CloudWatch. You must have the required IAM permissions to view the logs. For more information, see [AWS Managed (Predefined) Policies for CloudWatch Logs ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.html#managed-policies-cwl) in the *Amazon CloudWatch Logs User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
