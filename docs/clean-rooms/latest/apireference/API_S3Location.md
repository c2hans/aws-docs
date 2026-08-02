---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

The S3 location.

## Contents
<a name="API_S3Location_Contents"></a>

 ** bucket **   <a name="API-Type-S3Location-bucket"></a>
 The bucket name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `.*(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$).*`
Required: Yes

 ** key **   <a name="API-Type-S3Location-key"></a>
 The object key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9!_.*'()-/]+`
Required: Yes

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/S3Location)
