---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ConnectedAccountPrice.html
---

# ConnectedAccountPrice
<a name="API_ConnectedAccountPrice"></a>

The price per request for a connected account payment network, specifying the amount and cryptocurrency.

## Contents
<a name="API_ConnectedAccountPrice_Contents"></a>

 ** Amount **   <a name="WAF-Type-ConnectedAccountPrice-Amount"></a>
The price per request as a decimal string in the specified currency. Valid values range from 0.01 to 999999.99 USDC, with up to two decimal places. Sub-cent amounts are not supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 9.
Pattern: `^([1-9][0-9]{0,5}(\.[0-9]{1,2})?|0\.(0[1-9]|[1-9][0-9]?))$`
Required: Yes

 ** Currency **   <a name="WAF-Type-ConnectedAccountPrice-Currency"></a>
The cryptocurrency for payment. Currently only `USDC` is supported.
Type: String
Valid Values: `USDC`
Required: Yes

## See Also
<a name="API_ConnectedAccountPrice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ConnectedAccountPrice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ConnectedAccountPrice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ConnectedAccountPrice)
