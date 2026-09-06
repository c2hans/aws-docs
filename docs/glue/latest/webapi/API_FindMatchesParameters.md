---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FindMatchesParameters.html
---

# FindMatchesParameters
<a name="API_FindMatchesParameters"></a>

The parameters to configure the find matches transform.

## Contents
<a name="API_FindMatchesParameters_Contents"></a>

 ** AccuracyCostTradeoff **   <a name="Glue-Type-FindMatchesParameters-AccuracyCostTradeoff"></a>
The value that is selected when tuning your transform for a balance between accuracy and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate `FindMatches` transform, sometimes with unacceptable accuracy.
Accuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall.
Cost measures how many compute resources, and thus money, are consumed to run the transform.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** EnforceProvidedLabels **   <a name="Glue-Type-FindMatchesParameters-EnforceProvidedLabels"></a>
The value to switch on or off to force the output to match the provided labels from users. If the value is `True`, the `find matches` transform forces the output to match the provided labels. The results override the normal conflation results. If the value is `False`, the `find matches` transform does not ensure all the labels provided are respected, and the results rely on the trained model.
Note that setting this value to true may increase the conflation execution time.
Type: Boolean
Required: No

 ** PrecisionRecallTradeoff **   <a name="Glue-Type-FindMatchesParameters-PrecisionRecallTradeoff"></a>
The value selected when tuning your transform for a balance between precision and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision.
The precision metric indicates how often your model is correct when it predicts a match.
The recall metric indicates that for an actual match, how often your model predicts the match.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** PrimaryKeyColumnName **   <a name="Glue-Type-FindMatchesParameters-PrimaryKeyColumnName"></a>
The name of a column that uniquely identifies rows in the source table. Used to help identify matching records.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_FindMatchesParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FindMatchesParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FindMatchesParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FindMatchesParameters)
