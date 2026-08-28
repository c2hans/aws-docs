---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_MemberAccountEc2DeepInspectionStatus.html
---

# MemberAccountEc2DeepInspectionStatus
<a name="API_MemberAccountEc2DeepInspectionStatus"></a>

An object that contains details about the status of Amazon Inspector deep inspection for a member account in your organization.

## Contents
<a name="API_MemberAccountEc2DeepInspectionStatus_Contents"></a>

 ** accountId **   <a name="inspector2-Type-MemberAccountEc2DeepInspectionStatus-accountId"></a>
The unique identifier for the AWS account of the organization member.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** activateDeepInspection **   <a name="inspector2-Type-MemberAccountEc2DeepInspectionStatus-activateDeepInspection"></a>
Whether Amazon Inspector deep inspection is active in the account. If `TRUE` Amazon Inspector deep inspection is active, if `FALSE` it is not active.
Type: Boolean
Required: Yes

## See Also
<a name="API_MemberAccountEc2DeepInspectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/MemberAccountEc2DeepInspectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/MemberAccountEc2DeepInspectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/MemberAccountEc2DeepInspectionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
