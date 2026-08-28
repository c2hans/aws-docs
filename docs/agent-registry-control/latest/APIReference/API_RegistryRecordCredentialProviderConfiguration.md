---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordCredentialProviderConfiguration.html
---

# RegistryRecordCredentialProviderConfiguration
<a name="API_RegistryRecordCredentialProviderConfiguration"></a>

A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record's source URL.

## Contents
<a name="API_RegistryRecordCredentialProviderConfiguration_Contents"></a>

 ** credentialProvider **   <a name="agentregistrycontrol-Type-RegistryRecordCredentialProviderConfiguration-credentialProvider"></a>
The credential provider details corresponding to the specified credential provider type.
Type: [RegistryRecordCredentialProviderUnion](API_RegistryRecordCredentialProviderUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** credentialProviderType **   <a name="agentregistrycontrol-Type-RegistryRecordCredentialProviderConfiguration-credentialProviderType"></a>
The type of credential provider.
Type: String
Valid Values: `OAUTH | IAM`
Required: Yes

## See Also
<a name="API_RegistryRecordCredentialProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AgentRegistry Control Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
