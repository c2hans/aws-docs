---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/launch-the-spoke-stack.html
---

# Step 2: Launch the spoke stack
<a name="launch-the-spoke-stack"></a>

This automated CloudFormation template deploys the spoke for Cost Optimizer for Amazon WorkSpaces on the AWS Cloud.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/) and select the button to launch the `cost-optimizer-for-amazon-workspaces-spoke` AWS CloudFormation template.

    [![Solution launch button](https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fcost-optimizer-for-amazon-workspaces%2Flatest%2Fcost-optimizer-for-amazon-workspaces-spoke.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch Cost Optimizer for Amazon WorkSpaces in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
The spoke account template should be deployed in any account you want to monitor with from the hub account deployment. Once deployed, the spoke template will register this account with the hub account deployment. The ECS task in the hub account will now monitor the WorkSpaces in the spoke account. You do not need to deploy the spoke account in the hub account to monitor the WorkSpaces in the hub account.

1. On the **Create Stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/launch-the-spoke-stack.html)

1. Choose **Next.**

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

You can can view the status of the stack in the CloudFormation console in the Status column. You should receive a `CREATE_COMPLETE` status in approximately five minutes

**Note**
In addition to the **CostOptimizerCreateTask** AWS Lambda function, this solution includes the solution-helper Lambda function, which runs only during initial configuration or when resources are updated or deleted.

When running this solution, you will see all Lambda functions in the AWS Management Console, but only the `CostOptimizerCreateTask` function is regularly active. However, don’t delete the `solution-helper` function because it’s necessary to manage associated resources.
