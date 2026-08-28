---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleSet.html
---

# RuleSet
<a name="API_RuleSet"></a>

A rule set contains a list of rules that are evaluated in order. Each rule is evaluated sequentially for each email.

## Contents
<a name="API_RuleSet_Contents"></a>

 ** LastModificationDate **   <a name="sesmailmanager-Type-RuleSet-LastModificationDate"></a>
The last modification date of the rule set.
Type: Timestamp
Required: No

 ** RuleSetId **   <a name="sesmailmanager-Type-RuleSet-RuleSetId"></a>
The identifier of the rule set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** RuleSetName **   <a name="sesmailmanager-Type-RuleSet-RuleSetName"></a>
A user-friendly name for the rule set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_RuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
