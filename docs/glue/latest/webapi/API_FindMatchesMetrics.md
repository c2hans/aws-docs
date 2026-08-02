---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FindMatchesMetrics.html
---

# FindMatchesMetrics
<a name="API_FindMatchesMetrics"></a>

The evaluation metrics for the find matches algorithm. The quality of your machine learning transform is measured by getting your transform to predict some matches and comparing the results to known matches from the same dataset. The quality metrics are based on a subset of your data, so they are not precise.

## Contents
<a name="API_FindMatchesMetrics_Contents"></a>

 ** AreaUnderPRCurve **   <a name="Glue-Type-FindMatchesMetrics-AreaUnderPRCurve"></a>
The area under the precision/recall curve (AUPRC) is a single number measuring the overall quality of the transform, that is independent of the choice made for precision vs. recall. Higher values indicate that you have a more attractive precision vs. recall tradeoff.
For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) in Wikipedia.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** ColumnImportances **   <a name="Glue-Type-FindMatchesMetrics-ColumnImportances"></a>
A list of `ColumnImportance` structures containing column importance metrics, sorted in order of descending importance.
Type: Array of [ColumnImportance](API_ColumnImportance.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** ConfusionMatrix **   <a name="Glue-Type-FindMatchesMetrics-ConfusionMatrix"></a>
The confusion matrix shows you what your transform is predicting accurately and what types of errors it is making.
For more information, see [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) in Wikipedia.
Type: [ConfusionMatrix](API_ConfusionMatrix.md) object
Required: No

 ** F1 **   <a name="Glue-Type-FindMatchesMetrics-F1"></a>
The maximum F1 metric indicates the transform's accuracy between 0 and 1, where 1 is the best accuracy.
For more information, see [F1 score](https://en.wikipedia.org/wiki/F1_score) in Wikipedia.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** Precision **   <a name="Glue-Type-FindMatchesMetrics-Precision"></a>
The precision metric indicates when often your transform is correct when it predicts a match. Specifically, it measures how well the transform finds true positives from the total true positives possible.
For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) in Wikipedia.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** Recall **   <a name="Glue-Type-FindMatchesMetrics-Recall"></a>
The recall metric indicates that for an actual match, how often your transform predicts the match. Specifically, it measures how well the transform finds true positives from the total records in the source data.
For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) in Wikipedia.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

## See Also
<a name="API_FindMatchesMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FindMatchesMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FindMatchesMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FindMatchesMetrics)
