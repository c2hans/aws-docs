---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordCredentialProviderUnion.html
---

# RegistryRecordCredentialProviderUnion
<a name="API_RegistryRecordCredentialProviderUnion"></a>

The credential provider details for a registry record. Exactly one member is populated, matching the configured credential provider type.

## Contents
<a name="API_RegistryRecordCredentialProviderUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** iamCredentialProvider **   <a name="agentregistrycontrol-Type-RegistryRecordCredentialProviderUnion-iamCredentialProvider"></a>
The IAM role credential provider details.
Type: [RegistryRecordIamCredentialProvider](API_RegistryRecordIamCredentialProvider.md) object
Required: No

 ** oauthCredentialProvider **   <a name="agentregistrycontrol-Type-RegistryRecordCredentialProviderUnion-oauthCredentialProvider"></a>
The OAuth 2.0 credential provider details.
Type: [RegistryRecordOAuthCredentialProvider](API_RegistryRecordOAuthCredentialProvider.md) object
Required: No

## See Also
<a name="API_RegistryRecordCredentialProviderUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vestry-control-plane-2025-12-01/RegistryRecordCredentialProviderUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vestry-control-plane-2025-12-01/RegistryRecordCredentialProviderUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vestry-control-plane-2025-12-01/RegistryRecordCredentialProviderUnion)
