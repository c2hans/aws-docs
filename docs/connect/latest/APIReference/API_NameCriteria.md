---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_NameCriteria.html
---

# NameCriteria
<a name="API_NameCriteria"></a>

The search criteria based on the contact name

## Contents
<a name="API_NameCriteria_Contents"></a>

 ** MatchType **   <a name="connect-Type-NameCriteria-MatchType"></a>
The match type combining name search criteria using multiple search texts in a name criteria.
Type: String
Valid Values: `MATCH_ALL | MATCH_ANY | MATCH_EXACT | MATCH_NONE`
Required: Yes

 ** SearchText **   <a name="connect-Type-NameCriteria-SearchText"></a>
The words or phrases used to match the contact name.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Maximum length of 128.
Required: Yes

## See Also
<a name="API_NameCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/NameCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/NameCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/NameCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
