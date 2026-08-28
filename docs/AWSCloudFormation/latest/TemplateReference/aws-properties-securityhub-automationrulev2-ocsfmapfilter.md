---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-ocsfmapfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 OcsfMapFilter
<a name="aws-properties-securityhub-automationrulev2-ocsfmapfilter"></a>

Enables filtering of security findings based on map field values in OCSF.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-ocsfmapfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-ocsfmapfilter-syntax.json"></a>

```
{
  "[FieldName](#cfn-securityhub-automationrulev2-ocsfmapfilter-fieldname)" : {{String}},
  "[Filter](#cfn-securityhub-automationrulev2-ocsfmapfilter-filter)" : {{MapFilter}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-ocsfmapfilter-syntax.yaml"></a>

```
  [FieldName](#cfn-securityhub-automationrulev2-ocsfmapfilter-fieldname): {{String}}
  [Filter](#cfn-securityhub-automationrulev2-ocsfmapfilter-filter): {{
    MapFilter}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-ocsfmapfilter-properties"></a>

`FieldName`  <a name="cfn-securityhub-automationrulev2-ocsfmapfilter-fieldname"></a>
The name of the field.
*Required*: Yes
*Type*: String
*Allowed values*: `resources.tags`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filter`  <a name="cfn-securityhub-automationrulev2-ocsfmapfilter-filter"></a>
Enables filtering of security findings based on map field values in OCSF.
*Required*: Yes
*Type*: [MapFilter](aws-properties-securityhub-automationrulev2-mapfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
