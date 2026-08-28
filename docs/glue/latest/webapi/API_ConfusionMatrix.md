---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConfusionMatrix.html
---

# ConfusionMatrix
<a name="API_ConfusionMatrix"></a>

The confusion matrix shows you what your transform is predicting accurately and what types of errors it is making.

For more information, see [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) in Wikipedia.

## Contents
<a name="API_ConfusionMatrix_Contents"></a>

 ** NumFalseNegatives **   <a name="Glue-Type-ConfusionMatrix-NumFalseNegatives"></a>
The number of matches in the data that the transform didn't find, in the confusion matrix for your transform.
Type: Long
Required: No

 ** NumFalsePositives **   <a name="Glue-Type-ConfusionMatrix-NumFalsePositives"></a>
The number of nonmatches in the data that the transform incorrectly classified as a match, in the confusion matrix for your transform.
Type: Long
Required: No

 ** NumTrueNegatives **   <a name="Glue-Type-ConfusionMatrix-NumTrueNegatives"></a>
The number of nonmatches in the data that the transform correctly rejected, in the confusion matrix for your transform.
Type: Long
Required: No

 ** NumTruePositives **   <a name="Glue-Type-ConfusionMatrix-NumTruePositives"></a>
The number of matches in the data that the transform correctly found, in the confusion matrix for your transform.
Type: Long
Required: No

## See Also
<a name="API_ConfusionMatrix_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConfusionMatrix)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConfusionMatrix)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConfusionMatrix)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
