---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-identitycenterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource IdentityCenterConfiguration
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration"></a>

The parameters for an IAM Identity Center configuration.

## Syntax
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration-syntax.json"></a>

```
{
  "[EnableIdentityPropagation](#cfn-quicksight-datasource-identitycenterconfiguration-enableidentitypropagation)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration-syntax.yaml"></a>

```
  [EnableIdentityPropagation](#cfn-quicksight-datasource-identitycenterconfiguration-enableidentitypropagation): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-datasource-identitycenterconfiguration-properties"></a>

`EnableIdentityPropagation`  <a name="cfn-quicksight-datasource-identitycenterconfiguration-enableidentitypropagation"></a>
A Boolean option that controls whether Trusted Identity Propagation should be used.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
