---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SearchTypesResultItem.html
---

# SearchTypesResultItem
<a name="API_SearchTypesResultItem"></a>

The details of the results of the `SearchTypes` action.

## Contents
<a name="API_SearchTypesResultItem_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** assetTypeItem **   <a name="datazone-Type-SearchTypesResultItem-assetTypeItem"></a>
The asset type included in the results of the `SearchTypes` action.
Type: [AssetTypeItem](API_AssetTypeItem.md) object
Required: No

 ** formTypeItem **   <a name="datazone-Type-SearchTypesResultItem-formTypeItem"></a>
The form type included in the results of the `SearchTypes` action.
Type: [FormTypeData](API_FormTypeData.md) object
Required: No

 ** lineageNodeTypeItem **   <a name="datazone-Type-SearchTypesResultItem-lineageNodeTypeItem"></a>
The details of a data lineage node type.
Type: [LineageNodeTypeItem](API_LineageNodeTypeItem.md) object
Required: No

## See Also
<a name="API_SearchTypesResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SearchTypesResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SearchTypesResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SearchTypesResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
