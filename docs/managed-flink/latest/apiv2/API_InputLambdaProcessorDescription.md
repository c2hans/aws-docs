---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputLambdaProcessorDescription.html
---

# InputLambdaProcessorDescription
<a name="API_InputLambdaProcessorDescription"></a>

For a SQL-based Kinesis Data Analytics application, an object that contains the Amazon Resource Name (ARN) of the Amazon Lambda function that is used to preprocess records in the stream.

## Contents
<a name="API_InputLambdaProcessorDescription_Contents"></a>

 ** ResourceARN **   <a name="APIReference-Type-InputLambdaProcessorDescription-ResourceARN"></a>
The ARN of the Amazon Lambda function that is used to preprocess the records in the stream.
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: Amazon Lambda](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** RoleARN **   <a name="APIReference-Type-InputLambdaProcessorDescription-RoleARN"></a>
The ARN of the IAM role that is used to access the Amazon Lambda function.
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_InputLambdaProcessorDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/InputLambdaProcessorDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/InputLambdaProcessorDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/InputLambdaProcessorDescription)
