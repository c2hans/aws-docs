---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UDPEndpoint.html
---

# UDPEndpoint
<a name="API_UDPEndpoint"></a>

The domain name and port information for a UDP endpoint.

For Amazon GameLift Servers ping beacons, this endpoint is a fixed address that remains available as long as Amazon GameLift Servers supports game hosting in that location. For more information on UDP ping beacons, including guidance on how to implement latency measurements and best practices for caching beacon endpoints, refer to [UDP ping beacons](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-udp-ping-beacons.html) in the Amazon GameLift Servers Developer Guide.

## Contents
<a name="API_UDPEndpoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Domain **   <a name="gameliftservers-Type-UDPEndpoint-Domain"></a>
The domain name of the UDP endpoint.
For Amazon GameLift Servers ping beacons, this is typically in the format `gamelift-ping.<region>.api.aws` for AWS Regions, and `gamelift-ping-<local-zone-code>.<region>.api.aws` for AWS Local Zones.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Port **   <a name="gameliftservers-Type-UDPEndpoint-Port"></a>
The port number of the UDP endpoint. For Amazon GameLift Servers ping beacons, this is typically port 7770.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_UDPEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UDPEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UDPEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UDPEndpoint)
