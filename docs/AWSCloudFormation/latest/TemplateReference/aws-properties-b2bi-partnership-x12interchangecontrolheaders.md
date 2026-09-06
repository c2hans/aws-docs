---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership X12InterchangeControlHeaders
<a name="aws-properties-b2bi-partnership-x12interchangecontrolheaders"></a>

In X12, the Interchange Control Header is the first segment of an EDI document and is part of the Interchange Envelope. It contains information about the sender and receiver, the date and time of transmission, and the X12 version being used. It also includes delivery information, such as the sender and receiver IDs.

## Syntax
<a name="aws-properties-b2bi-partnership-x12interchangecontrolheaders-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-x12interchangecontrolheaders-syntax.json"></a>

```
{
  "[AcknowledgmentRequestedCode](#cfn-b2bi-partnership-x12interchangecontrolheaders-acknowledgmentrequestedcode)" : {{String}},
  "[ReceiverId](#cfn-b2bi-partnership-x12interchangecontrolheaders-receiverid)" : {{String}},
  "[ReceiverIdQualifier](#cfn-b2bi-partnership-x12interchangecontrolheaders-receiveridqualifier)" : {{String}},
  "[RepetitionSeparator](#cfn-b2bi-partnership-x12interchangecontrolheaders-repetitionseparator)" : {{String}},
  "[SenderId](#cfn-b2bi-partnership-x12interchangecontrolheaders-senderid)" : {{String}},
  "[SenderIdQualifier](#cfn-b2bi-partnership-x12interchangecontrolheaders-senderidqualifier)" : {{String}},
  "[UsageIndicatorCode](#cfn-b2bi-partnership-x12interchangecontrolheaders-usageindicatorcode)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-x12interchangecontrolheaders-syntax.yaml"></a>

```
  [AcknowledgmentRequestedCode](#cfn-b2bi-partnership-x12interchangecontrolheaders-acknowledgmentrequestedcode): {{String}}
  [ReceiverId](#cfn-b2bi-partnership-x12interchangecontrolheaders-receiverid): {{String}}
  [ReceiverIdQualifier](#cfn-b2bi-partnership-x12interchangecontrolheaders-receiveridqualifier): {{String}}
  [RepetitionSeparator](#cfn-b2bi-partnership-x12interchangecontrolheaders-repetitionseparator): {{String}}
  [SenderId](#cfn-b2bi-partnership-x12interchangecontrolheaders-senderid): {{String}}
  [SenderIdQualifier](#cfn-b2bi-partnership-x12interchangecontrolheaders-senderidqualifier): {{String}}
  [UsageIndicatorCode](#cfn-b2bi-partnership-x12interchangecontrolheaders-usageindicatorcode): {{String}}
```

## Properties
<a name="aws-properties-b2bi-partnership-x12interchangecontrolheaders-properties"></a>

`AcknowledgmentRequestedCode`  <a name="cfn-b2bi-partnership-x12interchangecontrolheaders-acknowledgmentrequestedcode"></a>
Located at position ISA-14 in the header. The value "1" indicates that the sender is requesting an interchange acknowledgment at receipt of the interchange. The value "0" is used otherwise.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReceiverId`  <a name="cfn-b2bi-partnership-x12interchangecontrolheaders-receiverid"></a>
Located at position ISA-08 in the header. This value (along with the `receiverIdQualifier`) identifies the intended recipient of the interchange.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9 ]*$`
*Minimum*: `15`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReceiverIdQualifier`  <a name="cfn-b2bi-partnership-x12interchangecontrolheaders-receiveridqualifier"></a>
Located at position ISA-07 in the header. Qualifier for the receiver ID. Together, the ID and qualifier uniquely identify the receiving trading partner.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]*$`
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepetitionSeparator`  <a name="cfn-b2bi-partnership-x12interchangecontrolheaders-repetitionseparator"></a>
Located at position ISA-11 in the header. This string makes it easier when you need to group similar adjacent element values together without using extra segments.
This parameter is only honored for version greater than 401 (`VERSION_4010` and higher).
For versions less than 401, this field is called [StandardsId](https://www.stedi.com/edi/x12-004010/segment/ISA#ISA-11), in which case our service sets the value to `U`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SenderId`  <a name="cfn-b2bi-partnership-x12interchangecontrolheaders-senderid"></a>
Located at position ISA-06 in the header. This value (along with the `senderIdQualifier`) identifies the sender of the interchange.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9 ]*$`
*Minimum*: `15`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SenderIdQualifier`  <a name="cfn-b2bi-partnership-x12interchangecontrolheaders-senderidqualifier"></a>
Located at position ISA-05 in the header. Qualifier for the sender ID. Together, the ID and qualifier uniquely identify the sending trading partner.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]*$`
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsageIndicatorCode`  <a name="cfn-b2bi-partnership-x12interchangecontrolheaders-usageindicatorcode"></a>
Located at position ISA-15 in the header. Specifies how this interchange is being used:
+ `T` indicates this interchange is for testing.
+ `P` indicates this interchange is for production.
+ `I` indicates this interchange is informational.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
