---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_S3AccessPointAttachmentsFilter.html
---

# S3AccessPointAttachmentsFilter
<a name="API_S3AccessPointAttachmentsFilter"></a>

A set of Name and Values pairs used to view a select set of S3 access point attachments.

## Contents
<a name="API_S3AccessPointAttachmentsFilter_Contents"></a>

 ** Name **   <a name="FSx-Type-S3AccessPointAttachmentsFilter-Name"></a>
The name of the filter.
Type: String
Valid Values: `file-system-id | volume-id | type`
Required: No

 ** Values **   <a name="FSx-Type-S3AccessPointAttachmentsFilter-Values"></a>
The values of the filter.
Type: Array of strings
Array Members: Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`
Required: No

## See Also
<a name="API_S3AccessPointAttachmentsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/S3AccessPointAttachmentsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/S3AccessPointAttachmentsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/S3AccessPointAttachmentsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
