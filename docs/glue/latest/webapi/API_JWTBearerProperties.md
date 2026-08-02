---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JWTBearerProperties.html
---

# JWTBearerProperties
<a name="API_JWTBearerProperties"></a>

JWT bearer token configuration that defines the properties needed for the JWT Bearer grant type flow.

## Contents
<a name="API_JWTBearerProperties_Contents"></a>

 ** ContentType **   <a name="Glue-Type-JWTBearerProperties-ContentType"></a>
The content type to use for JWT bearer token requests, such as application/x-www-form-urlencoded or application/json.
Type: String
Valid Values: `APPLICATION_JSON | URL_ENCODED`
Required: No

 ** JwtToken **   <a name="Glue-Type-JWTBearerProperties-JwtToken"></a>
The JWT token to be used in the bearer token grant flow for authentication.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** RequestMethod **   <a name="Glue-Type-JWTBearerProperties-RequestMethod"></a>
The HTTP method to use when making JWT bearer token requests, typically POST.
Type: String
Valid Values: `GET | POST`
Required: No

 ** TokenUrl **   <a name="Glue-Type-JWTBearerProperties-TokenUrl"></a>
The token endpoint URL where the JWT bearer token will be exchanged for an access token.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** TokenUrlParameters **   <a name="Glue-Type-JWTBearerProperties-TokenUrlParameters"></a>
Additional parameters to include in token URL requests as key-value pairs.
Type: Array of [ConnectorProperty](API_ConnectorProperty.md) objects
Required: No

## See Also
<a name="API_JWTBearerProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JWTBearerProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JWTBearerProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JWTBearerProperties)
