---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_Tunnel.html
---

# Tunnel
<a name="API_iot-secure-tunneling_Tunnel"></a>

A connection between a source computer and a destination device.

## Contents
<a name="API_iot-secure-tunneling_Tunnel_Contents"></a>

 ** createdAt **   <a name="iot-Type-iot-secure-tunneling_Tunnel-createdAt"></a>
The time when the tunnel was created.
Type: Timestamp
Required: No

 ** description **   <a name="iot-Type-iot-secure-tunneling_Tunnel-description"></a>
A description of the tunnel.
Type: String
Pattern: `[^\p{C}]{1,2048}`
Required: No

 ** destinationConfig **   <a name="iot-Type-iot-secure-tunneling_Tunnel-destinationConfig"></a>
The destination configuration that specifies the thing name of the destination device and a service name that the local proxy uses to connect to the destination application.
Type: [DestinationConfig](API_iot-secure-tunneling_DestinationConfig.md) object
Required: No

 ** destinationConnectionState **   <a name="iot-Type-iot-secure-tunneling_Tunnel-destinationConnectionState"></a>
The connection state of the destination application.
Type: [ConnectionState](API_iot-secure-tunneling_ConnectionState.md) object
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-iot-secure-tunneling_Tunnel-lastUpdatedAt"></a>
The last time the tunnel was updated.
Type: Timestamp
Required: No

 ** sourceConnectionState **   <a name="iot-Type-iot-secure-tunneling_Tunnel-sourceConnectionState"></a>
The connection state of the source application.
Type: [ConnectionState](API_iot-secure-tunneling_ConnectionState.md) object
Required: No

 ** status **   <a name="iot-Type-iot-secure-tunneling_Tunnel-status"></a>
The status of a tunnel. Valid values are: Open and Closed.
Type: String
Valid Values: `OPEN | CLOSED`
Required: No

 ** tags **   <a name="iot-Type-iot-secure-tunneling_Tunnel-tags"></a>
A list of tag metadata associated with the secure tunnel.
Type: Array of [Tag](API_iot-secure-tunneling_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** timeoutConfig **   <a name="iot-Type-iot-secure-tunneling_Tunnel-timeoutConfig"></a>
Timeout configuration for the tunnel.
Type: [TimeoutConfig](API_iot-secure-tunneling_TimeoutConfig.md) object
Required: No

 ** tunnelArn **   <a name="iot-Type-iot-secure-tunneling_Tunnel-tunnelArn"></a>
The Amazon Resource Name (ARN) of a tunnel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** tunnelId **   <a name="iot-Type-iot-secure-tunneling_Tunnel-tunnelId"></a>
A unique alpha-numeric ID that identifies a tunnel.
Type: String
Pattern: `[a-zA-Z0-9_\-+=:]{1,128}`
Required: No

## See Also
<a name="API_iot-secure-tunneling_Tunnel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/Tunnel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/Tunnel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/Tunnel)
