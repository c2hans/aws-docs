---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsLambdaFunctionDetails.html
---

# AwsLambdaFunctionDetails
<a name="API_AwsLambdaFunctionDetails"></a>

 A summary of information about the AWS Lambda function.

## Contents
<a name="API_AwsLambdaFunctionDetails_Contents"></a>

 ** codeSha256 **   <a name="inspector2-Type-AwsLambdaFunctionDetails-codeSha256"></a>
The SHA256 hash of the AWS Lambda function's deployment package.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** executionRoleArn **   <a name="inspector2-Type-AwsLambdaFunctionDetails-executionRoleArn"></a>
The AWS Lambda function's execution role.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** functionName **   <a name="inspector2-Type-AwsLambdaFunctionDetails-functionName"></a>
The name of the AWS Lambda function.
Type: String
Pattern: `[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** runtime **   <a name="inspector2-Type-AwsLambdaFunctionDetails-runtime"></a>
The runtime environment for the AWS Lambda function.
Type: String
Valid Values: `NODEJS | NODEJS_12_X | NODEJS_14_X | NODEJS_16_X | JAVA_8 | JAVA_8_AL2 | JAVA_11 | PYTHON_3_7 | PYTHON_3_8 | PYTHON_3_9 | UNSUPPORTED | NODEJS_18_X | GO_1_X | JAVA_17 | PYTHON_3_10 | PYTHON_3_11 | DOTNETCORE_3_1 | DOTNET_6 | DOTNET_7 | RUBY_2_7 | RUBY_3_2 | DOTNET_10 | NODEJS_24_X | NODEJS_22_X | JAVA_21 | JAVA_25`
Required: Yes

 ** version **   <a name="inspector2-Type-AwsLambdaFunctionDetails-version"></a>
The version of the AWS Lambda function.
Type: String
Pattern: `(\$LATEST|[0-9]+)`
Required: Yes

 ** architectures **   <a name="inspector2-Type-AwsLambdaFunctionDetails-architectures"></a>
The instruction set architecture that the AWS Lambda function supports. Architecture is a string array with one of the valid values. The default architecture value is `x86_64`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `X86_64 | ARM64`
Required: No

 ** lastModifiedAt **   <a name="inspector2-Type-AwsLambdaFunctionDetails-lastModifiedAt"></a>
The date and time that a user last updated the configuration, in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html)
Type: Timestamp
Required: No

 ** layers **   <a name="inspector2-Type-AwsLambdaFunctionDetails-layers"></a>
The AWS Lambda function's [ layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). A Lambda function can have up to five layers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+`
Required: No

 ** packageType **   <a name="inspector2-Type-AwsLambdaFunctionDetails-packageType"></a>
The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.
Type: String
Valid Values: `IMAGE | ZIP`
Required: No

 ** vpcConfig **   <a name="inspector2-Type-AwsLambdaFunctionDetails-vpcConfig"></a>
The AWS Lambda function's networking configuration.
Type: [LambdaVpcConfig](API_LambdaVpcConfig.md) object
Required: No

## See Also
<a name="API_AwsLambdaFunctionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AwsLambdaFunctionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AwsLambdaFunctionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AwsLambdaFunctionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
