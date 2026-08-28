---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_NetworkGeoLocation.html
---

# NetworkGeoLocation
<a name="API_NetworkGeoLocation"></a>

 Contains information about the location of a network endpoint involved in an Amazon GuardDuty Extended Threat Detection attack sequence. GuardDuty generates an attack sequence finding when multiple events align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you must have GuardDuty enabled. For more information, see [GuardDuty Extended Threat Detection ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) in the *Amazon GuardDuty User Guide*.

## Contents
<a name="API_NetworkGeoLocation_Contents"></a>

 ** City **   <a name="securityhub-Type-NetworkGeoLocation-City"></a>
 The name of the city.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Country **   <a name="securityhub-Type-NetworkGeoLocation-Country"></a>
 The name of the country.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Lat **   <a name="securityhub-Type-NetworkGeoLocation-Lat"></a>
 The latitude information of the endpoint location.
Type: Double
Required: No

 ** Lon **   <a name="securityhub-Type-NetworkGeoLocation-Lon"></a>
 The longitude information of the endpoint location.
Type: Double
Required: No

## See Also
<a name="API_NetworkGeoLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/NetworkGeoLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/NetworkGeoLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/NetworkGeoLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
