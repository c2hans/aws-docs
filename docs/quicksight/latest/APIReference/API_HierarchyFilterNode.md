---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_HierarchyFilterNode.html
---

# HierarchyFilterNode
<a name="API_HierarchyFilterNode"></a>

A node in the selection tree of a `HierarchyFilter`. Each node records the values that are selected at one level of the hierarchy. Nodes nest through `Children` to record selections at deeper levels.

The tree cannot be deeper than the number of levels declared in `HierarchyLevels`. A tree can be a maximum of 5 levels deep, and a node can have a maximum of 1,000 children.

## Contents
<a name="API_HierarchyFilterNode_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-HierarchyFilterNode-Column"></a>
The column that this node selects values from. This column must match the column of the corresponding level in `HierarchyFilter$HierarchyLevels`. The node at depth 1 must match the first level, the node at depth 2 must match the second level, and so on.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** Children **   <a name="QS-Type-HierarchyFilterNode-Children"></a>
The nodes that record the selections at the next level of the hierarchy. You can specify a maximum of 1,000 children per node.
Type: Array of [HierarchyFilterNode](#API_HierarchyFilterNode) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** HierarchyValues **   <a name="QS-Type-HierarchyFilterNode-HierarchyValues"></a>
The values that are selected at this level of the hierarchy. You can specify a maximum of 2,000 values per node.
Type: Array of strings
Array Members: Maximum number of 2000 items.
Length Constraints: Maximum length of 512.
Required: No

 ** ParentValue **   <a name="QS-Type-HierarchyFilterNode-ParentValue"></a>
The value in the parent node's `HierarchyValues` that this node belongs to. When a parent selects several values, each of its children repeats one of them here to identify which branch of the hierarchy that child describes.
Omit this attribute on the root node of `HierarchyTree`, which has no parent.
Type: String
Length Constraints: Maximum length of 512.
Required: No

## See Also
<a name="API_HierarchyFilterNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/HierarchyFilterNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/HierarchyFilterNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/HierarchyFilterNode)
