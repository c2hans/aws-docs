---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsLambdaFunctionCode.html
---

# AwsLambdaFunctionCode
<a name="API_AwsLambdaFunctionCode"></a>

The code for the Lambda function. You can specify either an object in Amazon S3, or upload a deployment package directly.

## Contents
<a name="API_AwsLambdaFunctionCode_Contents"></a>

 ** S3Bucket **   <a name="securityhub-Type-AwsLambdaFunctionCode-S3Bucket"></a>
An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** S3Key **   <a name="securityhub-Type-AwsLambdaFunctionCode-S3Key"></a>
The Amazon S3 key of the deployment package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** S3ObjectVersion **   <a name="securityhub-Type-AwsLambdaFunctionCode-S3ObjectVersion"></a>
For versioned objects, the version of the deployment package object to use.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ZipFile **   <a name="securityhub-Type-AwsLambdaFunctionCode-ZipFile"></a>
The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle the encoding for you.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsLambdaFunctionCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsLambdaFunctionCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsLambdaFunctionCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsLambdaFunctionCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
