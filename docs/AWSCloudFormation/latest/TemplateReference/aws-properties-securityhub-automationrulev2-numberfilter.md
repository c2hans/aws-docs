---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-numberfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 NumberFilter
<a name="aws-properties-securityhub-automationrulev2-numberfilter"></a>

A number filter for querying findings.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-numberfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-numberfilter-syntax.json"></a>

```
{
  "[Eq](#cfn-securityhub-automationrulev2-numberfilter-eq)" : {{Number}},
  "[Gte](#cfn-securityhub-automationrulev2-numberfilter-gte)" : {{Number}},
  "[Lte](#cfn-securityhub-automationrulev2-numberfilter-lte)" : {{Number}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-numberfilter-syntax.yaml"></a>

```
  [Eq](#cfn-securityhub-automationrulev2-numberfilter-eq): {{Number}}
  [Gte](#cfn-securityhub-automationrulev2-numberfilter-gte): {{Number}}
  [Lte](#cfn-securityhub-automationrulev2-numberfilter-lte): {{Number}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-numberfilter-properties"></a>

`Eq`  <a name="cfn-securityhub-automationrulev2-numberfilter-eq"></a>
The equal-to condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gte`  <a name="cfn-securityhub-automationrulev2-numberfilter-gte"></a>
The greater-than-equal condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lte`  <a name="cfn-securityhub-automationrulev2-numberfilter-lte"></a>
The less-than-equal condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
