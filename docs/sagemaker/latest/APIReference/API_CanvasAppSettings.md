---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CanvasAppSettings.html
---

# CanvasAppSettings
<a name="API_CanvasAppSettings"></a>

The SageMaker Canvas application settings.

## Contents
<a name="API_CanvasAppSettings_Contents"></a>

 ** DirectDeploySettings **   <a name="sagemaker-Type-CanvasAppSettings-DirectDeploySettings"></a>
The model deployment settings for the SageMaker Canvas application.
Type: [DirectDeploySettings](API_DirectDeploySettings.md) object
Required: No

 ** EmrServerlessSettings **   <a name="sagemaker-Type-CanvasAppSettings-EmrServerlessSettings"></a>
The settings for running Amazon EMR Serverless data processing jobs in SageMaker Canvas.
Type: [EmrServerlessSettings](API_EmrServerlessSettings.md) object
Required: No

 ** GenerativeAiSettings **   <a name="sagemaker-Type-CanvasAppSettings-GenerativeAiSettings"></a>
The generative AI settings for the SageMaker Canvas application.
Type: [GenerativeAiSettings](API_GenerativeAiSettings.md) object
Required: No

 ** IdentityProviderOAuthSettings **   <a name="sagemaker-Type-CanvasAppSettings-IdentityProviderOAuthSettings"></a>
The settings for connecting to an external data source with OAuth.
Type: Array of [IdentityProviderOAuthSetting](API_IdentityProviderOAuthSetting.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** KendraSettings **   <a name="sagemaker-Type-CanvasAppSettings-KendraSettings"></a>
The settings for document querying.
Type: [KendraSettings](API_KendraSettings.md) object
Required: No

 ** ModelRegisterSettings **   <a name="sagemaker-Type-CanvasAppSettings-ModelRegisterSettings"></a>
The model registry settings for the SageMaker Canvas application.
Type: [ModelRegisterSettings](API_ModelRegisterSettings.md) object
Required: No

 ** TimeSeriesForecastingSettings **   <a name="sagemaker-Type-CanvasAppSettings-TimeSeriesForecastingSettings"></a>
Time series forecast settings for the SageMaker Canvas application.
Type: [TimeSeriesForecastingSettings](API_TimeSeriesForecastingSettings.md) object
Required: No

 ** WorkspaceSettings **   <a name="sagemaker-Type-CanvasAppSettings-WorkspaceSettings"></a>
The workspace settings for the SageMaker Canvas application.
Type: [WorkspaceSettings](API_WorkspaceSettings.md) object
Required: No

## See Also
<a name="API_CanvasAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CanvasAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CanvasAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CanvasAppSettings)
