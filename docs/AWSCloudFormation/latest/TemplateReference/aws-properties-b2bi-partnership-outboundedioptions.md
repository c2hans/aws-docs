---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-outboundedioptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership OutboundEdiOptions
<a name="aws-properties-b2bi-partnership-outboundedioptions"></a>

A container for outbound EDI options.

## Syntax
<a name="aws-properties-b2bi-partnership-outboundedioptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-outboundedioptions-syntax.json"></a>

```
{
  "[X12](#cfn-b2bi-partnership-outboundedioptions-x12)" : {{X12Envelope}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-outboundedioptions-syntax.yaml"></a>

```
  [X12](#cfn-b2bi-partnership-outboundedioptions-x12): {{
    X12Envelope}}
```

## Properties
<a name="aws-properties-b2bi-partnership-outboundedioptions-properties"></a>

`X12`  <a name="cfn-b2bi-partnership-outboundedioptions-x12"></a>
A structure that contains an X12 envelope structure.
*Required*: Yes
*Type*: [X12Envelope](aws-properties-b2bi-partnership-x12envelope.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
