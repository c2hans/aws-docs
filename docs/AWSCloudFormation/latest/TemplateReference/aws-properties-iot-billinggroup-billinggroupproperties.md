---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-billinggroup-billinggroupproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::BillingGroup BillingGroupProperties
<a name="aws-properties-iot-billinggroup-billinggroupproperties"></a>

The properties of a billing group.

## Syntax
<a name="aws-properties-iot-billinggroup-billinggroupproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-billinggroup-billinggroupproperties-syntax.json"></a>

```
{
  "[BillingGroupDescription](#cfn-iot-billinggroup-billinggroupproperties-billinggroupdescription)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-billinggroup-billinggroupproperties-syntax.yaml"></a>

```
  [BillingGroupDescription](#cfn-iot-billinggroup-billinggroupproperties-billinggroupdescription): {{String}}
```

## Properties
<a name="aws-properties-iot-billinggroup-billinggroupproperties-properties"></a>

`BillingGroupDescription`  <a name="cfn-iot-billinggroup-billinggroupproperties-billinggroupdescription"></a>
The description of the billing group.
*Required*: No
*Type*: String
*Pattern*: `[\p{Graph}\x20]*`
*Maximum*: `2028`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
