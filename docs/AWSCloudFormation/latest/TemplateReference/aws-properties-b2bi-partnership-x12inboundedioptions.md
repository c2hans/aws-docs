---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-x12inboundedioptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership X12InboundEdiOptions
<a name="aws-properties-b2bi-partnership-x12inboundedioptions"></a>

Contains options specific to processing inbound X12 EDI files.

## Syntax
<a name="aws-properties-b2bi-partnership-x12inboundedioptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-x12inboundedioptions-syntax.json"></a>

```
{
  "[AcknowledgmentOptions](#cfn-b2bi-partnership-x12inboundedioptions-acknowledgmentoptions)" : {{X12AcknowledgmentOptions}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-x12inboundedioptions-syntax.yaml"></a>

```
  [AcknowledgmentOptions](#cfn-b2bi-partnership-x12inboundedioptions-acknowledgmentoptions): {{
    X12AcknowledgmentOptions}}
```

## Properties
<a name="aws-properties-b2bi-partnership-x12inboundedioptions-properties"></a>

`AcknowledgmentOptions`  <a name="cfn-b2bi-partnership-x12inboundedioptions-acknowledgmentoptions"></a>
Specifies acknowledgment options for inbound X12 EDI files. These options control how functional and technical acknowledgments are handled.
*Required*: No
*Type*: [X12AcknowledgmentOptions](aws-properties-b2bi-partnership-x12acknowledgmentoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
