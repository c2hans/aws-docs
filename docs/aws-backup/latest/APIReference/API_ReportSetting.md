---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ReportSetting.html
---

# ReportSetting
<a name="API_ReportSetting"></a>

Contains detailed information about a report setting.

## Contents
<a name="API_ReportSetting_Contents"></a>

 ** ReportTemplate **   <a name="Backup-Type-ReportSetting-ReportTemplate"></a>
Identifies the report template for the report. Reports are built using a report template. The report templates are:
 `RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT | SCAN_JOB_REPORT`
Type: String
Required: Yes

 ** Accounts **   <a name="Backup-Type-ReportSetting-Accounts"></a>
These are the accounts to be included in the report.
Use string value of `ROOT` to include all organizational units.
Type: Array of strings
Required: No

 ** FrameworkArns **   <a name="Backup-Type-ReportSetting-FrameworkArns"></a>
The Amazon Resource Names (ARNs) of the frameworks a report covers.
Type: Array of strings
Required: No

 ** NumberOfFrameworks **   <a name="Backup-Type-ReportSetting-NumberOfFrameworks"></a>
The number of frameworks a report covers.
Type: Integer
Required: No

 ** OrganizationUnits **   <a name="Backup-Type-ReportSetting-OrganizationUnits"></a>
These are the Organizational Units to be included in the report.
Type: Array of strings
Required: No

 ** Regions **   <a name="Backup-Type-ReportSetting-Regions"></a>
These are the Regions to be included in the report.
Use the wildcard as the string value to include all Regions.
Type: Array of strings
Required: No

## See Also
<a name="API_ReportSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ReportSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ReportSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ReportSetting)
