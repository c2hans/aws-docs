---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ExportSummary.html
---

# ExportSummary
<a name="API_ExportSummary"></a>

A summary of an export job, as returned by `ListExportJobsV2`.

## Contents
<a name="API_ExportSummary_Contents"></a>

 ** DataType **   <a name="securityhub-Type-ExportSummary-DataType"></a>
The category of data that the export job produces.
Type: String
Valid Values: `FINDINGS`
Required: Yes

 ** Destination **   <a name="securityhub-Type-ExportSummary-Destination"></a>
The destination that the export job writes to.
Type: [ExportDestination](API_ExportDestination.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** ExportJobId **   <a name="securityhub-Type-ExportSummary-ExportJobId"></a>
The unique identifier of the export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`
Required: Yes

 ** StartedAt **   <a name="securityhub-Type-ExportSummary-StartedAt"></a>
The time when the export job was created.
For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: Yes

 ** Status **   <a name="securityhub-Type-ExportSummary-Status"></a>
The current state of the export job.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | CANCELLED`
Required: Yes

 ** EndedAt **   <a name="securityhub-Type-ExportSummary-EndedAt"></a>
The time when the export job reached a terminal state. Absent while the job is `RUNNING`.
For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

 ** FailureCode **   <a name="securityhub-Type-ExportSummary-FailureCode"></a>
A code that classifies why the export job failed. Present only when `Status` is `FAILED`.
Type: String
Valid Values: `ACCESS_DENIED | RESOURCE_NOT_FOUND | INTERNAL_ERROR`
Required: No

 ** FailureMessage **   <a name="securityhub-Type-ExportSummary-FailureMessage"></a>
A human-readable message about why the export job failed. Present only when `Status` is `FAILED`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-ExportSummary-Name"></a>
The user-provided name of the export job, if one was specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** OutputConfiguration **   <a name="securityhub-Type-ExportSummary-OutputConfiguration"></a>
The output configuration of the export job. For findings exports, this reports the output format. Present only for findings exports; absent for other data types.
Type: [ExportOutputSummary](API_ExportOutputSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Scopes **   <a name="securityhub-Type-ExportSummary-Scopes"></a>
The organization scopes that the export job was started with, echoed verbatim. Absent if the caller didn't supply `Scopes`.
Type: [ExportScopes](API_ExportScopes.md) object
Required: No

## See Also
<a name="API_ExportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ExportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ExportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ExportSummary)
