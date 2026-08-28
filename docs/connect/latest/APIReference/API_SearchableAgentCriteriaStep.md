---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchableAgentCriteriaStep.html
---

# SearchableAgentCriteriaStep
<a name="API_SearchableAgentCriteriaStep"></a>

The agent criteria to search for preferred agents on the routing criteria.

## Contents
<a name="API_SearchableAgentCriteriaStep_Contents"></a>

 ** AgentIds **   <a name="connect-Type-SearchableAgentCriteriaStep-AgentIds"></a>
The identifiers of agents used in preferred agents matching.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** MatchType **   <a name="connect-Type-SearchableAgentCriteriaStep-MatchType"></a>
The match type combining multiple agent criteria steps.
Type: String
Valid Values: `MATCH_ALL | MATCH_ANY | MATCH_EXACT | MATCH_NONE`
Required: No

## See Also
<a name="API_SearchableAgentCriteriaStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchableAgentCriteriaStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchableAgentCriteriaStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchableAgentCriteriaStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
