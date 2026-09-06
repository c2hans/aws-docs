---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-inboundedioptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership InboundEdiOptions
<a name="aws-properties-b2bi-partnership-inboundedioptions"></a>

Contains options for processing inbound EDI files. These options allow for customizing how incoming EDI documents are processed.

## Syntax
<a name="aws-properties-b2bi-partnership-inboundedioptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-inboundedioptions-syntax.json"></a>

```
{
  "[X12](#cfn-b2bi-partnership-inboundedioptions-x12)" : {{X12InboundEdiOptions}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-inboundedioptions-syntax.yaml"></a>

```
  [X12](#cfn-b2bi-partnership-inboundedioptions-x12): {{
    X12InboundEdiOptions}}
```

## Properties
<a name="aws-properties-b2bi-partnership-inboundedioptions-properties"></a>

`X12`  <a name="cfn-b2bi-partnership-inboundedioptions-x12"></a>
A structure that contains X12-specific options for processing inbound X12 EDI files.
*Required*: No
*Type*: [X12InboundEdiOptions](aws-properties-b2bi-partnership-x12inboundedioptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
