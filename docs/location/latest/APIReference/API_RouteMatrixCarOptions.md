---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixCarOptions.html
---

# RouteMatrixCarOptions
<a name="API_RouteMatrixCarOptions"></a>

Travel mode options when the provided travel mode is `Car`.

## Contents
<a name="API_RouteMatrixCarOptions_Contents"></a>

 ** LicensePlate **   <a name="location-Type-RouteMatrixCarOptions-LicensePlate"></a>
The vehicle License Plate.
Type: [RouteMatrixVehicleLicensePlate](API_RouteMatrixVehicleLicensePlate.md) object
Required: No

 ** MaxSpeed **   <a name="location-Type-RouteMatrixCarOptions-MaxSpeed"></a>
Maximum speed
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 3.6. Maximum value of 252.0.
Required: No

 ** Occupancy **   <a name="location-Type-RouteMatrixCarOptions-Occupancy"></a>
The number of occupants in the vehicle.
Default value: `1`
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_RouteMatrixCarOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixCarOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixCarOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixCarOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
