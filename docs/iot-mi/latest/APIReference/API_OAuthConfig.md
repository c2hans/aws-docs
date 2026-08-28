---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_OAuthConfig.html
---

# OAuthConfig
<a name="API_OAuthConfig"></a>

Configuration details for OAuth authentication with a third-party service.

## Contents
<a name="API_OAuthConfig_Contents"></a>

 ** authUrl **   <a name="managedintegrations-Type-OAuthConfig-authUrl"></a>
The authorization URL for the OAuth service, where users are directed to authenticate and authorize access.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)`
Required: Yes

 ** tokenEndpointAuthenticationScheme **   <a name="managedintegrations-Type-OAuthConfig-tokenEndpointAuthenticationScheme"></a>
The authentication scheme used when requesting tokens from the token endpoint.
Type: String
Valid Values: `HTTP_BASIC | REQUEST_BODY_CREDENTIALS`
Required: Yes

 ** tokenUrl **   <a name="managedintegrations-Type-OAuthConfig-tokenUrl"></a>
The token URL for the OAuth service, where authorization codes are exchanged for access tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)`
Required: Yes

 ** oAuthCompleteRedirectUrl **   <a name="managedintegrations-Type-OAuthConfig-oAuthCompleteRedirectUrl"></a>
The URL where users are redirected after completing the OAuth authorization process.
Type: String
Required: No

 ** proactiveRefreshTokenRenewal **   <a name="managedintegrations-Type-OAuthConfig-proactiveRefreshTokenRenewal"></a>
Configuration for proactively refreshing OAuth tokens before they expire.
Type: [ProactiveRefreshTokenRenewal](API_ProactiveRefreshTokenRenewal.md) object
Required: No

 ** scope **   <a name="managedintegrations-Type-OAuthConfig-scope"></a>
The OAuth scopes requested during authorization, which define the permissions granted to the application.
Type: String
Required: No

## See Also
<a name="API_OAuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/OAuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/OAuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/OAuthConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
