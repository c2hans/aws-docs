---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSummary.html
---

# RouteSummary
<a name="API_RouteSummary"></a>

Summarized details for the leg including travel steps only. The Distance for the travel only portion of the journey is the same as the Distance within the Overview summary.

## Contents
<a name="API_RouteSummary_Contents"></a>

 ** Distance **   <a name="location-Type-RouteSummary-Distance"></a>
Distance of the route.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Duration **   <a name="location-Type-RouteSummary-Duration"></a>
Duration of the route.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Tolls **   <a name="location-Type-RouteSummary-Tolls"></a>
Toll summary for the complete route.
Type: [RouteTollSummary](API_RouteTollSummary.md) object
Required: No

## See Also
<a name="API_RouteSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
