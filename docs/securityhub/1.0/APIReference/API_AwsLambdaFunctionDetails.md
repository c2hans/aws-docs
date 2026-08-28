---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsLambdaFunctionDetails.html
---

# AwsLambdaFunctionDetails
<a name="API_AwsLambdaFunctionDetails"></a>

Details about an AWS Lambda function's configuration.

## Contents
<a name="API_AwsLambdaFunctionDetails_Contents"></a>

 ** Architectures **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Architectures"></a>
The instruction set architecture that the function uses. Valid values are `x86_64` or `arm64`.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Code **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Code"></a>
An `AwsLambdaFunctionCode` object.
Type: [AwsLambdaFunctionCode](API_AwsLambdaFunctionCode.md) object
Required: No

 ** CodeSha256 **   <a name="securityhub-Type-AwsLambdaFunctionDetails-CodeSha256"></a>
The SHA256 hash of the function's deployment package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeadLetterConfig **   <a name="securityhub-Type-AwsLambdaFunctionDetails-DeadLetterConfig"></a>
The function's dead letter queue.
Type: [AwsLambdaFunctionDeadLetterConfig](API_AwsLambdaFunctionDeadLetterConfig.md) object
Required: No

 ** Environment **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Environment"></a>
The function's environment variables.
Type: [AwsLambdaFunctionEnvironment](API_AwsLambdaFunctionEnvironment.md) object
Required: No

 ** FunctionName **   <a name="securityhub-Type-AwsLambdaFunctionDetails-FunctionName"></a>
The name of the function.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Handler **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Handler"></a>
The function that Lambda calls to begin executing your function.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsKeyArn **   <a name="securityhub-Type-AwsLambdaFunctionDetails-KmsKeyArn"></a>
The AWS KMS key that is used to encrypt the function's environment variables. This key is only returned if you've configured a customer managed customer managed key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastModified **   <a name="securityhub-Type-AwsLambdaFunctionDetails-LastModified"></a>
Indicates when the function was last updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Layers **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Layers"></a>
The function's layers.
Type: Array of [AwsLambdaFunctionLayer](API_AwsLambdaFunctionLayer.md) objects
Required: No

 ** MasterArn **   <a name="securityhub-Type-AwsLambdaFunctionDetails-MasterArn"></a>
For Lambda@Edge functions, the ARN of the master function.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MemorySize **   <a name="securityhub-Type-AwsLambdaFunctionDetails-MemorySize"></a>
The memory that is allocated to the function.
Type: Integer
Required: No

 ** PackageType **   <a name="securityhub-Type-AwsLambdaFunctionDetails-PackageType"></a>
The type of deployment package that's used to deploy the function code to Lambda. Set to `Image` for a container image and `Zip` for a .zip file archive.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RevisionId **   <a name="securityhub-Type-AwsLambdaFunctionDetails-RevisionId"></a>
The latest updated revision of the function or alias.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Role **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Role"></a>
The function's execution role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Runtime **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Runtime"></a>
The runtime environment for the Lambda function.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Timeout **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Timeout"></a>
The amount of time that Lambda allows a function to run before stopping it.
Type: Integer
Required: No

 ** TracingConfig **   <a name="securityhub-Type-AwsLambdaFunctionDetails-TracingConfig"></a>
The function's AWS X-Ray tracing configuration.
Type: [AwsLambdaFunctionTracingConfig](API_AwsLambdaFunctionTracingConfig.md) object
Required: No

 ** Version **   <a name="securityhub-Type-AwsLambdaFunctionDetails-Version"></a>
The version of the Lambda function.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcConfig **   <a name="securityhub-Type-AwsLambdaFunctionDetails-VpcConfig"></a>
The function's networking configuration.
Type: [AwsLambdaFunctionVpcConfig](API_AwsLambdaFunctionVpcConfig.md) object
Required: No

## See Also
<a name="API_AwsLambdaFunctionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsLambdaFunctionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsLambdaFunctionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsLambdaFunctionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
