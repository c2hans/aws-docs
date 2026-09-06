---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ScriptSource.html
---

# ScriptSource
<a name="API_ScriptSource"></a>

The source location and integrity information for a node lifecycle script.

## Contents
<a name="API_ScriptSource_Contents"></a>

 ** scriptLocation **   <a name="PCS-Type-ScriptSource-scriptLocation"></a>
The location of the script. Specify either an Amazon S3 URI in the format `s3://bucket-name/key` or an HTTPS URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+|https://([a-zA-Z0-9](?:[a-zA-Z0-9_-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}(?::[0-9]{1,5})?(?:[/?#][^\s]*)?)`
Required: Yes

 ** checksum **   <a name="PCS-Type-ScriptSource-checksum"></a>
The SHA-256 checksum of the script content, as a 64-character hexadecimal string. This value is optional. When specified, AWS PCS uses this value to verify the integrity of the downloaded script.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `[a-fA-F0-9]{64}`
Required: No

 ** s3VersionId **   <a name="PCS-Type-ScriptSource-s3VersionId"></a>
The Amazon S3 version ID of the script. Use this value to pin the script to a specific version in a versioned Amazon S3 bucket. This value is only valid when `scriptLocation` is an Amazon S3 URI.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ScriptSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ScriptSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ScriptSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ScriptSource)
