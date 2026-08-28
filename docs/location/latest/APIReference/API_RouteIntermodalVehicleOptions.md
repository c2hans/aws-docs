---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteIntermodalVehicleOptions.html
---

# RouteIntermodalVehicleOptions
<a name="API_RouteIntermodalVehicleOptions"></a>

Options for the vehicle leg of the intermodal route.

## Contents
<a name="API_RouteIntermodalVehicleOptions_Contents"></a>

 ** AllowedModes **   <a name="location-Type-RouteIntermodalVehicleOptions-AllowedModes"></a>
Allowed vehicle transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with `ExcludedModes`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `All | Car`
Required: No

 ** EnabledFor **   <a name="location-Type-RouteIntermodalVehicleOptions-EnabledFor"></a>
Specifies the portion of the route for which this leg type is enabled. By default, the leg type is enabled for all legs. Valid values:
+  `FirstLeg` - Enable this leg type for the first non-pedestrian leg of the route.
+  `LastLeg` - Enable this leg type for the last non-pedestrian leg of the route.
+  `EntireRoute` - Enable this leg type for the entire route.
+  `None` - Disable this leg type entirely.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `FirstLeg | LastLeg | EntireRoute | None`
Required: No

 ** ExcludedModes **   <a name="location-Type-RouteIntermodalVehicleOptions-ExcludedModes"></a>
Excluded vehicle transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with `AllowedModes`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `All | Car`
Required: No

## See Also
<a name="API_RouteIntermodalVehicleOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteIntermodalVehicleOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteIntermodalVehicleOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteIntermodalVehicleOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
