---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_RunBatchListItem.html
---

# RunBatchListItem
<a name="API_RunBatchListItem"></a>

A single run entry returned by `ListRunsInBatch`.

## Contents
<a name="API_RunBatchListItem_Contents"></a>

 ** runArn **   <a name="omics-Type-RunBatchListItem-runArn"></a>
The unique ARN of the workflow run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`
Required: No

 ** runId **   <a name="omics-Type-RunBatchListItem-runId"></a>
The HealthOmics-generated identifier for the workflow run. Empty if submission failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** runInternalUuid **   <a name="omics-Type-RunBatchListItem-runInternalUuid"></a>
The universally unique identifier (UUID) for the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** runSettingId **   <a name="omics-Type-RunBatchListItem-runSettingId"></a>
The customer-provided identifier for the run configuration. Use this to correlate results back to the input configuration provided in `inlineSettings` or `s3UriSettings`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** submissionFailureMessage **   <a name="omics-Type-RunBatchListItem-submissionFailureMessage"></a>
A detailed message describing the submission failure.
Type: String
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** submissionFailureReason **   <a name="omics-Type-RunBatchListItem-submissionFailureReason"></a>
The error category for a failed submission. See the run-level failure table in the HealthOmics User Guide for details on each value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** submissionStatus **   <a name="omics-Type-RunBatchListItem-submissionStatus"></a>
The submission outcome for this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `SUCCESS | FAILED | CANCEL_SUCCESS | CANCEL_FAILED | DELETE_SUCCESS | DELETE_FAILED`
Required: No

## See Also
<a name="API_RunBatchListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/RunBatchListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/RunBatchListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/RunBatchListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
