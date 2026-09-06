---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/launch-the-stack-hub-template.html
---

# Step 1: Launch the hub stack
<a name="launch-the-stack-hub-template"></a>

This automated AWS CloudFormation template deploys Cost Optimizer for Amazon WorkSpaces on the AWS Cloud.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/) and select the button to launch the `cost-optimizer-for-amazon-workspaces` AWS CloudFormation template.

    [![Solution launch button](http://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fcost-optimizer-for-amazon-workspaces%2Flatest%2Fcost-optimizer-for-amazon-workspaces.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch Cost Optimizer for Amazon WorkSpaces in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution can be launched as a single account deployment or multi account deployment. For single account deployment, you only need to deploy the hub template in the account you want to monitor the workspaces for. The multi account deployment works in the hub and spoke model.For multi account deployment, you need to deploy the hub template in a central account and provide AWS Organization ID and Management Account ID in the input parameters for the hub account.

1. On the **Create Stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.
**Important**
Don’t set the parameters **Simulate End of Month Cleanup** and **Terminate workspaces not used for a month** to `Yes` at the same time. Doing this will lead to unexpected WorkSpace termination

The **Simulate End of Month Cleanup** parameter will run the solution as if it’s the last day of the month and then terminate WorkSpaces unexpectedly. To use the Terminate unused WorkSpaces feature, set **Simulate End of Month Cleanup** to `No`.

| Parameter | Default | Description |
| --- | --- | --- |
|  **Select New or Existing VPC for AWS Fargate**  |  |  |
|  **Create New VPC**  |  `Yes`  | Select `Yes` to deploy the solution in a new Amazon VPC. |
|  **Existing VPC Settings**  |  |  |
|  **Public Subnet ID**  |  *<Optional input>*  | A public subnet ID to launch the gateway.<br />Leave this blank if you selected `Yes` for **Create New VPC** or enter an existing subnet ID to run an Amazon ECS task. |
|  **First Public Subnet ID**  |  *<Optional input>*  | A Private Subnet ID to launch ECS task. Leave this blank if you `Yes` for **Create New VPC** . |
|  **Second private subnet ID for second subnet**  |  *<Optional input>*  | A second private subnet ID to launch an Amazon ECS task.<br />Leave this blank if you selected `Yes` for **Create New VPC** or enter an existing subnet ID to run an Amazon ECS task. |
|  **Security group ID to launch ECS task**  |  *<Optional input>*  | Security group ID to launch an Amazon ECS task<br />Leave this blank if you selected `Yes` for **Create New VPC** or enter an existing security group ID to run an Amazon ECS task. |
|  **New VPC Settings**  |  |  |
|  **AWS Fargate VPC CIDR Block**  |  `10.215.0.0/16`  | The default VPC CIDR used to deploy the AWS Fargate container dynamically when the solution runs. |
|  **Public Subnet CIDR Block**  |  `10.215.10.0/24`  | A public subnet to which the internet gateway is deployed. |
|  **AWS Fargate Private Subnet1 CIDR Block**  |  `10.215.30.0/24`  | One of two private subnets in different Availability Zones where the AWS Fargate container is deployed. |
|  **AWS Fargate Private Subnet2 CIDR Block**  |  `10.215.40.0/24`  | The second of two subnets in different Availability Zones where the AWS Fargate container is deployed. |
|  **AWS Fargate SecurityGroup CIDR Block**  |  `0.0.0.0/0`  | The CIDR block to restrict the Amazon ECS container outbound access. |
|  **Testing Parameters**  |  |  |
|  **Launch in Dry Run Mode**  |  `Yes`  | Generates a change log, but does not inact any changes. For more information, refer to [Dry Run Mode](features-and-benefits.md#dry-run-mode). |
|  **Simulate End of Month Cleanup**  |  `No`  | Overrides date and forces the solution to run as if it is the end of the month. |
|  **Log Level**  |  `INFO`  | Sets the log level for the Lambda function logs in CloudWatch. |
|  **Pricing Parameters**  |  |  |
|  **ValueLimit**  |  `81`  | The number of hours a Value instance can run in a month before being converted to `ALWAYS_ON`. |
|  **StandardLimit**  |  `85`  | The number of hours a Standard instance can run in a month before being converted to `ALWAYS_ON`. |
|  **PerformanceLimit**  |  `83`  | The number of hours a Performance instance can run in a month before being converted to `ALWAYS_ON`. |
|  **GraphicsG4dnLimit**  |  `217`  | The number of hours a Graphics instance can run in a month before being converted to `ALWAYS_ON`. |
|  **GraphicsProG4dnLimit**  |  `80`  | The number of hours a GraphicsPro instance can run in a month before being converted to `ALWAYS_ON`. |
|  **PowerLimit**  |  `83`  | The number of hours a Power instance can run in a month before being converted to `ALWAYS_ON`. |
|  **PowerProLimit**  |  `80`  | The number of hours a PowerPro instance can run in a month before being converted to `ALWAYS_ON`. |
|  **GeneralPurpose4xlargeLimit**  |  `121`  | The number of hours a GeneralPurpose.4xlarge instance can run in a month before being converted to `ALWAYS_ON`. |
|  **GeneralPurpose8xlargeLimit**  |  `125`  | The number of hours a GeneralPurpose.8xlarge instance can run in a month before being converted to `ALWAYS_ON`. |
|  **Container Image**  |  |  |
|  **Auto-Update Container Image**  |  `Yes`  | Automatically use the most up to date and secure image up until the next minor release. Selecting `No` will pull the image as originally released, without any security updates. |
|  **List of AWS Regions**  |  |  |
|  **List of AWS Regions**  |  {{<Requires input>}}  | Comma separated list of AWS Regions for the solution to monitor.<br />Example: `us-east-1`, `us-west-2`. |
|  **Terminate unused workspaces**  |  |  |
|  **Terminate workspaces not used for a month**  |  `No`  | Select `Yes` to delete WorkSpaces not used for one month. |
|  **Number of months for termination check**  |  `1`  | Provide the number of months to check for inactive period before termination. Default value is `1` month. |
|  **Multi account deployment**  |  |  |
|  **Organization ID for multi account deployment**  |  *<Optional input>*  | AWS Organizations ID to support multi-account deployment.<br />Leave blank for single account deployments. |
|  **Account ID of the Management Account for the Organization**  |  *<Optional input>*  | Account ID for the Organization’s management account.<br />Leave blank for single account deployments. |

1. Choose **Next.**

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of CREATE\_COMPLETE in approximately five minutes.

**Note**
In addition to the `CostOptimizerCreateTask` AWS Lambda function, this solution includes the `solution-helper` Lambda function, which runs only during initial configuration or when resources are updated or deleted.
When running this solution, you will see all Lambda functions in the AWS Management Console, but only the `CostOptimizerCreateTask` function is regularly active. However, do not delete the `solution-helper` function as it is necessary to manage associated resources.
