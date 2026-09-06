---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/deployment-steps.html
---

# Deployment Steps
<a name="deployment-steps"></a>

## Step 1: Launch stack
<a name="step-1-launch-stack"></a>

 **Option 1: Launch directly in AWS Console**

Choose the following link to launch the CloudFormation stack directly in the AWS Management Console:

 [![Launch CloudFormation Console](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=SpatialDataManagement&templateURL=https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/SpatialDataManagementStack.template)

This opens the CloudFormation console with the template pre-loaded. You can select your preferred AWS Region from the console before proceeding.

 **Option 2: Download and upload template file**

You can also download the template and upload it manually:

1. Download the [CloudFormation template](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/SpatialDataManagementStack.template)

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. Choose **Create stack**, and then choose **With new resources (standard)**

1. Under **Specify template**, choose **Upload a template file**

1. Choose **Choose file** and select the downloaded template

1. Choose **Next**

![Create stack page showing template selection options](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/create-stack-select-template.png)

## Step 2: Configure Stack Details
<a name="step-2-configure-stack-details"></a>

Enter the stack name (for example, `SpatialDataManagement`) and configure basic options.

**Note**
If you choose a different stack name, replace `SpatialDataManagement` with your chosen name in all CLI commands throughout this guide.

![Stack details page showing default parameters for development deployment](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/poc-deploy-default-parameters.png)

## Step 3: Specify Stack Parameters
<a name="step-3-specify-stack-parameters"></a>

You can configure the deployment parameters based on your environment.

Key parameters to configure:

| Parameter | Description | Default | Valid Values |
| --- | --- | --- | --- |
|  `DeploymentMode`  | Deployment environment – Dev or Prod. You can use this to configure scale and cost tendencies |  `dev`  |  `dev`, `prod`  |

Optional Parameters

| Parameter | Description | Default | Valid Values |
| --- | --- | --- | --- |
|  `LogBucketRetentionDays`  | Number of days to retain logs in the log bucket |  `90`  | Any positive integer |
|  `PortalFullyQualifiedDomainName`  | Fully qualified domain name for custom domain | Empty | Valid domain name or empty |
|  `PortalRoute53HostedZoneId`  | Route53 hosted zone ID for custom domain | Empty | Valid Route53 hosted zone ID (starts with Z) or empty |
|  `ExistingDeadlineFarmId`  | ID of the Deadline Cloud Farm to use for jobs | Empty | Valid Deadline Cloud Farm ID (farm-<32 hex chars>) or empty |
|  `ExistingDeadlineQueueId`  | ID of the Deadline Cloud Queue to use for jobs | Empty | Valid Deadline Cloud Queue ID (queue-<32 hex chars>) or empty |
|  `ExistingVpcId`  | ID of an existing VPC to deploy into instead of creating a new one. When provided, the solution skips VPC creation and deploys into your existing VPC. See [Reuse existing networking infrastructure](reuse-existing-networking.md) for prerequisites. | Empty | Valid VPC ID (`vpc-<hex>`) or empty |
|  `ExistingVpcCidrBlock`  | CIDR block of the existing VPC (for example, `10.0.0.0/16`). Required when `ExistingVpcId` is set. | Empty | Valid CIDR range or empty |
|  `ExistingIsolatedSubnetIds`  | Comma-separated IDs of isolated subnets (no internet route) in the existing VPC. Optional — if omitted, all Lambdas are placed in private subnets. | Empty | Comma-separated subnet IDs or empty |
|  `ExistingPrivateSubnetIds`  | Comma-separated IDs of private subnets (with outbound internet route) in the existing VPC. Required when `ExistingVpcId` is set. | Empty | Comma-separated subnet IDs or empty |
|  `ExistingOpenSearchVpcEndpointId`  | ID of the Amazon OpenSearch Serverless VPC endpoint in the existing VPC. Required when `ExistingVpcId` is set and `UseVpcEndpoints` is `Yes`. | Empty | Valid VPC endpoint ID (`vpce-<hex>`) or empty |
|  `UseVpcEndpoints`  | For bring-your-own (BYO) VPC deployments: set to `No` to skip VPC endpoint creation and validation. When set to `No`, Lambda functions reach AWS services over the internet via NAT instead of through VPC endpoints. Only applicable when `ExistingVpcId` is provided. See [Reuse existing networking infrastructure](reuse-existing-networking.md) for details. |  `Yes`  |  `Yes`, `No`  |

![Advanced parameters configuration for production deployment](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/production-advanced-parameters-deploy.png)

## Step 4: Configure Stack Options
<a name="step-4-configure-stack-options"></a>

You can set additional stack options:

You can configure the following options:
+  **Stack policy** (optional) – Defines which IAM actions are allowed on specific resources. For more information, see [Prevent updates to stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html) in the AWS CloudFormation User Guide.
+  **Rollback configuration** – Specifies whether to roll back the stack if creation fails. For more information, see [Stack creation options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the AWS CloudFormation User Guide.
+  **Notification options** – Specifies Amazon SNS topics to receive stack-related notifications. For more information, see [Monitoring stack creation and updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-notifications.html) in the AWS CloudFormation User Guide.
+  **Tags** – Key-value pairs for resource organization and cost allocation. For more information, see [Tagging resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the AWS CloudFormation User Guide.

![CloudFormation stack options page showing basic configuration settings](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/cloudformation-basic-stack-options.png)

![CloudFormation stack options page showing permissions and advanced settings](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/cloud-formation-stack-options-set-2.png)

![CloudFormation stack options page showing tags and additional configuration](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/cloud-formation-stack-options-set-3.png)

## Step 5: Review and Create
<a name="step-5-review-and-create"></a>

Review your configuration and choose **Create stack** to begin deployment. The stack creation typically takes approximately 45 minutes to complete.

![Review page showing stack parameters and configuration summary](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/review-stack-parameters-and-create-set-1.png)

![Review page showing capabilities acknowledgment and create button](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/review-stack-parameters-and-create-set-2.png)

## Step 6: Monitor Deployment Progress
<a name="step-6-monitor-deployment-progress"></a>

You can monitor stack creation progress in the CloudFormation console:

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. Select your stack (SpatialDataManagement)

1. Choose the **Events** tab to view real-time creation progress

1. Watch for the **CREATE\_COMPLETE** status

For more information, see [Monitoring stack creation, update, and deletion progress](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-notifications.html) in the AWS CloudFormation User Guide.

## Step 7: Retrieve Outputs
<a name="step-7-retrieve-outputs"></a>

After successful deployment:

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. Select your stack (SpatialDataManagement)

1. Choose the **Outputs** tab to view deployment outputs

1. Copy the output values for use in post-deployment configuration

## Nested Stacks
<a name="nested-stacks"></a>

The main stack creates the following nested stacks:

1.  **VPC Stack** (5-7 minutes) – Amazon Virtual Private Cloud (Amazon VPC) with 2 Availability Zones – Public, private, and isolated subnets – NAT gateways – VPC endpoints for AWS services

1.  **Auth Stack** (3-5 minutes) – Amazon Cognito user pool for authentication – Amazon Cognito identity pool for authorization – User and group management

1.  **Asset Management Stack** (5-8 minutes) – Amazon DynamoDB tables for asset metadata – AWS Lambda functions for API operations – Amazon Simple Storage Service (Amazon S3) buckets for asset storage – Amazon Simple Queue Service (Amazon SQS) queues for asynchronous processing – Amazon API Gateway for REST endpoints

1.  **OpenSearch Stack** (3-5 minutes) – Amazon OpenSearch Serverless collection – VPC endpoint for private access – Security and network policies

1.  **Portal Stack** (2-3 minutes) – Amazon CloudFront distribution for content delivery – S3 bucket for web assets – CloudFront key pair for signed URLs

1.  **Deadline Stack** (2-3 minutes, if enabled) – AWS Deadline Cloud farm configuration – Integration with asset management system – Job queue setup

1.  **Monitoring Stack** (2-3 minutes) – Amazon CloudWatch alarms and dashboards – AWS CloudTrail for audit logging – Amazon Athena workgroup for log analysis
