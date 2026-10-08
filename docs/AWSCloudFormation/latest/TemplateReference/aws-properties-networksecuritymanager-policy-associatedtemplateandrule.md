---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-policy-associatedtemplateandrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Policy AssociatedTemplateAndRule
<a name="aws-properties-networksecuritymanager-policy-associatedtemplateandrule"></a>

Associates a single template or a single rule with a policy. Specify exactly one of `TemplateArn` or `RuleArn`.

## Syntax
<a name="aws-properties-networksecuritymanager-policy-associatedtemplateandrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-policy-associatedtemplateandrule-syntax.json"></a>

```
{
  "[RuleArn](#cfn-networksecuritymanager-policy-associatedtemplateandrule-rulearn)" : {{String}},
  "[TemplateArn](#cfn-networksecuritymanager-policy-associatedtemplateandrule-templatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-policy-associatedtemplateandrule-syntax.yaml"></a>

```
  [RuleArn](#cfn-networksecuritymanager-policy-associatedtemplateandrule-rulearn): {{String}}
  [TemplateArn](#cfn-networksecuritymanager-policy-associatedtemplateandrule-templatearn): {{String}}
```

## Properties
<a name="aws-properties-networksecuritymanager-policy-associatedtemplateandrule-properties"></a>

`RuleArn`  <a name="cfn-networksecuritymanager-policy-associatedtemplateandrule-rulearn"></a>
The Amazon Resource Name (ARN) of the rule to associate with the policy. Don't specify this property if you specify `TemplateArn`.
*Required*: No
*Type*: String
*Pattern*: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
*Minimum*: `20`
*Maximum*: `1010`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateArn`  <a name="cfn-networksecuritymanager-policy-associatedtemplateandrule-templatearn"></a>
The Amazon Resource Name (ARN) of the template to associate with the policy. Don't specify this property if you specify `RuleArn`.
*Required*: No
*Type*: String
*Pattern*: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
*Minimum*: `20`
*Maximum*: `1010`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
