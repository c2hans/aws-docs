---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_S3PropertiesPatch.html
---

# S3PropertiesPatch
<a name="API_S3PropertiesPatch"></a>

The Amazon S3 properties patch of a connection.

## Contents
<a name="API_S3PropertiesPatch_Contents"></a>

 ** s3Uri **   <a name="datazone-Type-S3PropertiesPatch-s3Uri"></a>
The Amazon S3 URI that's part of the Amazon S3 properties patch of a connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `s3://.+`
Required: Yes

 ** registerS3AccessGrantLocation **   <a name="datazone-Type-S3PropertiesPatch-registerS3AccessGrantLocation"></a>
Specifies whether to register the Amazon S3 Access Grant location.
Type: Boolean
Required: No

 ** s3AccessGrantLocationId **   <a name="datazone-Type-S3PropertiesPatch-s3AccessGrantLocationId"></a>
The Amazon S3 Access Grant location ID that's part of the Amazon S3 properties patch of a connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

## See Also
<a name="API_S3PropertiesPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/S3PropertiesPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/S3PropertiesPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/S3PropertiesPatch)
