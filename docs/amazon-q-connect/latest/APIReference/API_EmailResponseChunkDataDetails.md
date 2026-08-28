---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_EmailResponseChunkDataDetails.html
---

# EmailResponseChunkDataDetails
<a name="API_amazon-q-connect_EmailResponseChunkDataDetails"></a>

Details of streaming chunk data for email responses including completion text and pagination tokens.

## Contents
<a name="API_amazon-q-connect_EmailResponseChunkDataDetails_Contents"></a>

 ** completion **   <a name="connect-Type-amazon-q-connect_EmailResponseChunkDataDetails-completion"></a>
The partial or complete professional email response text with appropriate greetings and closings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** nextChunkToken **   <a name="connect-Type-amazon-q-connect_EmailResponseChunkDataDetails-nextChunkToken"></a>
Token for retrieving the next chunk of streaming response data, if available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_amazon-q-connect_EmailResponseChunkDataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/EmailResponseChunkDataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/EmailResponseChunkDataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/EmailResponseChunkDataDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
