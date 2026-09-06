---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-ocsfdatefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 OcsfDateFilter
<a name="aws-properties-securityhub-automationrulev2-ocsfdatefilter"></a>

Enables filtering of security findings based on date and timestamp fields in OCSF.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-ocsfdatefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-ocsfdatefilter-syntax.json"></a>

```
{
  "[FieldName](#cfn-securityhub-automationrulev2-ocsfdatefilter-fieldname)" : {{String}},
  "[Filter](#cfn-securityhub-automationrulev2-ocsfdatefilter-filter)" : {{DateFilter}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-ocsfdatefilter-syntax.yaml"></a>

```
  [FieldName](#cfn-securityhub-automationrulev2-ocsfdatefilter-fieldname): {{String}}
  [Filter](#cfn-securityhub-automationrulev2-ocsfdatefilter-filter): {{
    DateFilter}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-ocsfdatefilter-properties"></a>

`FieldName`  <a name="cfn-securityhub-automationrulev2-ocsfdatefilter-fieldname"></a>
The name of the field.
*Required*: Yes
*Type*: String
*Allowed values*: `finding_info.created_time_dt | finding_info.first_seen_time_dt | finding_info.last_seen_time_dt | finding_info.modified_time_dt`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filter`  <a name="cfn-securityhub-automationrulev2-ocsfdatefilter-filter"></a>
Enables filtering of security findings based on date and timestamp fields in OCSF.
*Required*: Yes
*Type*: [DateFilter](aws-properties-securityhub-automationrulev2-datefilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
