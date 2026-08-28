---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopBottomRankedComputation.html
---

# TopBottomRankedComputation
<a name="API_TopBottomRankedComputation"></a>

The top ranked and bottom ranked computation configuration.

## Contents
<a name="API_TopBottomRankedComputation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputationId **   <a name="QS-Type-TopBottomRankedComputation-ComputationId"></a>
The ID for a computation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Type **   <a name="QS-Type-TopBottomRankedComputation-Type"></a>
The computation type. Choose one of the following options:
+ TOP: A top ranked computation.
+ BOTTOM: A bottom ranked computation.
Type: String
Valid Values: `TOP | BOTTOM`
Required: Yes

 ** Category **   <a name="QS-Type-TopBottomRankedComputation-Category"></a>
The category field that is used in a computation.
Type: [DimensionField](API_DimensionField.md) object
Required: No

 ** Name **   <a name="QS-Type-TopBottomRankedComputation-Name"></a>
The name of a computation.
Type: String
Required: No

 ** ResultSize **   <a name="QS-Type-TopBottomRankedComputation-ResultSize"></a>
The result size of a top and bottom ranked computation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** Value **   <a name="QS-Type-TopBottomRankedComputation-Value"></a>
The value field that is used in a computation.
Type: [MeasureField](API_MeasureField.md) object
Required: No

## See Also
<a name="API_TopBottomRankedComputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopBottomRankedComputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopBottomRankedComputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopBottomRankedComputation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
