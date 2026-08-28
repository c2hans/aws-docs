---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixEntry.html
---

# RouteMatrixEntry
<a name="API_RouteMatrixEntry"></a>

The calculated route matrix containing the results for all pairs of Origins to Destination positions. Each row corresponds to one entry in Origins. Each entry in the row corresponds to the route from that entry in Origins to an entry in Destination positions.

## Contents
<a name="API_RouteMatrixEntry_Contents"></a>

 ** Distance **   <a name="location-Type-RouteMatrixEntry-Distance"></a>
The total distance of travel for the route.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Duration **   <a name="location-Type-RouteMatrixEntry-Duration"></a>
The expected duration of travel for the route.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Error **   <a name="location-Type-RouteMatrixEntry-Error"></a>
Error code that occurred during calculation of the route.
Type: String
Valid Values: `NoMatch | NoMatchDestination | NoMatchOrigin | NoRoute | OutOfBounds | OutOfBoundsDestination | OutOfBoundsOrigin | Other | Violation`
Required: No

## See Also
<a name="API_RouteMatrixEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
