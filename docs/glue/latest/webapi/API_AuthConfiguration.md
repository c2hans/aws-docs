---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AuthConfiguration.html
---

# AuthConfiguration
<a name="API_AuthConfiguration"></a>

The authentication configuration for a connection returned by the `DescribeConnectionType` API.

## Contents
<a name="API_AuthConfiguration_Contents"></a>

 ** AuthenticationType **   <a name="Glue-Type-AuthConfiguration-AuthenticationType"></a>
The type of authentication for a connection.
Type: [Property](API_Property.md) object
Required: Yes

 ** BasicAuthenticationProperties **   <a name="Glue-Type-AuthConfiguration-BasicAuthenticationProperties"></a>
A map of key-value pairs for the OAuth2 properties. Each value is a a `Property` object.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** CustomAuthenticationProperties **   <a name="Glue-Type-AuthConfiguration-CustomAuthenticationProperties"></a>
A map of key-value pairs for the custom authentication properties. Each value is a a `Property` object.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** OAuth2Properties **   <a name="Glue-Type-AuthConfiguration-OAuth2Properties"></a>
A map of key-value pairs for the OAuth2 properties. Each value is a a `Property` object.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SecretArn **   <a name="Glue-Type-AuthConfiguration-SecretArn"></a>
The Amazon Resource Name (ARN) for the Secrets Manager.
Type: [Property](API_Property.md) object
Required: No

## See Also
<a name="API_AuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AuthConfiguration)
