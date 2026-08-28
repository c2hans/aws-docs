---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-x12outboundediheaders.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership X12OutboundEdiHeaders
<a name="aws-properties-b2bi-partnership-x12outboundediheaders"></a>

A structure containing the details for an outbound EDI object.

## Syntax
<a name="aws-properties-b2bi-partnership-x12outboundediheaders-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-x12outboundediheaders-syntax.json"></a>

```
{
  "[ControlNumbers](#cfn-b2bi-partnership-x12outboundediheaders-controlnumbers)" : {{X12ControlNumbers}},
  "[Delimiters](#cfn-b2bi-partnership-x12outboundediheaders-delimiters)" : {{X12Delimiters}},
  "[FunctionalGroupHeaders](#cfn-b2bi-partnership-x12outboundediheaders-functionalgroupheaders)" : {{X12FunctionalGroupHeaders}},
  "[Gs05TimeFormat](#cfn-b2bi-partnership-x12outboundediheaders-gs05timeformat)" : {{String}},
  "[InterchangeControlHeaders](#cfn-b2bi-partnership-x12outboundediheaders-interchangecontrolheaders)" : {{X12InterchangeControlHeaders}},
  "[ValidateEdi](#cfn-b2bi-partnership-x12outboundediheaders-validateedi)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-x12outboundediheaders-syntax.yaml"></a>

```
  [ControlNumbers](#cfn-b2bi-partnership-x12outboundediheaders-controlnumbers): {{
    X12ControlNumbers}}
  [Delimiters](#cfn-b2bi-partnership-x12outboundediheaders-delimiters): {{
    X12Delimiters}}
  [FunctionalGroupHeaders](#cfn-b2bi-partnership-x12outboundediheaders-functionalgroupheaders): {{
    X12FunctionalGroupHeaders}}
  [Gs05TimeFormat](#cfn-b2bi-partnership-x12outboundediheaders-gs05timeformat): {{String}}
  [InterchangeControlHeaders](#cfn-b2bi-partnership-x12outboundediheaders-interchangecontrolheaders): {{
    X12InterchangeControlHeaders}}
  [ValidateEdi](#cfn-b2bi-partnership-x12outboundediheaders-validateedi): {{Boolean}}
```

## Properties
<a name="aws-properties-b2bi-partnership-x12outboundediheaders-properties"></a>

`ControlNumbers`  <a name="cfn-b2bi-partnership-x12outboundediheaders-controlnumbers"></a>
Specifies control number configuration for outbound X12 EDI headers. These settings determine the starting values for interchange, functional group, and transaction set control numbers.
*Required*: No
*Type*: [X12ControlNumbers](aws-properties-b2bi-partnership-x12controlnumbers.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Delimiters`  <a name="cfn-b2bi-partnership-x12outboundediheaders-delimiters"></a>
The delimiters, for example semicolon (`;`), that separates sections of the headers for the X12 object.
*Required*: No
*Type*: [X12Delimiters](aws-properties-b2bi-partnership-x12delimiters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionalGroupHeaders`  <a name="cfn-b2bi-partnership-x12outboundediheaders-functionalgroupheaders"></a>
The functional group headers for the X12 object.
*Required*: No
*Type*: [X12FunctionalGroupHeaders](aws-properties-b2bi-partnership-x12functionalgroupheaders.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gs05TimeFormat`  <a name="cfn-b2bi-partnership-x12outboundediheaders-gs05timeformat"></a>
Specifies the time format in the GS05 element (time) of the functional group header. The following formats use 24-hour clock time:
+ `HHMM` - Hours and minutes
+ `HHMMSS` - Hours, minutes, and seconds
+ `HHMMSSDD` - Hours, minutes, seconds, and decimal seconds
Where:
+ `HH` - Hours (00-23)
+ `MM` - Minutes (00-59)
+ `SS` - Seconds (00-59)
+ `DD` - Hundredths of seconds (00-99)
*Required*: No
*Type*: String
*Allowed values*: `HHMM | HHMMSS | HHMMSSDD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterchangeControlHeaders`  <a name="cfn-b2bi-partnership-x12outboundediheaders-interchangecontrolheaders"></a>
In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header.
*Required*: No
*Type*: [X12InterchangeControlHeaders](aws-properties-b2bi-partnership-x12interchangecontrolheaders.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidateEdi`  <a name="cfn-b2bi-partnership-x12outboundediheaders-validateedi"></a>
Specifies whether or not to validate the EDI for this X12 object: `TRUE` or `FALSE`. When enabled, this performs both standard EDI validation and applies any configured custom validation rules including element length constraints, code list validations, and element requirement checks. Validation results are returned in the response validation messages.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
