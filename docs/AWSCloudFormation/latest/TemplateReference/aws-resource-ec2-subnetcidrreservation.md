---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnetcidrreservation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SubnetCidrReservation
<a name="aws-resource-ec2-subnetcidrreservation"></a>

Describes a subnet CIDR reservation.

## Syntax
<a name="aws-resource-ec2-subnetcidrreservation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-subnetcidrreservation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::SubnetCidrReservation",
  "Properties" : {
      "[Cidr](#cfn-ec2-subnetcidrreservation-cidr)" : {{String}},
      "[Description](#cfn-ec2-subnetcidrreservation-description)" : {{String}},
      "[ReservationType](#cfn-ec2-subnetcidrreservation-reservationtype)" : {{String}},
      "[SubnetId](#cfn-ec2-subnetcidrreservation-subnetid)" : {{String}},
      "[Tags](#cfn-ec2-subnetcidrreservation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-subnetcidrreservation-syntax.yaml"></a>

```
Type: AWS::EC2::SubnetCidrReservation
Properties:
  [Cidr](#cfn-ec2-subnetcidrreservation-cidr): {{String}}
  [Description](#cfn-ec2-subnetcidrreservation-description): {{String}}
  [ReservationType](#cfn-ec2-subnetcidrreservation-reservationtype): {{String}}
  [SubnetId](#cfn-ec2-subnetcidrreservation-subnetid): {{String}}
  [Tags](#cfn-ec2-subnetcidrreservation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-subnetcidrreservation-properties"></a>

`Cidr`  <a name="cfn-ec2-subnetcidrreservation-cidr"></a>
The CIDR that has been reserved.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-ec2-subnetcidrreservation-description"></a>
The description assigned to the subnet CIDR reservation.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReservationType`  <a name="cfn-ec2-subnetcidrreservation-reservationtype"></a>
The type of reservation.
*Required*: Yes
*Type*: String
*Allowed values*: `prefix | explicit`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-ec2-subnetcidrreservation-subnetid"></a>
The ID of the subnet.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-subnetcidrreservation-tags"></a>
The tags assigned to the subnet CIDR reservation.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-subnetcidrreservation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-subnetcidrreservation-return-values"></a>

### Ref
<a name="aws-resource-ec2-subnetcidrreservation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-subnetcidrreservation-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-subnetcidrreservation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the account that owns the subnet CIDR reservation.

`SubnetCidrReservationId`  <a name="SubnetCidrReservationId-fn::getatt"></a>
The ID of the subnet CIDR reservation.
