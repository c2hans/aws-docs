---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteServerPropagation.html
---

# RouteServerPropagation
<a name="API_RouteServerPropagation"></a>

Describes the route propagation configuration between a route server and a route table.

When enabled, route server propagation installs the routes in the FIB on the route table you've specified. Route server supports IPv4 and IPv6 route propagation.

## Contents
<a name="API_RouteServerPropagation_Contents"></a>

 ** routeServerId **
The ID of the route server configured for route propagation.
Type: String
Required: No

 ** routeTableId **
The ID of the route table configured for route server propagation.
Type: String
Required: No

 ** state **
The current state of route propagation.
Type: String
Valid Values: `pending | available | deleting`
Required: No

## See Also
<a name="API_RouteServerPropagation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteServerPropagation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteServerPropagation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteServerPropagation)
