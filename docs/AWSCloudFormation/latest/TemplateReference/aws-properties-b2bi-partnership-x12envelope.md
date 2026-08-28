---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-x12envelope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership X12Envelope
<a name="aws-properties-b2bi-partnership-x12envelope"></a>

A wrapper structure for an X12 definition object.

the X12 envelope ensures the integrity of the data and the efficiency of the information exchange. The X12 message structure has hierarchical levels. From highest to the lowest, they are:
+ Interchange Envelope
+ Functional Group
+ Transaction Set

## Syntax
<a name="aws-properties-b2bi-partnership-x12envelope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-x12envelope-syntax.json"></a>

```
{
  "[Common](#cfn-b2bi-partnership-x12envelope-common)" : {{X12OutboundEdiHeaders}},
  "[WrapOptions](#cfn-b2bi-partnership-x12envelope-wrapoptions)" : {{WrapOptions}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-x12envelope-syntax.yaml"></a>

```
  [Common](#cfn-b2bi-partnership-x12envelope-common): {{
    X12OutboundEdiHeaders}}
  [WrapOptions](#cfn-b2bi-partnership-x12envelope-wrapoptions): {{
    WrapOptions}}
```

## Properties
<a name="aws-properties-b2bi-partnership-x12envelope-properties"></a>

`Common`  <a name="cfn-b2bi-partnership-x12envelope-common"></a>
A container for the X12 outbound EDI headers.
*Required*: No
*Type*: [X12OutboundEdiHeaders](aws-properties-b2bi-partnership-x12outboundediheaders.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WrapOptions`  <a name="cfn-b2bi-partnership-x12envelope-wrapoptions"></a>
Property description not available.
*Required*: No
*Type*: [WrapOptions](aws-properties-b2bi-partnership-wrapoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
