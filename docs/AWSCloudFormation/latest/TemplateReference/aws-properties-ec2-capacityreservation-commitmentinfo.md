---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-capacityreservation-commitmentinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::CapacityReservation CommitmentInfo
<a name="aws-properties-ec2-capacityreservation-commitmentinfo"></a>

Information about your commitment for a future-dated Capacity Reservation.

## Syntax
<a name="aws-properties-ec2-capacityreservation-commitmentinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-capacityreservation-commitmentinfo-syntax.json"></a>

```
{
  "[CommitmentEndDate](#cfn-ec2-capacityreservation-commitmentinfo-commitmentenddate)" : {{String}},
  "[CommittedInstanceCount](#cfn-ec2-capacityreservation-commitmentinfo-committedinstancecount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-capacityreservation-commitmentinfo-syntax.yaml"></a>

```
  [CommitmentEndDate](#cfn-ec2-capacityreservation-commitmentinfo-commitmentenddate): {{String}}
  [CommittedInstanceCount](#cfn-ec2-capacityreservation-commitmentinfo-committedinstancecount): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-capacityreservation-commitmentinfo-properties"></a>

`CommitmentEndDate`  <a name="cfn-ec2-capacityreservation-commitmentinfo-commitmentenddate"></a>
The date and time at which the commitment duration expires, in the ISO8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`). You can't decrease the instance count or cancel the Capacity Reservation before this date and time.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CommittedInstanceCount`  <a name="cfn-ec2-capacityreservation-commitmentinfo-committedinstancecount"></a>
The instance capacity that you committed to when you requested the future-dated Capacity Reservation.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
