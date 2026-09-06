---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayRouteTableRoute.html
---

# TransitGatewayRouteTableRoute
<a name="API_TransitGatewayRouteTableRoute"></a>

Describes a route in a transit gateway route table.

## Contents
<a name="API_TransitGatewayRouteTableRoute_Contents"></a>

 ** attachmentId **
The ID of the route attachment.
Type: String
Required: No

 ** destinationCidr **
The CIDR block used for destination matches.
Type: String
Required: No

 ** prefixListId **
The ID of the prefix list.
Type: String
Required: No

 ** resourceId **
The ID of the resource for the route attachment.
Type: String
Required: No

 ** resourceType **
The resource type for the route attachment.
Type: String
Required: No

 ** routeOrigin **
The route origin. The following are the possible values:
+ static
+ propagated
Type: String
Required: No

 ** state **
The state of the route.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayRouteTableRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayRouteTableRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayRouteTableRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayRouteTableRoute)
