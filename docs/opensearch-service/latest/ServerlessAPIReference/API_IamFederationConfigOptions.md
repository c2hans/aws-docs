---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IamFederationConfigOptions.html
---

# IamFederationConfigOptions
<a name="API_IamFederationConfigOptions"></a>

Describes IAM federation options for an OpenSearch Serverless security configuration in the form of a key-value map. These options define how OpenSearch Serverless integrates with external identity providers using federation.

## Contents
<a name="API_IamFederationConfigOptions_Contents"></a>

 ** groupAttribute **   <a name="opensearchserverless-Type-IamFederationConfigOptions-groupAttribute"></a>
The group attribute for this IAM federation integration. This attribute is used to map identity provider groups to OpenSearch Serverless permissions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z][A-Za-z0-9_.:/=+\-@]*`
Required: No

 ** userAttribute **   <a name="opensearchserverless-Type-IamFederationConfigOptions-userAttribute"></a>
The user attribute for this IAM federation integration. This attribute is used to identify users in the federated authentication process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z][A-Za-z0-9_.:/=+\-@]*`
Required: No

## See Also
<a name="API_IamFederationConfigOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/IamFederationConfigOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/IamFederationConfigOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/IamFederationConfigOptions)
