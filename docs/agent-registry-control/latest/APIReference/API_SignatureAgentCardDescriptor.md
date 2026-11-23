---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_SignatureAgentCardDescriptor.html
---

# SignatureAgentCardDescriptor

Descriptor that defines the content of a signature agent card, which identifies a web bot and references the JSON Web Key Set used to verify its HTTP message signatures.

## Contents
<a name="API_SignatureAgentCardDescriptor_Contents"></a>

 ** additionalData **   <a name="agentregistrycontrol-Type-SignatureAgentCardDescriptor-additionalData"></a>
Additional data associated with the signature agent card descriptor, such as the bot category.
Type: [SignatureAgentCardAdditionalData](API_SignatureAgentCardAdditionalData.md) object
Required: No

 ** data **   <a name="agentregistrycontrol-Type-SignatureAgentCardDescriptor-data"></a>
The signature agent card content, serialized as descriptor payload data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 102400.
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-SignatureAgentCardDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** source **   <a name="agentregistrycontrol-Type-SignatureAgentCardDescriptor-source"></a>
The optional source configuration used to synchronize the signature agent card descriptor content.
Type: [DescriptorSource](API_DescriptorSource.md) object
Required: No

## See Also
<a name="API_SignatureAgentCardDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/SignatureAgentCardDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/SignatureAgentCardDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/SignatureAgentCardDescriptor)
