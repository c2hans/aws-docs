---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_OAuth2Defaults.html
---

# OAuth2Defaults
<a name="API_OAuth2Defaults"></a>

Contains the default values required for OAuth 2.0 authentication.

## Contents
<a name="API_OAuth2Defaults_Contents"></a>

 ** authCodeUrls **   <a name="appflow-Type-OAuth2Defaults-authCodeUrls"></a>
Auth code URLs that can be used for OAuth 2.0 authentication.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

 ** oauth2CustomProperties **   <a name="appflow-Type-OAuth2Defaults-oauth2CustomProperties"></a>
List of custom parameters required for OAuth 2.0 authentication.
Type: Array of [OAuth2CustomParameter](API_OAuth2CustomParameter.md) objects
Required: No

 ** oauth2GrantTypesSupported **   <a name="appflow-Type-OAuth2Defaults-oauth2GrantTypesSupported"></a>
OAuth 2.0 grant types supported by the connector.
Type: Array of strings
Valid Values: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE | JWT_BEARER`
Required: No

 ** oauthScopes **   <a name="appflow-Type-OAuth2Defaults-oauthScopes"></a>
OAuth 2.0 scopes that the connector supports.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: No

 ** tokenUrls **   <a name="appflow-Type-OAuth2Defaults-tokenUrls"></a>
Token URLs that can be used for OAuth 2.0 authentication.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

## See Also
<a name="API_OAuth2Defaults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/OAuth2Defaults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/OAuth2Defaults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/OAuth2Defaults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
