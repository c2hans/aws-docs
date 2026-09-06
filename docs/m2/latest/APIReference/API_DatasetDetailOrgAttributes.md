---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_DatasetDetailOrgAttributes.html
---

# DatasetDetailOrgAttributes
<a name="API_DatasetDetailOrgAttributes"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Additional details about the data set. Different attributes correspond to different data set organizations. The values are populated based on datasetOrg, storageType and backend (Blu Age or Micro Focus).

## Contents
<a name="API_DatasetDetailOrgAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** gdg **   <a name="m2-Type-DatasetDetailOrgAttributes-gdg"></a>
The generation data group of the data set.
Type: [GdgDetailAttributes](API_GdgDetailAttributes.md) object
Required: No

 ** po **   <a name="m2-Type-DatasetDetailOrgAttributes-po"></a>
The details of a PO type data set.
Type: [PoDetailAttributes](API_PoDetailAttributes.md) object
Required: No

 ** ps **   <a name="m2-Type-DatasetDetailOrgAttributes-ps"></a>
The details of a PS type data set.
Type: [PsDetailAttributes](API_PsDetailAttributes.md) object
Required: No

 ** vsam **   <a name="m2-Type-DatasetDetailOrgAttributes-vsam"></a>
The details of a VSAM data set.
Type: [VsamDetailAttributes](API_VsamDetailAttributes.md) object
Required: No

## See Also
<a name="API_DatasetDetailOrgAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/DatasetDetailOrgAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/DatasetDetailOrgAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/DatasetDetailOrgAttributes)
