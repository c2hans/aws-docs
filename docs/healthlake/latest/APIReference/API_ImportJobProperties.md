---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ImportJobProperties.html
---

# ImportJobProperties
<a name="API_ImportJobProperties"></a>

The import job properties.

## Contents
<a name="API_ImportJobProperties_Contents"></a>

 ** DatastoreId **   <a name="HealthLake-Type-ImportJobProperties-DatastoreId"></a>
The data store identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** InputDataConfig **   <a name="HealthLake-Type-ImportJobProperties-InputDataConfig"></a>
The input data configuration supplied when the import job was created.
Type: [InputDataConfig](API_InputDataConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** JobId **   <a name="HealthLake-Type-ImportJobProperties-JobId"></a>
The import job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** JobStatus **   <a name="HealthLake-Type-ImportJobProperties-JobStatus"></a>
The import job status.
Type: String
Valid Values: `SUBMITTED | QUEUED | IN_PROGRESS | COMPLETED_WITH_ERRORS | COMPLETED | FAILED | CANCEL_SUBMITTED | CANCEL_IN_PROGRESS | CANCEL_COMPLETED | CANCEL_FAILED`
Required: Yes

 ** SubmitTime **   <a name="HealthLake-Type-ImportJobProperties-SubmitTime"></a>
The time the import job was submitted for processing.
Type: Timestamp
Required: Yes

 ** DataAccessRoleArn **   <a name="HealthLake-Type-ImportJobProperties-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) that grants AWS HealthLake access to the input data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** EndTime **   <a name="HealthLake-Type-ImportJobProperties-EndTime"></a>
The time the import job was completed.
Type: Timestamp
Required: No

 ** JobName **   <a name="HealthLake-Type-ImportJobProperties-JobName"></a>
The import job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** JobOutputDataConfig **   <a name="HealthLake-Type-ImportJobProperties-JobOutputDataConfig"></a>
The output data configuration supplied when the export job was created.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** JobProgressReport **   <a name="HealthLake-Type-ImportJobProperties-JobProgressReport"></a>
Displays the progress of the import job, including total resources scanned, total resources imported, and total size of data imported.
Type: [JobProgressReport](API_JobProgressReport.md) object
Required: No

 ** Message **   <a name="HealthLake-Type-ImportJobProperties-Message"></a>
An explanation of any errors that might have occurred during the FHIR import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** ValidationLevel **   <a name="HealthLake-Type-ImportJobProperties-ValidationLevel"></a>
The validation level of the import job.
Type: String
Valid Values: `strict | structure-only | minimal`
Required: No

## See Also
<a name="API_ImportJobProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/ImportJobProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/ImportJobProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/ImportJobProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
