---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopBottomMoversComputation.html
---

# TopBottomMoversComputation
<a name="API_TopBottomMoversComputation"></a>

The top movers and bottom movers computation setup.

## Contents
<a name="API_TopBottomMoversComputation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputationId **   <a name="QS-Type-TopBottomMoversComputation-ComputationId"></a>
The ID for a computation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Type **   <a name="QS-Type-TopBottomMoversComputation-Type"></a>
The computation type. Choose from the following options:
+ TOP: Top movers computation.
+ BOTTOM: Bottom movers computation.
Type: String
Valid Values: `TOP | BOTTOM`
Required: Yes

 ** Category **   <a name="QS-Type-TopBottomMoversComputation-Category"></a>
The category field that is used in a computation.
Type: [DimensionField](API_DimensionField.md) object
Required: No

 ** MoverSize **   <a name="QS-Type-TopBottomMoversComputation-MoverSize"></a>
The mover size setup of the top and bottom movers computation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** Name **   <a name="QS-Type-TopBottomMoversComputation-Name"></a>
The name of a computation.
Type: String
Required: No

 ** SortOrder **   <a name="QS-Type-TopBottomMoversComputation-SortOrder"></a>
The sort order setup of the top and bottom movers computation.
Type: String
Valid Values: `PERCENT_DIFFERENCE | ABSOLUTE_DIFFERENCE`
Required: No

 ** Time **   <a name="QS-Type-TopBottomMoversComputation-Time"></a>
The time field that is used in a computation.
Type: [DimensionField](API_DimensionField.md) object
Required: No

 ** Value **   <a name="QS-Type-TopBottomMoversComputation-Value"></a>
The value field that is used in a computation.
Type: [MeasureField](API_MeasureField.md) object
Required: No

## See Also
<a name="API_TopBottomMoversComputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopBottomMoversComputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopBottomMoversComputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopBottomMoversComputation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
