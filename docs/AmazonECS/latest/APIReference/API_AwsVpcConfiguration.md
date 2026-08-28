---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_AwsVpcConfiguration.html
---

# AwsVpcConfiguration
<a name="API_AwsVpcConfiguration"></a>

An object representing the networking details for a task or service. For example `awsVpcConfiguration={subnets=["subnet-12344321"],securityGroups=["sg-12344321"]}`.

## Contents
<a name="API_AwsVpcConfiguration_Contents"></a>

 ** subnets **   <a name="ECS-Type-AwsVpcConfiguration-subnets"></a>
The IDs of the subnets associated with the task or service. There's a limit of 16 subnets that can be specified.
All specified subnets must be from the same VPC.
Type: Array of strings
Required: Yes

 ** assignPublicIp **   <a name="ECS-Type-AwsVpcConfiguration-assignPublicIp"></a>
Whether the task's elastic network interface receives a public IP address.
Consider the following when you set this value:
+ When you use `create-service` or `update-service`, the default is `DISABLED`.
+ When the service `deploymentController` is `ECS`, the value must be `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** securityGroups **   <a name="ECS-Type-AwsVpcConfiguration-securityGroups"></a>
The IDs of the security groups associated with the task or service. If you don't specify a security group, the default security group for the VPC is used. There's a limit of 5 security groups that can be specified.
All specified security groups must be from the same VPC.
Type: Array of strings
Required: No

## See Also
<a name="API_AwsVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/AwsVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/AwsVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/AwsVpcConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
