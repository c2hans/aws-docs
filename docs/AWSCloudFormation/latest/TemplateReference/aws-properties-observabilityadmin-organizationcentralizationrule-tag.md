---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule Tag
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tag"></a>

 A key-value pair to filter resources in the organization based on tags associated with the resource. Fore more information about tags, see [What are tags?](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html)

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-observabilityadmin-organizationcentralizationrule-tag-key)" : {{String}},
  "[Value](#cfn-observabilityadmin-organizationcentralizationrule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tag-syntax.yaml"></a>

```
  [Key](#cfn-observabilityadmin-organizationcentralizationrule-tag-key): {{String}}
  [Value](#cfn-observabilityadmin-organizationcentralizationrule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-tag-properties"></a>

`Key`  <a name="cfn-observabilityadmin-organizationcentralizationrule-tag-key"></a>
One part of a key-value pair that makes up a tag associated with the organization's centralization rule resource. A key is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-observabilityadmin-organizationcentralizationrule-tag-value"></a>
One part of a key-value pair that make up a tag associated with the organization's centralization rule resource. A value acts as a descriptor within a tag category (key). The value can be empty or null.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
