---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LookbackWindow.html
---

# LookbackWindow
<a name="API_LookbackWindow"></a>

The lookback window setup of an incremental refresh configuration.

## Contents
<a name="API_LookbackWindow_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-LookbackWindow-ColumnName"></a>
The name of the lookback window column.
Type: String
Required: Yes

 ** Size **   <a name="QS-Type-LookbackWindow-Size"></a>
The lookback window column size.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** SizeUnit **   <a name="QS-Type-LookbackWindow-SizeUnit"></a>
The size unit that is used for the lookback window column. Valid values for this structure are `HOUR`, `DAY`, and `WEEK`.
Type: String
Valid Values: `HOUR | DAY | WEEK`
Required: Yes

## See Also
<a name="API_LookbackWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LookbackWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LookbackWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LookbackWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
