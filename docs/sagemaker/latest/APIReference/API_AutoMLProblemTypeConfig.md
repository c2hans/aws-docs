---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html
---

# AutoMLProblemTypeConfig
<a name="API_AutoMLProblemTypeConfig"></a>

A collection of settings specific to the problem type used to configure an AutoML job V2. There must be one and only one config of the following type.

## Contents
<a name="API_AutoMLProblemTypeConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ImageClassificationJobConfig **   <a name="sagemaker-Type-AutoMLProblemTypeConfig-ImageClassificationJobConfig"></a>
Settings used to configure an AutoML job V2 for the image classification problem type.
Type: [ImageClassificationJobConfig](API_ImageClassificationJobConfig.md) object
Required: No

 ** TabularJobConfig **   <a name="sagemaker-Type-AutoMLProblemTypeConfig-TabularJobConfig"></a>
Settings used to configure an AutoML job V2 for the tabular problem type (regression, classification).
Type: [TabularJobConfig](API_TabularJobConfig.md) object
Required: No

 ** TextClassificationJobConfig **   <a name="sagemaker-Type-AutoMLProblemTypeConfig-TextClassificationJobConfig"></a>
Settings used to configure an AutoML job V2 for the text classification problem type.
Type: [TextClassificationJobConfig](API_TextClassificationJobConfig.md) object
Required: No

 ** TextGenerationJobConfig **   <a name="sagemaker-Type-AutoMLProblemTypeConfig-TextGenerationJobConfig"></a>
Settings used to configure an AutoML job V2 for the text generation (LLMs fine-tuning) problem type.
The text generation models that support fine-tuning in Autopilot are currently accessible exclusively in regions supported by Canvas. Refer to the documentation of Canvas for the [full list of its supported Regions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html).
Type: [TextGenerationJobConfig](API_TextGenerationJobConfig.md) object
Required: No

 ** TimeSeriesForecastingJobConfig **   <a name="sagemaker-Type-AutoMLProblemTypeConfig-TimeSeriesForecastingJobConfig"></a>
Settings used to configure an AutoML job V2 for the time-series forecasting problem type.
Type: [TimeSeriesForecastingJobConfig](API_TimeSeriesForecastingJobConfig.md) object
Required: No

## See Also
<a name="API_AutoMLProblemTypeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLProblemTypeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLProblemTypeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLProblemTypeConfig)
