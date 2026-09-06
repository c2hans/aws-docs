---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Route.html
---

# Route
<a name="API_Route"></a>

Information about a route for a virtual interface.

## Contents
<a name="API_Route_Contents"></a>

 ** addressFamily **   <a name="DX-Type-Route-addressFamily"></a>
The address family of the route.
The valid values are `ipv4` and `ipv6`.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** asPath **   <a name="DX-Type-Route-asPath"></a>
The autonomous system (AS) path of the route.
Type: Array of [AsPathSegment](API_AsPathSegment.md) objects
Required: No

 ** awsLogicalDeviceId **   <a name="DX-Type-Route-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String
Required: No

 ** cidr **   <a name="DX-Type-Route-cidr"></a>
The CIDR (prefix) of the route.
Type: String
Required: No

 ** communities **   <a name="DX-Type-Route-communities"></a>
The BGP communities associated with the route.
Type: Array of strings
Required: No

 ** routeDirection **   <a name="DX-Type-Route-routeDirection"></a>
The direction of the route.
The valid values are `accepted` (received from the customer network) and `advertised` (advertised to the customer network).
Type: String
Valid Values: `accepted | advertised`
Required: No

 ** routeInstalledAt **   <a name="DX-Type-Route-routeInstalledAt"></a>
The time when the route was installed. The value is displayed in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_Route_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/Route)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/Route)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/Route)
