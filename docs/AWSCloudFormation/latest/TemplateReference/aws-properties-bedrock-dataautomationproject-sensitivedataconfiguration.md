---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject SensitiveDataConfiguration
<a name="aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration"></a>

Configuration for detecting and redacting sensitive data in content. Use this to control whether sensitive data is detected only or both detected and redacted, specify the scope of detection (standard output, custom output, or both), and configure specific PII entity types to detect along with how they should be masked when redacted.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration-syntax.json"></a>

```
{
  "[DetectionMode](#cfn-bedrock-dataautomationproject-sensitivedataconfiguration-detectionmode)" : {{String}},
  "[DetectionScope](#cfn-bedrock-dataautomationproject-sensitivedataconfiguration-detectionscope)" : {{[ String, ... ]}},
  "[PiiEntitiesConfiguration](#cfn-bedrock-dataautomationproject-sensitivedataconfiguration-piientitiesconfiguration)" : {{PIIEntitiesConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration-syntax.yaml"></a>

```
  [DetectionMode](#cfn-bedrock-dataautomationproject-sensitivedataconfiguration-detectionmode): {{String}}
  [DetectionScope](#cfn-bedrock-dataautomationproject-sensitivedataconfiguration-detectionscope): {{
    - String}}
  [PiiEntitiesConfiguration](#cfn-bedrock-dataautomationproject-sensitivedataconfiguration-piientitiesconfiguration): {{
    PIIEntitiesConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration-properties"></a>

`DetectionMode`  <a name="cfn-bedrock-dataautomationproject-sensitivedataconfiguration-detectionmode"></a>
Specifies the mode for handling sensitive data detection. Set to DETECTION to only identify sensitive data without modifying content - this produces one output file per detection scope containing detection information with original unredacted content. Set to DETECTION\_AND\_REDACTION to both identify and mask sensitive data - this produces two output files per detection scope: one unredacted file with detection information and one redacted file with masking applied to sensitive content. For example, if detectionScope includes both STANDARD and CUSTOM with DETECTION\_AND\_REDACTION mode, four output files will be generated (two for standard output and two for custom output).
*Required*: No
*Type*: String
*Allowed values*: `DETECTION | DETECTION_AND_REDACTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectionScope`  <a name="cfn-bedrock-dataautomationproject-sensitivedataconfiguration-detectionscope"></a>
Defines which BDA output types to apply sensitive data detection to. Specify STANDARD to detect sensitive data in standard output, CUSTOM to detect in custom output (blueprint-based extraction), or both to apply detection to both output types. If not specified, defaults to both STANDARD and CUSTOM. The number of output files generated depends on both the detection mode and the scopes selected - each scope specified will produce its own set of output files according to the detection mode configured.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PiiEntitiesConfiguration`  <a name="cfn-bedrock-dataautomationproject-sensitivedataconfiguration-piientitiesconfiguration"></a>
Configuration for detecting and redacting Personally Identifiable Information (PII) entities.
*Required*: No
*Type*: [PIIEntitiesConfiguration](aws-properties-bedrock-dataautomationproject-piientitiesconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
