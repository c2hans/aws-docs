---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_BotStatistics.html
---

# BotStatistics
<a name="API_BotStatistics"></a>

Statistics about a specific bot's traffic to a path, including the bot name, request count, and percentage of traffic.

## Contents
<a name="API_BotStatistics_Contents"></a>

 ** BotName **   <a name="WAF-Type-BotStatistics-BotName"></a>
The name of the bot. For example, `gptbot` or `googlebot`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** Percentage **   <a name="WAF-Type-BotStatistics-Percentage"></a>
The percentage of total requests to the associated path that came from this bot.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: Yes

 ** RequestCount **   <a name="WAF-Type-BotStatistics-RequestCount"></a>
The number of requests from this bot to the associated path within the specified time window.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_BotStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/BotStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/BotStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/BotStatistics)
