---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_RouteMatrixEntryError.html
---

# RouteMatrixEntryError
<a name="API_RouteMatrixEntryError"></a>

An error corresponding to the calculation of a route between the `DeparturePosition` and `DestinationPosition`.

The error code can be one of the following:
+  `RouteNotFound` - Unable to find a valid route with the given parameters.
+  `RouteTooLong` - Route calculation went beyond the maximum size of a route and was terminated before completion.
+  `PositionsNotFound` - One or more of the input positions were not found on the route network.
+  `DestinationPositionNotFound` - The destination position was not found on the route network.
+  `DeparturePositionNotFound` - The departure position was not found on the route network.
+  `OtherValidationError` - The given inputs were not valid or a route was not found. More information is given in the error `Message`

## Contents
<a name="API_RouteMatrixEntryError_Contents"></a>

 ** Code **   <a name="location-Type-RouteMatrixEntryError-Code"></a>
The type of error which occurred for the route calculation.
Type: String
Valid Values: `RouteNotFound | RouteTooLong | PositionsNotFound | DestinationPositionNotFound | DeparturePositionNotFound | OtherValidationError`
Required: Yes

 ** Message **   <a name="location-Type-RouteMatrixEntryError-Message"></a>
A message about the error that occurred for the route calculation.
Type: String
Required: No

## See Also
<a name="API_RouteMatrixEntryError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/RouteMatrixEntryError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/RouteMatrixEntryError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/RouteMatrixEntryError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
