---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SamlConfigOptions.html
---

# SamlConfigOptions
<a name="API_SamlConfigOptions"></a>

Describes SAML options for an OpenSearch Serverless security configuration in the form of a key-value map.

## Contents
<a name="API_SamlConfigOptions_Contents"></a>

 ** metadata **   <a name="opensearchserverless-Type-SamlConfigOptions-metadata"></a>
The XML IdP metadata file generated from your identity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Pattern: `.*[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+.*`
Required: Yes

 ** groupAttribute **   <a name="opensearchserverless-Type-SamlConfigOptions-groupAttribute"></a>
The group attribute for this SAML integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*[\w+=,.@-]+.*`
Required: No

 ** openSearchServerlessEntityId **   <a name="opensearchserverless-Type-SamlConfigOptions-openSearchServerlessEntityId"></a>
Custom entity ID attribute to override the default entity ID for this SAML integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `aws:opensearch:[0-9]{12}:*.*`
Required: No

 ** sessionTimeout **   <a name="opensearchserverless-Type-SamlConfigOptions-sessionTimeout"></a>
The session timeout, in minutes. Default is 60 minutes (12 hours).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 720.
Required: No

 ** userAttribute **   <a name="opensearchserverless-Type-SamlConfigOptions-userAttribute"></a>
A user attribute for this SAML integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*[\w+=,.@-]+.*`
Required: No

## See Also
<a name="API_SamlConfigOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/SamlConfigOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/SamlConfigOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/SamlConfigOptions)
