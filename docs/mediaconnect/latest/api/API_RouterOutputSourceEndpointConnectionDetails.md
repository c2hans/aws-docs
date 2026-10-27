---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterOutputSourceEndpointConnectionDetails.html
---

# RouterOutputSourceEndpointConnectionDetails
<a name="API_RouterOutputSourceEndpointConnectionDetails"></a>

The connection details for a source endpoint that represents a router output.

## Contents
<a name="API_RouterOutputSourceEndpointConnectionDetails_Contents"></a>

 ** destinationDecryptionConfiguration **   <a name="mediaconnect-Type-RouterOutputSourceEndpointConnectionDetails-destinationDecryptionConfiguration"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
Type: [EndpointEncryptionConfiguration](API_EndpointEncryptionConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** destinationDecryptionType **   <a name="mediaconnect-Type-RouterOutputSourceEndpointConnectionDetails-destinationDecryptionType"></a>
The type of decryption that the destination uses for the connection.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

 ** destinationEndpointType **   <a name="mediaconnect-Type-RouterOutputSourceEndpointConnectionDetails-destinationEndpointType"></a>
The type of the connected destination endpoint.
Type: String
Valid Values: `STANDARD | ROUTER_INPUT`
Required: No

## See Also
<a name="API_RouterOutputSourceEndpointConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterOutputSourceEndpointConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterOutputSourceEndpointConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterOutputSourceEndpointConnectionDetails)
