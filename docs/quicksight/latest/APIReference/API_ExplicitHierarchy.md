---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ExplicitHierarchy.html
---

# ExplicitHierarchy
<a name="API_ExplicitHierarchy"></a>

The option that determines the hierarchy of the fields that are built within a visual's field wells. These fields can't be duplicated to other visuals.

## Contents
<a name="API_ExplicitHierarchy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Columns **   <a name="QS-Type-ExplicitHierarchy-Columns"></a>
The list of columns that define the explicit hierarchy.
Type: Array of [ColumnIdentifier](API_ColumnIdentifier.md) objects
Array Members: Minimum number of 2 items. Maximum number of 10 items.
Required: Yes

 ** HierarchyId **   <a name="QS-Type-ExplicitHierarchy-HierarchyId"></a>
The hierarchy ID of the explicit hierarchy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** DrillDownFilters **   <a name="QS-Type-ExplicitHierarchy-DrillDownFilters"></a>
The option that determines the drill down filters for the explicit hierarchy.
Type: Array of [DrillDownFilter](API_DrillDownFilter.md) objects
Array Members: Maximum number of 10 items.
Required: No

## See Also
<a name="API_ExplicitHierarchy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ExplicitHierarchy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ExplicitHierarchy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ExplicitHierarchy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
