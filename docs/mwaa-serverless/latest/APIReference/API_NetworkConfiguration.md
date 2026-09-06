---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_NetworkConfiguration.html
---

# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

Network configuration for workflow execution. Specifies VPC security groups and subnets for secure network access. When provided, Amazon Managed Workflows for Apache Airflow Serverless deploys ECS worker tasks in your specified VPC configuration, enabling secure access to VPC-only resources. The service uses a proxy API container architecture where one container handles external communication while the worker container connects to your VPC for task execution. This design provides both security isolation and connectivity flexibility.

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

 ** SecurityGroupIds **   <a name="mwaaserverless-Type-NetworkConfiguration-SecurityGroupIds"></a>
A list of VPC security group IDs to associate with the workflow execution environment.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `sg-[a-z0-9]*`
Required: No

 ** SubnetIds **   <a name="mwaaserverless-Type-NetworkConfiguration-SubnetIds"></a>
A list of VPC subnet IDs where the workflow execution environment is deployed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `subnet-[a-z0-9]*`
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/NetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/NetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/NetworkConfiguration)
