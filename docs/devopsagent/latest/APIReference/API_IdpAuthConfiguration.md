---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_IdpAuthConfiguration.html
---

# IdpAuthConfiguration
<a name="API_IdpAuthConfiguration"></a>

Configuration for external Identity Provider OIDC authentication flow for the Operator App.

## Contents
<a name="API_IdpAuthConfiguration_Contents"></a>

 ** clientId **   <a name="devopsagent-Type-IdpAuthConfiguration-clientId"></a>
The OIDC client ID for the IdP application
Type: String
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-IdpAuthConfiguration-createdAt"></a>
The timestamp when the Operator App IdP auth flow was enabled.
Type: Timestamp
Required: Yes

 ** issuerUrl **   <a name="devopsagent-Type-IdpAuthConfiguration-issuerUrl"></a>
The OIDC issuer URL of the external Identity Provider
Type: String
Required: Yes

 ** operatorAppRoleArn **   <a name="devopsagent-Type-IdpAuthConfiguration-operatorAppRoleArn"></a>
The IAM role end users assume to access AIDevOps APIs
Type: String
Required: Yes

 ** provider **   <a name="devopsagent-Type-IdpAuthConfiguration-provider"></a>
The Identity Provider name (e.g., Entra, Okta, Google)
Type: String
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-IdpAuthConfiguration-updatedAt"></a>
The timestamp when the Operator App IdP auth flow was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_IdpAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/IdpAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/IdpAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/IdpAuthConfiguration)
