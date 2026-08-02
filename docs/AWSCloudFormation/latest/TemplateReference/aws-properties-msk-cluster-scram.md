---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-scram.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster Scram
<a name="aws-properties-msk-cluster-scram"></a>

Details for SASL/SCRAM client authentication.

## Syntax
<a name="aws-properties-msk-cluster-scram-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-scram-syntax.json"></a>

```
{
  "[Enabled](#cfn-msk-cluster-scram-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-cluster-scram-syntax.yaml"></a>

```
  [Enabled](#cfn-msk-cluster-scram-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-cluster-scram-properties"></a>

`Enabled`  <a name="cfn-msk-cluster-scram-enabled"></a>
SASL/SCRAM authentication is enabled or not.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
