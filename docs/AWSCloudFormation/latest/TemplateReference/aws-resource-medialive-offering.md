---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-offering.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Offering
<a name="aws-resource-medialive-offering"></a>

Reserved resources available for purchase

## Syntax
<a name="aws-resource-medialive-offering-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-offering-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::Offering"
}
```

### YAML
<a name="aws-resource-medialive-offering-syntax.yaml"></a>

```
Type: AWS::MediaLive::Offering
```

## Return values
<a name="aws-resource-medialive-offering-return-values"></a>

### Ref
<a name="aws-resource-medialive-offering-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-offering-return-values-fn--getatt"></a>

####
<a name="aws-resource-medialive-offering-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Unique offering ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:offering:87654321'

`CurrencyCode`  <a name="CurrencyCode-fn::getatt"></a>
Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'

`Duration`  <a name="Duration-fn::getatt"></a>
Lease duration, e.g. '12'

`DurationUnits`  <a name="DurationUnits-fn::getatt"></a>
Units for duration, e.g. 'MONTHS'

`FixedPrice`  <a name="FixedPrice-fn::getatt"></a>
One-time charge for each reserved resource, e.g. '0.0' for a NO\_UPFRONT offering

`OfferingDescription`  <a name="OfferingDescription-fn::getatt"></a>
Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)'

`OfferingId`  <a name="OfferingId-fn::getatt"></a>
Unique offering ID, e.g. '87654321'

`OfferingType`  <a name="OfferingType-fn::getatt"></a>
Offering type, e.g. 'NO\_UPFRONT'

`Region`  <a name="Region-fn::getatt"></a>
AWS Region, e.g. 'us-west-2'

`UsagePrice`  <a name="UsagePrice-fn::getatt"></a>
Recurring usage charge for each reserved resource, e.g. '157.0'
