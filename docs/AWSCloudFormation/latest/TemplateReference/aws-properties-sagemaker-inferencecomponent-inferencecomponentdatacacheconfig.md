---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentDataCacheConfig
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig"></a>

Settings that affect how the inference component caches data.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig-syntax.json"></a>

```
{
  "[EnableCaching](#cfn-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig-enablecaching)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig-syntax.yaml"></a>

```
  [EnableCaching](#cfn-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig-enablecaching): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig-properties"></a>

`EnableCaching`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig-enablecaching"></a>
Sets whether the endpoint that hosts the inference component caches the model artifacts and container image.
With caching enabled, the endpoint caches this data in each instance that it provisions for the inference component. That way, the inference component deploys faster during the auto scaling process. If caching isn't enabled, the inference component takes longer to deploy because of the time it spends downloading the data.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
