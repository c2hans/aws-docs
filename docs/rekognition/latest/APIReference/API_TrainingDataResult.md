---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_TrainingDataResult.html
---

# TrainingDataResult
<a name="API_TrainingDataResult"></a>

The data validation manifest created for the training dataset during model training.

## Contents
<a name="API_TrainingDataResult_Contents"></a>

 ** Input **   <a name="rekognition-Type-TrainingDataResult-Input"></a>
The training data that you supplied.
Type: [TrainingData](API_TrainingData.md) object
Required: No

 ** Output **   <a name="rekognition-Type-TrainingDataResult-Output"></a>
Reference to images (assets) that were actually used during training with trained model predictions.
Type: [TrainingData](API_TrainingData.md) object
Required: No

 ** Validation **   <a name="rekognition-Type-TrainingDataResult-Validation"></a>
A manifest that you supplied for training, with validation results for each line.
Type: [ValidationData](API_ValidationData.md) object
Required: No

## See Also
<a name="API_TrainingDataResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/TrainingDataResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/TrainingDataResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/TrainingDataResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
