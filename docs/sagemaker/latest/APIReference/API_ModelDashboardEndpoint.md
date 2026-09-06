---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDashboardEndpoint.html
---

# ModelDashboardEndpoint
<a name="API_ModelDashboardEndpoint"></a>

An endpoint that hosts a model displayed in the Amazon SageMaker Model Dashboard.

## Contents
<a name="API_ModelDashboardEndpoint_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-ModelDashboardEndpoint-CreationTime"></a>
A timestamp that indicates when the endpoint was created.
Type: Timestamp
Required: Yes

 ** EndpointArn **   <a name="sagemaker-Type-ModelDashboardEndpoint-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`
Required: Yes

 ** EndpointName **   <a name="sagemaker-Type-ModelDashboardEndpoint-EndpointName"></a>
The endpoint name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EndpointStatus **   <a name="sagemaker-Type-ModelDashboardEndpoint-EndpointStatus"></a>
The endpoint status.
Type: String
Valid Values: `OutOfService | Creating | Updating | SystemUpdating | RollingBack | InService | Deleting | Failed | UpdateRollbackFailed`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-ModelDashboardEndpoint-LastModifiedTime"></a>
The last time the endpoint was modified.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ModelDashboardEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelDashboardEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelDashboardEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelDashboardEndpoint)
