---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-recordset-azaffinity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::RecordSet AZAffinity

Specifies the location that an AZ-affinity resource record set answers DNS queries from. For the location types, from most to least specific, see `LocationType`. A query matches a location when Route 53 VPC Resolver reports that the query came from an Availability Zone (AZ) in that location. If Route 53 doesn't know which AZ a query came from, the query matches only the record for the `Global` location type. AZ-affinity routing chooses which record to return. It doesn't restrict which clients can get a record. You must specify both `LocationType` and `LocationId`.

To have Route 53 fall back to a less specific location when a resource is unhealthy, associate a health check with each record, or set `EvaluateTargetHealth` to `true` for alias records. If every record that matches a query is unhealthy, Route 53 responds with the most specific one.

## Syntax
<a name="aws-properties-route53-recordset-azaffinity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-recordset-azaffinity-syntax.json"></a>

```json
{
  "[LocationId](#cfn-route53-recordset-azaffinity-locationid)" : {{String}},
  "[LocationType](#cfn-route53-recordset-azaffinity-locationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-recordset-azaffinity-syntax.yaml"></a>

```yaml
  [LocationId](#cfn-route53-recordset-azaffinity-locationid): {{String}}
  [LocationType](#cfn-route53-recordset-azaffinity-locationtype): {{String}}
```

## Properties
<a name="aws-properties-route53-recordset-azaffinity-properties"></a>

`LocationId`  <a name="cfn-route53-recordset-azaffinity-locationid"></a>
The ID of the location. You can specify only generally available Availability Zones and Zone Groups. Zone Group, Region, and partition IDs must belong to a partition that you can use. Specify the ID in lowercase, in the format that corresponds to `LocationType`:
+ For `AvailabilityZone`, the Availability Zone ID (not the Availability Zone name or a Local Zone ID), such as `use1-az1`.
+ For `AvailabilityZoneGroup`, the Zone Group that an Availability Zone belongs to (not a Local Zone group), such as `us-east-1-zg-1`.
+ For `Region`, the Region code, such as `us-east-1`.
+ For `Partition`, the partition name, such as `aws`.
+ For `Global`, the value `global`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationType`  <a name="cfn-route53-recordset-azaffinity-locationtype"></a>
The level of the location that `LocationId` identifies. Valid values, from most to least specific:
+ `AvailabilityZone`: A single Availability Zone.
+ `AvailabilityZoneGroup`: A Zone Group, which is a group of Availability Zones in an AWS Region.
+ `Region`: An entire AWS Region.
+ `Partition`: An entire AWS partition.
+ `Global`: All locations.
We recommend that you create a record for the `Global` location type so that every query gets an answer. Route 53 responds with it when a query matches no more specific record, or when it's the only healthy record that matches. Without a `Global` record, Route 53 returns a "no answer" response to queries that don't match any other record.
*Required*: Yes
*Type*: String
*Allowed values*: `AvailabilityZone | AvailabilityZoneGroup | Region | Partition | Global`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
