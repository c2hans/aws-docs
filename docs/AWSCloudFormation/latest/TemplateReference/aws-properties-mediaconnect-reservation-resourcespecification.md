---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-reservation-resourcespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Reservation ResourceSpecification
<a name="aws-properties-mediaconnect-reservation-resourcespecification"></a>

 A definition of what is being billed for, including the type and amount.

## Syntax
<a name="aws-properties-mediaconnect-reservation-resourcespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-reservation-resourcespecification-syntax.json"></a>

```
{
  "[ReservedBitrate](#cfn-mediaconnect-reservation-resourcespecification-reservedbitrate)" : {{Integer}},
  "[ResourceType](#cfn-mediaconnect-reservation-resourcespecification-resourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-reservation-resourcespecification-syntax.yaml"></a>

```
  [ReservedBitrate](#cfn-mediaconnect-reservation-resourcespecification-reservedbitrate): {{Integer}}
  [ResourceType](#cfn-mediaconnect-reservation-resourcespecification-resourcetype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-reservation-resourcespecification-properties"></a>

`ReservedBitrate`  <a name="cfn-mediaconnect-reservation-resourcespecification-reservedbitrate"></a>
 The amount of outbound bandwidth that is discounted in the offering.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-mediaconnect-reservation-resourcespecification-resourcetype"></a>
 The type of resource and the unit that is being billed for.
*Required*: Yes
*Type*: String
*Allowed values*: `Mbps_Outbound_Bandwidth`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
