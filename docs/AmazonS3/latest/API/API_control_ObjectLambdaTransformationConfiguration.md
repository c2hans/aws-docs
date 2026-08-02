---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaTransformationConfiguration.html
---

# ObjectLambdaTransformationConfiguration
<a name="API_control_ObjectLambdaTransformationConfiguration"></a>

A configuration used when creating an Object Lambda Access Point transformation.

## Contents
<a name="API_control_ObjectLambdaTransformationConfiguration_Contents"></a>

 ** Actions **   <a name="AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-Actions"></a>
A container for the action of an Object Lambda Access Point configuration. Valid inputs are `GetObject`, `ListObjects`, `HeadObject`, and `ListObjectsV2`.
Type: Array of strings
Valid Values: `GetObject | HeadObject | ListObjects | ListObjectsV2`
Required: Yes

 ** ContentTransformation **   <a name="AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-ContentTransformation"></a>
A container for the content transformation of an Object Lambda Access Point configuration.
Type: [ObjectLambdaContentTransformation](API_control_ObjectLambdaContentTransformation.md) data type
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_control_ObjectLambdaTransformationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaTransformationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaTransformationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaTransformationConfiguration)
