---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardDestinationEndpointConnectionDetails.html
---

# StandardDestinationEndpointConnectionDetails
<a name="API_StandardDestinationEndpointConnectionDetails"></a>

The connection details for a standard destination endpoint.

## Contents
<a name="API_StandardDestinationEndpointConnectionDetails_Contents"></a>

 ** sourceEncryptionConfiguration **   <a name="mediaconnect-Type-StandardDestinationEndpointConnectionDetails-sourceEncryptionConfiguration"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
Type: [EndpointEncryptionConfiguration](API_EndpointEncryptionConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** sourceEncryptionType **   <a name="mediaconnect-Type-StandardDestinationEndpointConnectionDetails-sourceEncryptionType"></a>
The type of encryption that the source uses for the connection.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

 ** sourceEndpointType **   <a name="mediaconnect-Type-StandardDestinationEndpointConnectionDetails-sourceEndpointType"></a>
The type of the connected source endpoint.
Type: String
Valid Values: `STANDARD | ROUTER_OUTPUT`
Required: No

 ** sourceIpAddress **   <a name="mediaconnect-Type-StandardDestinationEndpointConnectionDetails-sourceIpAddress"></a>
The IP address of the source that is connected to the destination endpoint.
Type: String
Required: No

 ** sourceListenerPort **   <a name="mediaconnect-Type-StandardDestinationEndpointConnectionDetails-sourceListenerPort"></a>
The port on which the source listens for the connection.
Type: Integer
Required: No

## See Also
<a name="API_StandardDestinationEndpointConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardDestinationEndpointConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardDestinationEndpointConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardDestinationEndpointConnectionDetails)
