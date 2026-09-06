---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_MonetizationFilter.html
---

# MonetizationFilter
<a name="API_MonetizationFilter"></a>

A filter for narrowing monetization statistics and settlement record results. Specify a filter name and one or more values to match.

Filter behavior:
+ Multiple values within one filter: OR (match any)
+ Multiple filters: AND (all must match)
+ No duplicate filter names allowed (rejected with error)
+ Duplicate values within a filter are silently deduplicated
+ If no `CurrencyMode` filter is specified, defaults to `REAL`

## Contents
<a name="API_MonetizationFilter_Contents"></a>

 ** Name **   <a name="WAF-Type-MonetizationFilter-Name"></a>
The filter name. Format: Key is a string, Value is a list of strings.
Enum-restricted (invalid values rejected):
+  `CurrencyMode`: `REAL`, `TEST`
+  `ChainName`: `BASE`, `SOLANA`, `BASE_SEPOLIA`, `SOLANA_DEVNET`
+  `SettlementStatus`: `SETTLED`, `PENDING`, `FAILED`, `SERVICE_ERROR`, `SKIPPED_ORIGIN_ERROR`, `DUPLICATE`
+  `HttpSourceName`: `CF`, `ALB`, `APIGW`, `APPRUNNER`, `COGNITO`, `VERIFIED_ACCESS`
ARN-validated:
+  `WebACLArn`: valid WAFv2 web ACL ARN
Free-text (any string up to 256 chars):
+  `SourceName`: The name of the bot. Populated from Bot Control verified bot labels.
+  `SourceCategory`: The category classification of the bot. From Bot Control categorization.
+  `Intent`: The declared intent of the bot request.
+  `Organization`: The organization operating the bot.
+  `UriPathPrefix`: The URI path of the request that was monetized.
+  `RequestId`: The AWS WAF request ID associated with the transaction. Matches the requestId in AWS WAF logs. Pattern: `^[a-zA-Z0-9:._\-=+/]+$`
+  `TransactionId`: The blockchain transaction identifier. Pattern: `^[a-zA-Z0-9:._\-=+/]+$`
+  `TerminatingRuleName`: The name of the AWS WAF rule that triggered the Monetize action.
+  `PayerAddress`: The blockchain wallet address of the paying client. Pattern: `^[a-zA-Z0-9:._\-=+/]+$`
+  `HttpSourceId`: The identifier of the AWS resource associated with the web ACL (for example, CloudFront distribution ID).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Values **   <a name="WAF-Type-MonetizationFilter-Values"></a>
The values to filter on. Specify as a list of strings. Results match any of the specified values (OR logic). Duplicate values are silently deduplicated. Maximum: 20 values per filter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_MonetizationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/MonetizationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/MonetizationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/MonetizationFilter)
