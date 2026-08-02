---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PingBeacon.html
---

# PingBeacon
<a name="API_PingBeacon"></a>

Information about a UDP ping beacon that can be used to measure network latency between a player device and an Amazon GameLift Servers hosting location.

Ping beacons provide more accurate latency measurements than ICMP pings because they use UDP, which is the same protocol used by most game servers. For more information on UDP ping beacons, including guidance on how to implement latency measurements and best practices for caching beacon endpoints, refer to [UDP ping beacons](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-udp-ping-beacons.html) in the Amazon GameLift Servers Developer Guide.

## Contents
<a name="API_PingBeacon_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** UDPEndpoint **   <a name="gameliftservers-Type-PingBeacon-UDPEndpoint"></a>
The domain name and port of the UDP ping beacon. Your game client can send UDP messages to this endpoint and receive responses to measure network latency.
Type: [UDPEndpoint](API_UDPEndpoint.md) object
Required: No

## See Also
<a name="API_PingBeacon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PingBeacon)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PingBeacon)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PingBeacon)
