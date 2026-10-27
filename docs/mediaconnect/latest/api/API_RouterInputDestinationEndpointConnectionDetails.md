---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputDestinationEndpointConnectionDetails.html
---

# RouterInputDestinationEndpointConnectionDetails
<a name="API_RouterInputDestinationEndpointConnectionDetails"></a>

The connection details for a destination endpoint that represents a router input.

## Contents
<a name="API_RouterInputDestinationEndpointConnectionDetails_Contents"></a>

 ** sourceEncryptionConfiguration **   <a name="mediaconnect-Type-RouterInputDestinationEndpointConnectionDetails-sourceEncryptionConfiguration"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
Type: [EndpointEncryptionConfiguration](API_EndpointEncryptionConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** sourceEncryptionType **   <a name="mediaconnect-Type-RouterInputDestinationEndpointConnectionDetails-sourceEncryptionType"></a>
The type of encryption that the source uses for the connection.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

 ** sourceEndpointType **   <a name="mediaconnect-Type-RouterInputDestinationEndpointConnectionDetails-sourceEndpointType"></a>
The type of the connected source endpoint.
Type: String
Valid Values: `STANDARD | ROUTER_OUTPUT`
Required: No

## See Also
<a name="API_RouterInputDestinationEndpointConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputDestinationEndpointConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputDestinationEndpointConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputDestinationEndpointConnectionDetails)
