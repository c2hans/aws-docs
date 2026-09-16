---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html
---

# CreateModel
<a name="API_CreateModel"></a>

Creates a model in SageMaker. In the request, you name the model and describe a primary container. For the primary container, you specify the Docker image that contains inference code, artifacts (from prior training), and a custom environment map that the inference code uses when you deploy the model for predictions.

Use this API to create a model if you want to use SageMaker hosting services or run a batch transform job.

To host your model, you create an endpoint configuration with the `CreateEndpointConfig` API, and then create an endpoint with the `CreateEndpoint` API. SageMaker then deploys all of the containers that you defined for the model in the hosting environment.

To run a batch transform using your model, you start a job with the `CreateTransformJob` API. SageMaker uses your model and your dataset to get inferences which are then saved to a specified S3 location.

In the request, you also provide an IAM role that SageMaker can assume to access model artifacts and docker image for deployment on ML compute hosting instances or for batch transform jobs. In addition, you also use the IAM role to manage permissions the inference code needs. For example, if the inference code access any other AWS resources, you grant necessary permissions via this role.

## Request Syntax
<a name="API_CreateModel_RequestSyntax"></a>

```
{
   "Containers": [
      {
         "AdditionalModelDataSources": [
            {
               "ChannelName": "{{string}}",
               "S3DataSource": {
                  "CompressionType": "{{string}}",
                  "ETag": "{{string}}",
                  "HubAccessConfig": {
                     "HubContentArn": "{{string}}"
                  },
                  "ManifestEtag": "{{string}}",
                  "ManifestS3Uri": "{{string}}",
                  "ModelAccessConfig": {
                     "AcceptEula": {{boolean}}
                  },
                  "S3DataType": "{{string}}",
                  "S3Uri": "{{string}}"
               }
            }
         ],
         "ContainerHostname": "{{string}}",
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
         "Image": "{{string}}",
         "ImageConfig": {
            "RepositoryAccessMode": "{{string}}",
            "RepositoryAuthConfig": {
               "RepositoryCredentialsProviderArn": "{{string}}"
            }
         },
         "InferenceSpecificationName": "{{string}}",
         "Mode": "{{string}}",
         "ModelDataSource": {
            "S3DataSource": {
               "CompressionType": "{{string}}",
               "ETag": "{{string}}",
               "HubAccessConfig": {
                  "HubContentArn": "{{string}}"
               },
               "ManifestEtag": "{{string}}",
               "ManifestS3Uri": "{{string}}",
               "ModelAccessConfig": {
                  "AcceptEula": {{boolean}}
               },
               "S3DataType": "{{string}}",
               "S3Uri": "{{string}}"
            }
         },
         "ModelDataUrl": "{{string}}",
         "ModelPackageName": "{{string}}",
         "MultiModelConfig": {
            "ModelCacheSetting": "{{string}}"
         }
      }
   ],
   "EnableNetworkIsolation": {{boolean}},
   "ExecutionRoleArn": "{{string}}",
   "InferenceExecutionConfig": {
      "Mode": "{{string}}"
   },
   "ModelName": "{{string}}",
   "PrimaryContainer": {
      "AdditionalModelDataSources": [
         {
            "ChannelName": "{{string}}",
            "S3DataSource": {
               "CompressionType": "{{string}}",
               "ETag": "{{string}}",
               "HubAccessConfig": {
                  "HubContentArn": "{{string}}"
               },
               "ManifestEtag": "{{string}}",
               "ManifestS3Uri": "{{string}}",
               "ModelAccessConfig": {
                  "AcceptEula": {{boolean}}
               },
               "S3DataType": "{{string}}",
               "S3Uri": "{{string}}"
            }
         }
      ],
      "ContainerHostname": "{{string}}",
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
      "Image": "{{string}}",
      "ImageConfig": {
         "RepositoryAccessMode": "{{string}}",
         "RepositoryAuthConfig": {
            "RepositoryCredentialsProviderArn": "{{string}}"
         }
      },
      "InferenceSpecificationName": "{{string}}",
      "Mode": "{{string}}",
      "ModelDataSource": {
         "S3DataSource": {
            "CompressionType": "{{string}}",
            "ETag": "{{string}}",
            "HubAccessConfig": {
               "HubContentArn": "{{string}}"
            },
            "ManifestEtag": "{{string}}",
            "ManifestS3Uri": "{{string}}",
            "ModelAccessConfig": {
               "AcceptEula": {{boolean}}
            },
            "S3DataType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      },
      "ModelDataUrl": "{{string}}",
      "ModelPackageName": "{{string}}",
      "MultiModelConfig": {
         "ModelCacheSetting": "{{string}}"
      }
   },
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
<a name="API_CreateModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Containers](#API_CreateModel_RequestSyntax) **   <a name="sagemaker-CreateModel-request-Containers"></a>
Specifies the containers in the inference pipeline.
Type: Array of [ContainerDefinition](API_ContainerDefinition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Required: No

 ** [EnableNetworkIsolation](#API_CreateModel_RequestSyntax) **   <a name="sagemaker-CreateModel-request-EnableNetworkIsolation"></a>
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
Type: Boolean
Required: No

 ** [ExecutionRoleArn](#API_CreateModel_RequestSyntax) **   <a name="sagemaker-CreateModel-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that SageMaker can assume to access model artifacts and docker image for deployment on ML compute instances or for batch transform jobs. Deploying on ML compute instances is part of model hosting. For more information, see [SageMaker Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html).
To be able to pass this role to SageMaker, the caller of this API must have the `iam:PassRole` permission.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [InferenceExecutionConfig](#API_CreateModel_RequestSyntax) **   <a name="sagemaker-CreateModel-request-InferenceExecutionConfig"></a>
Specifies details of how containers in a multi-container endpoint are called.
Type: [InferenceExecutionConfig](API_InferenceExecutionConfig.md) object
Required: No

 ** [ModelName](#API_CreateModel_RequestSyntax) **   <a name="sagemaker-CreateModel-request-ModelName"></a>
The name of the new model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

 ** [PrimaryContainer](#API_CreateModel_RequestSyntax) **   <a name="sagemaker-CreateModel-request-PrimaryContainer"></a>
The location of the primary docker image containing inference code, associated artifacts, and custom environment map that the inference code uses when the model is deployed for predictions.
Type: [ContainerDefinition](API_ContainerDefinition.md) object
Required: No

 ** [Tags](#API_CreateModel_RequestSyntax) **   <a name="sagemaker-CreateModel-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [VpcConfig](#API_CreateModel_RequestSyntax) **   <a name="sagemaker-CreateModel-request-VpcConfig"></a>
A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want your model to connect to. Control access to and from your model container by configuring the VPC. `VpcConfig` is used in hosting services and in batch transform. For more information, see [Protect Endpoints by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html) and [Protect Data in Batch Transform Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-vpc.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateModel_ResponseSyntax"></a>

```
{
   "ModelArn": "string"
}
```

## Response Elements
<a name="API_CreateModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelArn](#API_CreateModel_ResponseSyntax) **   <a name="sagemaker-CreateModel-response-ModelArn"></a>
The ARN of the model created in SageMaker.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model/.*`

## Errors
<a name="API_CreateModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateModel)
