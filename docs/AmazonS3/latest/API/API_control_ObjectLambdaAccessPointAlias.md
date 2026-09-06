---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaAccessPointAlias.html
---

# ObjectLambdaAccessPointAlias
<a name="API_control_ObjectLambdaAccessPointAlias"></a>

The alias of an Object Lambda Access Point. For more information, see [How to use a bucket-style alias for your S3 bucket Object Lambda Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-use.html#ol-access-points-alias).

## Contents
<a name="API_control_ObjectLambdaAccessPointAlias_Contents"></a>

 ** Status **   <a name="AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status"></a>
The status of the Object Lambda Access Point alias. If the status is `PROVISIONING`, the Object Lambda Access Point is provisioning the alias and the alias is not ready for use yet. If the status is `READY`, the Object Lambda Access Point alias is successfully provisioned and ready for use.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 16.
Valid Values: `PROVISIONING | READY`
Required: No

 ** Value **   <a name="AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value"></a>
The alias value of the Object Lambda Access Point.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[0-9a-z\\-]{3,63}`
Required: No

## See Also
<a name="API_control_ObjectLambdaAccessPointAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectLambdaAccessPointAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectLambdaAccessPointAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectLambdaAccessPointAlias)
