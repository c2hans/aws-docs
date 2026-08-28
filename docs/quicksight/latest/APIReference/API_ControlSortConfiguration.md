---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ControlSortConfiguration.html
---

# ControlSortConfiguration
<a name="API_ControlSortConfiguration"></a>

The sort configuration for control values. This is a tagged union type. Specify either `SelectableValuesSort` or `ControlColumnSort`, but not both.

## Contents
<a name="API_ControlSortConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ControlColumnSort **   <a name="QS-Type-ControlSortConfiguration-ControlColumnSort"></a>
The sort configuration for controls that are tied to a dataset column. Use this option to sort control values by an aggregate of a column.
Type: [AggregationSortConfiguration](API_AggregationSortConfiguration.md) object
Required: No

 ** SelectableValuesSort **   <a name="QS-Type-ControlSortConfiguration-SelectableValuesSort"></a>
The sort configuration for user-specified values in the control. Use this option to sort values that are manually entered by users in a dropdown or list control.
Type: [SelectableValuesSort](API_SelectableValuesSort.md) object
Required: No

## See Also
<a name="API_ControlSortConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ControlSortConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ControlSortConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ControlSortConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
