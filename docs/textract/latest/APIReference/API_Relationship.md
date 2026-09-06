---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_Relationship.html
---

# Relationship
<a name="API_Relationship"></a>

Information about how blocks are related to each other. A `Block` object contains 0 or more `Relation` objects in a list, `Relationships`. For more information, see [Block](API_Block.md).

The `Type` element provides the type of the relationship for all blocks in the `IDs` array.

## Contents
<a name="API_Relationship_Contents"></a>

 ** Ids **   <a name="Textract-Type-Relationship-Ids"></a>
An array of IDs for related blocks. You can get the type of the relationship from the `Type` element.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="Textract-Type-Relationship-Type"></a>
The type of relationship between the blocks in the IDs array and the current block. The following list describes the relationship types that can be returned.
+  *VALUE* - A list that contains the ID of the VALUE block that's associated with the KEY of a key-value pair.
+  *CHILD* - A list of IDs that identify blocks found within the current block object. For example, WORD blocks have a CHILD relationship to the LINE block type.
+  *MERGED\_CELL* - A list of IDs that identify each of the MERGED\_CELL block types in a table.
+  *ANSWER* - A list that contains the ID of the QUERY\_RESULT block that’s associated with the corresponding QUERY block.
+  *TABLE* - A list of IDs that identify associated TABLE block types.
+  *TABLE\_TITLE* - A list that contains the ID for the TABLE\_TITLE block type in a table.
+  *TABLE\_FOOTER* - A list of IDs that identify the TABLE\_FOOTER block types in a table.
Type: String
Valid Values: `VALUE | CHILD | COMPLEX_FEATURES | MERGED_CELL | TITLE | ANSWER | TABLE | TABLE_TITLE | TABLE_FOOTER`
Required: No

## See Also
<a name="API_Relationship_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/Relationship)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/Relationship)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/Relationship)
