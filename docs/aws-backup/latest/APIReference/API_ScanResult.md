---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ScanResult.html
---

# ScanResult
<a name="API_ScanResult"></a>

Contains the results of a security scan, including scanner information, scan state, and any findings discovered.

## Contents
<a name="API_ScanResult_Contents"></a>

 ** Findings **   <a name="Backup-Type-ScanResult-Findings"></a>
An array of findings discovered during the scan.
Type: Array of strings
Valid Values: `MALWARE`
Required: No

 ** LastScanTimestamp **   <a name="Backup-Type-ScanResult-LastScanTimestamp"></a>
The timestamp of when the last scan was performed, in Unix format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** MalwareScanner **   <a name="Backup-Type-ScanResult-MalwareScanner"></a>
The malware scanner used to perform the scan. Currently only `GUARDDUTY` is supported.
Type: String
Valid Values: `GUARDDUTY`
Required: No

 ** ScanJobState **   <a name="Backup-Type-ScanResult-ScanJobState"></a>
The final state of the scan job.
Valid values: `COMPLETED` \| `FAILED` \| `CANCELED`.
Type: String
Valid Values: `COMPLETED | COMPLETED_WITH_ISSUES | FAILED | CANCELED`
Required: No

## See Also
<a name="API_ScanResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ScanResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ScanResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ScanResult)
