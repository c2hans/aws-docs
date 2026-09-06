---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityConfigSummary.html
---

# SecurityConfigSummary
<a name="API_SecurityConfigSummary"></a>

A summary of a security configuration for OpenSearch Serverless.

## Contents
<a name="API_SecurityConfigSummary_Contents"></a>

 ** configVersion **   <a name="opensearchserverless-Type-SecurityConfigSummary-configVersion"></a>
The version of the security configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 36.
Pattern: `([0-9a-zA-Z+/]{4})*(([0-9a-zA-Z+/]{2}==)|([0-9a-zA-Z+/]{3}=))?`
Required: No

 ** createdDate **   <a name="opensearchserverless-Type-SecurityConfigSummary-createdDate"></a>
The Epoch time when the security configuration was created.
Type: Long
Required: No

 ** description **   <a name="opensearchserverless-Type-SecurityConfigSummary-description"></a>
The description of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** id **   <a name="opensearchserverless-Type-SecurityConfigSummary-id"></a>
The unique identifier of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-SecurityConfigSummary-lastModifiedDate"></a>
The timestamp of when the configuration was last modified.
Type: Long
Required: No

 ** type **   <a name="opensearchserverless-Type-SecurityConfigSummary-type"></a>
The type of security configuration.
Type: String
Valid Values: `saml | iamidentitycenter | iamfederation`
Required: No

## See Also
<a name="API_SecurityConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/SecurityConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/SecurityConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/SecurityConfigSummary)
