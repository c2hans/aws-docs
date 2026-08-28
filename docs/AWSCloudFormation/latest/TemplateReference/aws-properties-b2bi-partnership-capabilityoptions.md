---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-capabilityoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership CapabilityOptions
<a name="aws-properties-b2bi-partnership-capabilityoptions"></a>

Contains the details for an Outbound EDI capability.

## Syntax
<a name="aws-properties-b2bi-partnership-capabilityoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-capabilityoptions-syntax.json"></a>

```
{
  "[InboundEdi](#cfn-b2bi-partnership-capabilityoptions-inboundedi)" : {{InboundEdiOptions}},
  "[OutboundEdi](#cfn-b2bi-partnership-capabilityoptions-outboundedi)" : {{OutboundEdiOptions}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-capabilityoptions-syntax.yaml"></a>

```
  [InboundEdi](#cfn-b2bi-partnership-capabilityoptions-inboundedi): {{
    InboundEdiOptions}}
  [OutboundEdi](#cfn-b2bi-partnership-capabilityoptions-outboundedi): {{
    OutboundEdiOptions}}
```

## Properties
<a name="aws-properties-b2bi-partnership-capabilityoptions-properties"></a>

`InboundEdi`  <a name="cfn-b2bi-partnership-capabilityoptions-inboundedi"></a>
A structure that contains the inbound EDI options for the capability.
*Required*: No
*Type*: [InboundEdiOptions](aws-properties-b2bi-partnership-inboundedioptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutboundEdi`  <a name="cfn-b2bi-partnership-capabilityoptions-outboundedi"></a>
A structure that contains the outbound EDI options.
*Required*: No
*Type*: [OutboundEdiOptions](aws-properties-b2bi-partnership-outboundedioptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
