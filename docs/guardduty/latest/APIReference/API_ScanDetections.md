---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScanDetections.html
---

# ScanDetections
<a name="API_ScanDetections"></a>

Contains a complete view providing malware scan result details.

## Contents
<a name="API_ScanDetections_Contents"></a>

 ** highestSeverityThreatDetails **   <a name="guardduty-Type-ScanDetections-highestSeverityThreatDetails"></a>
Details of the highest severity threat detected during malware scan and number of infected files.
Type: [HighestSeverityThreatDetails](API_HighestSeverityThreatDetails.md) object
Required: No

 ** scannedItemCount **   <a name="guardduty-Type-ScanDetections-scannedItemCount"></a>
Total number of scanned files.
Type: [ScannedItemCount](API_ScannedItemCount.md) object
Required: No

 ** threatDetectedByName **   <a name="guardduty-Type-ScanDetections-threatDetectedByName"></a>
Contains details about identified threats organized by threat name.
Type: [ThreatDetectedByName](API_ThreatDetectedByName.md) object
Required: No

 ** threatsDetectedItemCount **   <a name="guardduty-Type-ScanDetections-threatsDetectedItemCount"></a>
Total number of infected files.
Type: [ThreatsDetectedItemCount](API_ThreatsDetectedItemCount.md) object
Required: No

## See Also
<a name="API_ScanDetections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScanDetections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScanDetections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScanDetections)
