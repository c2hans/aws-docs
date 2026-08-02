---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_TunnelSummary.html
---

# TunnelSummary
<a name="API_iot-secure-tunneling_TunnelSummary"></a>

Information about the tunnel.

## Contents
<a name="API_iot-secure-tunneling_TunnelSummary_Contents"></a>

 ** createdAt **   <a name="iot-Type-iot-secure-tunneling_TunnelSummary-createdAt"></a>
The time the tunnel was created.
Type: Timestamp
Required: No

 ** description **   <a name="iot-Type-iot-secure-tunneling_TunnelSummary-description"></a>
A description of the tunnel.
Type: String
Pattern: `[^\p{C}]{1,2048}`
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-iot-secure-tunneling_TunnelSummary-lastUpdatedAt"></a>
The time the tunnel was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-iot-secure-tunneling_TunnelSummary-status"></a>
The status of a tunnel. Valid values are: Open and Closed.
Type: String
Valid Values: `OPEN | CLOSED`
Required: No

 ** tunnelArn **   <a name="iot-Type-iot-secure-tunneling_TunnelSummary-tunnelArn"></a>
The Amazon Resource Name of the tunnel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** tunnelId **   <a name="iot-Type-iot-secure-tunneling_TunnelSummary-tunnelId"></a>
The unique alpha-numeric identifier for the tunnel.
Type: String
Pattern: `[a-zA-Z0-9_\-+=:]{1,128}`
Required: No

## See Also
<a name="API_iot-secure-tunneling_TunnelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/TunnelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/TunnelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/TunnelSummary)
