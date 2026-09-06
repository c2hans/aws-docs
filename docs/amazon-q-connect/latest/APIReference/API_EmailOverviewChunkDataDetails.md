---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_EmailOverviewChunkDataDetails.html
---

# EmailOverviewChunkDataDetails
<a name="API_amazon-q-connect_EmailOverviewChunkDataDetails"></a>

Details of streaming chunk data for email overview including completion text and pagination tokens.

## Contents
<a name="API_amazon-q-connect_EmailOverviewChunkDataDetails_Contents"></a>

 ** completion **   <a name="connect-Type-amazon-q-connect_EmailOverviewChunkDataDetails-completion"></a>
The partial or complete overview text content in structured HTML format with customer issues, resolutions, and next steps.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** nextChunkToken **   <a name="connect-Type-amazon-q-connect_EmailOverviewChunkDataDetails-nextChunkToken"></a>
Token for retrieving the next chunk of streaming overview data, if available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_amazon-q-connect_EmailOverviewChunkDataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/EmailOverviewChunkDataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/EmailOverviewChunkDataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/EmailOverviewChunkDataDetails)
