---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Price.html
---

# Price
<a name="API_Price"></a>

The price per request for a payment network, specifying the amount and cryptocurrency.

## Contents
<a name="API_Price_Contents"></a>

 ** Amount **   <a name="WAF-Type-Price-Amount"></a>
The price per request as a decimal string in the specified currency. Minimum: 0.001. Maximum: 999999999.999. Supports up to 3 decimal places.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 13.
Pattern: `^([1-9][0-9]*(\.[0-9]{1,3})?|0\.([1-9][0-9]{0,2}|0[1-9][0-9]?|00[1-9]))$`
Required: Yes

 ** Currency **   <a name="WAF-Type-Price-Currency"></a>
The cryptocurrency for payment. Currently only `USDC` is supported.
Type: String
Valid Values: `USDC`
Required: Yes

## See Also
<a name="API_Price_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Price)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Price)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Price)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
