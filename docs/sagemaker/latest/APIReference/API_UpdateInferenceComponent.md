---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateInferenceComponent.html
---

# UpdateInferenceComponent
<a name="API_UpdateInferenceComponent"></a>

Updates an inference component.

## Request Syntax
<a name="API_UpdateInferenceComponent_RequestSyntax"></a>

```
{
   "DeploymentConfig": {
      "AutoRollbackConfiguration": {
         "Alarms": [
            {
               "AlarmName": "{{string}}"
            }
         ]
      },
      "RollingUpdatePolicy": {
         "MaximumBatchSize": {
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "MaximumExecutionTimeoutInSeconds": {{number}},
         "RollbackMaximumBatchSize": {
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "WaitIntervalInSeconds": {{number}}
      }
   },
   "InferenceComponentName": "{{string}}",
   "RuntimeConfig": {
      "CopyCount": {{number}}
   },
   "Specification": {
      "BaseInferenceComponentName": "{{string}}",
      "ComputeResourceRequirements": {
         "MaxMemoryRequiredInMb": {{number}},
         "MinMemoryRequiredInMb": {{number}},
         "NumberOfAcceleratorDevicesRequired": {{number}},
         "NumberOfCpuCoresRequired": {{number}}
      },
      "Container": {
         "ArtifactUrl": "{{string}}",
         "ContainerMetricsConfig": {
            "MetricsEndpoints": [
               {
                  "MetricPublishFrequencyInSeconds": {{number}},
                  "MetricsEndpointPath": "{{string}}"
               }
            ]
         },
         "Environment": {
            "{{string}}" : "{{string}}"
         },
         "Image": "{{string}}"
      },
      "DataCacheConfig": {
         "EnableCaching": {{boolean}}
      },
      "InstanceType": "{{string}}",
      "ModelName": "{{string}}",
      "SchedulingConfig": {
         "AvailabilityZoneBalance": {
            "EnforcementMode": "{{string}}",
            "MaxImbalance": {{number}}
         },
         "PlacementStrategy": "{{string}}"
      },
      "StartupParameters": {
         "ContainerStartupHealthCheckTimeoutInSeconds": {{number}},
         "ModelDataDownloadTimeoutInSeconds": {{number}}
      }
   },
   "Specifications": [
      {
         "BaseInferenceComponentName": "{{string}}",
         "ComputeResourceRequirements": {
            "MaxMemoryRequiredInMb": {{number}},
            "MinMemoryRequiredInMb": {{number}},
            "NumberOfAcceleratorDevicesRequired": {{number}},
            "NumberOfCpuCoresRequired": {{number}}
         },
         "Container": {
            "ArtifactUrl": "{{string}}",
            "ContainerMetricsConfig": {
               "MetricsEndpoints": [
                  {
                     "MetricPublishFrequencyInSeconds": {{number}},
                     "MetricsEndpointPath": "{{string}}"
                  }
               ]
            },
            "Environment": {
               "{{string}}" : "{{string}}"
            },
            "Image": "{{string}}"
         },
         "DataCacheConfig": {
            "EnableCaching": {{boolean}}
         },
         "InstanceType": "{{string}}",
         "ModelName": "{{string}}",
         "SchedulingConfig": {
            "AvailabilityZoneBalance": {
               "EnforcementMode": "{{string}}",
               "MaxImbalance": {{number}}
            },
            "PlacementStrategy": "{{string}}"
         },
         "StartupParameters": {
            "ContainerStartupHealthCheckTimeoutInSeconds": {{number}},
            "ModelDataDownloadTimeoutInSeconds": {{number}}
         }
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateInferenceComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeploymentConfig](#API_UpdateInferenceComponent_RequestSyntax) **   <a name="sagemaker-UpdateInferenceComponent-request-DeploymentConfig"></a>
The deployment configuration for the inference component. The configuration contains the desired deployment strategy and rollback settings.
Type: [InferenceComponentDeploymentConfig](API_InferenceComponentDeploymentConfig.md) object
Required: No

 ** [InferenceComponentName](#API_UpdateInferenceComponent_RequestSyntax) **   <a name="sagemaker-UpdateInferenceComponent-request-InferenceComponentName"></a>
The name of the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

 ** [RuntimeConfig](#API_UpdateInferenceComponent_RequestSyntax) **   <a name="sagemaker-UpdateInferenceComponent-request-RuntimeConfig"></a>
Runtime settings for a model that is deployed with an inference component.
Type: [InferenceComponentRuntimeConfig](API_InferenceComponentRuntimeConfig.md) object
Required: No

 ** [Specification](#API_UpdateInferenceComponent_RequestSyntax) **   <a name="sagemaker-UpdateInferenceComponent-request-Specification"></a>
Details about the resources to deploy with this inference component, including the model, container, and compute resources.
Type: [InferenceComponentSpecification](API_InferenceComponentSpecification.md) object
Required: No

 ** [Specifications](#API_UpdateInferenceComponent_RequestSyntax) **   <a name="sagemaker-UpdateInferenceComponent-request-Specifications"></a>
A list of specification objects for the inference component, one per instance type. Use this parameter when you want to specify different model or resource configurations for the inference component on each instance type. You can use either this parameter or the singular `Specification` parameter, but not both.
Type: Array of [InferenceComponentSpecification](API_InferenceComponentSpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## Response Syntax
<a name="API_UpdateInferenceComponent_ResponseSyntax"></a>

```
{
   "InferenceComponentArn": "string"
}
```

## Response Elements
<a name="API_UpdateInferenceComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceComponentArn](#API_UpdateInferenceComponent_ResponseSyntax) **   <a name="sagemaker-UpdateInferenceComponent-response-InferenceComponentArn"></a>
The Amazon Resource Name (ARN) of the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_UpdateInferenceComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_UpdateInferenceComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateInferenceComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateInferenceComponent)
