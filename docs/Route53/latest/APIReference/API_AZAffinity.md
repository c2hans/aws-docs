---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_AZAffinity.html
---

# AZAffinity

Specifies the location that an AZ-affinity resource record set answers DNS queries from. For the location types, from most to least specific, see `LocationType`. A query matches a location when Route 53 VPC Resolver reports that the query came from an Availability Zone (AZ) in that location. If Route 53 doesn't know which AZ a query came from, the query matches only the record for the `Global` location type. AZ-affinity routing chooses which record to return. It doesn't restrict which clients can get a record. You must specify both `LocationType` and `LocationId`.

To have Route 53 fall back to a less specific location when a resource is unhealthy, associate a health check with each record, or set `EvaluateTargetHealth` to `true` for alias records. If every record that matches a query is unhealthy, Route 53 responds with the most specific one.

## Contents
<a name="API_AZAffinity_Contents"></a>

 ** LocationId **   <a name="Route53-Type-AZAffinity-LocationId"></a>
The ID of the location. You can specify only generally available Availability Zones and Zone Groups. Zone Group, Region, and partition IDs must belong to a partition that you can use. Specify the ID in lowercase, in the format that corresponds to `LocationType`:
+ For `AvailabilityZone`, the Availability Zone ID (not the Availability Zone name or a Local Zone ID), such as `use1-az1`.
+ For `AvailabilityZoneGroup`, the Zone Group that an Availability Zone belongs to (not a Local Zone group), such as `us-east-1-zg-1`.
+ For `Region`, the Region code, such as `us-east-1`.
+ For `Partition`, the partition name, such as `aws`.
+ For `Global`, the value `global`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** LocationType **   <a name="Route53-Type-AZAffinity-LocationType"></a>
The level of the location that `LocationId` identifies. Valid values, from most to least specific:
+  `AvailabilityZone`: A single Availability Zone.
+  `AvailabilityZoneGroup`: A Zone Group, which is a group of Availability Zones in an AWS Region.
+  `Region`: An entire AWS Region.
+  `Partition`: An entire AWS partition.
+  `Global`: All locations.
We recommend that you create a record for the `Global` location type so that every query gets an answer. Route 53 responds with it when a query matches no more specific record, or when it's the only healthy record that matches. Without a `Global` record, Route 53 returns a "no answer" response to queries that don't match any other record.
Type: String
Valid Values: `AvailabilityZone | AvailabilityZoneGroup | Region | Partition | Global`
Required: No

## See Also
<a name="API_AZAffinity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/AZAffinity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/AZAffinity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/AZAffinity)
