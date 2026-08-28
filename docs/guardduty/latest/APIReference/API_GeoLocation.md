---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GeoLocation.html
---

# GeoLocation
<a name="API_GeoLocation"></a>

Contains information about the location of the remote IP address. By default, GuardDuty returns `Geolocation` with `Lat` and `Lon` as `0.0`.

## Contents
<a name="API_GeoLocation_Contents"></a>

 ** lat **   <a name="guardduty-Type-GeoLocation-lat"></a>
The latitude information of the remote IP address.
Type: Double
Required: No

 ** lon **   <a name="guardduty-Type-GeoLocation-lon"></a>
The longitude information of the remote IP address.
Type: Double
Required: No

## See Also
<a name="API_GeoLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GeoLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GeoLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GeoLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
