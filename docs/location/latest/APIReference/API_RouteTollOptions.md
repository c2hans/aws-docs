---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollOptions.html
---

# RouteTollOptions
<a name="API_RouteTollOptions"></a>

Options related to Tolls on a route.

## Contents
<a name="API_RouteTollOptions_Contents"></a>

 ** AllTransponders **   <a name="location-Type-RouteTollOptions-AllTransponders"></a>
Specifies if the user has valid transponder with access to all toll systems. This impacts toll calculation, and if true the price with transponders is used.
Type: Boolean
Required: No

 ** AllVignettes **   <a name="location-Type-RouteTollOptions-AllVignettes"></a>
Specifies if the user has valid vignettes with access for all toll roads. If a user has a vignette for a toll road, then toll cost for that road is omitted since no further payment is necessary.
Type: Boolean
Required: No

 ** Currency **   <a name="location-Type-RouteTollOptions-Currency"></a>
Currency code corresponding to the price. This is the same as Currency specified in the request.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

 ** EmissionType **   <a name="location-Type-RouteTollOptions-EmissionType"></a>
Emission type of the vehicle for toll cost calculation.
 **Valid values**: `Euro1, Euro2, Euro3, Euro4, Euro5, Euro6, EuroEev`
Type: [RouteEmissionType](API_RouteEmissionType.md) object
Required: No

 ** VehicleCategory **   <a name="location-Type-RouteTollOptions-VehicleCategory"></a>
Vehicle category for toll cost calculation.
Type: String
Valid Values: `Minibus`
Required: No

## See Also
<a name="API_RouteTollOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTollOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTollOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTollOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
