---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_LineageNodeSummary.html
---

# LineageNodeSummary
<a name="API_LineageNodeSummary"></a>

The summary of the data lineage node.

## Contents
<a name="API_LineageNodeSummary_Contents"></a>

 ** domainId **   <a name="datazone-Type-LineageNodeSummary-domainId"></a>
The ID of the domain of the data lineage node.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-LineageNodeSummary-id"></a>
The ID of the data lineage node.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** typeName **   <a name="datazone-Type-LineageNodeSummary-typeName"></a>
The name of the type of the data lineage node.
Type: String
Required: Yes

 ** createdAt **   <a name="datazone-Type-LineageNodeSummary-createdAt"></a>
The timestamp at which the data lineage node was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-LineageNodeSummary-createdBy"></a>
The user who created the data lineage node.
Type: String
Required: No

 ** description **   <a name="datazone-Type-LineageNodeSummary-description"></a>
The description of the data lineage node.
Type: String
Required: No

 ** eventTimestamp **   <a name="datazone-Type-LineageNodeSummary-eventTimestamp"></a>
The event timestamp of the data lineage node.
Type: Timestamp
Required: No

 ** name **   <a name="datazone-Type-LineageNodeSummary-name"></a>
The name of the data lineage node.
Type: String
Required: No

 ** sourceIdentifier **   <a name="datazone-Type-LineageNodeSummary-sourceIdentifier"></a>
The alternate ID of the data lineage node.
Type: String
Required: No

 ** typeRevision **   <a name="datazone-Type-LineageNodeSummary-typeRevision"></a>
The type of the revision of the data lineage node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** updatedAt **   <a name="datazone-Type-LineageNodeSummary-updatedAt"></a>
The timestamp at which the data lineage node was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-LineageNodeSummary-updatedBy"></a>
The user who updated the data lineage node.
Type: String
Required: No

## See Also
<a name="API_LineageNodeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/LineageNodeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/LineageNodeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/LineageNodeSummary)
