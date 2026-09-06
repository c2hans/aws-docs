---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_TransformationJobProperties.html
---

# TransformationJobProperties
<a name="API_TransformationJobProperties"></a>

Contains the properties of a data transformation job, including its status, configuration, and progress information. You retrieve this structure by calling `DescribeDataTransformationJob`.

## Contents
<a name="API_TransformationJobProperties_Contents"></a>

 ** DataAccessRoleArn **   <a name="HealthLake-Type-TransformationJobProperties-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants AWS HealthLake access to the specified Amazon S3 locations. AWS HealthLake assumes this role to read input files and write output files.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: Yes

 ** InputDataConfig **   <a name="HealthLake-Type-TransformationJobProperties-InputDataConfig"></a>
The Amazon S3 location and format of the source files for this job.
Type: [TransformationInputDataConfig](API_TransformationInputDataConfig.md) object
Required: Yes

 ** JobId **   <a name="HealthLake-Type-TransformationJobProperties-JobId"></a>
The unique identifier of the data transformation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** JobStatus **   <a name="HealthLake-Type-TransformationJobProperties-JobStatus"></a>
The current status of the data transformation job.
Type: String
Valid Values: `SUBMITTED | QUEUED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`
Required: Yes

 ** OutputDataConfig **   <a name="HealthLake-Type-TransformationJobProperties-OutputDataConfig"></a>
The Amazon S3 location and encryption configuration for the converted output.
Type: [TransformationOutputDataConfig](API_TransformationOutputDataConfig.md) object
Required: Yes

 ** SubmitTime **   <a name="HealthLake-Type-TransformationJobProperties-SubmitTime"></a>
The timestamp when the job was submitted.
Type: Timestamp
Required: Yes

 ** DriftDetectionEnabled **   <a name="HealthLake-Type-TransformationJobProperties-DriftDetectionEnabled"></a>
Specifies whether drift detection is enabled for this job. When enabled, AWS HealthLake writes a drift report to the output Amazon S3 location alongside the converted files.
Type: Boolean
Required: No

 ** EndTime **   <a name="HealthLake-Type-TransformationJobProperties-EndTime"></a>
The timestamp when the job completed or failed.
Type: Timestamp
Required: No

 ** JobName **   <a name="HealthLake-Type-TransformationJobProperties-JobName"></a>
The name of the data transformation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-%@]*`
Required: No

 ** JobProgressReport **   <a name="HealthLake-Type-TransformationJobProperties-JobProgressReport"></a>
The progress report for the data transformation job, including counts of files processed and resources generated.
Type: [TransformationJobProgressReport](API_TransformationJobProgressReport.md) object
Required: No

 ** Message **   <a name="HealthLake-Type-TransformationJobProperties-Message"></a>
An informational message about the job, such as an error description if the job failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ProfileId **   <a name="HealthLake-Type-TransformationJobProperties-ProfileId"></a>
The unique identifier of the data transformation profile used for this job.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`
Required: No

 ** ProfileName **   <a name="HealthLake-Type-TransformationJobProperties-ProfileName"></a>
The name of the data transformation profile used for this job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ProfileVersion **   <a name="HealthLake-Type-TransformationJobProperties-ProfileVersion"></a>
The version number of the data transformation profile used for this job.
Type: Integer
Required: No

 ** ProvenanceEnabled **   <a name="HealthLake-Type-TransformationJobProperties-ProvenanceEnabled"></a>
Specifies whether FHIR R4 Provenance resource generation is enabled for this transformation job. When provenance is enabled, the service also generates related DocumentReference and Device resources.
Type: Boolean
Required: No

## See Also
<a name="API_TransformationJobProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/TransformationJobProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/TransformationJobProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/TransformationJobProperties)
