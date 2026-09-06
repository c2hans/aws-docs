---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-piientitiesconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject PIIEntitiesConfiguration
<a name="aws-properties-bedrock-dataautomationproject-piientitiesconfiguration"></a>

Configuration for detecting and redacting Personally Identifiable Information (PII) entities. Specify which PII entity types to detect and the redaction mask mode. If not provided, defaults to ALL entity types with ENTITY\_TYPE redaction mask mode.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-piientitiesconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-piientitiesconfiguration-syntax.json"></a>

```
{
  "[PiiEntityTypes](#cfn-bedrock-dataautomationproject-piientitiesconfiguration-piientitytypes)" : {{[ String, ... ]}},
  "[RedactionMaskMode](#cfn-bedrock-dataautomationproject-piientitiesconfiguration-redactionmaskmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-piientitiesconfiguration-syntax.yaml"></a>

```
  [PiiEntityTypes](#cfn-bedrock-dataautomationproject-piientitiesconfiguration-piientitytypes): {{
    - String}}
  [RedactionMaskMode](#cfn-bedrock-dataautomationproject-piientitiesconfiguration-redactionmaskmode): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-piientitiesconfiguration-properties"></a>

`PiiEntityTypes`  <a name="cfn-bedrock-dataautomationproject-piientitiesconfiguration-piientitytypes"></a>
List of PII entity types to detect/redact in the output. Choose from specific entity types (such as ADDRESS, NAME, EMAIL, PHONE, US\_SOCIAL\_SECURITY\_NUMBER) or specify ALL to detect all supported PII types. If not specified, defaults to ALL.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedactionMaskMode`  <a name="cfn-bedrock-dataautomationproject-piientitiesconfiguration-redactionmaskmode"></a>
Defines how detected PII entities are masked in redacted output files. Set to PII to replace all detected entities with a generic [PII] marker regardless of entity type. Set to ENTITY\_TYPE to replace each detected entity with its specific type marker (for example, [NAME], [EMAIL], [ADDRESS]). This setting only applies when detectionMode is set to DETECTION\_AND\_REDACTION. If not specified, defaults to ENTITY\_TYPE.
*Required*: No
*Type*: String
*Allowed values*: `PII | ENTITY_TYPE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
