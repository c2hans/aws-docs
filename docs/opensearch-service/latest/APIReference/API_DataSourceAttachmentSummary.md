---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DataSourceAttachmentSummary.html
---

# DataSourceAttachmentSummary
<a name="API_DataSourceAttachmentSummary"></a>

Summary information about a data source attachment, including its identifier, data source ARN, and current status.

## Contents
<a name="API_DataSourceAttachmentSummary_Contents"></a>

 ** attachmentId **   <a name="opensearchservice-Type-DataSourceAttachmentSummary-attachmentId"></a>
The unique identifier assigned to the data source attachment.
Type: String
Required: No

 ** dataSourceArn **   <a name="opensearchservice-Type-DataSourceAttachmentSummary-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** status **   <a name="opensearchservice-Type-DataSourceAttachmentSummary-status"></a>
The current status of the data source attachment. Valid values are `PENDING`, `ATTACHED`, and `FAILED`.
Type: String
Valid Values: `PENDING | ATTACHED | FAILED`
Required: No

## See Also
<a name="API_DataSourceAttachmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DataSourceAttachmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DataSourceAttachmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DataSourceAttachmentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
