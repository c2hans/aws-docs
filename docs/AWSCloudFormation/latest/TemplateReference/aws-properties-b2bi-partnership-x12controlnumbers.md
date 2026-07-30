---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-x12controlnumbers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership X12ControlNumbers
<a name="aws-properties-b2bi-partnership-x12controlnumbers"></a>

Contains configuration for X12 control numbers used in X12 EDI generation. Control numbers are used to uniquely identify interchanges, functional groups, and transaction sets.

## Syntax
<a name="aws-properties-b2bi-partnership-x12controlnumbers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-x12controlnumbers-syntax.json"></a>

```
{
  "[StartingFunctionalGroupControlNumber](#cfn-b2bi-partnership-x12controlnumbers-startingfunctionalgroupcontrolnumber)" : {{Number}},
  "[StartingInterchangeControlNumber](#cfn-b2bi-partnership-x12controlnumbers-startinginterchangecontrolnumber)" : {{Number}},
  "[StartingTransactionSetControlNumber](#cfn-b2bi-partnership-x12controlnumbers-startingtransactionsetcontrolnumber)" : {{Number}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-x12controlnumbers-syntax.yaml"></a>

```
  [StartingFunctionalGroupControlNumber](#cfn-b2bi-partnership-x12controlnumbers-startingfunctionalgroupcontrolnumber): {{
    Number}}
  [StartingInterchangeControlNumber](#cfn-b2bi-partnership-x12controlnumbers-startinginterchangecontrolnumber): {{
    Number}}
  [StartingTransactionSetControlNumber](#cfn-b2bi-partnership-x12controlnumbers-startingtransactionsetcontrolnumber): {{
    Number}}
```

## Properties
<a name="aws-properties-b2bi-partnership-x12controlnumbers-properties"></a>

`StartingFunctionalGroupControlNumber`  <a name="cfn-b2bi-partnership-x12controlnumbers-startingfunctionalgroupcontrolnumber"></a>
Specifies the starting functional group control number (GS06) to use for X12 EDI generation. This number is incremented for each new functional group. For the GS (functional group) envelope, AWS B2B Data Interchange generates a functional group control number that is unique to the sender ID, receiver ID, and functional identifier code combination.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `999999999`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartingInterchangeControlNumber`  <a name="cfn-b2bi-partnership-x12controlnumbers-startinginterchangecontrolnumber"></a>
Specifies the starting interchange control number (ISA13) to use for X12 EDI generation. This number is incremented for each new interchange. For the ISA (interchange) envelope, AWS B2B Data Interchange generates an interchange control number that is unique for the ISA05 and ISA06 (sender) & ISA07 and ISA08 (receiver) combination.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `999999999`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartingTransactionSetControlNumber`  <a name="cfn-b2bi-partnership-x12controlnumbers-startingtransactionsetcontrolnumber"></a>
Specifies the starting transaction set control number (ST02) to use for X12 EDI generation. This number is incremented for each new transaction set.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `999999999`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
