---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsLambdaFunctionVpcConfig.html
---

# AwsLambdaFunctionVpcConfig
<a name="API_AwsLambdaFunctionVpcConfig"></a>

The VPC security groups and subnets that are attached to a Lambda function.

## Contents
<a name="API_AwsLambdaFunctionVpcConfig_Contents"></a>

 ** SecurityGroupIds **   <a name="securityhub-Type-AwsLambdaFunctionVpcConfig-SecurityGroupIds"></a>
A list of VPC security groups IDs.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SubnetIds **   <a name="securityhub-Type-AwsLambdaFunctionVpcConfig-SubnetIds"></a>
A list of VPC subnet IDs.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsLambdaFunctionVpcConfig-VpcId"></a>
The ID of the VPC.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsLambdaFunctionVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsLambdaFunctionVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsLambdaFunctionVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsLambdaFunctionVpcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
