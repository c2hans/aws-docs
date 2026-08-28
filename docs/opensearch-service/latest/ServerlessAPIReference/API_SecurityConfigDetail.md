---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityConfigDetail.html
---

# SecurityConfigDetail
<a name="API_SecurityConfigDetail"></a>

Details about a security configuration for OpenSearch Serverless.

## Contents
<a name="API_SecurityConfigDetail_Contents"></a>

 ** configVersion **   <a name="opensearchserverless-Type-SecurityConfigDetail-configVersion"></a>
The version of the security configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 36.
Pattern: `([0-9a-zA-Z+/]{4})*(([0-9a-zA-Z+/]{2}==)|([0-9a-zA-Z+/]{3}=))?`
Required: No

 ** createdDate **   <a name="opensearchserverless-Type-SecurityConfigDetail-createdDate"></a>
The date the configuration was created.
Type: Long
Required: No

 ** description **   <a name="opensearchserverless-Type-SecurityConfigDetail-description"></a>
The description of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** iamFederationOptions **   <a name="opensearchserverless-Type-SecurityConfigDetail-iamFederationOptions"></a>
Describes IAM federation options in the form of a key-value map. Contains configuration details about how OpenSearch Serverless integrates with external identity providers through federation.
Type: [IamFederationConfigOptions](API_IamFederationConfigOptions.md) object
Required: No

 ** iamIdentityCenterOptions **   <a name="opensearchserverless-Type-SecurityConfigDetail-iamIdentityCenterOptions"></a>
Describes IAM Identity Center options in the form of a key-value map.
Type: [IamIdentityCenterConfigOptions](API_IamIdentityCenterConfigOptions.md) object
Required: No

 ** id **   <a name="opensearchserverless-Type-SecurityConfigDetail-id"></a>
The unique identifier of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-SecurityConfigDetail-lastModifiedDate"></a>
The timestamp of when the configuration was last modified.
Type: Long
Required: No

 ** samlOptions **   <a name="opensearchserverless-Type-SecurityConfigDetail-samlOptions"></a>
SAML options for the security configuration in the form of a key-value map.
Type: [SamlConfigOptions](API_SamlConfigOptions.md) object
Required: No

 ** type **   <a name="opensearchserverless-Type-SecurityConfigDetail-type"></a>
The type of security configuration.
Type: String
Valid Values: `saml | iamidentitycenter | iamfederation`
Required: No

## See Also
<a name="API_SecurityConfigDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/SecurityConfigDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/SecurityConfigDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/SecurityConfigDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
