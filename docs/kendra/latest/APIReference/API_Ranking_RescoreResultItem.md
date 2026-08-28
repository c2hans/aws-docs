---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_RescoreResultItem.html
---

# RescoreResultItem
<a name="API_Ranking_RescoreResultItem"></a>

A result item for a document with a new relevancy score.

## Contents
<a name="API_Ranking_RescoreResultItem_Contents"></a>

 ** DocumentId **   <a name="kendra-Type-Ranking_RescoreResultItem-DocumentId"></a>
The identifier of the document from the search service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Score **   <a name="kendra-Type-Ranking_RescoreResultItem-Score"></a>
The relevancy score or rank that Amazon Kendra Intelligent Ranking gives to the result.
Type: Float
Valid Range: Minimum value of -100000. Maximum value of 100000.
Required: No

## See Also
<a name="API_Ranking_RescoreResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-ranking-2022-10-19/RescoreResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-ranking-2022-10-19/RescoreResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-ranking-2022-10-19/RescoreResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
