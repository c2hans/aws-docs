---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_S3Object.html
---

# S3Object
<a name="API_S3Object"></a>

Object stored in Amazon S3 containing ephemeris data.

## Contents
<a name="API_S3Object_Contents"></a>

 ** bucket **   <a name="groundstation-Type-S3Object-bucket"></a>
An Amazon S3 Bucket name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9.-]{3,63}`
Required: No

 ** key **   <a name="groundstation-Type-S3Object-key"></a>
An Amazon S3 key for the ephemeris.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9!*'\)\(./_-]{1,1024}`
Required: No

 ** version **   <a name="groundstation-Type-S3Object-version"></a>
For versioned Amazon S3 objects, the version to use for the ephemeris.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\s\S]{1,1024}`
Required: No

## See Also
<a name="API_S3Object_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/S3Object)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/S3Object)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/S3Object)
