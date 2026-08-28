---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_PropertygraphData.html
---

# PropertygraphData
<a name="API_PropertygraphData"></a>

A Gremlin or openCypher change record.

## Contents
<a name="API_PropertygraphData_Contents"></a>

 ** id **   <a name="neptunedata-Type-PropertygraphData-id"></a>
The ID of the Gremlin or openCypher element.
Type: String
Required: Yes

 ** key **   <a name="neptunedata-Type-PropertygraphData-key"></a>
The property name. For element labels, this is `label`.
Type: String
Required: Yes

 ** type **   <a name="neptunedata-Type-PropertygraphData-type"></a>
The type of this Gremlin or openCypher element. Must be one of:
+  ** `v1` **   -   Vertex label for Gremlin, or node label for openCypher.
+  ** `vp` **   -   Vertex properties for Gremlin, or node properties for openCypher.
+  ** `e` **   -   Edge and edge label for Gremlin, or relationship and relationship type for openCypher.
+  ** `ep` **   -   Edge properties for Gremlin, or relationship properties for openCypher.
Type: String
Required: Yes

 ** value **   <a name="neptunedata-Type-PropertygraphData-value"></a>
This is a JSON object that contains a value field for the value itself, and a datatype field for the JSON data type of that value:
Type: JSON value
Required: Yes

 ** from **   <a name="neptunedata-Type-PropertygraphData-from"></a>
If this is an edge (type = `e`), the ID of the corresponding `from` vertex or source node.
Type: String
Required: No

 ** to **   <a name="neptunedata-Type-PropertygraphData-to"></a>
If this is an edge (type = `e`), the ID of the corresponding `to` vertex or target node.
Type: String
Required: No

## See Also
<a name="API_PropertygraphData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/PropertygraphData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/PropertygraphData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/PropertygraphData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
