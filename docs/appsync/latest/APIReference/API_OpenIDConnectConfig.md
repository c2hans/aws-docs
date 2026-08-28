---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_OpenIDConnectConfig.html
---

# OpenIDConnectConfig
<a name="API_OpenIDConnectConfig"></a>

Describes an OpenID Connect (OIDC) configuration.

## Contents
<a name="API_OpenIDConnectConfig_Contents"></a>

 ** issuer **   <a name="appsync-Type-OpenIDConnectConfig-issuer"></a>
The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of `iss` in the ID token.
Type: String
Required: Yes

 ** authTTL **   <a name="appsync-Type-OpenIDConnectConfig-authTTL"></a>
The number of milliseconds that a token is valid after being authenticated.
Type: Long
Required: No

 ** clientId **   <a name="appsync-Type-OpenIDConnectConfig-clientId"></a>
The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.
Type: String
Required: No

 ** iatTTL **   <a name="appsync-Type-OpenIDConnectConfig-iatTTL"></a>
The number of milliseconds that a token is valid after it's issued to a user.
Type: Long
Required: No

## See Also
<a name="API_OpenIDConnectConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/OpenIDConnectConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/OpenIDConnectConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/OpenIDConnectConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
