---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-x12acknowledgmentoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership X12AcknowledgmentOptions
<a name="aws-properties-b2bi-partnership-x12acknowledgmentoptions"></a>

Contains options for configuring X12 acknowledgments. These options control how functional and technical acknowledgments are handled.

## Syntax
<a name="aws-properties-b2bi-partnership-x12acknowledgmentoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-x12acknowledgmentoptions-syntax.json"></a>

```
{
  "[FunctionalAcknowledgment](#cfn-b2bi-partnership-x12acknowledgmentoptions-functionalacknowledgment)" : {{String}},
  "[TechnicalAcknowledgment](#cfn-b2bi-partnership-x12acknowledgmentoptions-technicalacknowledgment)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-x12acknowledgmentoptions-syntax.yaml"></a>

```
  [FunctionalAcknowledgment](#cfn-b2bi-partnership-x12acknowledgmentoptions-functionalacknowledgment): {{String}}
  [TechnicalAcknowledgment](#cfn-b2bi-partnership-x12acknowledgmentoptions-technicalacknowledgment): {{String}}
```

## Properties
<a name="aws-properties-b2bi-partnership-x12acknowledgmentoptions-properties"></a>

`FunctionalAcknowledgment`  <a name="cfn-b2bi-partnership-x12acknowledgmentoptions-functionalacknowledgment"></a>
Specifies whether functional acknowledgments (997/999) should be generated for incoming X12 transactions. Valid values are `DO_NOT_GENERATE`, `GENERATE_ALL_SEGMENTS` and `GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP`.
If you choose `GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP`, AWS B2B Data Interchange skips the AK2\_Loop when generating an acknowledgment document.
*Required*: Yes
*Type*: String
*Allowed values*: `DO_NOT_GENERATE | GENERATE_ALL_SEGMENTS | GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TechnicalAcknowledgment`  <a name="cfn-b2bi-partnership-x12acknowledgmentoptions-technicalacknowledgment"></a>
Specifies whether technical acknowledgments (TA1) should be generated for incoming X12 interchanges. Valid values are `DO_NOT_GENERATE` and `GENERATE_ALL_SEGMENTS` and.
*Required*: Yes
*Type*: String
*Allowed values*: `DO_NOT_GENERATE | GENERATE_ALL_SEGMENTS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
