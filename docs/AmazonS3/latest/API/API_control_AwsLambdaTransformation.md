---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AwsLambdaTransformation.html
---

# AwsLambdaTransformation
<a name="API_control_AwsLambdaTransformation"></a>

 AWS Lambda function used to transform objects through an Object Lambda Access Point.

## Contents
<a name="API_control_AwsLambdaTransformation_Contents"></a>

 ** FunctionArn **   <a name="AmazonS3-Type-control_AwsLambdaTransformation-FunctionArn"></a>
The Amazon Resource Name (ARN) of the AWS Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** FunctionPayload **   <a name="AmazonS3-Type-control_AwsLambdaTransformation-FunctionPayload"></a>
Additional JSON that provides supplemental data to the Lambda function used to transform objects.
Type: String
Required: No

## See Also
<a name="API_control_AwsLambdaTransformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AwsLambdaTransformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AwsLambdaTransformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AwsLambdaTransformation)
