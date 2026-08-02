---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_CustomModelTransformParameters.html
---

# CustomModelTransformParameters
<a name="API_CustomModelTransformParameters"></a>

Contains custom model transform parameters. See [Use a trained model to generate new model artifacts](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-model-transform.html).

## Contents
<a name="API_CustomModelTransformParameters_Contents"></a>

 ** sourceS3DirectoryPath **   <a name="neptunedata-Type-CustomModelTransformParameters-sourceS3DirectoryPath"></a>
The path to the Amazon S3 location where the Python module implementing your model is located. This must point to a valid existing Amazon S3 location that contains, at a minimum, a training script, a transform script, and a `model-hpo-configuration.json` file.
Type: String
Required: Yes

 ** transformEntryPointScript **   <a name="neptunedata-Type-CustomModelTransformParameters-transformEntryPointScript"></a>
The name of the entry point in your module of a script that should be run after the best model from the hyperparameter search has been identified, to compute the model artifacts necessary for model deployment. It should be able to run with no command-line arguments. The default is `transform.py`.
Type: String
Required: No

## See Also
<a name="API_CustomModelTransformParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/CustomModelTransformParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/CustomModelTransformParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/CustomModelTransformParameters)
