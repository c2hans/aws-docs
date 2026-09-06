---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployResult.html
---

# ModelDeployResult
<a name="API_ModelDeployResult"></a>

Provides information about the endpoint of the model deployment.

## Contents
<a name="API_ModelDeployResult_Contents"></a>

 ** EndpointName **   <a name="sagemaker-Type-ModelDeployResult-EndpointName"></a>
The name of the endpoint to which the model has been deployed.
If model deployment fails, this field is omitted from the response.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_ModelDeployResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelDeployResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelDeployResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelDeployResult)
