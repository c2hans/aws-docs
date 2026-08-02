---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_OAuth2CustomParameter.html
---

# OAuth2CustomParameter
<a name="API_OAuth2CustomParameter"></a>

Custom parameter required for OAuth 2.0 authentication.

## Contents
<a name="API_OAuth2CustomParameter_Contents"></a>

 ** connectorSuppliedValues **   <a name="appflow-Type-OAuth2CustomParameter-connectorSuppliedValues"></a>
Contains default values for this authentication parameter that are supplied by the connector.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** description **   <a name="appflow-Type-OAuth2CustomParameter-description"></a>
A description about the custom parameter used for OAuth 2.0 authentication.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\s\w/!@#+=.-]*`
Required: No

 ** isRequired **   <a name="appflow-Type-OAuth2CustomParameter-isRequired"></a>
Indicates whether the custom parameter for OAuth 2.0 authentication is required.
Type: Boolean
Required: No

 ** isSensitiveField **   <a name="appflow-Type-OAuth2CustomParameter-isSensitiveField"></a>
Indicates whether this authentication custom parameter is a sensitive field.
Type: Boolean
Required: No

 ** key **   <a name="appflow-Type-OAuth2CustomParameter-key"></a>
The key of the custom parameter required for OAuth 2.0 authentication.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** label **   <a name="appflow-Type-OAuth2CustomParameter-label"></a>
The label of the custom parameter used for OAuth 2.0 authentication.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `.*`
Required: No

 ** type **   <a name="appflow-Type-OAuth2CustomParameter-type"></a>
Indicates whether custom parameter is used with TokenUrl or AuthUrl.
Type: String
Valid Values: `TOKEN_URL | AUTH_URL`
Required: No

## See Also
<a name="API_OAuth2CustomParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/OAuth2CustomParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/OAuth2CustomParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/OAuth2CustomParameter)
