---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html
---

# DescribeEndpoint
<a name="API_DescribeEndpoint"></a>

Returns the description of an endpoint.

## Request Syntax
<a name="API_DescribeEndpoint_RequestSyntax"></a>

```
{
   "EndpointName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointName](#API_DescribeEndpoint_RequestSyntax) **   <a name="sagemaker-DescribeEndpoint-request-EndpointName"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeEndpoint_ResponseSyntax"></a>

```
{
   "AsyncInferenceConfig": {
      "ClientConfig": {
         "MaxConcurrentInvocationsPerInstance": number
      },
      "OutputConfig": {
         "KmsKeyId": "string",
         "NotificationConfig": {
            "ErrorTopic": "string",
            "IncludeInferenceResponseIn": [ "string" ],
            "SuccessTopic": "string"
         },
         "S3FailurePath": "string",
         "S3OutputPath": "string"
      }
   },
   "DataCaptureConfig": {
      "CaptureStatus": "string",
      "CurrentSamplingPercentage": number,
      "DestinationS3Uri": "string",
      "EnableCapture": boolean,
      "KmsKeyId": "string"
   },
   "EndpointArn": "string",
   "EndpointConfigName": "string",
   "EndpointName": "string",
   "EndpointStatus": "string",
   "ExplainerConfig": {
      "ClarifyExplainerConfig": {
         "EnableExplanations": "string",
         "InferenceConfig": {
            "ContentTemplate": "string",
            "FeatureHeaders": [ "string" ],
            "FeaturesAttribute": "string",
            "FeatureTypes": [ "string" ],
            "LabelAttribute": "string",
            "LabelHeaders": [ "string" ],
            "LabelIndex": number,
            "MaxPayloadInMB": number,
            "MaxRecordCount": number,
            "ProbabilityAttribute": "string",
            "ProbabilityIndex": number
         },
         "ShapConfig": {
            "NumberOfSamples": number,
            "Seed": number,
            "ShapBaselineConfig": {
               "MimeType": "string",
               "ShapBaseline": "string",
               "ShapBaselineUri": "string"
            },
            "TextConfig": {
               "Granularity": "string",
               "Language": "string"
            },
            "UseLogit": boolean
         }
      }
   },
   "FailureReason": "string",
   "LastDeploymentConfig": {
      "AutoRollbackConfiguration": {
         "Alarms": [
            {
               "AlarmName": "string"
            }
         ]
      },
      "BlueGreenUpdatePolicy": {
         "MaximumExecutionTimeoutInSeconds": number,
         "TerminationWaitInSeconds": number,
         "TrafficRoutingConfiguration": {
            "CanarySize": {
               "Type": "string",
               "Value": number
            },
            "LinearStepSize": {
               "Type": "string",
               "Value": number
            },
            "Type": "string",
            "WaitIntervalInSeconds": number
         }
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
   "MetricsConfig": {
      "EnableDetailedObservability": boolean,
      "EnableEnhancedMetrics": boolean,
      "MetricPublishFrequencyInSeconds": number
   },
   "PendingDeploymentSummary": {
      "EndpointConfigName": "string",
      "ProductionVariants": [
         {
            "AcceleratorType": "string",
            "CurrentInstanceCount": number,
            "CurrentServerlessConfig": {
               "MaxConcurrency": number,
               "MemorySizeInMB": number,
               "ProvisionedConcurrency": number
            },
            "CurrentWeight": number,
            "DeployedImages": [
               {
                  "ResolvedImage": "string",
                  "SpecifiedImage": "string"
               }
            ],
            "DesiredInstanceCount": number,
            "DesiredServerlessConfig": {
               "MaxConcurrency": number,
               "MemorySizeInMB": number,
               "ProvisionedConcurrency": number
            },
            "DesiredWeight": number,
            "InstancePools": [
               {
                  "CurrentInstanceCount": number,
                  "InstanceType": "string"
               }
            ],
            "InstanceType": "string",
            "ManagedInstanceScaling": {
               "MaxInstanceCount": number,
               "MinInstanceCount": number,
               "ScaleInPolicy": {
                  "CooldownInMinutes": number,
                  "MaximumStepSize": number,
                  "Strategy": "string"
               },
               "Status": "string"
            },
            "RoutingConfig": {
               "PrefixAwareRoutingConfig": {
                  "ConcurrencyThreshold": number,
                  "PrefixLength": number
               },
               "RoutingStrategy": "string"
            },
            "VariantName": "string",
            "VariantStatus": [
               {
                  "Status": "string",
                  "StatusMessage": "string"
               }
            ]
         }
      ],
      "ShadowProductionVariants": [
         {
            "AcceleratorType": "string",
            "CurrentInstanceCount": number,
            "CurrentServerlessConfig": {
               "MaxConcurrency": number,
               "MemorySizeInMB": number,
               "ProvisionedConcurrency": number
            },
            "CurrentWeight": number,
            "DeployedImages": [
               {
                  "ResolvedImage": "string",
                  "SpecifiedImage": "string"
               }
            ],
            "DesiredInstanceCount": number,
            "DesiredServerlessConfig": {
               "MaxConcurrency": number,
               "MemorySizeInMB": number,
               "ProvisionedConcurrency": number
            },
            "DesiredWeight": number,
            "InstancePools": [
               {
                  "CurrentInstanceCount": number,
                  "InstanceType": "string"
               }
            ],
            "InstanceType": "string",
            "ManagedInstanceScaling": {
               "MaxInstanceCount": number,
               "MinInstanceCount": number,
               "ScaleInPolicy": {
                  "CooldownInMinutes": number,
                  "MaximumStepSize": number,
                  "Strategy": "string"
               },
               "Status": "string"
            },
            "RoutingConfig": {
               "PrefixAwareRoutingConfig": {
                  "ConcurrencyThreshold": number,
                  "PrefixLength": number
               },
               "RoutingStrategy": "string"
            },
            "VariantName": "string",
            "VariantStatus": [
               {
                  "Status": "string",
                  "StatusMessage": "string"
               }
            ]
         }
      ]
   },
   "ProductionVariants": [
      {
         "CapacityReservationConfig": {
            "AvailableInstanceCount": number,
            "CapacityReservationPreference": "string",
            "Ec2CapacityReservations": [
               {
                  "AvailableInstanceCount": number,
                  "Ec2CapacityReservationId": "string",
                  "TotalInstanceCount": number,
                  "UsedByCurrentEndpoint": number
               }
            ],
            "MlReservationArn": "string",
            "TotalInstanceCount": number,
            "UsedByCurrentEndpoint": number
         },
         "CurrentInstanceCount": number,
         "CurrentServerlessConfig": {
            "MaxConcurrency": number,
            "MemorySizeInMB": number,
            "ProvisionedConcurrency": number
         },
         "CurrentWeight": number,
         "DeployedImages": [
            {
               "ResolvedImage": "string",
               "SpecifiedImage": "string"
            }
         ],
         "DesiredInstanceCount": number,
         "DesiredServerlessConfig": {
            "MaxConcurrency": number,
            "MemorySizeInMB": number,
            "ProvisionedConcurrency": number
         },
         "DesiredWeight": number,
         "InstancePools": [
            {
               "CurrentInstanceCount": number,
               "InstanceType": "string"
            }
         ],
         "ManagedInstanceScaling": {
            "MaxInstanceCount": number,
            "MinInstanceCount": number,
            "ScaleInPolicy": {
               "CooldownInMinutes": number,
               "MaximumStepSize": number,
               "Strategy": "string"
            },
            "Status": "string"
         },
         "RoutingConfig": {
            "PrefixAwareRoutingConfig": {
               "ConcurrencyThreshold": number,
               "PrefixLength": number
            },
            "RoutingStrategy": "string"
         },
         "VariantName": "string",
         "VariantStatus": [
            {
               "Status": "string",
               "StatusMessage": "string"
            }
         ]
      }
   ],
   "ShadowProductionVariants": [
      {
         "CapacityReservationConfig": {
            "AvailableInstanceCount": number,
            "CapacityReservationPreference": "string",
            "Ec2CapacityReservations": [
               {
                  "AvailableInstanceCount": number,
                  "Ec2CapacityReservationId": "string",
                  "TotalInstanceCount": number,
                  "UsedByCurrentEndpoint": number
               }
            ],
            "MlReservationArn": "string",
            "TotalInstanceCount": number,
            "UsedByCurrentEndpoint": number
         },
         "CurrentInstanceCount": number,
         "CurrentServerlessConfig": {
            "MaxConcurrency": number,
            "MemorySizeInMB": number,
            "ProvisionedConcurrency": number
         },
         "CurrentWeight": number,
         "DeployedImages": [
            {
               "ResolvedImage": "string",
               "SpecifiedImage": "string"
            }
         ],
         "DesiredInstanceCount": number,
         "DesiredServerlessConfig": {
            "MaxConcurrency": number,
            "MemorySizeInMB": number,
            "ProvisionedConcurrency": number
         },
         "DesiredWeight": number,
         "InstancePools": [
            {
               "CurrentInstanceCount": number,
               "InstanceType": "string"
            }
         ],
         "ManagedInstanceScaling": {
            "MaxInstanceCount": number,
            "MinInstanceCount": number,
            "ScaleInPolicy": {
               "CooldownInMinutes": number,
               "MaximumStepSize": number,
               "Strategy": "string"
            },
            "Status": "string"
         },
         "RoutingConfig": {
            "PrefixAwareRoutingConfig": {
               "ConcurrencyThreshold": number,
               "PrefixLength": number
            },
            "RoutingStrategy": "string"
         },
         "VariantName": "string",
         "VariantStatus": [
            {
               "Status": "string",
               "StatusMessage": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AsyncInferenceConfig](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-AsyncInferenceConfig"></a>
Returns the description of an endpoint configuration created using the [`CreateEndpointConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) API.
Type: [AsyncInferenceConfig](API_AsyncInferenceConfig.md) object

 ** [DataCaptureConfig](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-DataCaptureConfig"></a>
The currently active data capture configuration used by your Endpoint.
Type: [DataCaptureConfigSummary](API_DataCaptureConfigSummary.md) object

 ** [EndpointArn](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`

 ** [EndpointConfigName](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-EndpointConfigName"></a>
The name of the endpoint configuration associated with this endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [EndpointName](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-EndpointName"></a>
Name of the endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [EndpointStatus](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-EndpointStatus"></a>
The status of the endpoint.
+  `OutOfService`: Endpoint is not available to take incoming requests.
+  `Creating`: [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) is executing.
+  `Updating`: [UpdateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) or [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) is executing.
+  `SystemUpdating`: Endpoint is undergoing maintenance and cannot be updated or deleted or re-scaled until it has completed. This maintenance operation does not change any customer-specified values such as VPC config, KMS encryption, model, instance type, or instance count.
+  `RollingBack`: Endpoint fails to scale up or down or change its variant weight and is in the process of rolling back to its previous configuration. Once the rollback completes, endpoint returns to an `InService` status. This transitional status only applies to an endpoint that has autoscaling enabled and is undergoing variant weight or capacity changes as part of an [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) call or when the [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) operation is called explicitly.
+  `InService`: Endpoint is available to process incoming requests.
+  `Deleting`: [DeleteEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html) is executing.
+  `Failed`: Endpoint could not be created, updated, or re-scaled. Use the `FailureReason` value returned by [DescribeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) for information about the failure. [DeleteEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html) is the only operation that can be performed on a failed endpoint.
+  `UpdateRollbackFailed`: Both the rolling deployment and auto-rollback failed. Your endpoint is in service with a mix of the old and new endpoint configurations. For information about how to remedy this issue and restore the endpoint's status to `InService`, see [Rolling Deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-rolling.html).
Type: String
Valid Values: `OutOfService | Creating | Updating | SystemUpdating | RollingBack | InService | Deleting | Failed | UpdateRollbackFailed`

 ** [ExplainerConfig](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-ExplainerConfig"></a>
The configuration parameters for an explainer.
Type: [ExplainerConfig](API_ExplainerConfig.md) object

 ** [FailureReason](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-FailureReason"></a>
If the status of the endpoint is `Failed`, the reason why it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastDeploymentConfig](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-LastDeploymentConfig"></a>
The most recent deployment configuration for the endpoint.
Type: [DeploymentConfig](API_DeploymentConfig.md) object

 ** [MetricsConfig](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-MetricsConfig"></a>
The configuration parameters for utilization metrics.
Type: [MetricsConfig](API_MetricsConfig.md) object

 ** [PendingDeploymentSummary](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-PendingDeploymentSummary"></a>
Returns the summary of an in-progress deployment. This field is only returned when the endpoint is creating or updating with a new endpoint configuration.
Type: [PendingDeploymentSummary](API_PendingDeploymentSummary.md) object

 ** [ProductionVariants](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-ProductionVariants"></a>
An array of [ProductionVariantSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantSummary.html) objects, one for each model hosted behind this endpoint.
Type: Array of [ProductionVariantSummary](API_ProductionVariantSummary.md) objects
Array Members: Minimum number of 1 item.

 ** [ShadowProductionVariants](#API_DescribeEndpoint_ResponseSyntax) **   <a name="sagemaker-DescribeEndpoint-response-ShadowProductionVariants"></a>
An array of [ProductionVariantSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantSummary.html) objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on `ProductionVariants`.
Type: Array of [ProductionVariantSummary](API_ProductionVariantSummary.md) objects
Array Members: Minimum number of 1 item.

## Errors
<a name="API_DescribeEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeEndpoint)
