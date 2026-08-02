---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_JobRun.html
---

# JobRun
<a name="API_JobRun"></a>

This entity describes a job run. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.

## Contents
<a name="API_JobRun_Contents"></a>

 ** arn **   <a name="emroneks-Type-JobRun-arn"></a>
The ARN of job run.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/virtualclusters\/[0-9a-zA-Z]+\/jobruns\/[0-9a-zA-Z]+$`
Required: No

 ** clientToken **   <a name="emroneks-Type-JobRun-clientToken"></a>
The client token used to start a job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

 ** configurationOverrides **   <a name="emroneks-Type-JobRun-configurationOverrides"></a>
The configuration settings that are used to override default configuration.
Type: [ConfigurationOverrides](API_ConfigurationOverrides.md) object
Required: No

 ** createdAt **   <a name="emroneks-Type-JobRun-createdAt"></a>
The date and time when the job run was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="emroneks-Type-JobRun-createdBy"></a>
The user who created the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+$`
Required: No

 ** executionRoleArn **   <a name="emroneks-Type-JobRun-executionRoleArn"></a>
The execution role ARN of the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
Required: No

 ** failureReason **   <a name="emroneks-Type-JobRun-failureReason"></a>
The reasons why the job run has failed.
Type: String
Valid Values: `INTERNAL_ERROR | USER_ERROR | VALIDATION_ERROR | CLUSTER_UNAVAILABLE`
Required: No

 ** finishedAt **   <a name="emroneks-Type-JobRun-finishedAt"></a>
The date and time when the job run has finished.
Type: Timestamp
Required: No

 ** id **   <a name="emroneks-Type-JobRun-id"></a>
The ID of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: No

 ** jobDriver **   <a name="emroneks-Type-JobRun-jobDriver"></a>
Parameters of job driver for the job run.
Type: [JobDriver](API_JobDriver.md) object
Required: No

 ** name **   <a name="emroneks-Type-JobRun-name"></a>
The name of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** releaseLabel **   <a name="emroneks-Type-JobRun-releaseLabel"></a>
The release version of Amazon EMR.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/A-Za-z0-9]+`
Required: No

 ** retryPolicyConfiguration **   <a name="emroneks-Type-JobRun-retryPolicyConfiguration"></a>
The configuration of the retry policy that the job runs on.
Type: [RetryPolicyConfiguration](API_RetryPolicyConfiguration.md) object
Required: No

 ** retryPolicyExecution **   <a name="emroneks-Type-JobRun-retryPolicyExecution"></a>
The current status of the retry policy executed on the job.
Type: [RetryPolicyExecution](API_RetryPolicyExecution.md) object
Required: No

 ** state **   <a name="emroneks-Type-JobRun-state"></a>
The state of the job run.
Type: String
Valid Values: `PENDING | SUBMITTED | RUNNING | FAILED | CANCELLED | CANCEL_PENDING | COMPLETED`
Required: No

 ** stateDetails **   <a name="emroneks-Type-JobRun-stateDetails"></a>
Additional details of the job run state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** tags **   <a name="emroneks-Type-JobRun-tags"></a>
The assigned tags of the job run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

 ** virtualClusterId **   <a name="emroneks-Type-JobRun-virtualClusterId"></a>
The ID of the job run's virtual cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: No

## See Also
<a name="API_JobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/JobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/JobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/JobRun)
