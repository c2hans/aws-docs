---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DryRunProgressStatus.html
---

# DryRunProgressStatus
<a name="API_DryRunProgressStatus"></a>

Information about the progress of a pre-upgrade dry run analysis.

## Contents
<a name="API_DryRunProgressStatus_Contents"></a>

 ** CreationDate **   <a name="opensearchservice-Type-DryRunProgressStatus-CreationDate"></a>
The timestamp when the dry run was initiated.
Type: String
Required: Yes

 ** DryRunId **   <a name="opensearchservice-Type-DryRunProgressStatus-DryRunId"></a>
The unique identifier of the dry run.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
Required: Yes

 ** DryRunStatus **   <a name="opensearchservice-Type-DryRunProgressStatus-DryRunStatus"></a>
The current status of the dry run.
Type: String
Required: Yes

 ** UpdateDate **   <a name="opensearchservice-Type-DryRunProgressStatus-UpdateDate"></a>
The timestamp when the dry run was last updated.
Type: String
Required: Yes

 ** ValidationFailures **   <a name="opensearchservice-Type-DryRunProgressStatus-ValidationFailures"></a>
Any validation failures that occurred as a result of the dry run.
Type: Array of [ValidationFailure](API_ValidationFailure.md) objects
Required: No

## See Also
<a name="API_DryRunProgressStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DryRunProgressStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DryRunProgressStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DryRunProgressStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
