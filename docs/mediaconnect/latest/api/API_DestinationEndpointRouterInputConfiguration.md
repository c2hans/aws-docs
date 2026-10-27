---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DestinationEndpointRouterInputConfiguration.html
---

# DestinationEndpointRouterInputConfiguration
<a name="API_DestinationEndpointRouterInputConfiguration"></a>

Configuration settings for a router input that is represented by a destination endpoint.

## Contents
<a name="API_DestinationEndpointRouterInputConfiguration_Contents"></a>

 ** endpointLifecycleManagement **   <a name="mediaconnect-Type-DestinationEndpointRouterInputConfiguration-endpointLifecycleManagement"></a>
The entity that manages the lifecycle of the associated destination endpoint. Valid values include the following:
+  `MANAGED` – MediaConnect manages the lifecycle of the associated destination endpoint.
+  `UNMANAGED` – You manage the lifecycle of the associated destination endpoint.
Type: String
Valid Values: `MANAGED | UNMANAGED`
Required: Yes

 ** sourceTransitDecryption **   <a name="mediaconnect-Type-DestinationEndpointRouterInputConfiguration-sourceTransitDecryption"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
Type: [EndpointEncryptionConfiguration](API_EndpointEncryptionConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sourceTransitDecryptionType **   <a name="mediaconnect-Type-DestinationEndpointRouterInputConfiguration-sourceTransitDecryptionType"></a>
The type of transit decryption applied to the source content that this router input receives. Valid values include the following:
+  `SECRETS_MANAGER` – The decryption key or passphrase is stored in AWS Secrets Manager.
+  `AUTOMATIC` – MediaConnect determines the decryption key when the endpoint connects.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

## See Also
<a name="API_DestinationEndpointRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DestinationEndpointRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DestinationEndpointRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DestinationEndpointRouterInputConfiguration)
