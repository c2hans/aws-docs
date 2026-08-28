---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ThousandSeparatorOptions.html
---

# ThousandSeparatorOptions
<a name="API_ThousandSeparatorOptions"></a>

The options that determine the thousands separator configuration.

## Contents
<a name="API_ThousandSeparatorOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GroupingStyle **   <a name="QS-Type-ThousandSeparatorOptions-GroupingStyle"></a>
Determines the way numbers are styled to accommodate different readability standards. The `DEFAULT` value uses the standard international grouping system and groups numbers by the thousands. The `LAKHS` value uses the Indian numbering system and groups numbers by lakhs and crores.
Type: String
Valid Values: `DEFAULT | LAKHS`
Required: No

 ** Symbol **   <a name="QS-Type-ThousandSeparatorOptions-Symbol"></a>
Determines the thousands separator symbol.
Type: String
Valid Values: `COMMA | DOT | SPACE`
Required: No

 ** Visibility **   <a name="QS-Type-ThousandSeparatorOptions-Visibility"></a>
Determines the visibility of the thousands separator.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_ThousandSeparatorOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ThousandSeparatorOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ThousandSeparatorOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ThousandSeparatorOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
