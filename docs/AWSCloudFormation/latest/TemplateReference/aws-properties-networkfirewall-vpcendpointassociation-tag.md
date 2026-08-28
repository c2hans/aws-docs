---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-vpcendpointassociation-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::VpcEndpointAssociation Tag
<a name="aws-properties-networkfirewall-vpcendpointassociation-tag"></a>

A key:value pair associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

## Syntax
<a name="aws-properties-networkfirewall-vpcendpointassociation-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-vpcendpointassociation-tag-syntax.json"></a>

```
{
  "[Key](#cfn-networkfirewall-vpcendpointassociation-tag-key)" : {{String}},
  "[Value](#cfn-networkfirewall-vpcendpointassociation-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-vpcendpointassociation-tag-syntax.yaml"></a>

```
  [Key](#cfn-networkfirewall-vpcendpointassociation-tag-key): {{String}}
  [Value](#cfn-networkfirewall-vpcendpointassociation-tag-value): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-vpcendpointassociation-tag-properties"></a>

`Key`  <a name="cfn-networkfirewall-vpcendpointassociation-tag-key"></a>
The part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networkfirewall-vpcendpointassociation-tag-value"></a>
The part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
