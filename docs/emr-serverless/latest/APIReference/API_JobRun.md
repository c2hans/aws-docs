---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobRun.html
---

# JobRun
<a name="API_JobRun"></a>

Information about a job run. A job run is a unit of work, such as a Spark JAR, Hive query, or SparkSQL query, that you submit to an Amazon EMR Serverless application.

## Contents
<a name="API_JobRun_Contents"></a>

 ** applicationId **   <a name="emrserverless-Type-JobRun-applicationId"></a>
The ID of the application the job is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** arn **   <a name="emrserverless-Type-JobRun-arn"></a>
The execution role ARN of the job run.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+\/jobruns\/[0-9a-zA-Z]+`
Required: Yes

 ** createdAt **   <a name="emrserverless-Type-JobRun-createdAt"></a>
The date and time when the job run was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="emrserverless-Type-JobRun-createdBy"></a>
The user who created the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+`
Required: Yes

 ** executionRole **   <a name="emrserverless-Type-JobRun-executionRole"></a>
The execution role ARN of the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** jobDriver **   <a name="emrserverless-Type-JobRun-jobDriver"></a>
The job driver for the job run.
Type: [JobDriver](API_JobDriver.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** jobRunId **   <a name="emrserverless-Type-JobRun-jobRunId"></a>
The ID of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** releaseLabel **   <a name="emrserverless-Type-JobRun-releaseLabel"></a>
The Amazon EMR release associated with the application your job is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: Yes

 ** state **   <a name="emrserverless-Type-JobRun-state"></a>
The state of the job run.
Type: String
Valid Values: `SUBMITTED | PENDING | SCHEDULED | RUNNING | SUCCESS | FAILED | CANCELLING | CANCELLED | QUEUED`
Required: Yes

 ** stateDetails **   <a name="emrserverless-Type-JobRun-stateDetails"></a>
The state details of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** updatedAt **   <a name="emrserverless-Type-JobRun-updatedAt"></a>
The date and time when the job run was updated.
Type: Timestamp
Required: Yes

 ** attempt **   <a name="emrserverless-Type-JobRun-attempt"></a>
The attempt of the job run.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** attemptCreatedAt **   <a name="emrserverless-Type-JobRun-attemptCreatedAt"></a>
The date and time of when the job run attempt was created.
Type: Timestamp
Required: No

 ** attemptUpdatedAt **   <a name="emrserverless-Type-JobRun-attemptUpdatedAt"></a>
The date and time of when the job run attempt was last updated.
Type: Timestamp
Required: No

 ** billedResourceUtilization **   <a name="emrserverless-Type-JobRun-billedResourceUtilization"></a>
The aggregate vCPU, memory, and storage that AWS has billed for the job run. The billed resources include a 1-minute minimum usage for workers, plus additional storage over 20 GB per worker. Note that billed resources do not include usage for idle pre-initialized workers.
Type: [ResourceUtilization](API_ResourceUtilization.md) object
Required: No

 ** configurationOverrides **   <a name="emrserverless-Type-JobRun-configurationOverrides"></a>
The configuration settings that are used to override default configuration.
Type: [ConfigurationOverrides](API_ConfigurationOverrides.md) object
Required: No

 ** endedAt **   <a name="emrserverless-Type-JobRun-endedAt"></a>
The date and time when the job was terminated.
Type: Timestamp
Required: No

 ** executionIamPolicy **   <a name="emrserverless-Type-JobRun-executionIamPolicy"></a>
Optional IAM policy. The resulting job IAM role permissions will be an intersection of the policies passed and the policy associated with your job execution role.
Type: [JobRunExecutionIamPolicy](API_JobRunExecutionIamPolicy.md) object
Required: No

 ** executionTimeoutMinutes **   <a name="emrserverless-Type-JobRun-executionTimeoutMinutes"></a>
Returns the job run timeout value from the `StartJobRun` call. If you didn't specify a timeout, this value defaults to 720 minutes.
For BATCH mode job runs, the maximum value is 10080 minutes (7 days) starting with Amazon EMR release 7.11.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

 ** imageConfiguration **   <a name="emrserverless-Type-JobRun-imageConfiguration"></a>
The applied image configuration.
Type: [ImageConfiguration](API_ImageConfiguration.md) object
Required: No

 ** mode **   <a name="emrserverless-Type-JobRun-mode"></a>
The mode of the job run.
Type: String
Valid Values: `BATCH | STREAMING`
Required: No

 ** name **   <a name="emrserverless-Type-JobRun-name"></a>
The optional job run name. This doesn't have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** networkConfiguration **   <a name="emrserverless-Type-JobRun-networkConfiguration"></a>
The network configuration for customer VPC connectivity.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** queuedDurationMilliseconds **   <a name="emrserverless-Type-JobRun-queuedDurationMilliseconds"></a>
The total time for a job in the QUEUED state in milliseconds.
Type: Long
Required: No

 ** retryPolicy **   <a name="emrserverless-Type-JobRun-retryPolicy"></a>
The retry policy of the job run.
Type: [RetryPolicy](API_RetryPolicy.md) object
Required: No

 ** startedAt **   <a name="emrserverless-Type-JobRun-startedAt"></a>
The date and time when the job moved to the RUNNING state.
Type: Timestamp
Required: No

 ** tags **   <a name="emrserverless-Type-JobRun-tags"></a>
The tags assigned to the job run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9 /_.:=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 /_.:=+@-]*`
Required: No

 ** totalExecutionDurationSeconds **   <a name="emrserverless-Type-JobRun-totalExecutionDurationSeconds"></a>
The job run total execution duration in seconds. This field is only available for job runs in a `COMPLETED`, `FAILED`, or `CANCELLED` state.
Type: Integer
Required: No

 ** totalResourceUtilization **   <a name="emrserverless-Type-JobRun-totalResourceUtilization"></a>
The aggregate vCPU, memory, and storage resources used from the time the job starts to execute, until the time the job terminates, rounded up to the nearest second.
Type: [TotalResourceUtilization](API_TotalResourceUtilization.md) object
Required: No

 ** workerTypeSpecifications **   <a name="emrserverless-Type-JobRun-workerTypeSpecifications"></a>
The specification applied to each worker type. Includes the JobRun-level ImageConfiguration when the applicationLevelDigestResolution is false for the application.
Type: String to [WorkerTypeSpecification](API_WorkerTypeSpecification.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Required: No

## See Also
<a name="API_JobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/JobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/JobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/JobRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
