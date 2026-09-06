---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StorageConfiguration.html
---

# StorageConfiguration
<a name="API_StorageConfiguration"></a>

A complex type that describes a location where recorded videos will be stored.

## Contents
<a name="API_StorageConfiguration_Contents"></a>

 ** arn **   <a name="ivsrealtimeeapireference-Type-StorageConfiguration-arn"></a>
ARN of the storage configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** name **   <a name="ivsrealtimeeapireference-Type-StorageConfiguration-name"></a>
Name of the storage configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** s3 **   <a name="ivsrealtimeeapireference-Type-StorageConfiguration-s3"></a>
An S3 destination configuration where recorded videos will be stored.
Type: [S3StorageConfiguration](API_S3StorageConfiguration.md) object
Required: No

 ** tags **   <a name="ivsrealtimeeapireference-Type-StorageConfiguration-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_StorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/StorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/StorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/StorageConfiguration)
