---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_SpellCorrectedQuery.html
---

# SpellCorrectedQuery
<a name="API_SpellCorrectedQuery"></a>

A query with suggested spell corrections.

## Contents
<a name="API_SpellCorrectedQuery_Contents"></a>

 ** Corrections **   <a name="kendra-Type-SpellCorrectedQuery-Corrections"></a>
The corrected misspelled word or words in a query.
Type: Array of [Correction](API_Correction.md) objects
Required: No

 ** SuggestedQueryText **   <a name="kendra-Type-SpellCorrectedQuery-SuggestedQueryText"></a>
The query with the suggested spell corrections.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_SpellCorrectedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/SpellCorrectedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/SpellCorrectedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/SpellCorrectedQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
