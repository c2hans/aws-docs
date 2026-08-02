---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/vpc.html
---

# VPC
<a name="vpc"></a>

The solution provides two options for Amazon VPC configuration:

1. Let the solution build an Amazon VPC for you.

1. Managing and bringing your own Amazon VPC for use within the solution.

## Let the solution build an Amazon VPC for you
<a name="let-the-solution-build-an-amazon-vpc-for-you"></a>

If you select the option to let the solution build an Amazon VPC, it will deploy as a 2-AZ architecture by default with a CIDR range 10.10.0.0/20. You have the option to use [Amazon VPC IP Address Manager (IPAM)](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html), with 1 public subnet and 1 private subnet in each AZ. The solution creates NAT Gateways in each of the public subnets, and configures Lambda functions to create the [ENIs](https://docs.aws.amazon.com/Lambda/latest/dg/foundation-networking.html) in the private subnets. Additionally, this configuration creates route tables and its entries, security groups and its rules, network ACLs, VPC endpoints (gateway and interface endpoints).

## Managing your own Amazon VPC
<a name="managing-your-own-amazon-vpc"></a>

When deploying the solution with an Amazon VPC, you have the option to use an existing Amazon VPC in your AWS account and Region. We recommended that you make your VPC available in at least two availability zones to ensure high availability. Your VPC must also have the following VPC endpoints and their associated IAM policies for your VPC and route table configurations.

### For a Deployment dashboard Amazon VPC
<a name="deployment-dashboard-2"></a>

1.  [Gateway endpoint for DynamoDB](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html).

1.  [Gateway endpoint for S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

1.  [Interface endpoint for CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-logs-and-interface-VPC.html).

1.  [Interface endpoint for AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-vpce-bucketnames.html).

### For a use case Amazon VPC
<a name="use-cases-2"></a>

1.  [Gateway endpoint for DynamoDB](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html).

1.  [Gateway endpoint for S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

1.  [Interface endpoint for CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-logs-and-interface-VPC.html).

1.  [Interface endpoint for Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html).
**Note**
The solution only requires `com.amazonaws.region.ssm`.

1.  [Interface endpoint for Amazon Bedrock (bedrock-runtime, agent-runtime, bedrock-agent-runtime)](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html).

1. Optional: If the deployment will use Amazon Kendra as a knowledge base, then an [interface endpoint for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/vpc-interface-endpoints.html) is needed.

1. Optional: if the deployment will use any LLM under Amazon Bedrock, then an [interface endpoint for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html) is needed.
**Note**
The solution only requires `com.amazonaws.region.bedrock-runtime`.

1. Optional: If the deployment will use Amazon SageMaker AI for the LLM, then an [interface endpoint for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html) is needed.

**Note**
The solution will not delete or modify the VPC configuration when using the **Bring your own VPC deployment** option. However, it will delete any VPCs that are created by the solution in the **Create a VPC for me** option. For this reason, you must be careful when sharing a solution-managed VPC across stacks/deployments.
For example, deployment A uses **Create a VPC for me** option. Deployment B uses **Bring my own VPC** using the VPC created by deployment A. If deployment A is deleted before deployment B, then deployment B will no longer work because the VPC has been deleted. Also because deployment B is using the ENIs created by the Lambda functions, deleting deployment A might have errors and retention of residual resources.
