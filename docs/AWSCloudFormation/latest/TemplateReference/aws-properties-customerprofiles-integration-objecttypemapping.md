---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-objecttypemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration ObjectTypeMapping
<a name="aws-properties-customerprofiles-integration-objecttypemapping"></a>

A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an `ObjectTypeName` (template) used to ingest the event.

## Syntax
<a name="aws-properties-customerprofiles-integration-objecttypemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-objecttypemapping-syntax.json"></a>

```
{
  "[Key](#cfn-customerprofiles-integration-objecttypemapping-key)" : {{String}},
  "[Value](#cfn-customerprofiles-integration-objecttypemapping-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-objecttypemapping-syntax.yaml"></a>

```
  [Key](#cfn-customerprofiles-integration-objecttypemapping-key): {{String}}
  [Value](#cfn-customerprofiles-integration-objecttypemapping-value): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-objecttypemapping-properties"></a>

`Key`  <a name="cfn-customerprofiles-integration-objecttypemapping-key"></a>
The key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-integration-objecttypemapping-value"></a>
The value.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
