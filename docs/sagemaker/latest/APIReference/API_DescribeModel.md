---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModel.html
---

# DescribeModel
<a name="API_DescribeModel"></a>

Describes a model that you created using the `CreateModel` API.

## Request Syntax
<a name="API_DescribeModel_RequestSyntax"></a>

```
{
   "ModelName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ModelName](#API_DescribeModel_RequestSyntax) **   <a name="sagemaker-DescribeModel-request-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

## Response Syntax
<a name="API_DescribeModel_ResponseSyntax"></a>

```
{
   "Containers": [
      {
         "AdditionalModelDataSources": [
            {
               "ChannelName": "string",
               "S3DataSource": {
                  "CompressionType": "string",
                  "ETag": "string",
                  "HubAccessConfig": {
                     "HubContentArn": "string"
                  },
                  "ManifestEtag": "string",
                  "ManifestS3Uri": "string",
                  "ModelAccessConfig": {
                     "AcceptEula": boolean
                  },
                  "S3DataType": "string",
                  "S3Uri": "string"
               }
            }
         ],
         "ContainerHostname": "string",
         "ContainerMetricsConfig": {
            "MetricsEndpoints": [
               {
                  "MetricPublishFrequencyInSeconds": number,
                  "MetricsEndpointPath": "string"
               }
            ]
         },
         "Environment": {
            "string" : "string"
         },
         "Image": "string",
         "ImageConfig": {
            "RepositoryAccessMode": "string",
            "RepositoryAuthConfig": {
               "RepositoryCredentialsProviderArn": "string"
            }
         },
         "InferenceSpecificationName": "string",
         "Mode": "string",
         "ModelDataSource": {
            "S3DataSource": {
               "CompressionType": "string",
               "ETag": "string",
               "HubAccessConfig": {
                  "HubContentArn": "string"
               },
               "ManifestEtag": "string",
               "ManifestS3Uri": "string",
               "ModelAccessConfig": {
                  "AcceptEula": boolean
               },
               "S3DataType": "string",
               "S3Uri": "string"
            }
         },
         "ModelDataUrl": "string",
         "ModelPackageName": "string",
         "MultiModelConfig": {
            "ModelCacheSetting": "string"
         }
      }
   ],
   "DeploymentRecommendation": {
      "RealTimeInferenceRecommendations": [
         {
            "Environment": {
               "string" : "string"
            },
            "InstanceType": "string",
            "RecommendationId": "string"
         }
      ],
      "RecommendationStatus": "string"
   },
   "EnableNetworkIsolation": boolean,
   "ExecutionRoleArn": "string",
   "InferenceExecutionConfig": {
      "Mode": "string"
   },
   "ModelArn": "string",
   "ModelName": "string",
   "PrimaryContainer": {
      "AdditionalModelDataSources": [
         {
            "ChannelName": "string",
            "S3DataSource": {
               "CompressionType": "string",
               "ETag": "string",
               "HubAccessConfig": {
                  "HubContentArn": "string"
               },
               "ManifestEtag": "string",
               "ManifestS3Uri": "string",
               "ModelAccessConfig": {
                  "AcceptEula": boolean
               },
               "S3DataType": "string",
               "S3Uri": "string"
            }
         }
      ],
      "ContainerHostname": "string",
      "ContainerMetricsConfig": {
         "MetricsEndpoints": [
            {
               "MetricPublishFrequencyInSeconds": number,
               "MetricsEndpointPath": "string"
            }
         ]
      },
      "Environment": {
         "string" : "string"
      },
      "Image": "string",
      "ImageConfig": {
         "RepositoryAccessMode": "string",
         "RepositoryAuthConfig": {
            "RepositoryCredentialsProviderArn": "string"
         }
      },
      "InferenceSpecificationName": "string",
      "Mode": "string",
      "ModelDataSource": {
         "S3DataSource": {
            "CompressionType": "string",
            "ETag": "string",
            "HubAccessConfig": {
               "HubContentArn": "string"
            },
            "ManifestEtag": "string",
            "ManifestS3Uri": "string",
            "ModelAccessConfig": {
               "AcceptEula": boolean
            },
            "S3DataType": "string",
            "S3Uri": "string"
         }
      },
      "ModelDataUrl": "string",
      "ModelPackageName": "string",
      "MultiModelConfig": {
         "ModelCacheSetting": "string"
      }
   },
   "VpcConfig": {
      "SecurityGroupIds": [ "string" ],
      "Subnets": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Containers](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-Containers"></a>
The containers in the inference pipeline.
Type: Array of [ContainerDefinition](API_ContainerDefinition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 15 items.

 ** [DeploymentRecommendation](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-DeploymentRecommendation"></a>
A set of recommended deployment configurations for the model.
Type: [DeploymentRecommendation](API_DeploymentRecommendation.md) object

 ** [EnableNetworkIsolation](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-EnableNetworkIsolation"></a>
If `True`, no inbound or outbound network calls can be made to or from the model container.
Type: Boolean

 ** [ExecutionRoleArn](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you specified for the model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [InferenceExecutionConfig](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-InferenceExecutionConfig"></a>
Specifies details of how containers in a multi-container endpoint are called.
Type: [InferenceExecutionConfig](API_InferenceExecutionConfig.md) object

 ** [ModelArn](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-ModelArn"></a>
The Amazon Resource Name (ARN) of the model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model/.*`

 ** [ModelName](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-ModelName"></a>
Name of the SageMaker model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`

 ** [PrimaryContainer](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-PrimaryContainer"></a>
The location of the primary inference code, associated artifacts, and custom environment map that the inference code uses when it is deployed in production.
Type: [ContainerDefinition](API_ContainerDefinition.md) object

 ** [VpcConfig](#API_DescribeModel_ResponseSyntax) **   <a name="sagemaker-DescribeModel-response-VpcConfig"></a>
A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that this model has access to. For more information, see [Protect Endpoints by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html)
Type: [VpcConfig](API_VpcConfig.md) object

## Errors
<a name="API_DescribeModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeModel)
