---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_IamActionDefinition.html
---

# IamActionDefinition
<a name="API_budgets_IamActionDefinition"></a>

The AWS Identity and Access Management (IAM) action definition details.

## Contents
<a name="API_budgets_IamActionDefinition_Contents"></a>

 ** PolicyArn **   <a name="awscostmanagement-Type-budgets_IamActionDefinition-PolicyArn"></a>
The Amazon Resource Name (ARN) of the policy to be attached.
Type: String
Length Constraints: Minimum length of 25. Maximum length of 684.
Pattern: `^arn:aws(-eusc|-cn|-us-gov|-iso|-iso-[a-z]{1})?:iam::(\d{12}|aws):policy(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$`
Required: Yes

 ** Groups **   <a name="awscostmanagement-Type-budgets_IamActionDefinition-Groups"></a>
A list of groups to be attached. There must be at least one group.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 640.
Pattern: `^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$`
Required: No

 ** Roles **   <a name="awscostmanagement-Type-budgets_IamActionDefinition-Roles"></a>
A list of roles to be attached. There must be at least one role.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 576.
Pattern: `^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$`
Required: No

 ** Users **   <a name="awscostmanagement-Type-budgets_IamActionDefinition-Users"></a>
A list of users to be attached. There must be at least one user.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 576.
Pattern: `^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$`
Required: No

## See Also
<a name="API_budgets_IamActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/IamActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/IamActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/IamActionDefinition)
