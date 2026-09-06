---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-ocsfstringfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 OcsfStringFilter
<a name="aws-properties-securityhub-automationrulev2-ocsfstringfilter"></a>

Enables filtering of security findings based on string field values in OCSF.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-ocsfstringfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-ocsfstringfilter-syntax.json"></a>

```
{
  "[FieldName](#cfn-securityhub-automationrulev2-ocsfstringfilter-fieldname)" : {{String}},
  "[Filter](#cfn-securityhub-automationrulev2-ocsfstringfilter-filter)" : {{StringFilter}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-ocsfstringfilter-syntax.yaml"></a>

```
  [FieldName](#cfn-securityhub-automationrulev2-ocsfstringfilter-fieldname): {{String}}
  [Filter](#cfn-securityhub-automationrulev2-ocsfstringfilter-filter): {{
    StringFilter}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-ocsfstringfilter-properties"></a>

`FieldName`  <a name="cfn-securityhub-automationrulev2-ocsfstringfilter-fieldname"></a>
The name of the field.
*Required*: Yes
*Type*: String
*Allowed values*: `activity_name | cloud.account.name | cloud.account.uid | cloud.provider | cloud.region | compliance.assessments.category | compliance.assessments.name | compliance.control | compliance.status | compliance.standards | finding_info.desc | finding_info.src_url | finding_info.title | finding_info.types | finding_info.uid | finding_info.related_events.uid | finding_info.related_events.product.uid | finding_info.related_events.title | metadata.product.feature.uid | metadata.product.name | metadata.product.uid | metadata.product.vendor_name | remediation.desc | remediation.references | resources.cloud_partition | resources.name | resources.region | resources.type | resources.uid | vulnerabilities.fix_coverage | class_name | vendor_attributes.severity`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filter`  <a name="cfn-securityhub-automationrulev2-ocsfstringfilter-filter"></a>
Enables filtering of security findings based on string field values in OCSF.
*Required*: Yes
*Type*: [StringFilter](aws-properties-securityhub-automationrulev2-stringfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
