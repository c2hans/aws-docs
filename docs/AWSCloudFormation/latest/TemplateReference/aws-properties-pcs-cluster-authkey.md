---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-authkey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster AuthKey
<a name="aws-properties-pcs-cluster-authkey"></a>

The shared Slurm key for authentication, also known as the **cluster secret**.

## Syntax
<a name="aws-properties-pcs-cluster-authkey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-authkey-syntax.json"></a>

```
{
  "[SecretArn](#cfn-pcs-cluster-authkey-secretarn)" : {{String}},
  "[SecretVersion](#cfn-pcs-cluster-authkey-secretversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-authkey-syntax.yaml"></a>

```
  [SecretArn](#cfn-pcs-cluster-authkey-secretarn): {{String}}
  [SecretVersion](#cfn-pcs-cluster-authkey-secretversion): {{String}}
```

## Properties
<a name="aws-properties-pcs-cluster-authkey-properties"></a>

`SecretArn`  <a name="cfn-pcs-cluster-authkey-secretarn"></a>
The Amazon Resource Name (ARN) of the shared Slurm key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretVersion`  <a name="cfn-pcs-cluster-authkey-secretversion"></a>
The version of the shared Slurm key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
