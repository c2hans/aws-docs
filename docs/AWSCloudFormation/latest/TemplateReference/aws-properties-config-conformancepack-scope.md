---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-conformancepack-scope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConformancePack Scope

Defines which resources trigger an evaluation for an AWS Config rule. The scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. Specify a scope to constrain which resources trigger an evaluation for a rule. Otherwise, evaluations for the rule are triggered when any resource in your recording group changes in configuration.

## Syntax
<a name="aws-properties-config-conformancepack-scope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-conformancepack-scope-syntax.json"></a>

```
{
  "[TagKey](#cfn-config-conformancepack-scope-tagkey)" : {{String}},
  "[TagValue](#cfn-config-conformancepack-scope-tagvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-conformancepack-scope-syntax.yaml"></a>

```
  [TagKey](#cfn-config-conformancepack-scope-tagkey): {{String}}
  [TagValue](#cfn-config-conformancepack-scope-tagvalue): {{String}}
```

## Properties
<a name="aws-properties-config-conformancepack-scope-properties"></a>

`TagKey`  <a name="cfn-config-conformancepack-scope-tagkey"></a>
The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagValue`  <a name="cfn-config-conformancepack-scope-tagvalue"></a>
The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for `TagValue`, you must also specify a value for `TagKey`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
