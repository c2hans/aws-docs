---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_EmailGenerativeAnswerChunkDataDetails.html
---

# EmailGenerativeAnswerChunkDataDetails
<a name="API_amazon-q-connect_EmailGenerativeAnswerChunkDataDetails"></a>

Details of streaming chunk data for email generative answers including completion text and references.

## Contents
<a name="API_amazon-q-connect_EmailGenerativeAnswerChunkDataDetails_Contents"></a>

 ** completion **   <a name="connect-Type-amazon-q-connect_EmailGenerativeAnswerChunkDataDetails-completion"></a>
The partial or complete text content of the generative answer response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** nextChunkToken **   <a name="connect-Type-amazon-q-connect_EmailGenerativeAnswerChunkDataDetails-nextChunkToken"></a>
Token for retrieving the next chunk of streaming response data, if available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** references **   <a name="connect-Type-amazon-q-connect_EmailGenerativeAnswerChunkDataDetails-references"></a>
Source references and citations from knowledge base articles used to generate the answer.
Type: Array of [DataSummary](API_amazon-q-connect_DataSummary.md) objects
Required: No

## See Also
<a name="API_amazon-q-connect_EmailGenerativeAnswerChunkDataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/EmailGenerativeAnswerChunkDataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/EmailGenerativeAnswerChunkDataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/EmailGenerativeAnswerChunkDataDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
