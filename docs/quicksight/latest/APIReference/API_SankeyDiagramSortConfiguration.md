---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SankeyDiagramSortConfiguration.html
---

# SankeyDiagramSortConfiguration
<a name="API_SankeyDiagramSortConfiguration"></a>

The sort configuration of a sankey diagram.

## Contents
<a name="API_SankeyDiagramSortConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DestinationItemsLimit **   <a name="QS-Type-SankeyDiagramSortConfiguration-DestinationItemsLimit"></a>
The limit on the number of destination nodes that are displayed in a sankey diagram.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** SourceItemsLimit **   <a name="QS-Type-SankeyDiagramSortConfiguration-SourceItemsLimit"></a>
The limit on the number of source nodes that are displayed in a sankey diagram.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** WeightSort **   <a name="QS-Type-SankeyDiagramSortConfiguration-WeightSort"></a>
The sort configuration of the weight fields.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_SankeyDiagramSortConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SankeyDiagramSortConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SankeyDiagramSortConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SankeyDiagramSortConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
