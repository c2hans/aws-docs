---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyTemplateItem.html
---

# PolicyTemplateItem
<a name="API_PolicyTemplateItem"></a>

Contains details about a policy template

This data type is used as a response parameter for the [ListPolicyTemplates](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyTemplates.html) operation.

## Contents
<a name="API_PolicyTemplateItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** createdDate **   <a name="verifiedpermissions-Type-PolicyTemplateItem-createdDate"></a>
The date and time that the policy template was created.
Type: Timestamp
Required: Yes

 ** lastUpdatedDate **   <a name="verifiedpermissions-Type-PolicyTemplateItem-lastUpdatedDate"></a>
The date and time that the policy template was most recently updated.
Type: Timestamp
Required: Yes

 ** policyStoreId **   <a name="verifiedpermissions-Type-PolicyTemplateItem-policyStoreId"></a>
The unique identifier of the policy store that contains the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** policyTemplateId **   <a name="verifiedpermissions-Type-PolicyTemplateItem-policyTemplateId"></a>
The unique identifier of the policy template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** description **   <a name="verifiedpermissions-Type-PolicyTemplateItem-description"></a>
The description attached to the policy template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

 ** name **   <a name="verifiedpermissions-Type-PolicyTemplateItem-name"></a>
The name of the policy template, if one was assigned when the policy template was created or last updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`
Required: No

## See Also
<a name="API_PolicyTemplateItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/PolicyTemplateItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/PolicyTemplateItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/PolicyTemplateItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
