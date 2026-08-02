---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clustercapacityrequirements.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterCapacityRequirements
<a name="aws-properties-sagemaker-cluster-clustercapacityrequirements"></a>

Defines the instance capacity requirements for an instance group, including configurations for both Spot and On-Demand capacity types.

## Syntax
<a name="aws-properties-sagemaker-cluster-clustercapacityrequirements-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clustercapacityrequirements-syntax.json"></a>

```
{
  "[OnDemand](#cfn-sagemaker-cluster-clustercapacityrequirements-ondemand)" : {{Json}},
  "[Spot](#cfn-sagemaker-cluster-clustercapacityrequirements-spot)" : {{Json}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clustercapacityrequirements-syntax.yaml"></a>

```
  [OnDemand](#cfn-sagemaker-cluster-clustercapacityrequirements-ondemand): {{Json}}
  [Spot](#cfn-sagemaker-cluster-clustercapacityrequirements-spot): {{Json}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clustercapacityrequirements-properties"></a>

`OnDemand`  <a name="cfn-sagemaker-cluster-clustercapacityrequirements-ondemand"></a>
Configuration options specific to On-Demand instances.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Spot`  <a name="cfn-sagemaker-cluster-clustercapacityrequirements-spot"></a>
Configuration options specific to Spot instances.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
