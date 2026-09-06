---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_LambdaOutputUpdate.html
---

# LambdaOutputUpdate
<a name="API_LambdaOutputUpdate"></a>

When you update an SQL-based Kinesis Data Analytics application's output configuration using the [UpdateApplication](API_UpdateApplication.md) operation, provides information about an Amazon Lambda function that is configured as the destination.

## Contents
<a name="API_LambdaOutputUpdate_Contents"></a>

 ** ResourceARNUpdate **   <a name="APIReference-Type-LambdaOutputUpdate-ResourceARNUpdate"></a>
The Amazon Resource Name (ARN) of the destination Amazon Lambda function.
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: Amazon Lambda](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

## See Also
<a name="API_LambdaOutputUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/LambdaOutputUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/LambdaOutputUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/LambdaOutputUpdate)
