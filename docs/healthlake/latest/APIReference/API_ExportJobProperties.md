---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ExportJobProperties.html
---

# ExportJobProperties
<a name="API_ExportJobProperties"></a>

The properties of a FHIR export job.

## Contents
<a name="API_ExportJobProperties_Contents"></a>

 ** DatastoreId **   <a name="HealthLake-Type-ExportJobProperties-DatastoreId"></a>
The data store identifier from which files are being exported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** JobId **   <a name="HealthLake-Type-ExportJobProperties-JobId"></a>
The export job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** JobStatus **   <a name="HealthLake-Type-ExportJobProperties-JobStatus"></a>
The export job status.
Type: String
Valid Values: `SUBMITTED | QUEUED | IN_PROGRESS | COMPLETED_WITH_ERRORS | COMPLETED | FAILED | CANCEL_SUBMITTED | CANCEL_IN_PROGRESS | CANCEL_COMPLETED | CANCEL_FAILED`
Required: Yes

 ** OutputDataConfig **   <a name="HealthLake-Type-ExportJobProperties-OutputDataConfig"></a>
The output data configuration supplied when the export job was created.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** SubmitTime **   <a name="HealthLake-Type-ExportJobProperties-SubmitTime"></a>
The time the export job was initiated.
Type: Timestamp
Required: Yes

 ** DataAccessRoleArn **   <a name="HealthLake-Type-ExportJobProperties-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) used during the initiation of the export job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** EndTime **   <a name="HealthLake-Type-ExportJobProperties-EndTime"></a>
The time the export job completed.
Type: Timestamp
Required: No

 ** JobName **   <a name="HealthLake-Type-ExportJobProperties-JobName"></a>
The export job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** Message **   <a name="HealthLake-Type-ExportJobProperties-Message"></a>
An explanation of any errors that might have occurred during the export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

## See Also
<a name="API_ExportJobProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/ExportJobProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/ExportJobProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/ExportJobProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
