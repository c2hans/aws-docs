---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EbsVolumeScanDetails.html
---

# EbsVolumeScanDetails
<a name="API_EbsVolumeScanDetails"></a>

Contains details from the malware scan that created a finding.

## Contents
<a name="API_EbsVolumeScanDetails_Contents"></a>

 ** scanCompletedAt **   <a name="guardduty-Type-EbsVolumeScanDetails-scanCompletedAt"></a>
Returns the completion date and time of the malware scan.
Type: Timestamp
Required: No

 ** scanDetections **   <a name="guardduty-Type-EbsVolumeScanDetails-scanDetections"></a>
Contains a complete view providing malware scan result details.
Type: [ScanDetections](API_ScanDetections.md) object
Required: No

 ** scanId **   <a name="guardduty-Type-EbsVolumeScanDetails-scanId"></a>
Unique Id of the malware scan that generated the finding.
Type: String
Required: No

 ** scanStartedAt **   <a name="guardduty-Type-EbsVolumeScanDetails-scanStartedAt"></a>
Returns the start date and time of the malware scan.
Type: Timestamp
Required: No

 ** scanType **   <a name="guardduty-Type-EbsVolumeScanDetails-scanType"></a>
Specifies the scan type that invoked the malware scan.
Type: String
Valid Values: `GUARDDUTY_INITIATED | ON_DEMAND`
Required: No

 ** sources **   <a name="guardduty-Type-EbsVolumeScanDetails-sources"></a>
Contains list of threat intelligence sources used to detect threats.
Type: Array of strings
Required: No

 ** triggerFindingId **   <a name="guardduty-Type-EbsVolumeScanDetails-triggerFindingId"></a>
GuardDuty finding ID that triggered a malware scan.
Type: String
Required: No

## See Also
<a name="API_EbsVolumeScanDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EbsVolumeScanDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EbsVolumeScanDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EbsVolumeScanDetails)
