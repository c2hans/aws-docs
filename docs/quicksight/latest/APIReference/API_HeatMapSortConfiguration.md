---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_HeatMapSortConfiguration.html
---

# HeatMapSortConfiguration
<a name="API_HeatMapSortConfiguration"></a>

The sort configuration of a heat map.

## Contents
<a name="API_HeatMapSortConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** HeatMapColumnItemsLimitConfiguration **   <a name="QS-Type-HeatMapSortConfiguration-HeatMapColumnItemsLimitConfiguration"></a>
The limit on the number of columns that are displayed in a heat map.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** HeatMapColumnSort **   <a name="QS-Type-HeatMapSortConfiguration-HeatMapColumnSort"></a>
The column sort configuration for heat map for columns that aren't a part of a field well.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** HeatMapRowItemsLimitConfiguration **   <a name="QS-Type-HeatMapSortConfiguration-HeatMapRowItemsLimitConfiguration"></a>
The limit on the number of rows that are displayed in a heat map.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** HeatMapRowSort **   <a name="QS-Type-HeatMapSortConfiguration-HeatMapRowSort"></a>
The field sort configuration of the rows fields.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_HeatMapSortConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/HeatMapSortConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/HeatMapSortConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/HeatMapSortConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
