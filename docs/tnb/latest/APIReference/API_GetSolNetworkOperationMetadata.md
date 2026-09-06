---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkOperationMetadata.html
---

# GetSolNetworkOperationMetadata
<a name="API_GetSolNetworkOperationMetadata"></a>

Metadata related to a network operation occurrence.

A network operation is any operation that is done to your network, such as network instance instantiation or termination.

## Contents
<a name="API_GetSolNetworkOperationMetadata_Contents"></a>

 ** createdAt **   <a name="TNB-Type-GetSolNetworkOperationMetadata-createdAt"></a>
The date that the resource was created.
Type: Timestamp
Required: Yes

 ** lastModified **   <a name="TNB-Type-GetSolNetworkOperationMetadata-lastModified"></a>
The date that the resource was last modified.
Type: Timestamp
Required: Yes

 ** instantiateMetadata **   <a name="TNB-Type-GetSolNetworkOperationMetadata-instantiateMetadata"></a>
Metadata related to the network operation occurrence for network instantiation. This is populated only if the lcmOperationType is `INSTANTIATE`.
Type: [InstantiateMetadata](API_InstantiateMetadata.md) object
Required: No

 ** modifyVnfInfoMetadata **   <a name="TNB-Type-GetSolNetworkOperationMetadata-modifyVnfInfoMetadata"></a>
Metadata related to the network operation occurrence for network function updates in a network instance. This is populated only if the lcmOperationType is `UPDATE` and the updateType is `MODIFY_VNF_INFORMATION`.
Type: [ModifyVnfInfoMetadata](API_ModifyVnfInfoMetadata.md) object
Required: No

 ** updateNsMetadata **   <a name="TNB-Type-GetSolNetworkOperationMetadata-updateNsMetadata"></a>
Metadata related to the network operation occurrence for network instance updates. This is populated only if the lcmOperationType is `UPDATE` and the updateType is `UPDATE_NS`.
Type: [UpdateNsMetadata](API_UpdateNsMetadata.md) object
Required: No

## See Also
<a name="API_GetSolNetworkOperationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolNetworkOperationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolNetworkOperationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolNetworkOperationMetadata)
