---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordSynchronizedSource.html
---

# RegistryRecordSynchronizedSource

The source that a skill record's content was last synchronized from. Exactly one member is set, for the source's provider.

## Contents
<a name="API_RegistryRecordSynchronizedSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** gitHub **   <a name="agentregistrycontrol-Type-RegistryRecordSynchronizedSource-gitHub"></a>
The GitHub source that the registry read.
Type: [GitHubSynchronizedSource](API_GitHubSynchronizedSource.md) object
Required: No

 ** s3 **   <a name="agentregistrycontrol-Type-RegistryRecordSynchronizedSource-s3"></a>
The Amazon S3 source that the registry read.
Type: [S3SynchronizedSource](API_S3SynchronizedSource.md) object
Required: No

## See Also
<a name="API_RegistryRecordSynchronizedSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordSynchronizedSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordSynchronizedSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordSynchronizedSource)
