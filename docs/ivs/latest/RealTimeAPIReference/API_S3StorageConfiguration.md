---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_S3StorageConfiguration.html
---

# S3StorageConfiguration
<a name="API_S3StorageConfiguration"></a>

A complex type that describes an S3 location where recorded videos will be stored.

## Contents
<a name="API_S3StorageConfiguration_Contents"></a>

 ** bucketName **   <a name="ivsrealtimeeapireference-Type-S3StorageConfiguration-bucketName"></a>
Location (S3 bucket name) where recorded videos will be stored. Note that the StorageConfiguration and S3 bucket must be in the same region as the Composition.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9-.]+`
Required: Yes

## See Also
<a name="API_S3StorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/S3StorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/S3StorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/S3StorageConfiguration)
