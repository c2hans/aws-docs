---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_AlgorithmSpecification.html
---

# AlgorithmSpecification
<a name="API_AlgorithmSpecification"></a>

Defines the Amazon Braket hybrid job to be created. Specifies the container image the job uses and the paths to the Python scripts used for entry and training.

## Contents
<a name="API_AlgorithmSpecification_Contents"></a>

 ** containerImage **   <a name="braket-Type-AlgorithmSpecification-containerImage"></a>
The container image used to create an Amazon Braket hybrid job.
Type: [ContainerImage](API_ContainerImage.md) object
Required: No

 ** scriptModeConfig **   <a name="braket-Type-AlgorithmSpecification-scriptModeConfig"></a>
Configures the paths to the Python scripts used for entry and training.
Type: [ScriptModeConfig](API_ScriptModeConfig.md) object
Required: No

## See Also
<a name="API_AlgorithmSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/AlgorithmSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/AlgorithmSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/AlgorithmSpecification)
