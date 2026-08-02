---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-offering.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Offering
<a name="aws-resource-mediaconnect-offering"></a>

 A savings plan that reserves a certain amount of outbound bandwidth usage at a discounted rate each month over a period of time.

## Syntax
<a name="aws-resource-mediaconnect-offering-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-offering-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::Offering"
}
```

### YAML
<a name="aws-resource-mediaconnect-offering-syntax.yaml"></a>

```
Type: AWS::MediaConnect::Offering
```

## Return values
<a name="aws-resource-mediaconnect-offering-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-offering-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediaconnect-offering-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediaconnect-offering-return-values-fn--getatt-fn--getatt"></a>

`CurrencyCode`  <a name="CurrencyCode-fn::getatt"></a>
 The type of currency that is used for billing. The currencyCode used for all reservations is US dollars.

`Duration`  <a name="Duration-fn::getatt"></a>
 The length of time that your reservation would be active.

`DurationUnits`  <a name="DurationUnits-fn::getatt"></a>
 The unit of measurement for the duration of the offering.

`OfferingArn`  <a name="OfferingArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) that MediaConnect assigns to the offering.

`OfferingDescription`  <a name="OfferingDescription-fn::getatt"></a>
 A description of the offering.

`PricePerUnit`  <a name="PricePerUnit-fn::getatt"></a>
 The cost of a single unit. This value, in combination with priceUnits, makes up the rate.

`PriceUnits`  <a name="PriceUnits-fn::getatt"></a>
 The unit of measurement that is used for billing. This value, in combination with pricePerUnit, makes up the rate.
