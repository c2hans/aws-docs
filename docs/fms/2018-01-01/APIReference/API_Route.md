---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Route.html
---

# Route
<a name="API_Route"></a>

Describes a route in a route table.

## Contents
<a name="API_Route_Contents"></a>

 ** Destination **   <a name="fms-Type-Route-Destination"></a>
The destination of the route.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** DestinationType **   <a name="fms-Type-Route-DestinationType"></a>
The type of destination for the route.
Type: String
Valid Values: `IPV4 | IPV6 | PREFIX_LIST`
Required: No

 ** Target **   <a name="fms-Type-Route-Target"></a>
The route's target.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** TargetType **   <a name="fms-Type-Route-TargetType"></a>
The type of target for the route.
Type: String
Valid Values: `GATEWAY | CARRIER_GATEWAY | INSTANCE | LOCAL_GATEWAY | NAT_GATEWAY | NETWORK_INTERFACE | VPC_ENDPOINT | VPC_PEERING_CONNECTION | EGRESS_ONLY_INTERNET_GATEWAY | TRANSIT_GATEWAY`
Required: No

## See Also
<a name="API_Route_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/Route)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/Route)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/Route)
