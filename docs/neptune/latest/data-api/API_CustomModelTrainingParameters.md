---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_CustomModelTrainingParameters.html
---

# CustomModelTrainingParameters
<a name="API_CustomModelTrainingParameters"></a>

Contains custom model training parameters. See [Custom models in Neptune ML](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-custom-models.html).

## Contents
<a name="API_CustomModelTrainingParameters_Contents"></a>

 ** sourceS3DirectoryPath **   <a name="neptunedata-Type-CustomModelTrainingParameters-sourceS3DirectoryPath"></a>
The path to the Amazon S3 location where the Python module implementing your model is located. This must point to a valid existing Amazon S3 location that contains, at a minimum, a training script, a transform script, and a `model-hpo-configuration.json` file.
Type: String
Required: Yes

 ** trainingEntryPointScript **   <a name="neptunedata-Type-CustomModelTrainingParameters-trainingEntryPointScript"></a>
The name of the entry point in your module of a script that performs model training and takes hyperparameters as command-line arguments, including fixed hyperparameters. The default is `training.py`.
Type: String
Required: No

 ** transformEntryPointScript **   <a name="neptunedata-Type-CustomModelTrainingParameters-transformEntryPointScript"></a>
The name of the entry point in your module of a script that should be run after the best model from the hyperparameter search has been identified, to compute the model artifacts necessary for model deployment. It should be able to run with no command-line arguments.The default is `transform.py`.
Type: String
Required: No

## See Also
<a name="API_CustomModelTrainingParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/CustomModelTrainingParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/CustomModelTrainingParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/CustomModelTrainingParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
