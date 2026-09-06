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
