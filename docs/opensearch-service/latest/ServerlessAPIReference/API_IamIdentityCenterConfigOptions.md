---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IamIdentityCenterConfigOptions.html
---

# IamIdentityCenterConfigOptions
<a name="API_IamIdentityCenterConfigOptions"></a>

Describes IAM Identity Center options for an OpenSearch Serverless security configuration in the form of a key-value map.

## Contents
<a name="API_IamIdentityCenterConfigOptions_Contents"></a>

 ** applicationArn **   <a name="opensearchserverless-Type-IamIdentityCenterConfigOptions-applicationArn"></a>
The ARN of the IAM Identity Center application used to integrate with OpenSearch Serverless.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: No

 ** applicationDescription **   <a name="opensearchserverless-Type-IamIdentityCenterConfigOptions-applicationDescription"></a>
The description of the IAM Identity Center application used to integrate with OpenSearch Serverless.
Type: String
Required: No

 ** applicationName **   <a name="opensearchserverless-Type-IamIdentityCenterConfigOptions-applicationName"></a>
The name of the IAM Identity Center application used to integrate with OpenSearch Serverless.
Type: String
Required: No

 ** groupAttribute **   <a name="opensearchserverless-Type-IamIdentityCenterConfigOptions-groupAttribute"></a>
The group attribute for this IAM Identity Center integration. Defaults to `GroupId`.
Type: String
Valid Values: `GroupId | GroupName`
Required: No

 ** instanceArn **   <a name="opensearchserverless-Type-IamIdentityCenterConfigOptions-instanceArn"></a>
The ARN of the IAM Identity Center instance used to integrate with OpenSearch Serverless.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: No

 ** userAttribute **   <a name="opensearchserverless-Type-IamIdentityCenterConfigOptions-userAttribute"></a>
The user attribute for this IAM Identity Center integration. Defaults to `UserId`
Type: String
Valid Values: `UserId | UserName | Email`
Required: No

## See Also
<a name="API_IamIdentityCenterConfigOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/IamIdentityCenterConfigOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/IamIdentityCenterConfigOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/IamIdentityCenterConfigOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
