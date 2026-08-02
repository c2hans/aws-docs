---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_WorkflowVersionListItem.html
---

# WorkflowVersionListItem
<a name="API_WorkflowVersionListItem"></a>

A list of workflow version items.

## Contents
<a name="API_WorkflowVersionListItem_Contents"></a>

 ** arn **   <a name="omics-Type-WorkflowVersionListItem-arn"></a>
ARN of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `arn:.+`
Required: No

 ** creationTime **   <a name="omics-Type-WorkflowVersionListItem-creationTime"></a>
The creation time of the workflow version.
Type: Timestamp
Required: No

 ** description **   <a name="omics-Type-WorkflowVersionListItem-description"></a>
The description of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** digest **   <a name="omics-Type-WorkflowVersionListItem-digest"></a>
The digist of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** metadata **   <a name="omics-Type-WorkflowVersionListItem-metadata"></a>
Metadata for the workflow version.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** status **   <a name="omics-Type-WorkflowVersionListItem-status"></a>
The status of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | ACTIVE | UPDATING | DELETED | FAILED | INACTIVE`
Required: No

 ** type **   <a name="omics-Type-WorkflowVersionListItem-type"></a>
The type of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`
Required: No

 ** versionName **   <a name="omics-Type-WorkflowVersionListItem-versionName"></a>
The name of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: No

 ** workflowId **   <a name="omics-Type-WorkflowVersionListItem-workflowId"></a>
The workflow's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

## See Also
<a name="API_WorkflowVersionListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/WorkflowVersionListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/WorkflowVersionListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/WorkflowVersionListItem)
