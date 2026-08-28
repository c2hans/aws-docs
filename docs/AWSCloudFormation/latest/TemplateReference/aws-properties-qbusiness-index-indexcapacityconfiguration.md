---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-index-indexcapacityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Index IndexCapacityConfiguration
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration"></a>

Provides information about index capacity configuration.

## Syntax
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration-syntax.json"></a>

```
{
  "[Units](#cfn-qbusiness-index-indexcapacityconfiguration-units)" : {{Number}}
}
```

### YAML
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration-syntax.yaml"></a>

```
  [Units](#cfn-qbusiness-index-indexcapacityconfiguration-units): {{Number}}
```

## Properties
<a name="aws-properties-qbusiness-index-indexcapacityconfiguration-properties"></a>

`Units`  <a name="cfn-qbusiness-index-indexcapacityconfiguration-units"></a>
The number of storage units configured for an Amazon Q Business index.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
