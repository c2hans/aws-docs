---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-conformancepack-scope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConformancePack Scope

Defines which resources trigger an evaluation for the AWS Config rules in a managed conformance pack. The scope is a tag key, or a tag key and value, that is applied to every rule in the conformance pack. Specify a scope to constrain which resources trigger an evaluation for the rules. Otherwise, evaluations of the rules are triggered when any resource in your recording group changes in configuration.

## Syntax
<a name="aws-properties-config-conformancepack-scope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-conformancepack-scope-syntax.json"></a>

```json
{
  "[TagKey](#cfn-config-conformancepack-scope-tagkey)" : {{String}},
  "[TagValue](#cfn-config-conformancepack-scope-tagvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-conformancepack-scope-syntax.yaml"></a>

```yaml
  [TagKey](#cfn-config-conformancepack-scope-tagkey): {{String}}
  [TagValue](#cfn-config-conformancepack-scope-tagvalue): {{String}}
```

## Properties
<a name="aws-properties-config-conformancepack-scope-properties"></a>

`TagKey`  <a name="cfn-config-conformancepack-scope-tagkey"></a>
The tag key that applies to only those AWS resources that you want to trigger an evaluation for the rules in the conformance pack.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagValue`  <a name="cfn-config-conformancepack-scope-tagvalue"></a>
The tag value that applies to only those AWS resources that you want to trigger an evaluation for the rules in the conformance pack. If you don't specify a value for `TagValue`, resources that have the tag key `TagKey` trigger an evaluation, regardless of the tag value.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
