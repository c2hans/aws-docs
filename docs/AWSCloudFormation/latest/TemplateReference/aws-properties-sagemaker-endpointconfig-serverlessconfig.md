---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-serverlessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ServerlessConfig
<a name="aws-properties-sagemaker-endpointconfig-serverlessconfig"></a>

Specifies the serverless configuration for an endpoint variant.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-serverlessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-serverlessconfig-syntax.json"></a>

```
{
  "[MaxConcurrency](#cfn-sagemaker-endpointconfig-serverlessconfig-maxconcurrency)" : {{Integer}},
  "[MemorySizeInMB](#cfn-sagemaker-endpointconfig-serverlessconfig-memorysizeinmb)" : {{Integer}},
  "[ProvisionedConcurrency](#cfn-sagemaker-endpointconfig-serverlessconfig-provisionedconcurrency)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-serverlessconfig-syntax.yaml"></a>

```
  [MaxConcurrency](#cfn-sagemaker-endpointconfig-serverlessconfig-maxconcurrency): {{Integer}}
  [MemorySizeInMB](#cfn-sagemaker-endpointconfig-serverlessconfig-memorysizeinmb): {{Integer}}
  [ProvisionedConcurrency](#cfn-sagemaker-endpointconfig-serverlessconfig-provisionedconcurrency): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-serverlessconfig-properties"></a>

`MaxConcurrency`  <a name="cfn-sagemaker-endpointconfig-serverlessconfig-maxconcurrency"></a>
The maximum number of concurrent invocations your serverless endpoint can process.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemorySizeInMB`  <a name="cfn-sagemaker-endpointconfig-serverlessconfig-memorysizeinmb"></a>
The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `6144`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProvisionedConcurrency`  <a name="cfn-sagemaker-endpointconfig-serverlessconfig-provisionedconcurrency"></a>
The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency`.
This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
