---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_QAResult.html
---

# QAResult
<a name="API_QAResult"></a>

The QA result that is made from the `DashboardVisual` or `GeneratedAnswer`.

## Contents
<a name="API_QAResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DashboardVisual **   <a name="QS-Type-QAResult-DashboardVisual"></a>
The representation of a dashboard visual result.
Type: [DashboardVisualResult](API_DashboardVisualResult.md) object
Required: No

 ** GeneratedAnswer **   <a name="QS-Type-QAResult-GeneratedAnswer"></a>
The representation of a generated answer result.
Type: [GeneratedAnswerResult](API_GeneratedAnswerResult.md) object
Required: No

 ** ResultType **   <a name="QS-Type-QAResult-ResultType"></a>
The type of QA result.
Type: String
Valid Values: `DASHBOARD_VISUAL | GENERATED_ANSWER | NO_ANSWER`
Required: No

## See Also
<a name="API_QAResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/QAResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/QAResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/QAResult)
