---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Endpoint.html
---

# Endpoint
<a name="API_Endpoint"></a>

A hosted endpoint for real-time inference.

## Contents
<a name="API_Endpoint_Contents"></a>

 ** EndpointArn **   <a name="sagemaker-Type-Endpoint-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`
Required: Yes

 ** EndpointConfigName **   <a name="sagemaker-Type-Endpoint-EndpointConfigName"></a>
The endpoint configuration associated with the endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EndpointName **   <a name="sagemaker-Type-Endpoint-EndpointName"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EndpointStatus **   <a name="sagemaker-Type-Endpoint-EndpointStatus"></a>
The status of the endpoint.
Type: String
Valid Values: `OutOfService | Creating | Updating | SystemUpdating | RollingBack | InService | Deleting | Failed | UpdateRollbackFailed`
Required: Yes

 ** DataCaptureConfig **   <a name="sagemaker-Type-Endpoint-DataCaptureConfig"></a>
The currently active data capture configuration used by your Endpoint.
Type: [DataCaptureConfigSummary](API_DataCaptureConfigSummary.md) object
Required: No

 ** FailureReason **   <a name="sagemaker-Type-Endpoint-FailureReason"></a>
If the endpoint failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** MonitoringSchedules **   <a name="sagemaker-Type-Endpoint-MonitoringSchedules"></a>
A list of monitoring schedules for the endpoint. For information about model monitoring, see [Amazon SageMaker Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html).
Type: Array of [MonitoringSchedule](API_MonitoringSchedule.md) objects
Required: No

 ** ProductionVariants **   <a name="sagemaker-Type-Endpoint-ProductionVariants"></a>
A list of the production variants hosted on the endpoint. Each production variant is a model.
Type: Array of [ProductionVariantSummary](API_ProductionVariantSummary.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ShadowProductionVariants **   <a name="sagemaker-Type-Endpoint-ShadowProductionVariants"></a>
A list of the shadow variants hosted on the endpoint. Each shadow variant is a model in shadow mode with production traffic replicated from the production variant.
Type: Array of [ProductionVariantSummary](API_ProductionVariantSummary.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** Tags **   <a name="sagemaker-Type-Endpoint-Tags"></a>
A list of the tags associated with the endpoint. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Endpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Endpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Endpoint)
