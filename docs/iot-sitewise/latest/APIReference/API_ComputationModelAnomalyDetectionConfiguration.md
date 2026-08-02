---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ComputationModelAnomalyDetectionConfiguration.html
---

# ComputationModelAnomalyDetectionConfiguration
<a name="API_ComputationModelAnomalyDetectionConfiguration"></a>

Contains the configuration of the type of anomaly detection computation model.

## Contents
<a name="API_ComputationModelAnomalyDetectionConfiguration_Contents"></a>

 ** inputProperties **   <a name="iotsitewise-Type-ComputationModelAnomalyDetectionConfiguration-inputProperties"></a>
Define the variable name associated with input properties, with the following format `${VariableName}`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `^\$\{[a-z][a-z0-9_]*\}`
Required: Yes

 ** resultProperty **   <a name="iotsitewise-Type-ComputationModelAnomalyDetectionConfiguration-resultProperty"></a>
Define the variable name associated with the result property, and the following format `${VariableName}`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `^\$\{[a-z][a-z0-9_]*\}`
Required: Yes

## See Also
<a name="API_ComputationModelAnomalyDetectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ComputationModelAnomalyDetectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ComputationModelAnomalyDetectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ComputationModelAnomalyDetectionConfiguration)
