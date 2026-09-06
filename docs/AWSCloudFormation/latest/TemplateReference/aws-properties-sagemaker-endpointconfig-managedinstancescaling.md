---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-managedinstancescaling.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ManagedInstanceScaling
<a name="aws-properties-sagemaker-endpointconfig-managedinstancescaling"></a>

<a name="aws-properties-sagemaker-endpointconfig-managedinstancescaling-description"></a>The `ManagedInstanceScaling` property type specifies Property description not available. for an [AWS::SageMaker::EndpointConfig](aws-resource-sagemaker-endpointconfig.md).

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-managedinstancescaling-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-managedinstancescaling-syntax.json"></a>

```
{
  "[MaxInstanceCount](#cfn-sagemaker-endpointconfig-managedinstancescaling-maxinstancecount)" : {{Integer}},
  "[MinInstanceCount](#cfn-sagemaker-endpointconfig-managedinstancescaling-mininstancecount)" : {{Integer}},
  "[ScaleInPolicy](#cfn-sagemaker-endpointconfig-managedinstancescaling-scaleinpolicy)" : {{ScaleInPolicy}},
  "[Status](#cfn-sagemaker-endpointconfig-managedinstancescaling-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-managedinstancescaling-syntax.yaml"></a>

```
  [MaxInstanceCount](#cfn-sagemaker-endpointconfig-managedinstancescaling-maxinstancecount): {{Integer}}
  [MinInstanceCount](#cfn-sagemaker-endpointconfig-managedinstancescaling-mininstancecount): {{Integer}}
  [ScaleInPolicy](#cfn-sagemaker-endpointconfig-managedinstancescaling-scaleinpolicy): {{
    ScaleInPolicy}}
  [Status](#cfn-sagemaker-endpointconfig-managedinstancescaling-status): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-managedinstancescaling-properties"></a>

`MaxInstanceCount`  <a name="cfn-sagemaker-endpointconfig-managedinstancescaling-maxinstancecount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinInstanceCount`  <a name="cfn-sagemaker-endpointconfig-managedinstancescaling-mininstancecount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScaleInPolicy`  <a name="cfn-sagemaker-endpointconfig-managedinstancescaling-scaleinpolicy"></a>
Property description not available.
*Required*: No
*Type*: [ScaleInPolicy](aws-properties-sagemaker-endpointconfig-scaleinpolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Status`  <a name="cfn-sagemaker-endpointconfig-managedinstancescaling-status"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
