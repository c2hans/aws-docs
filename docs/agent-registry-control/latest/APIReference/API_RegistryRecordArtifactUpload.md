---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordArtifactUpload.html
---

# RegistryRecordArtifactUpload

A skill package to upload with a registry record: a ZIP archive of a skill that follows the Agent Skills specification. The registry validates the package asynchronously, stores it, and sets `skillMd.data` from the package's SKILL.md.

## Contents
<a name="API_RegistryRecordArtifactUpload_Contents"></a>

 ** content **   <a name="agentregistrycontrol-Type-RegistryRecordArtifactUpload-content"></a>
The ZIP archive of the skill package, up to 5 MiB (5,242,880 bytes). In a JSON request, the content is base64-encoded. The AWS SDKs encode it for you.
Type: Base64-encoded binary data object
Required: Yes

 ** sha256 **   <a name="agentregistrycontrol-Type-RegistryRecordArtifactUpload-sha256"></a>
The optional SHA-256 checksum of the ZIP archive, as 64 lowercase hexadecimal characters, computed over the archive's bytes rather than its base64 text. If it doesn't match the content, the request fails with a `ValidationException`.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `[0-9a-f]{64}`
Required: No

## See Also
<a name="API_RegistryRecordArtifactUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordArtifactUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordArtifactUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordArtifactUpload)
