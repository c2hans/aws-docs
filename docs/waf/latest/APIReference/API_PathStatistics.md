---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_PathStatistics.html
---

# PathStatistics
<a name="API_PathStatistics"></a>

Statistics about bot traffic to a specific URI path, including the path, request count, percentage of total traffic, and the top bots accessing that path.

## Contents
<a name="API_PathStatistics_Contents"></a>

 ** Path **   <a name="WAF-Type-PathStatistics-Path"></a>
The URI path. For example, `/api/` or `/api/v1/users`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Percentage **   <a name="WAF-Type-PathStatistics-Percentage"></a>
The percentage of total requests that were made to this path.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: Yes

 ** RequestCount **   <a name="WAF-Type-PathStatistics-RequestCount"></a>
The number of requests to this path within the specified time window.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** Source **   <a name="WAF-Type-PathStatistics-Source"></a>
Information about the bot filter that was applied to generate these statistics. This field is only populated when you filter by bot category, organization, or name.
Type: [FilterSource](API_FilterSource.md) object
Required: No

 ** TopBots **   <a name="WAF-Type-PathStatistics-TopBots"></a>
The list of top bots accessing this path, ordered by request count. The number of bots included is determined by the `NumberOfTopTrafficBotsPerPath` parameter in the request.
Type: Array of [BotStatistics](API_BotStatistics.md) objects
Required: No

## See Also
<a name="API_PathStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/PathStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/PathStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/PathStatistics)
