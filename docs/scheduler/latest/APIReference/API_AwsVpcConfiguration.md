---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_AwsVpcConfiguration.html
---

# AwsVpcConfiguration
<a name="API_AwsVpcConfiguration"></a>

This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.

## Contents
<a name="API_AwsVpcConfiguration_Contents"></a>

 ** Subnets **   <a name="scheduler-Type-AwsVpcConfiguration-Subnets"></a>
Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** AssignPublicIp **   <a name="scheduler-Type-AwsVpcConfiguration-AssignPublicIp"></a>
Specifies whether the task's elastic network interface receives a public IP address. You can specify `ENABLED` only when `LaunchType` in `EcsParameters` is set to `FARGATE`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** SecurityGroups **   <a name="scheduler-Type-AwsVpcConfiguration-SecurityGroups"></a>
Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_AwsVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/AwsVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/AwsVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/AwsVpcConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
