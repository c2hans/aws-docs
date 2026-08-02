---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_AWSResources.html
---

# AWSResources
<a name="API_AWSResources"></a>

The AWS resources associated with an agent space, including VPCs, log groups, S3 buckets, secrets, Lambda functions, and IAM roles.

## Contents
<a name="API_AWSResources_Contents"></a>

 ** iamRoles **   <a name="securityagent-Type-AWSResources-iamRoles"></a>
The IAM roles associated with the agent space.
Type: Array of strings
Required: No

 ** lambdaFunctionArns **   <a name="securityagent-Type-AWSResources-lambdaFunctionArns"></a>
The Amazon Resource Names (ARNs) of the Lambda functions associated with the agent space.
Type: Array of strings
Required: No

 ** logGroups **   <a name="securityagent-Type-AWSResources-logGroups"></a>
The Amazon Resource Names (ARNs) of the CloudWatch log groups associated with the agent space.
Type: Array of strings
Required: No

 ** s3Buckets **   <a name="securityagent-Type-AWSResources-s3Buckets"></a>
The Amazon Resource Names (ARNs) of the S3 buckets associated with the agent space.
Type: Array of strings
Required: No

 ** secretArns **   <a name="securityagent-Type-AWSResources-secretArns"></a>
The Amazon Resource Names (ARNs) of the Secrets Manager secrets associated with the agent space.
Type: Array of strings
Required: No

 ** vpcs **   <a name="securityagent-Type-AWSResources-vpcs"></a>
The VPC configurations associated with the agent space.
Type: Array of [VpcConfig](API_VpcConfig.md) objects
Required: No

## See Also
<a name="API_AWSResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/AWSResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/AWSResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/AWSResources)
