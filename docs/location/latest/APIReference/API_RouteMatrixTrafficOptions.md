---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixTrafficOptions.html
---

# RouteMatrixTrafficOptions
<a name="API_RouteMatrixTrafficOptions"></a>

Traffic related options.

## Contents
<a name="API_RouteMatrixTrafficOptions_Contents"></a>

 ** FlowEventThresholdOverride **   <a name="location-Type-RouteMatrixTrafficOptions-FlowEventThresholdOverride"></a>
Duration for which flow traffic is considered valid. For this period, the flow traffic is used over historical traffic data. Flow traffic refers to congestion, which changes very quickly. Duration in seconds for which flow traffic event would be considered valid. While flow traffic event is valid it will be used over the historical traffic data.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Usage **   <a name="location-Type-RouteMatrixTrafficOptions-Usage"></a>
Determines if traffic should be used or ignored while calculating the route.
Default value: `UseTrafficData`
Type: String
Valid Values: `IgnoreTrafficData | UseTrafficData`
Required: No

## See Also
<a name="API_RouteMatrixTrafficOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixTrafficOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixTrafficOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixTrafficOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
