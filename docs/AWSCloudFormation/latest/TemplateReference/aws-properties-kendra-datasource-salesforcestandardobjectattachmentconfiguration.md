---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource SalesforceStandardObjectAttachmentConfiguration
<a name="aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration"></a>

Provides the configuration information for processing attachments to Salesforce standard objects.

## Syntax
<a name="aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration-syntax.json"></a>

```
{
  "[DocumentTitleFieldName](#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-documenttitlefieldname)" : {{String}},
  "[FieldMappings](#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-fieldmappings)" : {{[ DataSourceToIndexFieldMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration-syntax.yaml"></a>

```
  [DocumentTitleFieldName](#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-documenttitlefieldname): {{String}}
  [FieldMappings](#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-fieldmappings): {{
    - DataSourceToIndexFieldMapping}}
```

## Properties
<a name="aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration-properties"></a>

`DocumentTitleFieldName`  <a name="cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-documenttitlefieldname"></a>
The name of the field used for the document title.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldMappings`  <a name="cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-fieldmappings"></a>
One or more objects that map fields in attachments to Amazon Kendra index fields.
*Required*: No
*Type*: Array of [DataSourceToIndexFieldMapping](aws-properties-kendra-datasource-datasourcetoindexfieldmapping.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
