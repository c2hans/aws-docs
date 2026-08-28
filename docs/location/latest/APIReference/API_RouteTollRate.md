---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollRate.html
---

# RouteTollRate
<a name="API_RouteTollRate"></a>

The toll rate.

## Contents
<a name="API_RouteTollRate_Contents"></a>

 ** Id **   <a name="location-Type-RouteTollRate-Id"></a>
The Toll rate Id.
Type: String
Required: Yes

 ** LocalPrice **   <a name="location-Type-RouteTollRate-LocalPrice"></a>
Price in the local regional currency.
Type: [RouteTollPrice](API_RouteTollPrice.md) object
Required: Yes

 ** Name **   <a name="location-Type-RouteTollRate-Name"></a>
The name of the toll.
Type: String
Required: Yes

 ** PaymentMethods **   <a name="location-Type-RouteTollRate-PaymentMethods"></a>
Accepted payment methods at the toll.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 8 items.
Valid Values: `BankCard | Cash | CashExact | CreditCard | PassSubscription | TravelCard | Transponder | VideoToll`
Required: Yes

 ** Transponders **   <a name="location-Type-RouteTollRate-Transponders"></a>
Transponders for which this toll can be applied.
Type: Array of [RouteTransponder](API_RouteTransponder.md) objects
Required: Yes

 ** ApplicableTimes **   <a name="location-Type-RouteTollRate-ApplicableTimes"></a>
Time when the rate is valid.
Type: String
Required: No

 ** ConvertedPrice **   <a name="location-Type-RouteTollRate-ConvertedPrice"></a>
Price in the converted currency as specified in the request.
Type: [RouteTollPrice](API_RouteTollPrice.md) object
Required: No

 ** Pass **   <a name="location-Type-RouteTollRate-Pass"></a>
Details if the toll rate can be a pass that supports multiple trips.
Type: [RouteTollPass](API_RouteTollPass.md) object
Required: No

## See Also
<a name="API_RouteTollRate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTollRate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTollRate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTollRate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
