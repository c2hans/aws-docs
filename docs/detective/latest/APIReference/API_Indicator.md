---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_Indicator.html
---

# Indicator
<a name="API_Indicator"></a>

Detective investigations triages indicators of compromises such as a finding and surfaces only the most critical and suspicious issues, so you can focus on high-level investigations. An `Indicator` lets you determine if an AWS resource is involved in unusual activity that could indicate malicious behavior and its impact.

## Contents
<a name="API_Indicator_Contents"></a>

 ** IndicatorDetail **   <a name="detective-Type-Indicator-IndicatorDetail"></a>
Details about the indicators of compromise that are used to determine if a resource is involved in a security incident. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident.
Type: [IndicatorDetail](API_IndicatorDetail.md) object
Required: No

 ** IndicatorType **   <a name="detective-Type-Indicator-IndicatorType"></a>
The type of indicator.
Type: String
Valid Values: `TTP_OBSERVED | IMPOSSIBLE_TRAVEL | FLAGGED_IP_ADDRESS | NEW_GEOLOCATION | NEW_ASO | NEW_USER_AGENT | RELATED_FINDING | RELATED_FINDING_GROUP`
Required: No

## See Also
<a name="API_Indicator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/Indicator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/Indicator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/Indicator)
