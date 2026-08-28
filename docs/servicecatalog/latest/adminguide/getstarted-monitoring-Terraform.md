---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-monitoring-Terraform.html
---

# Step 10: Monitoring Terraform provisioning operations
<a name="getstarted-monitoring-Terraform"></a>

If you want to monitor provisioning operations, you can review Amazon CloudWatch logs and AWS Step Functions for any provisioning workflow.

There are two state machines for the provisioning workflow:
+ `ManageProvisionedProductStateMachine` — AWS Service Catalog invokes this state machine when provisioning a new Terraform product and when updating an existing Terraform provisioned product.
+ `TerminateProvisionedProductStateMachine` — AWS Service Catalog invokes this state machine when terminating an existing Terraform provisioned product.

**To execute the monitoring state machine**

1. Open the AWS management console and log in as an administrator in the admin hub account where the Terraform provisioning engine is installed.

1. Open **AWS Step Functions**.

1. In the left navigation panel, choose **State machines**.

1. Choose **ManageProvisionedProductStateMachine**.

1. In the **Executions** list, enter the provisioned product ID to locate your execution.
**Note**
AWS Service Catalog creates the provisioned product ID when you provision the product. The provisioned product ID is formatted as follows: **pp-1111pwtn[ID number]**.

1. Choose the **execution ID**.

On the resulting **Execution details** page, you can view all of the steps in the provisioning workflow. You can also review any failed steps to identify the cause of the failure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
