---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_LineageNodeTypeItem.html
---

# LineageNodeTypeItem
<a name="API_LineageNodeTypeItem"></a>

The details of a data lineage node type.

## Contents
<a name="API_LineageNodeTypeItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-LineageNodeTypeItem-domainId"></a>
The ID of the domain where the data lineage node type lives.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** formsOutput **   <a name="datazone-Type-LineageNodeTypeItem-formsOutput"></a>
The forms output of the data lineage node type.
Type: String to [FormEntryOutput](API_FormEntryOutput.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** revision **   <a name="datazone-Type-LineageNodeTypeItem-revision"></a>
The revision of the data lineage node type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** createdAt **   <a name="datazone-Type-LineageNodeTypeItem-createdAt"></a>
The timestamp at which the data lineage node type was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-LineageNodeTypeItem-createdBy"></a>
The user who created the data lineage node type.
Type: String
Required: No

 ** description **   <a name="datazone-Type-LineageNodeTypeItem-description"></a>
The description of the data lineage node type.
Type: String
Required: No

 ** name **   <a name="datazone-Type-LineageNodeTypeItem-name"></a>
The name of the data lineage node type.
Type: String
Required: No

 ** updatedAt **   <a name="datazone-Type-LineageNodeTypeItem-updatedAt"></a>
The timestamp at which the data lineage node type was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-LineageNodeTypeItem-updatedBy"></a>
The user who updated the data lineage node type.
Type: String
Required: No

## See Also
<a name="API_LineageNodeTypeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/LineageNodeTypeItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/LineageNodeTypeItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/LineageNodeTypeItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
