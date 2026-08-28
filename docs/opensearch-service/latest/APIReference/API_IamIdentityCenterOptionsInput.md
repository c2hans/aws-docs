---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_IamIdentityCenterOptionsInput.html
---

# IamIdentityCenterOptionsInput
<a name="API_IamIdentityCenterOptionsInput"></a>

Configuration settings for enabling and managing IAM Identity Center.

## Contents
<a name="API_IamIdentityCenterOptionsInput_Contents"></a>

 ** enabled **   <a name="opensearchservice-Type-IamIdentityCenterOptionsInput-enabled"></a>
Specifies whether IAM Identity Center is enabled or disabled.
Type: Boolean
Required: No

 ** iamIdentityCenterInstanceArn **   <a name="opensearchservice-Type-IamIdentityCenterOptionsInput-iamIdentityCenterInstanceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** iamRoleForIdentityCenterApplicationArn **   <a name="opensearchservice-Type-IamIdentityCenterOptionsInput-iamRoleForIdentityCenterApplicationArn"></a>
The ARN of the IAM role associated with the IAM Identity Center application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):iam::[0-9]+:role\/.*`
Required: No

## See Also
<a name="API_IamIdentityCenterOptionsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/IamIdentityCenterOptionsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/IamIdentityCenterOptionsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/IamIdentityCenterOptionsInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
