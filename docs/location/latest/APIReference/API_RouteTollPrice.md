---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollPrice.html
---

# RouteTollPrice
<a name="API_RouteTollPrice"></a>

The toll price.

## Contents
<a name="API_RouteTollPrice_Contents"></a>

 ** Currency **   <a name="location-Type-RouteTollPrice-Currency"></a>
Currency code corresponding to the price. This is the same as Currency specified in the request.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: Yes

 ** Estimate **   <a name="location-Type-RouteTollPrice-Estimate"></a>
If the price is an estimate or an exact value.
Type: Boolean
Required: Yes

 ** Range **   <a name="location-Type-RouteTollPrice-Range"></a>
If the price is a range or an exact value. If any of the toll fares making up the route is a range, the overall price is also a range.
Type: Boolean
Required: Yes

 ** Value **   <a name="location-Type-RouteTollPrice-Value"></a>
Exact price, if not a range.
Type: Double
Valid Range: Minimum value of 0.0.
Required: Yes

 ** PerDuration **   <a name="location-Type-RouteTollPrice-PerDuration"></a>
Duration for which the price corresponds to.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** RangeValue **   <a name="location-Type-RouteTollPrice-RangeValue"></a>
Price range with a minimum and maximum value, if a range.
Type: [RouteTollPriceValueRange](API_RouteTollPriceValueRange.md) object
Required: No

## See Also
<a name="API_RouteTollPrice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTollPrice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTollPrice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTollPrice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
