---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_DefaultRunSetting.html
---

# DefaultRunSetting
<a name="API_DefaultRunSetting"></a>

Shared configuration applied to all runs in a batch. Fields specified in a per-run `InlineSetting` entry override the corresponding fields in this object for that run. The `parameters` and `runTags` fields are merged rather than replaced — run-specific values take precedence when keys overlap.

## Contents
<a name="API_DefaultRunSetting_Contents"></a>

 ** roleArn **   <a name="omics-Type-DefaultRunSetting-roleArn"></a>
The IAM role ARN that grants HealthOmics permissions to access required AWS resources such as Amazon S3 and CloudWatch. The role must have the same permissions required for individual `StartRun` calls.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`
Required: Yes

 ** workflowId **   <a name="omics-Type-DefaultRunSetting-workflowId"></a>
The identifier of the workflow to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

 ** cacheBehavior **   <a name="omics-Type-DefaultRunSetting-cacheBehavior"></a>
The cache behavior for the runs. Requires `cacheId` to be set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CACHE_ON_FAILURE | CACHE_ALWAYS`
Required: No

 ** cacheId **   <a name="omics-Type-DefaultRunSetting-cacheId"></a>
The identifier of the run cache to associate with the runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** configurationName **   <a name="omics-Type-DefaultRunSetting-configurationName"></a>
Optional configuration name to use for the workflow run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: No

 ** engineSettings **   <a name="omics-Type-DefaultRunSetting-engineSettings"></a>
Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).
Type: JSON value
Required: No

 ** logLevel **   <a name="omics-Type-DefaultRunSetting-logLevel"></a>
The verbosity level for CloudWatch Logs emitted during each run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `OFF | FATAL | ERROR | ALL`
Required: No

 ** name **   <a name="omics-Type-DefaultRunSetting-name"></a>
An optional user-friendly name applied to each workflow run. Can be overridden per run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** networkingMode **   <a name="omics-Type-DefaultRunSetting-networkingMode"></a>
Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.
Type: String
Valid Values: `RESTRICTED | VPC`
Required: No

 ** outputBucketOwnerId **   <a name="omics-Type-DefaultRunSetting-outputBucketOwnerId"></a>
The expected AWS account ID of the owner of the output S3 bucket. Can be overridden per run.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** outputUri **   <a name="omics-Type-DefaultRunSetting-outputUri"></a>
The destination S3 URI for workflow outputs. Must begin with `s3://`. The `roleArn` must grant write permissions to this bucket. Can be overridden per run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** parameters **   <a name="omics-Type-DefaultRunSetting-parameters"></a>
Workflow parameter names and values shared across all runs. Merged with per-run parameters; run-specific values take precedence when keys overlap. Can be overridden per run.
Type: JSON value
Required: No

 ** priority **   <a name="omics-Type-DefaultRunSetting-priority"></a>
An integer priority for the workflow runs. Higher values correspond to higher priority. A value of 0 corresponds to the lowest priority. Can be overridden per run.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** retentionMode **   <a name="omics-Type-DefaultRunSetting-retentionMode"></a>
The retention behavior for runs after completion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `RETAIN | REMOVE`
Required: No

 ** runGroupId **   <a name="omics-Type-DefaultRunSetting-runGroupId"></a>
The ID of the run group to contain all workflow runs in the batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** runTags **   <a name="omics-Type-DefaultRunSetting-runTags"></a>
AWS tags to associate with each workflow run. Merged with per-run `runTags`; run-specific values take precedence when keys overlap.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** scratchStorageMode **   <a name="omics-Type-DefaultRunSetting-scratchStorageMode"></a>
Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If not specified, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `LOCAL | SHARED`
Required: No

 ** storageCapacity **   <a name="omics-Type-DefaultRunSetting-storageCapacity"></a>
The filesystem size in gibibytes (GiB) provisioned for each workflow run and shared by all tasks in that run. Defaults to 1200 GiB if not specified.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** storageType **   <a name="omics-Type-DefaultRunSetting-storageType"></a>
The storage type for the workflow runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** workflowOwnerId **   <a name="omics-Type-DefaultRunSetting-workflowOwnerId"></a>
The AWS account ID of the workflow owner, used for cross-account workflow sharing.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** workflowType **   <a name="omics-Type-DefaultRunSetting-workflowType"></a>
The type of the originating workflow. Batch runs are not supported with `READY2RUN` workflows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`
Required: No

 ** workflowVersionName **   <a name="omics-Type-DefaultRunSetting-workflowVersionName"></a>
The version name of the specified workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: No

## See Also
<a name="API_DefaultRunSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/DefaultRunSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/DefaultRunSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/DefaultRunSetting)
