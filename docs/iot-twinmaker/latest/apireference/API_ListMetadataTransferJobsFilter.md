---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListMetadataTransferJobsFilter.html
---

# ListMetadataTransferJobsFilter
<a name="API_ListMetadataTransferJobsFilter"></a>

The ListMetadataTransferJobs filter.

## Contents
<a name="API_ListMetadataTransferJobsFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** state **   <a name="tm-Type-ListMetadataTransferJobsFilter-state"></a>
The filter state.
Type: String
Valid Values: `VALIDATING | PENDING | RUNNING | CANCELLING | ERROR | COMPLETED | CANCELLED`
Required: No

 ** workspaceId **   <a name="tm-Type-ListMetadataTransferJobsFilter-workspaceId"></a>
The workspace Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_ListMetadataTransferJobsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListMetadataTransferJobsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListMetadataTransferJobsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListMetadataTransferJobsFilter)
