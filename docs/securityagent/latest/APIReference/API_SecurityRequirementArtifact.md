---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_SecurityRequirementArtifact.html
---

# SecurityRequirementArtifact
<a name="API_SecurityRequirementArtifact"></a>

A document used as source material for importing security requirements.

## Contents
<a name="API_SecurityRequirementArtifact_Contents"></a>

 ** content **   <a name="securityagent-Type-SecurityRequirementArtifact-content"></a>
The binary content of the document.
Type: Base64-encoded binary data object
Required: Yes

 ** format **   <a name="securityagent-Type-SecurityRequirementArtifact-format"></a>
The format of the document. Valid values are MD, PDF, TXT, DOCX, and DOC.
Type: String
Valid Values: `MD | PDF | TXT | DOCX | DOC`
Required: Yes

 ** name **   <a name="securityagent-Type-SecurityRequirementArtifact-name"></a>
The file name of the document.
Type: String
Required: Yes

## See Also
<a name="API_SecurityRequirementArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/SecurityRequirementArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/SecurityRequirementArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/SecurityRequirementArtifact)
