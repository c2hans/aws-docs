---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateIamIdentityCenterConfigOptions.html
---

# UpdateIamIdentityCenterConfigOptions
<a name="API_UpdateIamIdentityCenterConfigOptions"></a>

Describes IAM Identity Center options for updating an OpenSearch Serverless security configuration in the form of a key-value map.

## Contents
<a name="API_UpdateIamIdentityCenterConfigOptions_Contents"></a>

 ** groupAttribute **   <a name="opensearchserverless-Type-UpdateIamIdentityCenterConfigOptions-groupAttribute"></a>
The group attribute for this IAM Identity Center integration. Defaults to `GroupId`.
Type: String
Valid Values: `GroupId | GroupName`
Required: No

 ** userAttribute **   <a name="opensearchserverless-Type-UpdateIamIdentityCenterConfigOptions-userAttribute"></a>
The user attribute for this IAM Identity Center integration. Defaults to `UserId`.
Type: String
Valid Values: `UserId | UserName | Email`
Required: No

## See Also
<a name="API_UpdateIamIdentityCenterConfigOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateIamIdentityCenterConfigOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateIamIdentityCenterConfigOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateIamIdentityCenterConfigOptions)
