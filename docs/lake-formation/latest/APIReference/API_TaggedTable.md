---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_TaggedTable.html
---

# TaggedTable
<a name="API_TaggedTable"></a>

A structure describing a table resource with LF-tags.

## Contents
<a name="API_TaggedTable_Contents"></a>

 ** LFTagOnDatabase **   <a name="lakeformation-Type-TaggedTable-LFTagOnDatabase"></a>
A list of LF-tags attached to the database where the table resides.
Type: Array of [LFTagPair](API_LFTagPair.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** LFTagsOnColumns **   <a name="lakeformation-Type-TaggedTable-LFTagsOnColumns"></a>
A list of LF-tags attached to columns in the table.
Type: Array of [ColumnLFTag](API_ColumnLFTag.md) objects
Required: No

 ** LFTagsOnTable **   <a name="lakeformation-Type-TaggedTable-LFTagsOnTable"></a>
A list of LF-tags attached to the table.
Type: Array of [LFTagPair](API_LFTagPair.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Table **   <a name="lakeformation-Type-TaggedTable-Table"></a>
A table that has LF-tags attached to it.
Type: [TableResource](API_TableResource.md) object
Required: No

## See Also
<a name="API_TaggedTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/TaggedTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/TaggedTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/TaggedTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
