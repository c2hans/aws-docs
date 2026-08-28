---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoProximityLocation.html
---

# GeoProximityLocation
<a name="API_GeoProximityLocation"></a>

 (Resource record sets only): A complex type that lets you specify where your resources are located. Only one of `LocalZoneGroup`, `Coordinates`, or ` AWSRegion` is allowed per request at a time.

For more information about geoproximity routing, see [Geoproximity routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html) in the *Amazon Route 53 Developer Guide*.

## Contents
<a name="API_GeoProximityLocation_Contents"></a>

 ** AWSRegion **   <a name="Route53-Type-GeoProximityLocation-AWSRegion"></a>
 The AWS Region the resource you are directing DNS traffic to, is in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Bias **   <a name="Route53-Type-GeoProximityLocation-Bias"></a>
 The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource.
To use `Bias` to change the size of the geographic region, specify the applicable value for the bias:
+ To expand the size of the geographic region from which Route 53 routes traffic to a resource, specify a positive integer from 1 to 99 for the bias. Route 53 shrinks the size of adjacent regions.
+ To shrink the size of the geographic region from which Route 53 routes traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands the size of adjacent regions.
Type: Integer
Valid Range: Minimum value of -99. Maximum value of 99.
Required: No

 ** Coordinates **   <a name="Route53-Type-GeoProximityLocation-Coordinates"></a>
 Contains the longitude and latitude for a geographic region.
Type: [Coordinates](API_Coordinates.md) object
Required: No

 ** LocalZoneGroup **   <a name="Route53-Type-GeoProximityLocation-LocalZoneGroup"></a>
 Specifies an AWS Local Zone Group.
A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is `us-east-1-bue-1a` the Local Zone Group is `us-east-1-bue-1`.
You can identify the Local Zones Group for a specific Local Zone by using the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) CLI command:
This command returns: `"GroupName": "us-west-2-den-1"`, specifying that the Local Zone `us-west-2-den-1a` belongs to the Local Zone Group `us-west-2-den-1`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_GeoProximityLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GeoProximityLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GeoProximityLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GeoProximityLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
