---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_AggregatedScanResult.html
---

# AggregatedScanResult
<a name="API_AggregatedScanResult"></a>

Contains aggregated scan results across multiple scan operations, providing a summary of scan status and findings.

## Contents
<a name="API_AggregatedScanResult_Contents"></a>

 ** FailedScan **   <a name="Backup-Type-AggregatedScanResult-FailedScan"></a>
A Boolean value indicating whether any of the aggregated scans failed.
Type: Boolean
Required: No

 ** Findings **   <a name="Backup-Type-AggregatedScanResult-Findings"></a>
An array of findings discovered across all aggregated scans.
Type: Array of strings
Valid Values: `MALWARE`
Required: No

 ** LastComputed **   <a name="Backup-Type-AggregatedScanResult-LastComputed"></a>
The timestamp when the aggregated scan result was last computed, in Unix format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

## See Also
<a name="API_AggregatedScanResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/AggregatedScanResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/AggregatedScanResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/AggregatedScanResult)
