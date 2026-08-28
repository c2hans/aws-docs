---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PossibleRemediationAction.html
---

# PossibleRemediationAction
<a name="API_PossibleRemediationAction"></a>

A list of remediation actions.

## Contents
<a name="API_PossibleRemediationAction_Contents"></a>

 ** OrderedRemediationActions **   <a name="fms-Type-PossibleRemediationAction-OrderedRemediationActions"></a>
The ordered list of remediation actions.
Type: Array of [RemediationActionWithOrder](API_RemediationActionWithOrder.md) objects
Required: Yes

 ** Description **   <a name="fms-Type-PossibleRemediationAction-Description"></a>
A description of the list of remediation actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** IsDefaultAction **   <a name="fms-Type-PossibleRemediationAction-IsDefaultAction"></a>
Information about whether an action is taken by default.
Type: Boolean
Required: No

## See Also
<a name="API_PossibleRemediationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PossibleRemediationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PossibleRemediationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PossibleRemediationAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
