---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html
---

# CreateEndpointConfig
<a name="API_CreateEndpointConfig"></a>

Creates an endpoint configuration that SageMaker hosting services uses to deploy models. In the configuration, you identify one or more models, created using the `CreateModel` API, to deploy and the resources that you want SageMaker to provision. Then you call the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) API.

**Note**
 Use this API if you want to use SageMaker hosting services to deploy models into production.

In the request, you define a `ProductionVariant`, for each model that you want to deploy. Each `ProductionVariant` parameter also describes the resources that you want SageMaker to provision. This includes the number and type of ML compute instances to deploy.

If you are hosting multiple models, you also assign a `VariantWeight` to specify how much traffic you want to allocate to each model. For example, suppose that you want to host two models, A and B, and you assign traffic weight 2 for model A and 1 for model B. SageMaker distributes two-thirds of the traffic to Model A, and one-third to model B.

**Note**
When you call [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html), a load call is made to DynamoDB to verify that your endpoint configuration exists. When you read data from a DynamoDB table supporting [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), the response might not reflect the results of a recently completed write operation. The response might include some stale data. If the dependent entities are not yet in DynamoDB, this causes a validation error. If you repeat your read request after a short time, the response should return the latest data. So retry logic is recommended to handle these possible issues. We also recommend that customers call [DescribeEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html) before calling [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) to minimize the potential impact of a DynamoDB eventually consistent read.

## Request Syntax
<a name="API_CreateEndpointConfig_RequestSyntax"></a>

```
{
   "AsyncInferenceConfig": {
      "ClientConfig": {
         "MaxConcurrentInvocationsPerInstance": {{number}}
      },
      "OutputConfig": {
         "KmsKeyId": "{{string}}",
         "NotificationConfig": {
            "ErrorTopic": "{{string}}",
            "IncludeInferenceResponseIn": [ "{{string}}" ],
            "SuccessTopic": "{{string}}"
         },
         "S3FailurePath": "{{string}}",
         "S3OutputPath": "{{string}}"
      }
   },
   "DataCaptureConfig": {
      "CaptureContentTypeHeader": {
         "CsvContentTypes": [ "{{string}}" ],
         "JsonContentTypes": [ "{{string}}" ]
      },
      "CaptureOptions": [
         {
            "CaptureMode": "{{string}}"
         }
      ],
      "DestinationS3Uri": "{{string}}",
      "EnableCapture": {{boolean}},
      "InitialSamplingPercentage": {{number}},
      "KmsKeyId": "{{string}}"
   },
   "EnableNetworkIsolation": {{boolean}},
   "EndpointConfigName": "{{string}}",
   "ExecutionRoleArn": "{{string}}",
   "ExplainerConfig": {
      "ClarifyExplainerConfig": {
         "EnableExplanations": "{{string}}",
         "InferenceConfig": {
            "ContentTemplate": "{{string}}",
            "FeatureHeaders": [ "{{string}}" ],
            "FeaturesAttribute": "{{string}}",
            "FeatureTypes": [ "{{string}}" ],
            "LabelAttribute": "{{string}}",
            "LabelHeaders": [ "{{string}}" ],
            "LabelIndex": {{number}},
            "MaxPayloadInMB": {{number}},
            "MaxRecordCount": {{number}},
            "ProbabilityAttribute": "{{string}}",
            "ProbabilityIndex": {{number}}
         },
         "ShapConfig": {
            "NumberOfSamples": {{number}},
            "Seed": {{number}},
            "ShapBaselineConfig": {
               "MimeType": "{{string}}",
               "ShapBaseline": "{{string}}",
               "ShapBaselineUri": "{{string}}"
            },
            "TextConfig": {
               "Granularity": "{{string}}",
               "Language": "{{string}}"
            },
            "UseLogit": {{boolean}}
         }
      }
   },
   "KmsKeyId": "{{string}}",
   "MetricsConfig": {
      "EnableDetailedObservability": {{boolean}},
      "EnableEnhancedMetrics": {{boolean}},
      "MetricPublishFrequencyInSeconds": {{number}}
   },
   "ProductionVariants": [
      {
         "AcceleratorType": "{{string}}",
         "CapacityReservationConfig": {
            "CapacityReservationPreference": "{{string}}",
            "MlReservationArn": "{{string}}"
         },
         "ContainerStartupHealthCheckTimeoutInSeconds": {{number}},
         "CoreDumpConfig": {
            "DestinationS3Uri": "{{string}}",
            "KmsKeyId": "{{string}}"
         },
         "EnableSSMAccess": {{boolean}},
         "InferenceAmiVersion": "{{string}}",
         "InitialInstanceCount": {{number}},
         "InitialVariantWeight": {{number}},
         "InstancePools": [
            {
               "InstanceType": "{{string}}",
               "ModelNameOverride": "{{string}}",
               "Priority": {{number}}
            }
         ],
         "InstanceType": "{{string}}",
         "ManagedInstanceScaling": {
            "MaxInstanceCount": {{number}},
            "MinInstanceCount": {{number}},
            "ScaleInPolicy": {
               "CooldownInMinutes": {{number}},
               "MaximumStepSize": {{number}},
               "Strategy": "{{string}}"
            },
            "Status": "{{string}}"
         },
         "ModelDataDownloadTimeoutInSeconds": {{number}},
         "ModelName": "{{string}}",
         "RoutingConfig": {
            "RoutingStrategy": "{{string}}"
         },
         "ServerlessConfig": {
            "MaxConcurrency": {{number}},
            "MemorySizeInMB": {{number}},
            "ProvisionedConcurrency": {{number}}
         },
         "VariantInstanceProvisionTimeoutInSeconds": {{number}},
         "VariantName": "{{string}}",
         "VolumeSizeInGB": {{number}}
      }
   ],
   "ShadowProductionVariants": [
      {
         "AcceleratorType": "{{string}}",
         "CapacityReservationConfig": {
            "CapacityReservationPreference": "{{string}}",
            "MlReservationArn": "{{string}}"
         },
         "ContainerStartupHealthCheckTimeoutInSeconds": {{number}},
         "CoreDumpConfig": {
            "DestinationS3Uri": "{{string}}",
            "KmsKeyId": "{{string}}"
         },
         "EnableSSMAccess": {{boolean}},
         "InferenceAmiVersion": "{{string}}",
         "InitialInstanceCount": {{number}},
         "InitialVariantWeight": {{number}},
         "InstancePools": [
            {
               "InstanceType": "{{string}}",
               "ModelNameOverride": "{{string}}",
               "Priority": {{number}}
            }
         ],
         "InstanceType": "{{string}}",
         "ManagedInstanceScaling": {
            "MaxInstanceCount": {{number}},
            "MinInstanceCount": {{number}},
            "ScaleInPolicy": {
               "CooldownInMinutes": {{number}},
               "MaximumStepSize": {{number}},
               "Strategy": "{{string}}"
            },
            "Status": "{{string}}"
         },
         "ModelDataDownloadTimeoutInSeconds": {{number}},
         "ModelName": "{{string}}",
         "RoutingConfig": {
            "RoutingStrategy": "{{string}}"
         },
         "ServerlessConfig": {
            "MaxConcurrency": {{number}},
            "MemorySizeInMB": {{number}},
            "ProvisionedConcurrency": {{number}}
         },
         "VariantInstanceProvisionTimeoutInSeconds": {{number}},
         "VariantName": "{{string}}",
         "VolumeSizeInGB": {{number}}
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_CreateEndpointConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AsyncInferenceConfig](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-AsyncInferenceConfig"></a>
Specifies configuration for how an endpoint performs asynchronous inference. This is a required field in order for your Endpoint to be invoked using [InvokeEndpointAsync](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointAsync.html).
Type: [AsyncInferenceConfig](API_AsyncInferenceConfig.md) object
Required: No

 ** [DataCaptureConfig](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-DataCaptureConfig"></a>
Configuration to control how SageMaker AI captures inference data.
Type: [DataCaptureConfig](API_DataCaptureConfig.md) object
Required: No

 ** [EnableNetworkIsolation](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-EnableNetworkIsolation"></a>
Sets whether all model containers deployed to the endpoint are isolated. If they are, no inbound or outbound network calls can be made to or from the model containers.
Type: Boolean
Required: No

 ** [EndpointConfigName](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-EndpointConfigName"></a>
The name of the endpoint configuration. You specify this name in a [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ExecutionRoleArn](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform actions on your behalf. For more information, see [SageMaker AI Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html).
To be able to pass this role to Amazon SageMaker AI, the caller of this action must have the `iam:PassRole` permission.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [ExplainerConfig](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-ExplainerConfig"></a>
A member of `CreateEndpointConfig` that enables explainers.
Type: [ExplainerConfig](API_ExplainerConfig.md) object
Required: No

 ** [KmsKeyId](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-KmsKeyId"></a>
The Amazon Resource Name (ARN) of a AWS Key Management Service key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
The KmsKeyId can be any of the following formats:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Alias name: `alias/ExampleAlias`
+ Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`
The KMS key policy must grant permission to the IAM role that you specify in your `CreateEndpoint`, `UpdateEndpoint` requests. For more information, refer to the AWS Key Management Service section[ Using Key Policies in AWS KMS ](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)
Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. If any of the models that you specify in the `ProductionVariants` parameter use nitro-based instances with local storage, the `KmsKeyId` parameter does not encrypt instance local storage.
For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes).
For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** [MetricsConfig](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-MetricsConfig"></a>
The configuration parameters for utilization metrics.
Type: [MetricsConfig](API_MetricsConfig.md) object
Required: No

 ** [ProductionVariants](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-ProductionVariants"></a>
An array of `ProductionVariant` objects, one for each model that you want to host at this endpoint.
Type: Array of [ProductionVariant](API_ProductionVariant.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [ShadowProductionVariants](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-ShadowProductionVariants"></a>
An array of `ProductionVariant` objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on `ProductionVariants`. If you use this field, you can only specify one variant for `ProductionVariants` and one variant for `ShadowProductionVariants`.
Type: Array of [ProductionVariant](API_ProductionVariant.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [Tags](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [VpcConfig](#API_CreateEndpointConfig_RequestSyntax) **   <a name="sagemaker-CreateEndpointConfig-request-VpcConfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateEndpointConfig_ResponseSyntax"></a>

```
{
   "EndpointConfigArn": "string"
}
```

## Response Elements
<a name="API_CreateEndpointConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointConfigArn](#API_CreateEndpointConfig_ResponseSyntax) **   <a name="sagemaker-CreateEndpointConfig-response-EndpointConfigArn"></a>
The Amazon Resource Name (ARN) of the endpoint configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint-config/.*`

## Errors
<a name="API_CreateEndpointConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateEndpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateEndpointConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateEndpointConfig)
