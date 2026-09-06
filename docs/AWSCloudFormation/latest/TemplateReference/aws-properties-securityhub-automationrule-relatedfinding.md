---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrule-relatedfinding.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRule RelatedFinding
<a name="aws-properties-securityhub-automationrule-relatedfinding"></a>

 Provides details about a list of findings that the current finding relates to.

## Syntax
<a name="aws-properties-securityhub-automationrule-relatedfinding-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrule-relatedfinding-syntax.json"></a>

```
{
  "[Id](#cfn-securityhub-automationrule-relatedfinding-id)" : {{String}},
  "[ProductArn](#cfn-securityhub-automationrule-relatedfinding-productarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrule-relatedfinding-syntax.yaml"></a>

```
  [Id](#cfn-securityhub-automationrule-relatedfinding-id): {{String}}
  [ProductArn](#cfn-securityhub-automationrule-relatedfinding-productarn): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrule-relatedfinding-properties"></a>

`Id`  <a name="cfn-securityhub-automationrule-relatedfinding-id"></a>
 The product-generated identifier for a related finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductArn`  <a name="cfn-securityhub-automationrule-relatedfinding-productarn"></a>
 The Amazon Resource Name (ARN) for the product that generated a related finding.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-?[a-z]{0,2}):[A-Za-z0-9]{1,63}:[a-z]+-([a-z]{1,10}-)?[a-z]+-[0-9]+:([0-9]{12})?:.+$`
*Minimum*: `12`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
