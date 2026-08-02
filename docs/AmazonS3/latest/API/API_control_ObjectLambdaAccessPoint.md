---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaAccessPoint.html
---

# ObjectLambdaAccessPoint
<a name="API_control_ObjectLambdaAccessPoint"></a>

An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.

## Contents
<a name="API_control_ObjectLambdaAccessPoint_Contents"></a>

 ** Name **   <a name="AmazonS3-Type-control_ObjectLambdaAccessPoint-Name"></a>
The name of the Object Lambda Access Point.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 45.
Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
Required: Yes

 ** Alias **   <a name="AmazonS3-Type-control_ObjectLambdaAccessPoint-Alias"></a>
The alias of the Object Lambda Access Point.
Type: [ObjectLambdaAccessPointAlias](API_control_ObjectLambdaAccessPointAlias.md) data type
Required: No

 ** ObjectLambdaAccessPointArn **   <a name="AmazonS3-Type-control_ObjectLambdaAccessPoint-ObjectLambdaAccessPointArn"></a>
Specifies the ARN for the Object Lambda Access Point.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[^:]+:s3-object-lambda:[^:]*:\d{12}:accesspoint/.*`
Required: No

## See Also
<a name="API_control_ObjectLambdaAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaAccessPoint)
