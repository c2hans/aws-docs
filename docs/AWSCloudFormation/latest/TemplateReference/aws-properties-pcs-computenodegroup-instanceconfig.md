---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-instanceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup InstanceConfig
<a name="aws-properties-pcs-computenodegroup-instanceconfig"></a>

An EC2 instance configuration AWS PCS uses to launch compute nodes.

## Syntax
<a name="aws-properties-pcs-computenodegroup-instanceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-instanceconfig-syntax.json"></a>

```
{
  "[InstanceType](#cfn-pcs-computenodegroup-instanceconfig-instancetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-instanceconfig-syntax.yaml"></a>

```
  [InstanceType](#cfn-pcs-computenodegroup-instanceconfig-instancetype): {{String}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-instanceconfig-properties"></a>

`InstanceType`  <a name="cfn-pcs-computenodegroup-instanceconfig-instancetype"></a>
The EC2 instance type that AWS PCS can provision in the compute node group.
 Example: `t2.xlarge`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
