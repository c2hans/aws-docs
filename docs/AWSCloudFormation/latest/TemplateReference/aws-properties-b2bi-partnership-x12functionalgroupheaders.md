---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-x12functionalgroupheaders.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership X12FunctionalGroupHeaders
<a name="aws-properties-b2bi-partnership-x12functionalgroupheaders"></a>

Part of the X12 message structure. These are the functional group headers for the X12 EDI object.

## Syntax
<a name="aws-properties-b2bi-partnership-x12functionalgroupheaders-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-x12functionalgroupheaders-syntax.json"></a>

```
{
  "[ApplicationReceiverCode](#cfn-b2bi-partnership-x12functionalgroupheaders-applicationreceivercode)" : {{String}},
  "[ApplicationSenderCode](#cfn-b2bi-partnership-x12functionalgroupheaders-applicationsendercode)" : {{String}},
  "[ResponsibleAgencyCode](#cfn-b2bi-partnership-x12functionalgroupheaders-responsibleagencycode)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-x12functionalgroupheaders-syntax.yaml"></a>

```
  [ApplicationReceiverCode](#cfn-b2bi-partnership-x12functionalgroupheaders-applicationreceivercode): {{String}}
  [ApplicationSenderCode](#cfn-b2bi-partnership-x12functionalgroupheaders-applicationsendercode): {{String}}
  [ResponsibleAgencyCode](#cfn-b2bi-partnership-x12functionalgroupheaders-responsibleagencycode): {{String}}
```

## Properties
<a name="aws-properties-b2bi-partnership-x12functionalgroupheaders-properties"></a>

`ApplicationReceiverCode`  <a name="cfn-b2bi-partnership-x12functionalgroupheaders-applicationreceivercode"></a>
A value representing the code used to identify the party receiving a message, at position GS-03.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9 ]*$`
*Minimum*: `2`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationSenderCode`  <a name="cfn-b2bi-partnership-x12functionalgroupheaders-applicationsendercode"></a>
A value representing the code used to identify the party transmitting a message, at position GS-02.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9 ]*$`
*Minimum*: `2`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponsibleAgencyCode`  <a name="cfn-b2bi-partnership-x12functionalgroupheaders-responsibleagencycode"></a>
A code that identifies the issuer of the standard, at position GS-07.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
