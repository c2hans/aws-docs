---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_OrderedOrganizationPolicyType.html
---

# OrderedOrganizationPolicyType
<a name="API_OrderedOrganizationPolicyType"></a>

Represents one level of an Organizations hierarchy—the organization root, an organizational unit (OU), or an account—together with the service control policies (SCPs) that apply at that level. Each element in the list represents one level of the hierarchy, ordered from the organization root down to the account.

For more information about SCPs, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *Organizations User Guide*.

## Contents
<a name="API_OrderedOrganizationPolicyType_Contents"></a>

 ** ServiceControlPolicyInputList.member.N **
A list of SCP documents that apply at this level of the Organizations hierarchy. Each document is specified as a string containing the complete, valid JSON text of an SCP.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

## See Also
<a name="API_OrderedOrganizationPolicyType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/OrderedOrganizationPolicyType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/OrderedOrganizationPolicyType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/OrderedOrganizationPolicyType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
