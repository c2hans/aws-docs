---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkOperationsInfo.html
---

# ListSolNetworkOperationsInfo
<a name="API_ListSolNetworkOperationsInfo"></a>

Information parameters for a network operation.

## Contents
<a name="API_ListSolNetworkOperationsInfo_Contents"></a>

 ** arn **   <a name="TNB-Type-ListSolNetworkOperationsInfo-arn"></a>
Network operation ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-operation/no-[a-f0-9]{17})`
Required: Yes

 ** id **   <a name="TNB-Type-ListSolNetworkOperationsInfo-id"></a>
ID of this network operation.
Type: String
Pattern: `no-[a-f0-9]{17}`
Required: Yes

 ** lcmOperationType **   <a name="TNB-Type-ListSolNetworkOperationsInfo-lcmOperationType"></a>
Type of lifecycle management network operation.
Type: String
Valid Values: `INSTANTIATE | UPDATE | TERMINATE`
Required: Yes

 ** nsInstanceId **   <a name="TNB-Type-ListSolNetworkOperationsInfo-nsInstanceId"></a>
ID of the network instance related to this operation.
Type: String
Pattern: `ni-[a-f0-9]{17}`
Required: Yes

 ** operationState **   <a name="TNB-Type-ListSolNetworkOperationsInfo-operationState"></a>
The state of the network operation.
Type: String
Valid Values: `PROCESSING | COMPLETED | FAILED | CANCELLING | CANCELLED`
Required: Yes

 ** error **   <a name="TNB-Type-ListSolNetworkOperationsInfo-error"></a>
Error related to this specific network operation.
Type: [ProblemDetails](API_ProblemDetails.md) object
Required: No

 ** metadata **   <a name="TNB-Type-ListSolNetworkOperationsInfo-metadata"></a>
Metadata related to this network operation.
Type: [ListSolNetworkOperationsMetadata](API_ListSolNetworkOperationsMetadata.md) object
Required: No

 ** updateType **   <a name="TNB-Type-ListSolNetworkOperationsInfo-updateType"></a>
Type of the update. Only present if the network operation lcmOperationType is `UPDATE`.
Type: String
Valid Values: `MODIFY_VNF_INFORMATION | UPDATE_NS`
Required: No

## See Also
<a name="API_ListSolNetworkOperationsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolNetworkOperationsInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolNetworkOperationsInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolNetworkOperationsInfo)
