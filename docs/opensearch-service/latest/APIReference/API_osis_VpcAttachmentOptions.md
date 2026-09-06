---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_VpcAttachmentOptions.html
---

# VpcAttachmentOptions
<a name="API_osis_VpcAttachmentOptions"></a>

Options for attaching a VPC to pipeline.

## Contents
<a name="API_osis_VpcAttachmentOptions_Contents"></a>

 ** AttachToVpc **   <a name="opensearchservice-Type-osis_VpcAttachmentOptions-AttachToVpc"></a>
Whether a VPC is attached to the pipeline.
Type: Boolean
Required: Yes

 ** CidrBlock **   <a name="opensearchservice-Type-osis_VpcAttachmentOptions-CidrBlock"></a>
The CIDR block to be reserved for OpenSearch Ingestion to create elastic network interfaces (ENIs).
Type: String
Pattern: `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/24$`
Required: No

## See Also
<a name="API_osis_VpcAttachmentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/VpcAttachmentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/VpcAttachmentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/VpcAttachmentOptions)
