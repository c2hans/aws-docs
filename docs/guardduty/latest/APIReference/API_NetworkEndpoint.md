---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_NetworkEndpoint.html
---

# NetworkEndpoint
<a name="API_NetworkEndpoint"></a>

Contains information about network endpoints that were observed in the attack sequence.

## Contents
<a name="API_NetworkEndpoint_Contents"></a>

 ** id **   <a name="guardduty-Type-NetworkEndpoint-id"></a>
The ID of the network endpoint.
Type: String
Required: Yes

 ** autonomousSystem **   <a name="guardduty-Type-NetworkEndpoint-autonomousSystem"></a>
The Autonomous System (AS) of the network endpoint.
Type: [AutonomousSystem](API_AutonomousSystem.md) object
Required: No

 ** connection **   <a name="guardduty-Type-NetworkEndpoint-connection"></a>
Information about the network connection.
Type: [NetworkConnection](API_NetworkConnection.md) object
Required: No

 ** domain **   <a name="guardduty-Type-NetworkEndpoint-domain"></a>
The domain information for the network endpoint.
Type: String
Required: No

 ** ip **   <a name="guardduty-Type-NetworkEndpoint-ip"></a>
The IP address associated with the network endpoint.
Type: String
Required: No

 ** location **   <a name="guardduty-Type-NetworkEndpoint-location"></a>
Information about the location of the network endpoint.
Type: [NetworkGeoLocation](API_NetworkGeoLocation.md) object
Required: No

 ** port **   <a name="guardduty-Type-NetworkEndpoint-port"></a>
The port number associated with the network endpoint.
Type: Integer
Required: No

## See Also
<a name="API_NetworkEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/NetworkEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/NetworkEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/NetworkEndpoint)
