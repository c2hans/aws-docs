---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateIamIdentityCenterConfigOptions.html
---

# CreateIamIdentityCenterConfigOptions
<a name="API_CreateIamIdentityCenterConfigOptions"></a>

Describes IAM Identity Center options for creating an OpenSearch Serverless security configuration in the form of a key-value map.

## Contents
<a name="API_CreateIamIdentityCenterConfigOptions_Contents"></a>

 ** instanceArn **   <a name="opensearchserverless-Type-CreateIamIdentityCenterConfigOptions-instanceArn"></a>
The ARN of the IAM Identity Center instance used to integrate with OpenSearch Serverless.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** groupAttribute **   <a name="opensearchserverless-Type-CreateIamIdentityCenterConfigOptions-groupAttribute"></a>
The group attribute for this IAM Identity Center integration. Defaults to `GroupId`.
Type: String
Valid Values: `GroupId | GroupName`
Required: No

 ** userAttribute **   <a name="opensearchserverless-Type-CreateIamIdentityCenterConfigOptions-userAttribute"></a>
The user attribute for this IAM Identity Center integration. Defaults to `UserId`.
Type: String
Valid Values: `UserId | UserName | Email`
Required: No

## See Also
<a name="API_CreateIamIdentityCenterConfigOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateIamIdentityCenterConfigOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateIamIdentityCenterConfigOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateIamIdentityCenterConfigOptions)
