---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryNotice.html
---

# RouteFerryNotice
<a name="API_RouteFerryNotice"></a>

Notices are additional information returned that indicate issues that occurred during route calculation.

## Contents
<a name="API_RouteFerryNotice_Contents"></a>

 ** Code **   <a name="location-Type-RouteFerryNotice-Code"></a>
Code corresponding to the issue.
Type: String
Valid Values: `AccuratePolylineUnavailable | NoSchedule | Other | ViolatedAvoidFerry | ViolatedAvoidRailFerry | SeasonalClosure | PotentialViolatedVehicleRestrictionUsage | ViolatedAvoidAreas | ViolatedVehicleRestriction`
Required: Yes

 ** Impact **   <a name="location-Type-RouteFerryNotice-Impact"></a>
Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.
Type: String
Valid Values: `High | Low`
Required: No

## See Also
<a name="API_RouteFerryNotice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteFerryNotice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteFerryNotice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteFerryNotice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
