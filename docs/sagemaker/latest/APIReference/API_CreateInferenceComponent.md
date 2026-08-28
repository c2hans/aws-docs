---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceComponent.html
---

# CreateInferenceComponent
<a name="API_CreateInferenceComponent"></a>

Creates an inference component, which is a SageMaker AI hosting object that you can use to deploy a model to an endpoint. In the inference component settings, you specify the model, the endpoint, and how the model utilizes the resources that the endpoint hosts. You can optimize resource utilization by tailoring how the required CPU cores, accelerators, and memory are allocated. You can deploy multiple inference components to an endpoint, where each inference component contains one model and the resource utilization needs for that individual model. After you deploy an inference component, you can directly invoke the associated model when you use the InvokeEndpoint API action.

## Request Syntax
<a name="API_CreateInferenceComponent_RequestSyntax"></a>

```
{
   "EndpointName": "{{string}}",
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
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VariantName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateInferenceComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointName](#API_CreateInferenceComponent_RequestSyntax) **   <a name="sagemaker-CreateInferenceComponent-request-EndpointName"></a>
The name of an existing endpoint where you host the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [InferenceComponentName](#API_CreateInferenceComponent_RequestSyntax) **   <a name="sagemaker-CreateInferenceComponent-request-InferenceComponentName"></a>
A unique name to assign to the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

 ** [RuntimeConfig](#API_CreateInferenceComponent_RequestSyntax) **   <a name="sagemaker-CreateInferenceComponent-request-RuntimeConfig"></a>
Runtime settings for a model that is deployed with an inference component.
Type: [InferenceComponentRuntimeConfig](API_InferenceComponentRuntimeConfig.md) object
Required: No

 ** [Specification](#API_CreateInferenceComponent_RequestSyntax) **   <a name="sagemaker-CreateInferenceComponent-request-Specification"></a>
Details about the resources to deploy with this inference component, including the model, container, and compute resources.
Type: [InferenceComponentSpecification](API_InferenceComponentSpecification.md) object
Required: No

 ** [Specifications](#API_CreateInferenceComponent_RequestSyntax) **   <a name="sagemaker-CreateInferenceComponent-request-Specifications"></a>
A list of specification objects for the inference component, one per instance type. Use this parameter when you want to deploy a different model or resource configuration for the inference component on each instance type. You can use either this parameter or the singular `Specification` parameter, but not both.
Type: Array of [InferenceComponentSpecification](API_InferenceComponentSpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [Tags](#API_CreateInferenceComponent_RequestSyntax) **   <a name="sagemaker-CreateInferenceComponent-request-Tags"></a>
A list of key-value pairs associated with the model. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [VariantName](#API_CreateInferenceComponent_RequestSyntax) **   <a name="sagemaker-CreateInferenceComponent-request-VariantName"></a>
The name of an existing production variant where you host the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## Response Syntax
<a name="API_CreateInferenceComponent_ResponseSyntax"></a>

```
{
   "InferenceComponentArn": "string"
}
```

## Response Elements
<a name="API_CreateInferenceComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceComponentArn](#API_CreateInferenceComponent_ResponseSyntax) **   <a name="sagemaker-CreateInferenceComponent-response-InferenceComponentArn"></a>
The Amazon Resource Name (ARN) of the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_CreateInferenceComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateInferenceComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateInferenceComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateInferenceComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
