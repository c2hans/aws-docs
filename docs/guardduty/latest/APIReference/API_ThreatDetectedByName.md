---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ThreatDetectedByName.html
---

# ThreatDetectedByName
<a name="API_ThreatDetectedByName"></a>

Contains details about identified threats organized by threat name.

## Contents
<a name="API_ThreatDetectedByName_Contents"></a>

 ** itemCount **   <a name="guardduty-Type-ThreatDetectedByName-itemCount"></a>
Total number of infected files identified.
Type: Integer
Required: No

 ** shortened **   <a name="guardduty-Type-ThreatDetectedByName-shortened"></a>
Flag to determine if the finding contains every single infected file-path and/or every threat.
Type: Boolean
Required: No

 ** threatNames **   <a name="guardduty-Type-ThreatDetectedByName-threatNames"></a>
List of identified threats with details, organized by threat name.
Type: Array of [ScanThreatName](API_ScanThreatName.md) objects
Required: No

 ** uniqueThreatNameCount **   <a name="guardduty-Type-ThreatDetectedByName-uniqueThreatNameCount"></a>
Total number of unique threats by name identified, as part of the malware scan.
Type: Integer
Required: No

## See Also
<a name="API_ThreatDetectedByName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ThreatDetectedByName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ThreatDetectedByName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ThreatDetectedByName)
