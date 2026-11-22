---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_S3SynchronizedSource.html
---

# S3SynchronizedSource

An Amazon S3 source that a skill record's content was synchronized from, and the object version that the registry read. At most one of `versionId` and `eTag` is set.

## Contents
<a name="API_S3SynchronizedSource_Contents"></a>

 ** synchronizedAt **   <a name="agentregistrycontrol-Type-S3SynchronizedSource-synchronizedAt"></a>
The timestamp when the registry read the source.
Type: Timestamp
Required: Yes

 ** url **   <a name="agentregistrycontrol-Type-S3SynchronizedSource-url"></a>
The source URL that the registry read.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** eTag **   <a name="agentregistrycontrol-Type-S3SynchronizedSource-eTag"></a>
The entity tag (ETag) of the object that the registry read, without quotes, when the object has no version ID. Not recorded for a SKILL.md source on a registry that is encrypted with a customer managed key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** versionId **   <a name="agentregistrycontrol-Type-S3SynchronizedSource-versionId"></a>
The version ID of the object that the registry read. Absent when the bucket isn't versioned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3SynchronizedSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/S3SynchronizedSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/S3SynchronizedSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/S3SynchronizedSource)
