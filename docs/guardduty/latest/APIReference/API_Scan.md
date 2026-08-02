---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Scan.html
---

# Scan
<a name="API_Scan"></a>

Contains information about malware scans associated with GuardDuty Malware Protection for EC2.

## Contents
<a name="API_Scan_Contents"></a>

 ** accountId **   <a name="guardduty-Type-Scan-accountId"></a>
The ID for the account that belongs to the scan.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** adminDetectorId **   <a name="guardduty-Type-Scan-adminDetectorId"></a>
The unique detector ID of the administrator account that the request is associated with. If the account is an administrator, the `AdminDetectorId` will be the same as the one used for `DetectorId`.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** attachedVolumes **   <a name="guardduty-Type-Scan-attachedVolumes"></a>
List of volumes that were attached to the original instance to be scanned.
Type: Array of [VolumeDetail](API_VolumeDetail.md) objects
Required: No

 ** detectorId **   <a name="guardduty-Type-Scan-detectorId"></a>
The unique ID of the detector that is associated with the request.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** failureReason **   <a name="guardduty-Type-Scan-failureReason"></a>
Represents the reason for `FAILED` scan status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** fileCount **   <a name="guardduty-Type-Scan-fileCount"></a>
Represents the number of files that were scanned.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** resourceDetails **   <a name="guardduty-Type-Scan-resourceDetails"></a>
Represents the resources that were scanned in the scan entry.
Type: [ResourceDetails](API_ResourceDetails.md) object
Required: No

 ** scanEndTime **   <a name="guardduty-Type-Scan-scanEndTime"></a>
The timestamp of when the scan was finished.
Type: Timestamp
Required: No

 ** scanId **   <a name="guardduty-Type-Scan-scanId"></a>
The unique scan ID associated with a scan entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** scanResultDetails **   <a name="guardduty-Type-Scan-scanResultDetails"></a>
Represents the result of the scan.
Type: [ScanResultDetails](API_ScanResultDetails.md) object
Required: No

 ** scanStartTime **   <a name="guardduty-Type-Scan-scanStartTime"></a>
The timestamp of when the scan was triggered.
Type: Timestamp
Required: No

 ** scanStatus **   <a name="guardduty-Type-Scan-scanStatus"></a>
An enum value representing possible scan statuses.
Type: String
Valid Values: `RUNNING | COMPLETED | FAILED | SKIPPED`
Required: No

 ** scanType **   <a name="guardduty-Type-Scan-scanType"></a>
Specifies the scan type that invoked the malware scan.
Type: String
Valid Values: `GUARDDUTY_INITIATED | ON_DEMAND`
Required: No

 ** totalBytes **   <a name="guardduty-Type-Scan-totalBytes"></a>
Represents total bytes that were scanned.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** triggerDetails **   <a name="guardduty-Type-Scan-triggerDetails"></a>
Specifies the reason why the scan was initiated.
Type: [TriggerDetails](API_TriggerDetails.md) object
Required: No

## See Also
<a name="API_Scan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Scan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Scan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Scan)
