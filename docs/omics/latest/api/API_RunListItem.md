---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_RunListItem.html
---

# RunListItem
<a name="API_RunListItem"></a>

A workflow run.

## Contents
<a name="API_RunListItem_Contents"></a>

 ** arn **   <a name="omics-Type-RunListItem-arn"></a>
The run's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`
Required: No

 ** batchId **   <a name="omics-Type-RunListItem-batchId"></a>
The run's batch ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** creationTime **   <a name="omics-Type-RunListItem-creationTime"></a>
When the run was created.
Type: Timestamp
Required: No

 ** id **   <a name="omics-Type-RunListItem-id"></a>
The run's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** name **   <a name="omics-Type-RunListItem-name"></a>
The run's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** priority **   <a name="omics-Type-RunListItem-priority"></a>
The run's priority.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** startTime **   <a name="omics-Type-RunListItem-startTime"></a>
When the run started.
Type: Timestamp
Required: No

 ** status **   <a name="omics-Type-RunListItem-status"></a>
The run's status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PENDING | STARTING | RUNNING | STOPPING | COMPLETED | DELETED | CANCELLED | FAILED`
Required: No

 ** stopTime **   <a name="omics-Type-RunListItem-stopTime"></a>
When the run stopped.
Type: Timestamp
Required: No

 ** storageCapacity **   <a name="omics-Type-RunListItem-storageCapacity"></a>
The run's storage capacity in gibibytes. For dynamic storage, after the run has completed, this value is the maximum amount of storage used during the run.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** storageType **   <a name="omics-Type-RunListItem-storageType"></a>
The run's storage type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** workflowId **   <a name="omics-Type-RunListItem-workflowId"></a>
The run's workflow ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** workflowName **   <a name="omics-Type-RunListItem-workflowName"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** workflowVersionName **   <a name="omics-Type-RunListItem-workflowVersionName"></a>
The name of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: No

## See Also
<a name="API_RunListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/RunListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/RunListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/RunListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
