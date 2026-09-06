---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

Specifies the details for the Amazon S3 file location that is being used with AWS B2B Data Interchange. File locations in Amazon S3 are identified using a combination of the bucket and key.

## Contents
<a name="API_S3Location_Contents"></a>

 ** bucketName **   <a name="b2bi-Type-S3Location-bucketName"></a>
Specifies the name of the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** key **   <a name="b2bi-Type-S3Location-key"></a>
Specifies the Amazon S3 key for the file location.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/S3Location)
