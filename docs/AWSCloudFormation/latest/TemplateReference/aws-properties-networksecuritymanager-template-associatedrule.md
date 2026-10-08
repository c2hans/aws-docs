---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-template-associatedrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Template AssociatedRule
<a name="aws-properties-networksecuritymanager-template-associatedrule"></a>

Specifies an association between a template and a rule. Every rule that you associate with a template must use the same firewall type as the template.

## Syntax
<a name="aws-properties-networksecuritymanager-template-associatedrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-template-associatedrule-syntax.json"></a>

```
{
  "[RuleArn](#cfn-networksecuritymanager-template-associatedrule-rulearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-template-associatedrule-syntax.yaml"></a>

```
  [RuleArn](#cfn-networksecuritymanager-template-associatedrule-rulearn): {{String}}
```

## Properties
<a name="aws-properties-networksecuritymanager-template-associatedrule-properties"></a>

`RuleArn`  <a name="cfn-networksecuritymanager-template-associatedrule-rulearn"></a>
The ARN of the associated rule.
*Required*: Yes
*Type*: String
*Pattern*: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
*Minimum*: `20`
*Maximum*: `1010`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
