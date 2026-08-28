---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_TruckWeight.html
---

# TruckWeight
<a name="API_TruckWeight"></a>

Contains details about the truck's weight specifications. Used to avoid roads that can't support or allow the total weight for requests that specify `TravelMode` as `Truck`.

## Contents
<a name="API_TruckWeight_Contents"></a>

 ** Total **   <a name="location-Type-TruckWeight-Total"></a>
The total weight of the truck.
+ For example, `3500`.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** Unit **   <a name="location-Type-TruckWeight-Unit"></a>
The unit of measurement to use for the truck weight.
Default Value: `Kilograms`
Type: String
Valid Values: `Kilograms | Pounds`
Required: No

## See Also
<a name="API_TruckWeight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/TruckWeight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/TruckWeight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/TruckWeight)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
