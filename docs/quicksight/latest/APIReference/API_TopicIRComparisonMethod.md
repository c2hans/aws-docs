---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicIRComparisonMethod.html
---

# TopicIRComparisonMethod
<a name="API_TopicIRComparisonMethod"></a>

The definition of a `TopicIRComparisonMethod`.

## Contents
<a name="API_TopicIRComparisonMethod_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Period **   <a name="QS-Type-TopicIRComparisonMethod-Period"></a>
The period for the `TopicIRComparisonMethod`.
Type: String
Valid Values: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
Required: No

 ** Type **   <a name="QS-Type-TopicIRComparisonMethod-Type"></a>
The type for the `TopicIRComparisonMethod`.
Type: String
Valid Values: `DIFF | PERC_DIFF | DIFF_AS_PERC | POP_CURRENT_DIFF_AS_PERC | POP_CURRENT_DIFF | POP_OVERTIME_DIFF_AS_PERC | POP_OVERTIME_DIFF | PERCENT_OF_TOTAL | RUNNING_SUM | MOVING_AVERAGE`
Required: No

 ** WindowSize **   <a name="QS-Type-TopicIRComparisonMethod-WindowSize"></a>
The window size for the `TopicIRComparisonMethod`.
Type: Integer
Required: No

## See Also
<a name="API_TopicIRComparisonMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicIRComparisonMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicIRComparisonMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicIRComparisonMethod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
