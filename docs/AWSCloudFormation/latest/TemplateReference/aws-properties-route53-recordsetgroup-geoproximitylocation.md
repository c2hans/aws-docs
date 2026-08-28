---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-recordsetgroup-geoproximitylocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::RecordSetGroup GeoProximityLocation
<a name="aws-properties-route53-recordsetgroup-geoproximitylocation"></a>

 (Resource record sets only): A complex type that lets you specify where your resources are located. Only one of `LocalZoneGroup`, `Coordinates`, or `AWSRegion` is allowed per request at a time.

For more information about geoproximity routing, see [Geoproximity routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html) in the *Amazon Route 53 Developer Guide*.

## Syntax
<a name="aws-properties-route53-recordsetgroup-geoproximitylocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-recordsetgroup-geoproximitylocation-syntax.json"></a>

```
{
  "[AWSRegion](#cfn-route53-recordsetgroup-geoproximitylocation-awsregion)" : {{String}},
  "[Bias](#cfn-route53-recordsetgroup-geoproximitylocation-bias)" : {{Integer}},
  "[Coordinates](#cfn-route53-recordsetgroup-geoproximitylocation-coordinates)" : {{Coordinates}},
  "[LocalZoneGroup](#cfn-route53-recordsetgroup-geoproximitylocation-localzonegroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-recordsetgroup-geoproximitylocation-syntax.yaml"></a>

```
  [AWSRegion](#cfn-route53-recordsetgroup-geoproximitylocation-awsregion): {{String}}
  [Bias](#cfn-route53-recordsetgroup-geoproximitylocation-bias): {{Integer}}
  [Coordinates](#cfn-route53-recordsetgroup-geoproximitylocation-coordinates): {{
    Coordinates}}
  [LocalZoneGroup](#cfn-route53-recordsetgroup-geoproximitylocation-localzonegroup): {{String}}
```

## Properties
<a name="aws-properties-route53-recordsetgroup-geoproximitylocation-properties"></a>

`AWSRegion`  <a name="cfn-route53-recordsetgroup-geoproximitylocation-awsregion"></a>
 The AWS Region the resource you are directing DNS traffic to, is in.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Bias`  <a name="cfn-route53-recordsetgroup-geoproximitylocation-bias"></a>
 The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource.
To use `Bias` to change the size of the geographic region, specify the applicable value for the bias:
+ To expand the size of the geographic region from which Route 53 routes traffic to a resource, specify a positive integer from 1 to 99 for the bias. Route 53 shrinks the size of adjacent regions.
+ To shrink the size of the geographic region from which Route 53 routes traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands the size of adjacent regions.
*Required*: No
*Type*: Integer
*Minimum*: `-99`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Coordinates`  <a name="cfn-route53-recordsetgroup-geoproximitylocation-coordinates"></a>
 Contains the longitude and latitude for a geographic region.
*Required*: No
*Type*: [Coordinates](aws-properties-route53-recordsetgroup-coordinates.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalZoneGroup`  <a name="cfn-route53-recordsetgroup-geoproximitylocation-localzonegroup"></a>
 Specifies an AWS Local Zone Group.
A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is `us-east-1-bue-1a` the Local Zone Group is `us-east-1-bue-1`.
You can identify the Local Zones Group for a specific Local Zone by using the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) CLI command:
This command returns: `"GroupName": "us-west-2-den-1"`, specifying that the Local Zone `us-west-2-den-1a` belongs to the Local Zone Group `us-west-2-den-1`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
