---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteServerRoute.html
---

# RouteServerRoute
<a name="API_RouteServerRoute"></a>

Describes a route in the route server's routing database.

## Contents
<a name="API_RouteServerRoute_Contents"></a>

 ** AsPathSet.N **
The AS path attributes of the BGP route.
Type: Array of strings
Required: No

 ** med **
The Multi-Exit Discriminator (MED) value of the BGP route.
Type: Integer
Required: No

 ** nextHopIp **
The IP address for the next hop.
Type: String
Required: No

 ** prefix **
The destination CIDR block of the route.
Type: String
Required: No

 ** RouteInstallationDetailSet.N **
Details about the installation status of this route in route tables.
Type: Array of [RouteServerRouteInstallationDetail](API_RouteServerRouteInstallationDetail.md) objects
Required: No

 ** routeServerEndpointId **
The ID of the route server endpoint that received this route.
Type: String
Required: No

 ** routeServerPeerId **
The ID of the route server peer that advertised this route.
Type: String
Required: No

 ** routeStatus **
The current status of the route in the routing database. Values are `in-rib` or `in-fib` depending on if the routes are in the RIB or the FIB database.
The [Routing Information Base (RIB)](https://en.wikipedia.org/wiki/Routing_table) serves as a database that stores all the routing information and network topology data collected by a router or routing system, such as routes learned from BGP peers. The RIB is constantly updated as new routing information is received or existing routes change. This ensures that the route server always has the most current view of the network topology and can make optimal routing decisions.
The [Forwarding Information Base (FIB)](https://en.wikipedia.org/wiki/Forwarding_information_base) serves as a forwarding table for what route server has determined are the best-path routes in the RIB after evaluating all available routing information and policies. The FIB routes are installed on the route tables. The FIB is recomputed whenever there are changes to the RIB.
Type: String
Valid Values: `in-rib | in-fib`
Required: No

## See Also
<a name="API_RouteServerRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteServerRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteServerRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteServerRoute)
