---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-billingconductor-customlineitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::CustomLineItem
<a name="aws-resource-billingconductor-customlineitem"></a>

Creates a custom line item that can be used to create a one-time or recurring, fixed or percentage-based charge that you can apply to a single billing group. You can apply custom line items to the current or previous billing period. You can create either a fee or a discount custom line item.

## Syntax
<a name="aws-resource-billingconductor-customlineitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-billingconductor-customlineitem-syntax.json"></a>

```
{
  "Type" : "AWS::BillingConductor::CustomLineItem",
  "Properties" : {
      "[AccountId](#cfn-billingconductor-customlineitem-accountid)" : {{String}},
      "[BillingGroupArn](#cfn-billingconductor-customlineitem-billinggrouparn)" : {{String}},
      "[BillingPeriodRange](#cfn-billingconductor-customlineitem-billingperiodrange)" : {{BillingPeriodRange}},
      "[ComputationRule](#cfn-billingconductor-customlineitem-computationrule)" : {{String}},
      "[CustomLineItemChargeDetails](#cfn-billingconductor-customlineitem-customlineitemchargedetails)" : {{CustomLineItemChargeDetails}},
      "[Description](#cfn-billingconductor-customlineitem-description)" : {{String}},
      "[Name](#cfn-billingconductor-customlineitem-name)" : {{String}},
      "[PresentationDetails](#cfn-billingconductor-customlineitem-presentationdetails)" : {{PresentationDetails}},
      "[Tags](#cfn-billingconductor-customlineitem-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-billingconductor-customlineitem-syntax.yaml"></a>

```
Type: AWS::BillingConductor::CustomLineItem
Properties:
  [AccountId](#cfn-billingconductor-customlineitem-accountid): {{String}}
  [BillingGroupArn](#cfn-billingconductor-customlineitem-billinggrouparn): {{String}}
  [BillingPeriodRange](#cfn-billingconductor-customlineitem-billingperiodrange): {{
    BillingPeriodRange}}
  [ComputationRule](#cfn-billingconductor-customlineitem-computationrule): {{String}}
  [CustomLineItemChargeDetails](#cfn-billingconductor-customlineitem-customlineitemchargedetails): {{
    CustomLineItemChargeDetails}}
  [Description](#cfn-billingconductor-customlineitem-description): {{String}}
  [Name](#cfn-billingconductor-customlineitem-name): {{String}}
  [PresentationDetails](#cfn-billingconductor-customlineitem-presentationdetails): {{
    PresentationDetails}}
  [Tags](#cfn-billingconductor-customlineitem-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-billingconductor-customlineitem-properties"></a>

`AccountId`  <a name="cfn-billingconductor-customlineitem-accountid"></a>
The AWS account in which this custom line item will be applied to.
*Required*: No
*Type*: String
*Pattern*: `[0-9]{12}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BillingGroupArn`  <a name="cfn-billingconductor-customlineitem-billinggrouparn"></a>
The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/?[a-zA-Z0-9]{10,12}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BillingPeriodRange`  <a name="cfn-billingconductor-customlineitem-billingperiodrange"></a>
A time range for which the custom line item is effective.
*Required*: No
*Type*: [BillingPeriodRange](aws-properties-billingconductor-customlineitem-billingperiodrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputationRule`  <a name="cfn-billingconductor-customlineitem-computationrule"></a>
The computation rule that determines how the custom line item charges are computed and reflected in the bill.
*Required*: No
*Type*: String
*Allowed values*: `CONSOLIDATED | ITEMIZED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomLineItemChargeDetails`  <a name="cfn-billingconductor-customlineitem-customlineitemchargedetails"></a>
The charge details of a custom line item. It should contain only one of `Flat` or `Percentage`.
*Required*: No
*Type*: [CustomLineItemChargeDetails](aws-properties-billingconductor-customlineitem-customlineitemchargedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-billingconductor-customlineitem-description"></a>
The custom line item's description. This is shown on the Bills page in association with the charge value.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-billingconductor-customlineitem-name"></a>
The custom line item's name.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_\+=\.\-@]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PresentationDetails`  <a name="cfn-billingconductor-customlineitem-presentationdetails"></a>
Configuration details specifying how the custom line item charges are presented, including which service the charges are shown under.
*Required*: No
*Type*: [PresentationDetails](aws-properties-billingconductor-customlineitem-presentationdetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-billingconductor-customlineitem-tags"></a>
A map that contains tag keys and tag values that are attached to a custom line item.
*Required*: No
*Type*: Array of [Tag](aws-properties-billingconductor-customlineitem-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-billingconductor-customlineitem-return-values"></a>

### Ref
<a name="aws-resource-billingconductor-customlineitem-return-values-ref"></a>

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-billingconductor-customlineitem-return-values-fn--getatt"></a>

####
<a name="aws-resource-billingconductor-customlineitem-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.

`AssociationSize`  <a name="AssociationSize-fn::getatt"></a>
The number of resources that are associated to the custom line item.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time created.

`CurrencyCode`  <a name="CurrencyCode-fn::getatt"></a>
The custom line item's charge value currency. Only one of the valid values can be used.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The most recent time the custom line item was modified.

`ProductCode`  <a name="ProductCode-fn::getatt"></a>
The product code associated with the custom line item.

## Examples
<a name="aws-resource-billingconductor-customlineitem--examples"></a>

**Topics**
+ [Flat custom line item](#aws-resource-billingconductor-customlineitem--examples--Flat_custom_line_item)
+ [Percentage custom line item](#aws-resource-billingconductor-customlineitem--examples--Percentage_custom_line_item)

### Flat custom line item
<a name="aws-resource-billingconductor-customlineitem--examples--Flat_custom_line_item"></a>

The following example shows a flat charge custom line item of $10 attached to a billing group.

#### JSON
<a name="aws-resource-billingconductor-customlineitem--examples--Flat_custom_line_item--json"></a>

```
{
  "Resources": {
      "TestFlatCustomLineItem": {
          "Type": "AWS::BillingConductor::CustomLineItem",
          "Properties": {
              "Name": "TestFlatCustomLineItem",
              "Description": "Test flat custom line item created through CloudFormation for a $10 charge.",
              "BillingGroupArn": {
                  "Fn::GetAtt": ["TestBillingGroup", "Arn"]
              },
              "CustomLineItemChargeDetails": {
                  "Flat": {
                      "ChargeValue": 10
                  },
                  "Type": "FEE"
              },
              "BillingPeriodRange": {
              "InclusiveStartBillingPeriod": "2022-11"
              }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-billingconductor-customlineitem--examples--Flat_custom_line_item--yaml"></a>

```
Resources:
  TestFlatCustomLineItem:
      Type: 'AWS::BillingConductor::CustomLineItem'
      Properties:
          Name: 'TestFlatCustomLineItem'
          Description: 'Test flat custom line item created through CloudFormation for a $10 charge.'
          BillingGroupArn: !GetAtt TestBillingGroup.Arn
          CustomLineItemChargeDetails:
              Flat:
                  ChargeValue: 10
              Type: 'FEE'
          BillingPeriodRange:
            InclusiveStartBillingPeriod: 2022-11
```

### Percentage custom line item
<a name="aws-resource-billingconductor-customlineitem--examples--Percentage_custom_line_item"></a>

The following example shows a percentage charge custom line item that is 10% of the billing group total cost.

#### JSON
<a name="aws-resource-billingconductor-customlineitem--examples--Percentage_custom_line_item--json"></a>

```
{
  "Resources": {
      "TestPercentageCustomLineItem": {
          "Type": "AWS::BillingConductor::CustomLineItem",
          "Properties": {
              "Name": "TestPercentageCustomLineItem",
              "Description": "Test percentage custom line item created through CloudFormation for a %10 additional charge on the overall total bill of the billing group.",
              "BillingGroupArn": {
                  "Fn::GetAtt": ["TestBillingGroup", "Arn"]
              },
              "CustomLineItemChargeDetails": {
                  "Percentage": {
                      "PercentageValue": 10,
                      "ChildAssociatedResources": [
                          {"Fn::GetAtt": ["TestBillingGroup", "Arn"]}
                      ]
                  },
                  "Type": "FEE"
              }
          }
      }
  }
}
```

#### YAML
<a name="aws-resource-billingconductor-customlineitem--examples--Percentage_custom_line_item--yaml"></a>

```
Resources:
        TestPercentageCustomLineItem:
        Type: 'AWS::BillingConductor::CustomLineItem'
        Properties:
        Name: 'TestPercentageCustomLineItem'
        Description: 'Test percentage custom line item created through CloudFormation for a %10 additional charge on the overall total bill of the billing group.'
        BillingGroupArn: !GetAtt TestBillingGroup.Arn
        CustomLineItemChargeDetails:
        Percentage:
        PercentageValue: 10
        ChildAssociatedResources:
        - !GetAtt TestBillingGroup.Arn
        Type: 'FEE'
```
