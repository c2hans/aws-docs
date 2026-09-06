---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-capability-capabilityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Capability CapabilityConfiguration
<a name="aws-properties-b2bi-capability-capabilityconfiguration"></a>

A capability object. Currently, only EDI (electronic data interchange) capabilities are supported. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

## Syntax
<a name="aws-properties-b2bi-capability-capabilityconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-capability-capabilityconfiguration-syntax.json"></a>

```
{
  "[Edi](#cfn-b2bi-capability-capabilityconfiguration-edi)" : {{EdiConfiguration}}
}
```

### YAML
<a name="aws-properties-b2bi-capability-capabilityconfiguration-syntax.yaml"></a>

```
  [Edi](#cfn-b2bi-capability-capabilityconfiguration-edi): {{
    EdiConfiguration}}
```

## Properties
<a name="aws-properties-b2bi-capability-capabilityconfiguration-properties"></a>

`Edi`  <a name="cfn-b2bi-capability-capabilityconfiguration-edi"></a>
An EDI (electronic data interchange) configuration object.
*Required*: Yes
*Type*: [EdiConfiguration](aws-properties-b2bi-capability-ediconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
