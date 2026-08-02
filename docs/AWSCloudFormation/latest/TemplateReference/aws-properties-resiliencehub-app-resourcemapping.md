---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehub-app-resourcemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::App ResourceMapping
<a name="aws-properties-resiliencehub-app-resourcemapping"></a>

Defines a resource mapping.

## Syntax
<a name="aws-properties-resiliencehub-app-resourcemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehub-app-resourcemapping-syntax.json"></a>

```
{
  "[EksSourceName](#cfn-resiliencehub-app-resourcemapping-ekssourcename)" : {{String}},
  "[LogicalStackName](#cfn-resiliencehub-app-resourcemapping-logicalstackname)" : {{String}},
  "[MappingType](#cfn-resiliencehub-app-resourcemapping-mappingtype)" : {{String}},
  "[PhysicalResourceId](#cfn-resiliencehub-app-resourcemapping-physicalresourceid)" : {{PhysicalResourceId}},
  "[ResourceName](#cfn-resiliencehub-app-resourcemapping-resourcename)" : {{String}},
  "[TerraformSourceName](#cfn-resiliencehub-app-resourcemapping-terraformsourcename)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehub-app-resourcemapping-syntax.yaml"></a>

```
  [EksSourceName](#cfn-resiliencehub-app-resourcemapping-ekssourcename): {{String}}
  [LogicalStackName](#cfn-resiliencehub-app-resourcemapping-logicalstackname): {{String}}
  [MappingType](#cfn-resiliencehub-app-resourcemapping-mappingtype): {{String}}
  [PhysicalResourceId](#cfn-resiliencehub-app-resourcemapping-physicalresourceid): {{
    PhysicalResourceId}}
  [ResourceName](#cfn-resiliencehub-app-resourcemapping-resourcename): {{String}}
  [TerraformSourceName](#cfn-resiliencehub-app-resourcemapping-terraformsourcename): {{String}}
```

## Properties
<a name="aws-properties-resiliencehub-app-resourcemapping-properties"></a>

`EksSourceName`  <a name="cfn-resiliencehub-app-resourcemapping-ekssourcename"></a>
Name of the Amazon Elastic Kubernetes Service cluster and namespace that this resource is mapped to when the `mappingType` is `EKS`.
This parameter accepts values in "eks-cluster/namespace" format.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalStackName`  <a name="cfn-resiliencehub-app-resourcemapping-logicalstackname"></a>
Name of the CloudFormation stack this resource is mapped to when the `mappingType` is `CfnStack`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MappingType`  <a name="cfn-resiliencehub-app-resourcemapping-mappingtype"></a>
Specifies the type of resource mapping.
*Required*: Yes
*Type*: String
*Pattern*: `CfnStack|Resource|Terraform|EKS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhysicalResourceId`  <a name="cfn-resiliencehub-app-resourcemapping-physicalresourceid"></a>
Identifier of the physical resource.
*Required*: Yes
*Type*: [PhysicalResourceId](aws-properties-resiliencehub-app-physicalresourceid.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceName`  <a name="cfn-resiliencehub-app-resourcemapping-resourcename"></a>
Name of the resource that this resource is mapped to when the `mappingType` is `Resource`.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TerraformSourceName`  <a name="cfn-resiliencehub-app-resourcemapping-terraformsourcename"></a>
Name of the Terraform source that this resource is mapped to when the `mappingType` is `Terraform`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
