---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceComponent.html
---

# DescribeInferenceComponent
<a name="API_DescribeInferenceComponent"></a>

Returns information about an inference component.

## Request Syntax
<a name="API_DescribeInferenceComponent_RequestSyntax"></a>

```
{
   "InferenceComponentName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInferenceComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InferenceComponentName](#API_DescribeInferenceComponent_RequestSyntax) **   <a name="sagemaker-DescribeInferenceComponent-request-InferenceComponentName"></a>
The name of the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

## Response Syntax
<a name="API_DescribeInferenceComponent_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "EndpointArn": "string",
   "EndpointName": "string",
   "FailureReason": "string",
   "InferenceComponentArn": "string",
   "InferenceComponentName": "string",
   "InferenceComponentStatus": "string",
   "LastDeploymentConfig": {
      "AutoRollbackConfiguration": {
         "Alarms": [
            {
               "AlarmName": "string"
            }
         ]
      },
      "RollingUpdatePolicy": {
         "MaximumBatchSize": {
            "Type": "string",
            "Value": number
         },
         "MaximumExecutionTimeoutInSeconds": number,
         "RollbackMaximumBatchSize": {
            "Type": "string",
            "Value": number
         },
         "WaitIntervalInSeconds": number
      }
   },
   "LastModifiedTime": number,
   "RuntimeConfig": {
      "CurrentCopyCount": number,
      "DesiredCopyCount": number,
      "PlacementStatus": [
         {
            "CurrentCopyCount": number,
            "InstanceType": "string"
         }
      ]
   },
   "Specification": {
      "BaseInferenceComponentName": "string",
      "ComputeResourceRequirements": {
         "MaxMemoryRequiredInMb": number,
         "MinMemoryRequiredInMb": number,
         "NumberOfAcceleratorDevicesRequired": number,
         "NumberOfCpuCoresRequired": number
      },
      "Container": {
         "ArtifactUrl": "string",
         "ContainerMetricsConfig": {
            "MetricsEndpoints": [
               {
                  "MetricPublishFrequencyInSeconds": number,
                  "MetricsEndpointPath": "string"
               }
            ]
         },
         "DeployedImage": {
            "ResolutionTime": number,
            "ResolvedImage": "string",
            "SpecifiedImage": "string"
         },
         "Environment": {
            "string" : "string"
         }
      },
      "DataCacheConfig": {
         "EnableCaching": boolean
      },
      "InstanceType": "string",
      "ModelName": "string",
      "SchedulingConfig": {
         "AvailabilityZoneBalance": {
            "EnforcementMode": "string",
            "MaxImbalance": number
         },
         "PlacementStrategy": "string"
      },
      "StartupParameters": {
         "ContainerStartupHealthCheckTimeoutInSeconds": number,
         "ModelDataDownloadTimeoutInSeconds": number
      }
   },
   "Specifications": [
      {
         "BaseInferenceComponentName": "string",
         "ComputeResourceRequirements": {
            "MaxMemoryRequiredInMb": number,
            "MinMemoryRequiredInMb": number,
            "NumberOfAcceleratorDevicesRequired": number,
            "NumberOfCpuCoresRequired": number
         },
         "Container": {
            "ArtifactUrl": "string",
            "ContainerMetricsConfig": {
               "MetricsEndpoints": [
                  {
                     "MetricPublishFrequencyInSeconds": number,
                     "MetricsEndpointPath": "string"
                  }
               ]
            },
            "DeployedImage": {
               "ResolutionTime": number,
               "ResolvedImage": "string",
               "SpecifiedImage": "string"
            },
            "Environment": {
               "string" : "string"
            }
         },
         "DataCacheConfig": {
            "EnableCaching": boolean
         },
         "InstanceType": "string",
         "ModelName": "string",
         "SchedulingConfig": {
            "AvailabilityZoneBalance": {
               "EnforcementMode": "string",
               "MaxImbalance": number
            },
            "PlacementStrategy": "string"
         },
         "StartupParameters": {
            "ContainerStartupHealthCheckTimeoutInSeconds": number,
            "ModelDataDownloadTimeoutInSeconds": number
         }
      }
   ],
   "VariantName": "string"
}
```

## Response Elements
<a name="API_DescribeInferenceComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-CreationTime"></a>
The time when the inference component was created.
Type: Timestamp

 ** [EndpointArn](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint that hosts the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`

 ** [EndpointName](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-EndpointName"></a>
The name of the endpoint that hosts the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [FailureReason](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-FailureReason"></a>
If the inference component status is `Failed`, the reason for the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [InferenceComponentArn](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-InferenceComponentArn"></a>
The Amazon Resource Name (ARN) of the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [InferenceComponentName](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-InferenceComponentName"></a>
The name of the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`

 ** [InferenceComponentStatus](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-InferenceComponentStatus"></a>
The status of the inference component.
Type: String
Valid Values: `InService | Creating | Updating | Failed | Deleting`

 ** [LastDeploymentConfig](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-LastDeploymentConfig"></a>
The deployment and rollback settings that you assigned to the inference component.
Type: [InferenceComponentDeploymentConfig](API_InferenceComponentDeploymentConfig.md) object

 ** [LastModifiedTime](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-LastModifiedTime"></a>
The time when the inference component was last updated.
Type: Timestamp

 ** [RuntimeConfig](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-RuntimeConfig"></a>
Details about the runtime settings for the model that is deployed with the inference component.
Type: [InferenceComponentRuntimeConfigSummary](API_InferenceComponentRuntimeConfigSummary.md) object

 ** [Specification](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-Specification"></a>
Details about the resources that are deployed with this inference component.
Type: [InferenceComponentSpecificationSummary](API_InferenceComponentSpecificationSummary.md) object

 ** [Specifications](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-Specifications"></a>
A list of specification summaries for the inference component, one per instance type. This parameter is populated when the inference component was created with multiple specifications. When this parameter is populated, the singular `Specification` parameter is not returned.
Type: Array of [InferenceComponentSpecificationSummary](API_InferenceComponentSpecificationSummary.md) objects
Array Members: Minimum number of 1 item.

 ** [VariantName](#API_DescribeInferenceComponent_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceComponent-response-VariantName"></a>
The name of the production variant that hosts the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_DescribeInferenceComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeInferenceComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeInferenceComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeInferenceComponent)
