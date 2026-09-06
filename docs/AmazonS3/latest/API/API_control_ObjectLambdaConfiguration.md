---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaConfiguration.html
---

# ObjectLambdaConfiguration
<a name="API_control_ObjectLambdaConfiguration"></a>

A configuration used when creating an Object Lambda Access Point.

## Contents
<a name="API_control_ObjectLambdaConfiguration_Contents"></a>

 ** SupportingAccessPoint **   <a name="AmazonS3-Type-control_ObjectLambdaConfiguration-SupportingAccessPoint"></a>
Standard access point associated with the Object Lambda Access Point.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[^:]+:s3:[^:]*:\d{12}:accesspoint/.*`
Required: Yes

 ** TransformationConfigurations **   <a name="AmazonS3-Type-control_ObjectLambdaConfiguration-TransformationConfigurations"></a>
A container for transformation configurations for an Object Lambda Access Point.
Type: Array of [ObjectLambdaTransformationConfiguration](API_control_ObjectLambdaTransformationConfiguration.md) data types
Required: Yes

 ** AllowedFeatures **   <a name="AmazonS3-Type-control_ObjectLambdaConfiguration-AllowedFeatures"></a>
A container for allowed features. Valid inputs are `GetObject-Range`, `GetObject-PartNumber`, `HeadObject-Range`, and `HeadObject-PartNumber`.
Type: Array of strings
Valid Values: `GetObject-Range | GetObject-PartNumber | HeadObject-Range | HeadObject-PartNumber`
Required: No

 ** CloudWatchMetricsEnabled **   <a name="AmazonS3-Type-control_ObjectLambdaConfiguration-CloudWatchMetricsEnabled"></a>
A container for whether the CloudWatch metrics configuration is enabled.
Type: Boolean
Required: No

## See Also
<a name="API_control_ObjectLambdaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaConfiguration)
