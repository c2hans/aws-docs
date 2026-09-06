---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_OdbPeeringConnection.html
---

# OdbPeeringConnection
<a name="API_OdbPeeringConnection"></a>

A peering connection between an ODB network and either another ODB network or a customer-owned VPC.

## Contents
<a name="API_OdbPeeringConnection_Contents"></a>

 ** odbPeeringConnectionId **   <a name="odb-Type-OdbPeeringConnection-odbPeeringConnectionId"></a>
The unique identifier of the ODB peering connection. A sample ID is `odbpcx-abcdefgh12345678`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** createdAt **   <a name="odb-Type-OdbPeeringConnection-createdAt"></a>
The timestamp when the ODB peering connection was created.
Type: Timestamp
Required: No

 ** displayName **   <a name="odb-Type-OdbPeeringConnection-displayName"></a>
The display name of the ODB peering connection.
Type: String
Required: No

 ** odbNetworkArn **   <a name="odb-Type-OdbPeeringConnection-odbNetworkArn"></a>
The Amazon Resource Name (ARN) of the ODB network that initiated the peering connection.
Type: String
Required: No

 ** odbPeeringConnectionArn **   <a name="odb-Type-OdbPeeringConnection-odbPeeringConnectionArn"></a>
The Amazon Resource Name (ARN) of the ODB peering connection.
Example: `arn:aws:odb:us-east-1:123456789012:odb-peering-connection/odbpcx-abcdefgh12345678`
Type: String
Required: No

 ** odbPeeringConnectionType **   <a name="odb-Type-OdbPeeringConnection-odbPeeringConnectionType"></a>
The type of the ODB peering connection.
Valid Values: `ODB-VPC | ODB-ODB`
Type: String
Required: No

 ** peerNetworkArn **   <a name="odb-Type-OdbPeeringConnection-peerNetworkArn"></a>
The Amazon Resource Name (ARN) of the peer network.
Type: String
Required: No

 ** peerNetworkCidrs **   <a name="odb-Type-OdbPeeringConnection-peerNetworkCidrs"></a>
The CIDR blocks associated with the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `(?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)\/(?:[1-2][0-9]|3[0-2]|[1-9])`
Required: No

 ** percentProgress **   <a name="odb-Type-OdbPeeringConnection-percentProgress"></a>
The percentage progress of the ODB peering connection creation or deletion.
Type: Float
Required: No

 ** status **   <a name="odb-Type-OdbPeeringConnection-status"></a>
The status of the ODB peering connection.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-OdbPeeringConnection-statusReason"></a>
The reason for the current status of the ODB peering connection.
Type: String
Required: No

## See Also
<a name="API_OdbPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/OdbPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/OdbPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/OdbPeeringConnection)
