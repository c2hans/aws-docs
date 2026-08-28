---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CaseRuleSummary.html
---

# CaseRuleSummary
<a name="API_connect-cases_CaseRuleSummary"></a>

Summary information of this case rule. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_CaseRuleSummary_Contents"></a>

 ** caseRuleArn **   <a name="connect-Type-connect-cases_CaseRuleSummary-caseRuleArn"></a>
The Amazon Resource Name (ARN) of the case rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** caseRuleId **   <a name="connect-Type-connect-cases_CaseRuleSummary-caseRuleId"></a>
Unique identifier of a case rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** name **   <a name="connect-Type-connect-cases_CaseRuleSummary-name"></a>
Name of the case rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

 ** ruleType **   <a name="connect-Type-connect-cases_CaseRuleSummary-ruleType"></a>
Possible types for a rule.
Type: String
Valid Values: `Required | Hidden | FieldOptions`
Required: Yes

 ** description **   <a name="connect-Type-connect-cases_CaseRuleSummary-description"></a>
Description of a case rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_connect-cases_CaseRuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CaseRuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CaseRuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CaseRuleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
