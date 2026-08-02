---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ScanJobSummary.html
---

# ScanJobSummary
<a name="API_ScanJobSummary"></a>

Contains summary information about scan jobs, including counts and metadata for a specific time period and criteria.

## Contents
<a name="API_ScanJobSummary_Contents"></a>

 ** AccountId **   <a name="Backup-Type-ScanJobSummary-AccountId"></a>
The account ID that owns the scan jobs included in this summary.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** Count **   <a name="Backup-Type-ScanJobSummary-Count"></a>
The number of scan jobs that match the specified criteria.
Type: Integer
Required: No

 ** EndTime **   <a name="Backup-Type-ScanJobSummary-EndTime"></a>
The value of time in number format of a job end time.
This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** MalwareScanner **   <a name="Backup-Type-ScanJobSummary-MalwareScanner"></a>
Specifies the malware scanner used during the scan job. Currently only supports `GUARDDUTY`.
Type: String
Valid Values: `GUARDDUTY`
Required: No

 ** Region **   <a name="Backup-Type-ScanJobSummary-Region"></a>
The AWS Region where the scan jobs were executed.
Type: String
Required: No

 ** ResourceType **   <a name="Backup-Type-ScanJobSummary-ResourceType"></a>
The type of AWS resource for the scan jobs included in this summary.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

 ** ScanResultStatus **   <a name="Backup-Type-ScanJobSummary-ScanResultStatus"></a>
The scan result status for the scan jobs included in this summary.
Valid values: `THREATS_FOUND` \| `NO_THREATS_FOUND`.
Type: String
Valid Values: `NO_THREATS_FOUND | THREATS_FOUND | UNKNOWN`
Required: No

 ** StartTime **   <a name="Backup-Type-ScanJobSummary-StartTime"></a>
The value of time in number format of a job start time.
This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** State **   <a name="Backup-Type-ScanJobSummary-State"></a>
The state of the scan jobs included in this summary.
Valid values: `CREATED` \| `RUNNING` \| `COMPLETED` \| `COMPLETED_WITH_ISSUES` \| `FAILED` \| `CANCELED`.
Type: String
Valid Values: `CREATED | COMPLETED | COMPLETED_WITH_ISSUES | RUNNING | FAILED | CANCELED | AGGREGATE_ALL | ANY`
Required: No

## See Also
<a name="API_ScanJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ScanJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ScanJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ScanJobSummary)
