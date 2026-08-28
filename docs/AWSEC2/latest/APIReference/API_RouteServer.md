---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteServer.html
---

# RouteServer
<a name="API_RouteServer"></a>

Describes a route server and its configuration.

Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads.

Route server supports the follow route table types:
+ VPC route tables not associated with subnets
+ Subnet route tables
+ Internet gateway route tables

Route server does not support route tables associated with virtual private gateways. To propagate routes into a transit gateway route table, use [Transit Gateway Connect](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html).

## Contents
<a name="API_RouteServer_Contents"></a>

 ** amazonSideAsn **
The Border Gateway Protocol (BGP) Autonomous System Number (ASN) for the appliance. Valid values are from 1 to 4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.
Type: Long
Required: No

 ** persistRoutesDuration **
The number of minutes a route server will wait after BGP is re-established to unpersist the routes in the FIB and RIB. Value must be in the range of 1-5. The default value is 1. Only valid if `persistRoutesState` is 'enabled'.
If you set the duration to 1 minute, then when your network appliance re-establishes BGP with route server, it has 1 minute to relearn it's adjacent network and advertise those routes to route server before route server resumes normal functionality. In most cases, 1 minute is probably sufficient. If, however, you have concerns that your BGP network may not be capable of fully re-establishing and re-learning everything in 1 minute, you can increase the duration up to 5 minutes.
Type: Long
Required: No

 ** persistRoutesState **
The current state of route persistence for the route server.
Type: String
Valid Values: `enabling | enabled | resetting | disabling | disabled | modifying`
Required: No

 ** routeServerId **
The unique identifier of the route server.
Type: String
Required: No

 ** snsNotificationsEnabled **
Indicates whether SNS notifications are enabled for the route server. Enabling SNS notifications persists BGP status changes to an SNS topic provisioned by AWS.
Type: Boolean
Required: No

 ** snsTopicArn **
The ARN of the SNS topic where notifications are published.
Type: String
Required: No

 ** state **
The current state of the route server.
Type: String
Valid Values: `pending | available | modifying | deleting | deleted`
Required: No

 ** TagSet.N **
Any tags assigned to the route server.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_RouteServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
