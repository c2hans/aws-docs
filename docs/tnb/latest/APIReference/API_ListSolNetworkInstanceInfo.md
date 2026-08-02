---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkInstanceInfo.html
---

# ListSolNetworkInstanceInfo
<a name="API_ListSolNetworkInstanceInfo"></a>

Info about the specific network instance.

A network instance is a single network created in AWS TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.

## Contents
<a name="API_ListSolNetworkInstanceInfo_Contents"></a>

 ** arn **   <a name="TNB-Type-ListSolNetworkInstanceInfo-arn"></a>
Network instance ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-instance/ni-[a-f0-9]{17})`
Required: Yes

 ** id **   <a name="TNB-Type-ListSolNetworkInstanceInfo-id"></a>
ID of the network instance.
Type: String
Pattern: `ni-[a-f0-9]{17}`
Required: Yes

 ** metadata **   <a name="TNB-Type-ListSolNetworkInstanceInfo-metadata"></a>
The metadata of the network instance.
Type: [ListSolNetworkInstanceMetadata](API_ListSolNetworkInstanceMetadata.md) object
Required: Yes

 ** nsdId **   <a name="TNB-Type-ListSolNetworkInstanceInfo-nsdId"></a>
ID of the network service descriptor in the network package.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** nsdInfoId **   <a name="TNB-Type-ListSolNetworkInstanceInfo-nsdInfoId"></a>
ID of the network service descriptor in the network package.
Type: String
Pattern: `np-[a-f0-9]{17}`
Required: Yes

 ** nsInstanceDescription **   <a name="TNB-Type-ListSolNetworkInstanceInfo-nsInstanceDescription"></a>
Human-readable description of the network instance.
Type: String
Required: Yes

 ** nsInstanceName **   <a name="TNB-Type-ListSolNetworkInstanceInfo-nsInstanceName"></a>
Human-readable name of the network instance.
Type: String
Required: Yes

 ** nsState **   <a name="TNB-Type-ListSolNetworkInstanceInfo-nsState"></a>
The state of the network instance.
Type: String
Valid Values: `INSTANTIATED | NOT_INSTANTIATED | UPDATED | IMPAIRED | UPDATE_FAILED | STOPPED | DELETED | INSTANTIATE_IN_PROGRESS | INTENT_TO_UPDATE_IN_PROGRESS | UPDATE_IN_PROGRESS | TERMINATE_IN_PROGRESS`
Required: Yes

## See Also
<a name="API_ListSolNetworkInstanceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolNetworkInstanceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolNetworkInstanceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolNetworkInstanceInfo)
