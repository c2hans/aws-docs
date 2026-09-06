---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

A location in Amazon S3.

## Contents
<a name="API_S3Location_Contents"></a>

 ** BucketName **   <a name="panorama-Type-S3Location-BucketName"></a>
A bucket name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** ObjectKey **   <a name="panorama-Type-S3Location-ObjectKey"></a>
An object key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** Region **   <a name="panorama-Type-S3Location-Region"></a>
The bucket's Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/S3Location)
