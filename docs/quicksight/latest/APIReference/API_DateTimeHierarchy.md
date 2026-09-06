---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DateTimeHierarchy.html
---

# DateTimeHierarchy
<a name="API_DateTimeHierarchy"></a>

The option that determines the hierarchy of any `DateTime` fields.

## Contents
<a name="API_DateTimeHierarchy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** HierarchyId **   <a name="QS-Type-DateTimeHierarchy-HierarchyId"></a>
The hierarchy ID of the `DateTime` hierarchy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** DrillDownFilters **   <a name="QS-Type-DateTimeHierarchy-DrillDownFilters"></a>
The option that determines the drill down filters for the `DateTime` hierarchy.
Type: Array of [DrillDownFilter](API_DrillDownFilter.md) objects
Array Members: Maximum number of 10 items.
Required: No

## See Also
<a name="API_DateTimeHierarchy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DateTimeHierarchy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DateTimeHierarchy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DateTimeHierarchy)
