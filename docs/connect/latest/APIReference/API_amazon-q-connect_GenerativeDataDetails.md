---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_GenerativeDataDetails.html
---

# GenerativeDataDetails
<a name="API_amazon-q-connect_GenerativeDataDetails"></a>

Details about generative data.

## Contents
<a name="API_amazon-q-connect_GenerativeDataDetails_Contents"></a>

 ** completion **   <a name="connect-Type-amazon-q-connect_GenerativeDataDetails-completion"></a>
The LLM response.
Type: String
Required: Yes

 ** rankingData **   <a name="connect-Type-amazon-q-connect_GenerativeDataDetails-rankingData"></a>
Details about the generative content ranking data.
Type: [RankingData](API_amazon-q-connect_RankingData.md) object
Required: Yes

 ** references **   <a name="connect-Type-amazon-q-connect_GenerativeDataDetails-references"></a>
The references used to generative the LLM response.
Type: Array of [DataSummary](API_amazon-q-connect_DataSummary.md) objects
Required: Yes

## See Also
<a name="API_amazon-q-connect_GenerativeDataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GenerativeDataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GenerativeDataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GenerativeDataDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
