---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ActivateReadSetJobItem.html
---

# ActivateReadSetJobItem
<a name="API_ActivateReadSetJobItem"></a>

A read set activation job.

## Contents
<a name="API_ActivateReadSetJobItem_Contents"></a>

 ** creationTime **   <a name="omics-Type-ActivateReadSetJobItem-creationTime"></a>
When the job was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="omics-Type-ActivateReadSetJobItem-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** sequenceStoreId **   <a name="omics-Type-ActivateReadSetJobItem-sequenceStoreId"></a>
The job's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** status **   <a name="omics-Type-ActivateReadSetJobItem-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`
Required: Yes

 ** completionTime **   <a name="omics-Type-ActivateReadSetJobItem-completionTime"></a>
When the job completed.
Type: Timestamp
Required: No

## See Also
<a name="API_ActivateReadSetJobItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ActivateReadSetJobItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ActivateReadSetJobItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ActivateReadSetJobItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
