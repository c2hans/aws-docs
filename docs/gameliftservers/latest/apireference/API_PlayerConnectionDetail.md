---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlayerConnectionDetail.html
---

# PlayerConnectionDetail
<a name="API_PlayerConnectionDetail"></a>

Connection information for a game client to connect to a game session. This object contains the IP address(es), port(s), and authentication details your game client needs to establish a connection.

 **With player gateway enabled:** Contains relay endpoints and a player gateway token. Your game client must prepend player gateway token to each payload for validation and connection through relay endpoints.

 **With player gateway disabled:** Contains game server endpoint. Player gateway token and expiration fields are empty.

## Contents
<a name="API_PlayerConnectionDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Endpoints **   <a name="gameliftservers-Type-PlayerConnectionDetail-Endpoints"></a>
List of connection endpoints for the game client. Your game client uses these IP address(es) and port(s) to connect to the game session.
When player gateway is enabled, these are relay endpoints with benefits such as DDoS protection. When disabled, this is the game server endpoint.
Type: Array of [PlayerConnectionEndpoint](API_PlayerConnectionEndpoint.md) objects
Required: No

 ** Expiration **   <a name="gameliftservers-Type-PlayerConnectionDetail-Expiration"></a>
When player gateway is enabled, this is the timestamp indicating when player gateway token expires. Your game backend should call [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to retrieve fresh connection information for your game clients before this time. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
This value is empty when player gateway is disabled.
Type: Timestamp
Required: No

 ** PlayerGatewayToken **   <a name="gameliftservers-Type-PlayerConnectionDetail-PlayerGatewayToken"></a>
Access token that your game client must prepend to all traffic sent through player gateway. Player gateway verifies identity and authorizes connection based on this token.
This value is empty when player gateway is disabled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** PlayerId **   <a name="gameliftservers-Type-PlayerConnectionDetail-PlayerId"></a>
A unique identifier for a player associated with this connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_PlayerConnectionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PlayerConnectionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PlayerConnectionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PlayerConnectionDetail)
