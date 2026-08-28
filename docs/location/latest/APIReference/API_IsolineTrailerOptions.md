---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineTrailerOptions.html
---

# IsolineTrailerOptions
<a name="API_IsolineTrailerOptions"></a>

Additional specifications when the vehicle includes one or more trailers.

## Contents
<a name="API_IsolineTrailerOptions_Contents"></a>

 ** AxleCount **   <a name="location-Type-IsolineTrailerOptions-AxleCount"></a>
The total number of axles across all trailers. Used for weight distribution calculations and road restrictions.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** TrailerCount **   <a name="location-Type-IsolineTrailerOptions-TrailerCount"></a>
The number of trailers being pulled. Affects which roads can be used based on local regulations.
Default value: `0`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 255.
Required: No

## See Also
<a name="API_IsolineTrailerOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineTrailerOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineTrailerOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineTrailerOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
