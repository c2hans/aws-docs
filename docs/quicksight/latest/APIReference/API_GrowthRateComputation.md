---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GrowthRateComputation.html
---

# GrowthRateComputation
<a name="API_GrowthRateComputation"></a>

The growth rate computation configuration.

## Contents
<a name="API_GrowthRateComputation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputationId **   <a name="QS-Type-GrowthRateComputation-ComputationId"></a>
The ID for a computation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Name **   <a name="QS-Type-GrowthRateComputation-Name"></a>
The name of a computation.
Type: String
Required: No

 ** PeriodSize **   <a name="QS-Type-GrowthRateComputation-PeriodSize"></a>
The period size setup of a growth rate computation.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 52.
Required: No

 ** Time **   <a name="QS-Type-GrowthRateComputation-Time"></a>
The time field that is used in a computation.
Type: [DimensionField](API_DimensionField.md) object
Required: No

 ** Value **   <a name="QS-Type-GrowthRateComputation-Value"></a>
The value field that is used in a computation.
Type: [MeasureField](API_MeasureField.md) object
Required: No

## See Also
<a name="API_GrowthRateComputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GrowthRateComputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GrowthRateComputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GrowthRateComputation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
