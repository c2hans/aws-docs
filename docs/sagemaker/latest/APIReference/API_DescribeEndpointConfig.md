---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html
---

# DescribeEndpointConfig
<a name="API_DescribeEndpointConfig"></a>

Returns the description of an endpoint configuration created using the `CreateEndpointConfig` API.

## Request Syntax
<a name="API_DescribeEndpointConfig_RequestSyntax"></a>

```
{
   "EndpointConfigName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEndpointConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointConfigName](#API_DescribeEndpointConfig_RequestSyntax) **   <a name="sagemaker-DescribeEndpointConfig-request-EndpointConfigName"></a>
The name of the endpoint configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeEndpointConfig_ResponseSyntax"></a>

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
   "CreationTime": number,
   "DataCaptureConfig": {
      "CaptureContentTypeHeader": {
         "CsvContentTypes": [ "string" ],
         "JsonContentTypes": [ "string" ]
      },
      "CaptureOptions": [
         {
            "CaptureMode": "string"
         }
      ],
      "DestinationS3Uri": "string",
      "EnableCapture": boolean,
      "InitialSamplingPercentage": number,
      "KmsKeyId": "string"
   },
   "EnableNetworkIsolation": boolean,
   "EndpointConfigArn": "string",
   "EndpointConfigName": "string",
   "ExecutionRoleArn": "string",
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
   "KmsKeyId": "string",
   "MetricsConfig": {
      "EnableDetailedObservability": boolean,
      "EnableEnhancedMetrics": boolean,
      "MetricPublishFrequencyInSeconds": number
   },
   "ProductionVariants": [
      {
         "AcceleratorType": "string",
         "CapacityReservationConfig": {
            "CapacityReservationPreference": "string",
            "MlReservationArn": "string"
         },
         "ContainerStartupHealthCheckTimeoutInSeconds": number,
         "CoreDumpConfig": {
            "DestinationS3Uri": "string",
            "KmsKeyId": "string"
         },
         "EnableSSMAccess": boolean,
         "InferenceAmiVersion": "string",
         "InitialInstanceCount": number,
         "InitialVariantWeight": number,
         "InstancePools": [
            {
               "InstanceType": "string",
               "ModelNameOverride": "string",
               "Priority": number
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
         "ModelDataDownloadTimeoutInSeconds": number,
         "ModelName": "string",
         "RoutingConfig": {
            "PrefixAwareRoutingConfig": {
               "ConcurrencyThreshold": number,
               "PrefixLength": number
            },
            "RoutingStrategy": "string"
         },
         "ServerlessConfig": {
            "MaxConcurrency": number,
            "MemorySizeInMB": number,
            "ProvisionedConcurrency": number
         },
         "VariantInstanceProvisionTimeoutInSeconds": number,
         "VariantName": "string",
         "VolumeSizeInGB": number
      }
   ],
   "ShadowProductionVariants": [
      {
         "AcceleratorType": "string",
         "CapacityReservationConfig": {
            "CapacityReservationPreference": "string",
            "MlReservationArn": "string"
         },
         "ContainerStartupHealthCheckTimeoutInSeconds": number,
         "CoreDumpConfig": {
            "DestinationS3Uri": "string",
            "KmsKeyId": "string"
         },
         "EnableSSMAccess": boolean,
         "InferenceAmiVersion": "string",
         "InitialInstanceCount": number,
         "InitialVariantWeight": number,
         "InstancePools": [
            {
               "InstanceType": "string",
               "ModelNameOverride": "string",
               "Priority": number
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
         "ModelDataDownloadTimeoutInSeconds": number,
         "ModelName": "string",
         "RoutingConfig": {
            "PrefixAwareRoutingConfig": {
               "ConcurrencyThreshold": number,
               "PrefixLength": number
            },
            "RoutingStrategy": "string"
         },
         "ServerlessConfig": {
            "MaxConcurrency": number,
            "MemorySizeInMB": number,
            "ProvisionedConcurrency": number
         },
         "VariantInstanceProvisionTimeoutInSeconds": number,
         "VariantName": "string",
         "VolumeSizeInGB": number
      }
   ],
   "VpcConfig": {
      "SecurityGroupIds": [ "string" ],
      "Subnets": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeEndpointConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AsyncInferenceConfig](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-AsyncInferenceConfig"></a>
Returns the description of an endpoint configuration created using the [`CreateEndpointConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) API.
Type: [AsyncInferenceConfig](API_AsyncInferenceConfig.md) object

 ** [CreationTime](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-CreationTime"></a>
A timestamp that shows when the endpoint configuration was created.
Type: Timestamp

 ** [DataCaptureConfig](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-DataCaptureConfig"></a>
Configuration to control how SageMaker AI captures inference data.
Type: [DataCaptureConfig](API_DataCaptureConfig.md) object

 ** [EnableNetworkIsolation](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-EnableNetworkIsolation"></a>
Indicates whether all model containers deployed to the endpoint are isolated. If they are, no inbound or outbound network calls can be made to or from the model containers.
Type: Boolean

 ** [EndpointConfigArn](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-EndpointConfigArn"></a>
The Amazon Resource Name (ARN) of the endpoint configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint-config/.*`

 ** [EndpointConfigName](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-EndpointConfigName"></a>
Name of the SageMaker endpoint configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ExecutionRoleArn](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you assigned to the endpoint configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [ExplainerConfig](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-ExplainerConfig"></a>
The configuration parameters for an explainer.
Type: [ExplainerConfig](API_ExplainerConfig.md) object

 ** [KmsKeyId](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-KmsKeyId"></a>
 AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the ML storage volume attached to the instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`

 ** [MetricsConfig](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-MetricsConfig"></a>
The configuration parameters for utilization metrics.
Type: [MetricsConfig](API_MetricsConfig.md) object

 ** [ProductionVariants](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-ProductionVariants"></a>
An array of `ProductionVariant` objects, one for each model that you want to host at this endpoint.
Type: Array of [ProductionVariant](API_ProductionVariant.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [ShadowProductionVariants](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-ShadowProductionVariants"></a>
An array of `ProductionVariant` objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on `ProductionVariants`.
Type: Array of [ProductionVariant](API_ProductionVariant.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [VpcConfig](#API_DescribeEndpointConfig_ResponseSyntax) **   <a name="sagemaker-DescribeEndpointConfig-response-VpcConfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: [VpcConfig](API_VpcConfig.md) object

## Errors
<a name="API_DescribeEndpointConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEndpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeEndpointConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeEndpointConfig)
