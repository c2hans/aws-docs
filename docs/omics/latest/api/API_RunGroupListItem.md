---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_RunGroupListItem.html
---

# RunGroupListItem
<a name="API_RunGroupListItem"></a>

A run group.

## Contents
<a name="API_RunGroupListItem_Contents"></a>

 ** arn **   <a name="omics-Type-RunGroupListItem-arn"></a>
The group's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`
Required: No

 ** creationTime **   <a name="omics-Type-RunGroupListItem-creationTime"></a>
When the group was created.
Type: Timestamp
Required: No

 ** id **   <a name="omics-Type-RunGroupListItem-id"></a>
The group's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** maxCpus **   <a name="omics-Type-RunGroupListItem-maxCpus"></a>
The group's maximum CPU count setting.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** maxDuration **   <a name="omics-Type-RunGroupListItem-maxDuration"></a>
The group's maximum duration setting in minutes.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** maxGpus **   <a name="omics-Type-RunGroupListItem-maxGpus"></a>
 The maximum GPUs that can be used by a run group.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** maxRuns **   <a name="omics-Type-RunGroupListItem-maxRuns"></a>
The group's maximum concurrent run setting.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** name **   <a name="omics-Type-RunGroupListItem-name"></a>
The group's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_RunGroupListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/RunGroupListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/RunGroupListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/RunGroupListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
