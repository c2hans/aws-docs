---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Prediction.html
---

# Prediction
<a name="API_Prediction"></a>

The output from a `Predict` operation:
+  `Details` - Contains the following attributes: `DetailsAttributes.PREDICTIVE_MODEL_TYPE - REGRESSION | BINARY | MULTICLASS` `DetailsAttributes.ALGORITHM - SGD`
+  `PredictedLabel` - Present for either a `BINARY` or `MULTICLASS` `MLModel` request.
+  `PredictedScores` - Contains the raw classification score corresponding to each label.
+  `PredictedValue` - Present for a `REGRESSION` `MLModel` request.

## Contents
<a name="API_Prediction_Contents"></a>

 ** details **   <a name="amazonml-Type-Prediction-details"></a>
Provides any additional details regarding the prediction.
Type: String to string map
Valid Keys: `PredictiveModelType | Algorithm`
Value Length Constraints: Minimum length of 1.
Required: No

 ** predictedLabel **   <a name="amazonml-Type-Prediction-predictedLabel"></a>
The prediction label for either a `BINARY` or `MULTICLASS` `MLModel`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** predictedScores **   <a name="amazonml-Type-Prediction-predictedScores"></a>
Provides the raw classification score corresponding to each label.
Type: String to float map
Key Length Constraints: Minimum length of 1.
Required: No

 ** predictedValue **   <a name="amazonml-Type-Prediction-predictedValue"></a>
The prediction value for `REGRESSION` `MLModel`.
Type: Float
Required: No

## See Also
<a name="API_Prediction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/Prediction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/Prediction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/Prediction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
