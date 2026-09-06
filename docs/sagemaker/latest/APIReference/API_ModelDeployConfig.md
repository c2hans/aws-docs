---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployConfig.html
---

# ModelDeployConfig
<a name="API_ModelDeployConfig"></a>

Specifies how to generate the endpoint name for an automatic one-click Autopilot model deployment.

## Contents
<a name="API_ModelDeployConfig_Contents"></a>

 ** AutoGenerateEndpointName **   <a name="sagemaker-Type-ModelDeployConfig-AutoGenerateEndpointName"></a>
Set to `True` to automatically generate an endpoint name for a one-click Autopilot model deployment; set to `False` otherwise. The default value is `False`.
If you set `AutoGenerateEndpointName` to `True`, do not specify the `EndpointName`; otherwise a 400 error is thrown.
Type: Boolean
Required: No

 ** EndpointName **   <a name="sagemaker-Type-ModelDeployConfig-EndpointName"></a>
Specifies the endpoint name to use for a one-click Autopilot model deployment if the endpoint name is not generated automatically.
Specify the `EndpointName` if and only if you set `AutoGenerateEndpointName` to `False`; otherwise a 400 error is thrown.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_ModelDeployConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelDeployConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelDeployConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelDeployConfig)
