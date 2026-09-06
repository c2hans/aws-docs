---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-queue-computenodegroupconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Queue ComputeNodeGroupConfiguration
<a name="aws-properties-pcs-queue-computenodegroupconfiguration"></a>

The compute node group configuration for a queue.

## Syntax
<a name="aws-properties-pcs-queue-computenodegroupconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-queue-computenodegroupconfiguration-syntax.json"></a>

```
{
  "[ComputeNodeGroupId](#cfn-pcs-queue-computenodegroupconfiguration-computenodegroupid)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-queue-computenodegroupconfiguration-syntax.yaml"></a>

```
  [ComputeNodeGroupId](#cfn-pcs-queue-computenodegroupconfiguration-computenodegroupid): {{String}}
```

## Properties
<a name="aws-properties-pcs-queue-computenodegroupconfiguration-properties"></a>

`ComputeNodeGroupId`  <a name="cfn-pcs-queue-computenodegroupconfiguration-computenodegroupid"></a>
The compute node group ID for the compute node group configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
