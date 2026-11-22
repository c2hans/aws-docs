---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordArtifactDownload.html
---

# RegistryRecordArtifactDownload

The skill package of a registry record, as a short-lived download URL and the package's SHA-256 checksum. Responses never include the package bytes.

## Contents
<a name="API_RegistryRecordArtifactDownload_Contents"></a>

 ** downloadUrl **   <a name="agentregistrycontrol-Type-RegistryRecordArtifactDownload-downloadUrl"></a>
A presigned Amazon S3 URL that downloads the package. The URL is valid for up to 5 minutes, and the response doesn't include its expiry time. To get a new URL, call the operation again. Anyone who has the URL can download the package until it expires, so don't log, store, or share it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** sha256 **   <a name="agentregistrycontrol-Type-RegistryRecordArtifactDownload-sha256"></a>
The SHA-256 checksum of the package, as 64 lowercase hexadecimal characters. The download response carries no signature that you can check, so compare the checksum of the file that you download with this value before you use the package.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `[0-9a-f]{64}`
Required: No

## See Also
<a name="API_RegistryRecordArtifactDownload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordArtifactDownload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordArtifactDownload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordArtifactDownload)
