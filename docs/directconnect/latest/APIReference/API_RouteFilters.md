---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_RouteFilters.html
---

# RouteFilters
<a name="API_RouteFilters"></a>

The filters used to limit the routes returned by [ListVirtualInterfaceRoutes](API_ListVirtualInterfaceRoutes.md).

## Contents
<a name="API_RouteFilters_Contents"></a>

 ** addressFamily **   <a name="DX-Type-RouteFilters-addressFamily"></a>
The address family of the routes to return.
The valid values are `ipv4` and `ipv6`.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** asPath **   <a name="DX-Type-RouteFilters-asPath"></a>
The autonomous system (AS) numbers used to filter the routes by their AS path.
Type: Array of longs
Required: No

 ** cidrs **   <a name="DX-Type-RouteFilters-cidrs"></a>
The CIDRs (prefixes) used to filter the routes. You can specify up to 10 CIDRs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** communities **   <a name="DX-Type-RouteFilters-communities"></a>
The BGP communities used to filter the routes.
Type: Array of strings
Required: No

 ** routeDirection **   <a name="DX-Type-RouteFilters-routeDirection"></a>
The direction of the routes to return.
The valid values are `accepted` (routes received from the customer network) and `advertised` (routes advertised to the customer network).
Type: String
Valid Values: `accepted | advertised`
Required: No

## See Also
<a name="API_RouteFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/RouteFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/RouteFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/RouteFilters)
