---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-ocsfnumberfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 OcsfNumberFilter
<a name="aws-properties-securityhub-automationrulev2-ocsfnumberfilter"></a>

Enables filtering of security findings based on numerical field values in OCSF.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-ocsfnumberfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-ocsfnumberfilter-syntax.json"></a>

```
{
  "[FieldName](#cfn-securityhub-automationrulev2-ocsfnumberfilter-fieldname)" : {{String}},
  "[Filter](#cfn-securityhub-automationrulev2-ocsfnumberfilter-filter)" : {{NumberFilter}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-ocsfnumberfilter-syntax.yaml"></a>

```
  [FieldName](#cfn-securityhub-automationrulev2-ocsfnumberfilter-fieldname): {{String}}
  [Filter](#cfn-securityhub-automationrulev2-ocsfnumberfilter-filter): {{
    NumberFilter}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-ocsfnumberfilter-properties"></a>

`FieldName`  <a name="cfn-securityhub-automationrulev2-ocsfnumberfilter-fieldname"></a>
The name of the field.
*Required*: Yes
*Type*: String
*Allowed values*: `activity_id | compliance.status_id | confidence_score | finding_info.related_events_count | vendor_attributes.severity_id`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filter`  <a name="cfn-securityhub-automationrulev2-ocsfnumberfilter-filter"></a>
Enables filtering of security findings based on numerical field values in OCSF.
*Required*: Yes
*Type*: [NumberFilter](aws-properties-securityhub-automationrulev2-numberfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
