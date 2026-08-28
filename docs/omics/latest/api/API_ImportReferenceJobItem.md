---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ImportReferenceJobItem.html
---

# ImportReferenceJobItem
<a name="API_ImportReferenceJobItem"></a>

An import reference job.

## Contents
<a name="API_ImportReferenceJobItem_Contents"></a>

 ** creationTime **   <a name="omics-Type-ImportReferenceJobItem-creationTime"></a>
When the job was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="omics-Type-ImportReferenceJobItem-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** referenceStoreId **   <a name="omics-Type-ImportReferenceJobItem-referenceStoreId"></a>
The job's reference store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** roleArn **   <a name="omics-Type-ImportReferenceJobItem-roleArn"></a>
The job's service role ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** status **   <a name="omics-Type-ImportReferenceJobItem-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`
Required: Yes

 ** completionTime **   <a name="omics-Type-ImportReferenceJobItem-completionTime"></a>
When the job completed.
Type: Timestamp
Required: No

## See Also
<a name="API_ImportReferenceJobItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ImportReferenceJobItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ImportReferenceJobItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ImportReferenceJobItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
