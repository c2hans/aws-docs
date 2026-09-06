---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::PartnerAccount SidewalkUpdateAccount
<a name="aws-properties-iotwireless-partneraccount-sidewalkupdateaccount"></a>

Sidewalk update.

## Syntax
<a name="aws-properties-iotwireless-partneraccount-sidewalkupdateaccount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-partneraccount-sidewalkupdateaccount-syntax.json"></a>

```
{
  "[AppServerPrivateKey](#cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-partneraccount-sidewalkupdateaccount-syntax.yaml"></a>

```
  [AppServerPrivateKey](#cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-partneraccount-sidewalkupdateaccount-properties"></a>

`AppServerPrivateKey`  <a name="cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey"></a>
The new Sidewalk application server private key.
*Required*: No
*Type*: String
*Pattern*: `[a-fA-F0-9]{64}`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
