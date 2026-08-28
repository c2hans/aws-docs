---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityGroupRemediationAction.html
---

# SecurityGroupRemediationAction
<a name="API_SecurityGroupRemediationAction"></a>

Remediation option for the rule specified in the `ViolationTarget`.

## Contents
<a name="API_SecurityGroupRemediationAction_Contents"></a>

 ** Description **   <a name="fms-Type-SecurityGroupRemediationAction-Description"></a>
Brief description of the action that will be performed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** IsDefaultAction **   <a name="fms-Type-SecurityGroupRemediationAction-IsDefaultAction"></a>
Indicates if the current action is the default action.
Type: Boolean
Required: No

 ** RemediationActionType **   <a name="fms-Type-SecurityGroupRemediationAction-RemediationActionType"></a>
The remediation action that will be performed.
Type: String
Valid Values: `REMOVE | MODIFY`
Required: No

 ** RemediationResult **   <a name="fms-Type-SecurityGroupRemediationAction-RemediationResult"></a>
The final state of the rule specified in the `ViolationTarget` after it is remediated.
Type: [SecurityGroupRuleDescription](API_SecurityGroupRuleDescription.md) object
Required: No

## See Also
<a name="API_SecurityGroupRemediationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/SecurityGroupRemediationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/SecurityGroupRemediationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/SecurityGroupRemediationAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
