---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_InlineSetting.html
---

# InlineSetting
<a name="API_InlineSetting"></a>

A per-run configuration that overrides or merges with fields from `DefaultRunSetting` for a specific run.

## Contents
<a name="API_InlineSetting_Contents"></a>

 ** runSettingId **   <a name="omics-Type-InlineSetting-runSettingId"></a>
A customer-provided unique identifier for this run configuration within the batch. After submission, use `ListRunsInBatch` to map each `runSettingId` to the HealthOmics-generated `runId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** engineSettings **   <a name="omics-Type-InlineSetting-engineSettings"></a>
Per-run engine-specific settings. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles). Overrides `defaultRunSetting.engineSettings` for this run.
Type: JSON value
Required: No

 ** name **   <a name="omics-Type-InlineSetting-name"></a>
An optional user-friendly name for this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** outputBucketOwnerId **   <a name="omics-Type-InlineSetting-outputBucketOwnerId"></a>
The expected AWS account ID of the owner of the output S3 bucket for this run.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** outputUri **   <a name="omics-Type-InlineSetting-outputUri"></a>
Override the destination S3 URI for this run's outputs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** parameters **   <a name="omics-Type-InlineSetting-parameters"></a>
Per-run workflow parameters. Merged with `defaultRunSetting.parameters`; values in this object take precedence when keys overlap.
Type: JSON value
Required: No

 ** priority **   <a name="omics-Type-InlineSetting-priority"></a>
Override the priority for this run.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** runTags **   <a name="omics-Type-InlineSetting-runTags"></a>
Per-run AWS tags. Merged with `defaultRunSetting.runTags`; values in this object take precedence when keys overlap.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_InlineSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/InlineSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/InlineSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/InlineSetting)
