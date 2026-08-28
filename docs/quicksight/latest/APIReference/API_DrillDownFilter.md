---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DrillDownFilter.html
---

# DrillDownFilter
<a name="API_DrillDownFilter"></a>

The drill down filter for the column hierarchies.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_DrillDownFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryFilter **   <a name="QS-Type-DrillDownFilter-CategoryFilter"></a>
The category type drill down filter. This filter is used for string type columns.
Type: [CategoryDrillDownFilter](API_CategoryDrillDownFilter.md) object
Required: No

 ** NumericEqualityFilter **   <a name="QS-Type-DrillDownFilter-NumericEqualityFilter"></a>
The numeric equality type drill down filter. This filter is used for number type columns.
Type: [NumericEqualityDrillDownFilter](API_NumericEqualityDrillDownFilter.md) object
Required: No

 ** TimeRangeFilter **   <a name="QS-Type-DrillDownFilter-TimeRangeFilter"></a>
The time range drill down filter. This filter is used for date time columns.
Type: [TimeRangeDrillDownFilter](API_TimeRangeDrillDownFilter.md) object
Required: No

## See Also
<a name="API_DrillDownFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DrillDownFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DrillDownFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DrillDownFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
