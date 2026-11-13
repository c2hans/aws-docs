---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-connectedaccountprice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ConnectedAccountPrice
<a name="aws-properties-wafv2-webacl-connectedaccountprice"></a>

The price per request for a connected account payment network, specifying the amount and cryptocurrency.

## Syntax
<a name="aws-properties-wafv2-webacl-connectedaccountprice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-connectedaccountprice-syntax.json"></a>

```
{
  "[Amount](#cfn-wafv2-webacl-connectedaccountprice-amount)" : {{String}},
  "[Currency](#cfn-wafv2-webacl-connectedaccountprice-currency)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-connectedaccountprice-syntax.yaml"></a>

```
  [Amount](#cfn-wafv2-webacl-connectedaccountprice-amount): {{String}}
  [Currency](#cfn-wafv2-webacl-connectedaccountprice-currency): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-connectedaccountprice-properties"></a>

`Amount`  <a name="cfn-wafv2-webacl-connectedaccountprice-amount"></a>
The price per request as a decimal string in the specified currency. Valid values range from 0.01 to 999999.99 USDC, with up to two decimal places. Sub-cent amounts are not supported.
*Required*: Yes
*Type*: String
*Pattern*: `^([1-9][0-9]{0,5}(\.[0-9]{1,2})?|0\.(0[1-9]|[1-9][0-9]?))$`
*Minimum*: `1`
*Maximum*: `9`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Currency`  <a name="cfn-wafv2-webacl-connectedaccountprice-currency"></a>
The cryptocurrency for payment. Currently only `USDC` is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `USDC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
