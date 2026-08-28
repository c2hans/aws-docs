---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_BatchListItem.html
---

# BatchListItem
<a name="API_BatchListItem"></a>

A summary of a batch returned by `ListBatch`.

## Contents
<a name="API_BatchListItem_Contents"></a>

 ** createdAt **   <a name="omics-Type-BatchListItem-createdAt"></a>
The timestamp when the batch was created.
Type: Timestamp
Required: No

 ** id **   <a name="omics-Type-BatchListItem-id"></a>
The batch identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** name **   <a name="omics-Type-BatchListItem-name"></a>
The batch name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** status **   <a name="omics-Type-BatchListItem-status"></a>
The current batch status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | PENDING | SUBMITTING | INPROGRESS | STOPPING | CANCELLED | FAILED | PROCESSED | RUNS_DELETING | RUNS_DELETE_FAILED | RUNS_DELETED`
Required: No

 ** totalRuns **   <a name="omics-Type-BatchListItem-totalRuns"></a>
The total number of runs in the batch.
Type: Integer
Required: No

 ** workflowId **   <a name="omics-Type-BatchListItem-workflowId"></a>
The identifier of the workflow used for the batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

## See Also
<a name="API_BatchListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/BatchListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/BatchListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/BatchListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
