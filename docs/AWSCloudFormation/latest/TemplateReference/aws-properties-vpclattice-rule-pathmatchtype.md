---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-rule-pathmatchtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Rule PathMatchType
<a name="aws-properties-vpclattice-rule-pathmatchtype"></a>

Describes a path match type. Each rule can include only one of the following types of paths.

## Syntax
<a name="aws-properties-vpclattice-rule-pathmatchtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-rule-pathmatchtype-syntax.json"></a>

```
{
  "[Exact](#cfn-vpclattice-rule-pathmatchtype-exact)" : {{String}},
  "[Prefix](#cfn-vpclattice-rule-pathmatchtype-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-rule-pathmatchtype-syntax.yaml"></a>

```
  [Exact](#cfn-vpclattice-rule-pathmatchtype-exact): {{String}}
  [Prefix](#cfn-vpclattice-rule-pathmatchtype-prefix): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-rule-pathmatchtype-properties"></a>

`Exact`  <a name="cfn-vpclattice-rule-pathmatchtype-exact"></a>
An exact match of the path.
*Required*: No
*Type*: String
*Pattern*: `^\/[a-zA-Z0-9@:%_+.~#?&\/=-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-vpclattice-rule-pathmatchtype-prefix"></a>
A prefix match of the path.
*Required*: No
*Type*: String
*Pattern*: `^\/[a-zA-Z0-9@:%_+.~#?&\/=-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
