---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_LineageNodeItem.html
---

# LineageNodeItem
<a name="API_LineageNodeItem"></a>

The summary and output forms of a LineageNode

## Contents
<a name="API_LineageNodeItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-LineageNodeItem-domainId"></a>
The ID of the domain of the data lineage node.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-LineageNodeItem-id"></a>
The ID of the data lineage node.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** typeName **   <a name="datazone-Type-LineageNodeItem-typeName"></a>
The name of the type of the data lineage node.
Type: String
Required: Yes

 ** createdAt **   <a name="datazone-Type-LineageNodeItem-createdAt"></a>
The timestamp at which the data lineage node was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-LineageNodeItem-createdBy"></a>
The user who created the data lineage node.
Type: String
Required: No

 ** description **   <a name="datazone-Type-LineageNodeItem-description"></a>
The description of the data lineage node.
Type: String
Required: No

 ** downstreamLineageNodeIds **   <a name="datazone-Type-LineageNodeItem-downstreamLineageNodeIds"></a>
The IDs of the downstream data lineage nodes.
Type: Array of strings
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** eventTimestamp **   <a name="datazone-Type-LineageNodeItem-eventTimestamp"></a>
The event timestamp of the data lineage node.
Type: Timestamp
Required: No

 ** formsOutput **   <a name="datazone-Type-LineageNodeItem-formsOutput"></a>
The forms included in the additional attributes of a data lineage node.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** name **   <a name="datazone-Type-LineageNodeItem-name"></a>
The name of the data lineage node.
Type: String
Required: No

 ** sourceIdentifier **   <a name="datazone-Type-LineageNodeItem-sourceIdentifier"></a>
The alternate ID of the data lineage node.
Type: String
Required: No

 ** typeRevision **   <a name="datazone-Type-LineageNodeItem-typeRevision"></a>
The type of the revision of the data lineage node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** updatedAt **   <a name="datazone-Type-LineageNodeItem-updatedAt"></a>
The timestamp at which the data lineage node was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-LineageNodeItem-updatedBy"></a>
The user who updated the data lineage node.
Type: String
Required: No

 ** upstreamLineageNodeIds **   <a name="datazone-Type-LineageNodeItem-upstreamLineageNodeIds"></a>
The IDs of the upstream data lineage nodes.
Type: Array of strings
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_LineageNodeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/LineageNodeItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/LineageNodeItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/LineageNodeItem)
