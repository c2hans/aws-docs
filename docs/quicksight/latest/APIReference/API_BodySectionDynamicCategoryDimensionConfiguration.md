---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BodySectionDynamicCategoryDimensionConfiguration.html
---

# BodySectionDynamicCategoryDimensionConfiguration
<a name="API_BodySectionDynamicCategoryDimensionConfiguration"></a>

Describes the **Category** dataset column and constraints for the dynamic values used to repeat the contents of a section.

## Contents
<a name="API_BodySectionDynamicCategoryDimensionConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-BodySectionDynamicCategoryDimensionConfiguration-Column"></a>
A column of a data set.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** Limit **   <a name="QS-Type-BodySectionDynamicCategoryDimensionConfiguration-Limit"></a>
Number of values to use from the column for repetition.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** SortByMetrics **   <a name="QS-Type-BodySectionDynamicCategoryDimensionConfiguration-SortByMetrics"></a>
Sort criteria on the column values that you use for repetition.
Type: Array of [ColumnSort](API_ColumnSort.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_BodySectionDynamicCategoryDimensionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BodySectionDynamicCategoryDimensionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BodySectionDynamicCategoryDimensionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BodySectionDynamicCategoryDimensionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
