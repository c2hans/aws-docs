---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDomainConfiguration.html
---

# UpdateDomainConfiguration
<a name="API_UpdateDomainConfiguration"></a>

Updates values stored in the domain configuration. Domain configurations for default endpoints can't be updated.

Requires permission to access the [UpdateDomainConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateDomainConfiguration_RequestSyntax"></a>

```
PUT /domainConfigurations/{{domainConfigurationName}} HTTP/1.1
Content-type: application/json

{
   "applicationProtocol": "{{string}}",
   "authenticationType": "{{string}}",
   "authorizerConfig": {
      "allowAuthorizerOverride": {{boolean}},
      "defaultAuthorizerName": "{{string}}"
   },
   "clientCertificateConfig": {
      "clientCertificateCallbackArn": "{{string}}"
   },
   "domainConfigurationStatus": "{{string}}",
   "removeAuthorizerConfig": {{boolean}},
   "serverCertificateConfig": {
      "enableOCSPCheck": {{boolean}},
      "ocspAuthorizedResponderArn": "{{string}}",
      "ocspLambdaArn": "{{string}}"
   },
   "tlsConfig": {
      "securityPolicy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateDomainConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainConfigurationName](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-uri-domainConfigurationName"></a>
The name of the domain configuration to be updated.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w.:-]+`
Required: Yes

## Request Body
<a name="API_UpdateDomainConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationProtocol](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-applicationProtocol"></a>
An enumerated string that speciﬁes the application-layer protocol.
+  `SECURE_MQTT` - MQTT over TLS.
+  `MQTT_WSS` - MQTT over WebSocket.
+  `HTTPS` - HTTP over TLS.
+  `DEFAULT` - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify application\_layer protocol. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html).
Type: String
Valid Values: `SECURE_MQTT | MQTT_WSS | HTTPS | DEFAULT`
Required: No

 ** [authenticationType](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-authenticationType"></a>
An enumerated string that speciﬁes the authentication type.
+  `CUSTOM_AUTH_X509` - Use custom authentication and authorization with additional details from the X.509 client certificate.
+  `CUSTOM_AUTH` - Use custom authentication and authorization. For more information, see [Custom authentication and authorization](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html).
+  `AWS_X509` - Use X.509 client certificates without custom authentication and authorization. For more information, see [X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html).
+  `AWS_SIGV4` - Use AWS Signature Version 4. For more information, see [IAM users, groups, and roles](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html).
+  `DEFAULT ` - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify authentication type. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html).
Type: String
Valid Values: `CUSTOM_AUTH_X509 | CUSTOM_AUTH | AWS_X509 | AWS_SIGV4 | DEFAULT`
Required: No

 ** [authorizerConfig](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-authorizerConfig"></a>
An object that specifies the authorization service for a domain.
Type: [AuthorizerConfig](API_AuthorizerConfig.md) object
Required: No

 ** [clientCertificateConfig](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-clientCertificateConfig"></a>
An object that speciﬁes the client certificate conﬁguration for a domain.
Type: [ClientCertificateConfig](API_ClientCertificateConfig.md) object
Required: No

 ** [domainConfigurationStatus](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-domainConfigurationStatus"></a>
The status to which the domain configuration should be updated.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [removeAuthorizerConfig](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-removeAuthorizerConfig"></a>
Removes the authorization configuration from a domain.
Type: Boolean
Required: No

 ** [serverCertificateConfig](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-serverCertificateConfig"></a>
The server certificate configuration.
Type: [ServerCertificateConfig](API_ServerCertificateConfig.md) object
Required: No

 ** [tlsConfig](#API_UpdateDomainConfiguration_RequestSyntax) **   <a name="iot-UpdateDomainConfiguration-request-tlsConfig"></a>
An object that specifies the TLS configuration for a domain.
Type: [TlsConfig](API_TlsConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateDomainConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainConfigurationArn": "string",
   "domainConfigurationName": "string"
}
```

## Response Elements
<a name="API_UpdateDomainConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainConfigurationArn](#API_UpdateDomainConfiguration_ResponseSyntax) **   <a name="iot-UpdateDomainConfiguration-response-domainConfigurationArn"></a>
The ARN of the domain configuration that was updated.
Type: String

 ** [domainConfigurationName](#API_UpdateDomainConfiguration_ResponseSyntax) **   <a name="iot-UpdateDomainConfiguration-response-domainConfigurationName"></a>
The name of the domain configuration that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w.:-]+`

## Errors
<a name="API_UpdateDomainConfiguration_Errors"></a>

 ** CertificateValidationException **
The certificate is invalid.
 ** message **
Additional information about the exception.
HTTP Status Code: 400

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_UpdateDomainConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateDomainConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateDomainConfiguration)
