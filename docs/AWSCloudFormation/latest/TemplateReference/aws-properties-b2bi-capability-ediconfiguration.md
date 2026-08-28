---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-capability-ediconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Capability EdiConfiguration
<a name="aws-properties-b2bi-capability-ediconfiguration"></a>

Specifies the details for the EDI (electronic data interchange) transformation.

## Syntax
<a name="aws-properties-b2bi-capability-ediconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-capability-ediconfiguration-syntax.json"></a>

```
{
  "[CapabilityDirection](#cfn-b2bi-capability-ediconfiguration-capabilitydirection)" : {{String}},
  "[InputLocation](#cfn-b2bi-capability-ediconfiguration-inputlocation)" : {{S3Location}},
  "[OutputLocation](#cfn-b2bi-capability-ediconfiguration-outputlocation)" : {{S3Location}},
  "[TransformerId](#cfn-b2bi-capability-ediconfiguration-transformerid)" : {{String}},
  "[Type](#cfn-b2bi-capability-ediconfiguration-type)" : {{EdiType}}
}
```

### YAML
<a name="aws-properties-b2bi-capability-ediconfiguration-syntax.yaml"></a>

```
  [CapabilityDirection](#cfn-b2bi-capability-ediconfiguration-capabilitydirection): {{String}}
  [InputLocation](#cfn-b2bi-capability-ediconfiguration-inputlocation): {{
    S3Location}}
  [OutputLocation](#cfn-b2bi-capability-ediconfiguration-outputlocation): {{
    S3Location}}
  [TransformerId](#cfn-b2bi-capability-ediconfiguration-transformerid): {{String}}
  [Type](#cfn-b2bi-capability-ediconfiguration-type): {{
    EdiType}}
```

## Properties
<a name="aws-properties-b2bi-capability-ediconfiguration-properties"></a>

`CapabilityDirection`  <a name="cfn-b2bi-capability-ediconfiguration-capabilitydirection"></a>
Specifies whether this is capability is for inbound or outbound transformations.
*Required*: No
*Type*: String
*Allowed values*: `INBOUND | OUTBOUND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputLocation`  <a name="cfn-b2bi-capability-ediconfiguration-inputlocation"></a>
Contains the Amazon S3 bucket and prefix for the location of the input file, which is contained in an `S3Location` object.
*Required*: Yes
*Type*: [S3Location](aws-properties-b2bi-capability-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputLocation`  <a name="cfn-b2bi-capability-ediconfiguration-outputlocation"></a>
Contains the Amazon S3 bucket and prefix for the location of the output file, which is contained in an `S3Location` object.
*Required*: Yes
*Type*: [S3Location](aws-properties-b2bi-capability-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransformerId`  <a name="cfn-b2bi-capability-ediconfiguration-transformerid"></a>
Returns the system-assigned unique identifier for the transformer.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-b2bi-capability-ediconfiguration-type"></a>
Returns the type of the capability. Currently, only `edi` is supported.
*Required*: Yes
*Type*: [EdiType](aws-properties-b2bi-capability-editype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
