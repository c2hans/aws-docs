---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PeriodToDateComputation.html
---

# PeriodToDateComputation
<a name="API_PeriodToDateComputation"></a>

The period to date computation configuration.

## Contents
<a name="API_PeriodToDateComputation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputationId **   <a name="QS-Type-PeriodToDateComputation-ComputationId"></a>
The ID for a computation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Name **   <a name="QS-Type-PeriodToDateComputation-Name"></a>
The name of a computation.
Type: String
Required: No

 ** PeriodTimeGranularity **   <a name="QS-Type-PeriodToDateComputation-PeriodTimeGranularity"></a>
The time granularity setup of period to date computation. Choose from the following options:
+ YEAR: Year to date.
+ MONTH: Month to date.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

 ** Time **   <a name="QS-Type-PeriodToDateComputation-Time"></a>
The time field that is used in a computation.
Type: [DimensionField](API_DimensionField.md) object
Required: No

 ** Value **   <a name="QS-Type-PeriodToDateComputation-Value"></a>
The value field that is used in a computation.
Type: [MeasureField](API_MeasureField.md) object
Required: No

## See Also
<a name="API_PeriodToDateComputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PeriodToDateComputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PeriodToDateComputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PeriodToDateComputation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
