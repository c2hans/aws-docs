---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupSourceCustomActionsDetails.html
---

# RuleGroupSourceCustomActionsDetails
<a name="API_RuleGroupSourceCustomActionsDetails"></a>

A custom action definition. A custom action is an optional, non-standard action to use for stateless packet handling.

## Contents
<a name="API_RuleGroupSourceCustomActionsDetails_Contents"></a>

 ** ActionDefinition **   <a name="securityhub-Type-RuleGroupSourceCustomActionsDetails-ActionDefinition"></a>
The definition of a custom action.
Type: [StatelessCustomActionDefinition](API_StatelessCustomActionDefinition.md) object
Required: No

 ** ActionName **   <a name="securityhub-Type-RuleGroupSourceCustomActionsDetails-ActionName"></a>
A descriptive name of the custom action.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RuleGroupSourceCustomActionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupSourceCustomActionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupSourceCustomActionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupSourceCustomActionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
