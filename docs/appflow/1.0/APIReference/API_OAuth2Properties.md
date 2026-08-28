---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_OAuth2Properties.html
---

# OAuth2Properties
<a name="API_OAuth2Properties"></a>

The OAuth 2.0 properties required for OAuth 2.0 authentication.

## Contents
<a name="API_OAuth2Properties_Contents"></a>

 ** oAuth2GrantType **   <a name="appflow-Type-OAuth2Properties-oAuth2GrantType"></a>
The OAuth 2.0 grant type used by connector for OAuth 2.0 authentication.
Type: String
Valid Values: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE | JWT_BEARER`
Required: Yes

 ** tokenUrl **   <a name="appflow-Type-OAuth2Properties-tokenUrl"></a>
The token URL required for OAuth 2.0 authentication.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: Yes

 ** tokenUrlCustomProperties **   <a name="appflow-Type-OAuth2Properties-tokenUrlCustomProperties"></a>
Associates your token URL with a map of properties that you define. Use this parameter to provide any additional details that the connector requires to authenticate your request.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w]+`
Value Length Constraints: Maximum length of 2048.
Value Pattern: `\S+`
Required: No

## See Also
<a name="API_OAuth2Properties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/OAuth2Properties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/OAuth2Properties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/OAuth2Properties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
