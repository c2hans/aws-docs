---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_PublishedDateFilter.html
---

# PublishedDateFilter
<a name="API_PublishedDateFilter"></a>

A publication time range for the results. Both bounds are optional, and both are inclusive. If `publishedAfter` is later than `publishedBefore`, the request fails with a `ValidationException`.

## Contents
<a name="API_PublishedDateFilter_Contents"></a>

 ** publishedAfter **   <a name="BedrockAgentCore-Type-PublishedDateFilter-publishedAfter"></a>
The earliest publication time of the results, inclusive.
Type: Timestamp
Required: No

 ** publishedBefore **   <a name="BedrockAgentCore-Type-PublishedDateFilter-publishedBefore"></a>
The latest publication time of the results, inclusive. A date without a time, such as one passed to the AWS CLI, means midnight UTC. To include a whole day, use the last second of that day, for example `2026-01-31T23:59:59Z`.
Type: Timestamp
Required: No

## See Also
<a name="API_PublishedDateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PublishedDateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PublishedDateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PublishedDateFilter)
