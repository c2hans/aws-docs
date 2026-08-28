---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineGranularityOptions.html
---

# IsolineGranularityOptions
<a name="API_IsolineGranularityOptions"></a>

Controls the detail level and smoothness of generated isolines. More detailed isolines provide better visual representation of reachable areas but require more processing time and result in larger responses.

## Contents
<a name="API_IsolineGranularityOptions_Contents"></a>

 ** MaxPoints **   <a name="location-Type-IsolineGranularityOptions-MaxPoints"></a>
The maximum number of points used to define each isoline. Higher values create smoother, more detailed shapes.
Type: Integer
Valid Range: Minimum value of 31.
Required: No

 ** MaxResolution **   <a name="location-Type-IsolineGranularityOptions-MaxResolution"></a>
The maximum distance in meters between points along the isoline. Smaller values create more detailed shapes.
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_IsolineGranularityOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineGranularityOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineGranularityOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineGranularityOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
