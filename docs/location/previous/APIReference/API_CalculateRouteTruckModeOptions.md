---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteTruckModeOptions.html
---

# CalculateRouteTruckModeOptions
<a name="API_CalculateRouteTruckModeOptions"></a>

Contains details about additional route preferences for requests that specify `TravelMode` as `Truck`.

## Contents
<a name="API_CalculateRouteTruckModeOptions_Contents"></a>

 ** AvoidFerries **   <a name="location-Type-CalculateRouteTruckModeOptions-AvoidFerries"></a>
Avoids ferries when calculating routes.
Default Value: `false`
Valid Values: `false` \| `true`
Type: Boolean
Required: No

 ** AvoidTolls **   <a name="location-Type-CalculateRouteTruckModeOptions-AvoidTolls"></a>
Avoids tolls when calculating routes.
Default Value: `false`
Valid Values: `false` \| `true`
Type: Boolean
Required: No

 ** Dimensions **   <a name="location-Type-CalculateRouteTruckModeOptions-Dimensions"></a>
Specifies the truck's dimension specifications including length, height, width, and unit of measurement. Used to avoid roads that can't support the truck's dimensions.
Type: [TruckDimensions](API_TruckDimensions.md) object
Required: No

 ** Weight **   <a name="location-Type-CalculateRouteTruckModeOptions-Weight"></a>
Specifies the truck's weight specifications including total weight and unit of measurement. Used to avoid roads that can't support the truck's weight.
Type: [TruckWeight](API_TruckWeight.md) object
Required: No

## See Also
<a name="API_CalculateRouteTruckModeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CalculateRouteTruckModeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CalculateRouteTruckModeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CalculateRouteTruckModeOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
