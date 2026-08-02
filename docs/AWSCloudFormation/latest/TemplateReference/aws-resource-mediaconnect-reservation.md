---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-reservation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Reservation
<a name="aws-resource-mediaconnect-reservation"></a>

 A pricing agreement for a discounted rate for a specific outbound bandwidth that your MediaConnect account will use each month over a specific time period. The discounted rate in the reservation applies to outbound bandwidth for all flows from your account until your account reaches the amount of bandwidth in your reservation. If you use more outbound bandwidth than the agreed upon amount in a single month, the overage is charged at the on-demand rate.

## Syntax
<a name="aws-resource-mediaconnect-reservation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-reservation-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::Reservation"
}
```

### YAML
<a name="aws-resource-mediaconnect-reservation-syntax.yaml"></a>

```
Type: AWS::MediaConnect::Reservation
```

## Return values
<a name="aws-resource-mediaconnect-reservation-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-reservation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediaconnect-reservation-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediaconnect-reservation-return-values-fn--getatt-fn--getatt"></a>

`CurrencyCode`  <a name="CurrencyCode-fn::getatt"></a>
 The type of currency that is used for billing. The currencyCode used for your reservation is US dollars.

`Duration`  <a name="Duration-fn::getatt"></a>
 The length of time that this reservation is active. MediaConnect defines this value in the offering.

`DurationUnits`  <a name="DurationUnits-fn::getatt"></a>
 The unit of measurement for the duration of the reservation. MediaConnect defines this value in the offering.

`End`  <a name="End-fn::getatt"></a>
 The day and time that this reservation expires. This value is calculated based on the start date and time that you set and the offering's duration.

`OfferingArn`  <a name="OfferingArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) that MediaConnect assigns to the offering.

`OfferingDescription`  <a name="OfferingDescription-fn::getatt"></a>
 A description of the offering. MediaConnect defines this value in the offering.

`PricePerUnit`  <a name="PricePerUnit-fn::getatt"></a>
 The cost of a single unit. This value, in combination with priceUnits, makes up the rate. MediaConnect defines this value in the offering.

`PriceUnits`  <a name="PriceUnits-fn::getatt"></a>
 The unit of measurement that is used for billing. This value, in combination with pricePerUnit, makes up the rate. MediaConnect defines this value in the offering.

`ReservationArn`  <a name="ReservationArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) that MediaConnect assigns to the reservation when you purchase an offering.

`ReservationName`  <a name="ReservationName-fn::getatt"></a>
 The name that you assigned to the reservation when you purchased the offering.

`ReservationState`  <a name="ReservationState-fn::getatt"></a>
 The status of your reservation.

`Start`  <a name="Start-fn::getatt"></a>
 The day and time that the reservation becomes active. You set this value when you purchase the offering.
