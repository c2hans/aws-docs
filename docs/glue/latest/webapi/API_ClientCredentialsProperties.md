---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ClientCredentialsProperties.html
---

# ClientCredentialsProperties
<a name="API_ClientCredentialsProperties"></a>

OAuth2 client credentials configuration that defines the properties needed for the Client Credentials grant type flow.

## Contents
<a name="API_ClientCredentialsProperties_Contents"></a>

 ** ClientId **   <a name="Glue-Type-ClientCredentialsProperties-ClientId"></a>
The OAuth2 client identifier provided by the authorization server.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** ClientSecret **   <a name="Glue-Type-ClientCredentialsProperties-ClientSecret"></a>
The OAuth2 client secret provided by the authorization server.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** ContentType **   <a name="Glue-Type-ClientCredentialsProperties-ContentType"></a>
The content type to use for token requests, such as application/x-www-form-urlencoded or application/json.
Type: String
Valid Values: `APPLICATION_JSON | URL_ENCODED`
Required: No

 ** RequestMethod **   <a name="Glue-Type-ClientCredentialsProperties-RequestMethod"></a>
The HTTP method to use when making token requests, typically POST.
Type: String
Valid Values: `GET | POST`
Required: No

 ** Scope **   <a name="Glue-Type-ClientCredentialsProperties-Scope"></a>
The OAuth2 scope that defines the level of access requested for the client credentials flow.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** TokenUrl **   <a name="Glue-Type-ClientCredentialsProperties-TokenUrl"></a>
The token endpoint URL where the client will request access tokens using client credentials.
Type: [ConnectorProperty](API_ConnectorProperty.md) object
Required: No

 ** TokenUrlParameters **   <a name="Glue-Type-ClientCredentialsProperties-TokenUrlParameters"></a>
Additional parameters to include in token URL requests as key-value pairs.
Type: Array of [ConnectorProperty](API_ConnectorProperty.md) objects
Required: No

## See Also
<a name="API_ClientCredentialsProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ClientCredentialsProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ClientCredentialsProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ClientCredentialsProperties)
