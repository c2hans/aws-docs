---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_SourceStatistics.html
---

# SourceStatistics
<a name="API_SourceStatistics"></a>

Revenue statistics for a single AI bot source, including the bot name, revenue amount, request count, and verification status.

## Contents
<a name="API_SourceStatistics_Contents"></a>

 ** Amount **   <a name="WAF-Type-SourceStatistics-Amount"></a>
The total revenue amount from this source in the specified currency.
Type: String
Required: Yes

 ** Percentage **   <a name="WAF-Type-SourceStatistics-Percentage"></a>
The percentage of total revenue from this source.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: Yes

 ** RequestCount **   <a name="WAF-Type-SourceStatistics-RequestCount"></a>
The number of monetized requests from this source.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** SourceName **   <a name="WAF-Type-SourceStatistics-SourceName"></a>
The name of the AI bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** GroupByValue **   <a name="WAF-Type-SourceStatistics-GroupByValue"></a>
The value for the group-by dimension, when grouping is applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Intent **   <a name="WAF-Type-SourceStatistics-Intent"></a>
The declared intent of the AI bot (for example, summarize, index, or train).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Organization **   <a name="WAF-Type-SourceStatistics-Organization"></a>
The organization associated with the AI bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** SourceCategory **   <a name="WAF-Type-SourceStatistics-SourceCategory"></a>
The category of this AI bot source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Verified **   <a name="WAF-Type-SourceStatistics-Verified"></a>
Indicates whether the AI bot's identity was verified — for example, through a cryptographically signed request (Web Bot Auth) or another published verification method. This value is meaningful only when GroupBy is NAME, where each result represents a single, identifiable bot. For all other GroupBy values (CATEGORY, INTENT, ORGANIZATION, or WEBACL), a result aggregates multiple bots that may have different verification states, so Verified is always returned as false and should be ignored. Type and required-ness are unchanged (Boolean, optional).
Type: Boolean
Required: No

## See Also
<a name="API_SourceStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/SourceStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/SourceStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/SourceStatistics)
