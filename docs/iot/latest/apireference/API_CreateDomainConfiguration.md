---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDomainConfiguration.html
---

# CreateDomainConfiguration
<a name="API_CreateDomainConfiguration"></a>

Creates a domain configuration.

Requires permission to access the [CreateDomainConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateDomainConfiguration_RequestSyntax"></a>

```
POST /domainConfigurations/{{domainConfigurationName}} HTTP/1.1
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
   "domainName": "{{string}}",
   "serverCertificateArns": [ "{{string}}" ],
   "serverCertificateConfig": {
      "enableOCSPCheck": {{boolean}},
      "ocspAuthorizedResponderArn": "{{string}}",
      "ocspLambdaArn": "{{string}}"
   },
   "serviceType": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "tlsConfig": {
      "securityPolicy": "{{string}}"
   },
   "validationCertificateArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDomainConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainConfigurationName](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-uri-domainConfigurationName"></a>
The name of the domain configuration. This value must be unique to a region.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w.-]+`
Required: Yes

## Request Body
<a name="API_CreateDomainConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationProtocol](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-applicationProtocol"></a>
An enumerated string that speciﬁes the application-layer protocol.
+  `SECURE_MQTT` - MQTT over TLS.
+  `MQTT_WSS` - MQTT over WebSocket.
+  `HTTPS` - HTTP over TLS.
+  `DEFAULT` - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify application\_layer protocol. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html).
Type: String
Valid Values: `SECURE_MQTT | MQTT_WSS | HTTPS | DEFAULT`
Required: No

 ** [authenticationType](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-authenticationType"></a>
An enumerated string that speciﬁes the authentication type.
+  `CUSTOM_AUTH_X509` - Use custom authentication and authorization with additional details from the X.509 client certificate.
+  `CUSTOM_AUTH` - Use custom authentication and authorization. For more information, see [Custom authentication and authorization](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html).
+  `AWS_X509` - Use X.509 client certificates without custom authentication and authorization. For more information, see [X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html).
+  `AWS_SIGV4` - Use AWS Signature Version 4. For more information, see [IAM users, groups, and roles](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html).
+  `DEFAULT` - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify authentication type. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html).
Type: String
Valid Values: `CUSTOM_AUTH_X509 | CUSTOM_AUTH | AWS_X509 | AWS_SIGV4 | DEFAULT`
Required: No

 ** [authorizerConfig](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-authorizerConfig"></a>
An object that specifies the authorization service for a domain.
Type: [AuthorizerConfig](API_AuthorizerConfig.md) object
Required: No

 ** [clientCertificateConfig](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-clientCertificateConfig"></a>
An object that speciﬁes the client certificate conﬁguration for a domain.
Type: [ClientCertificateConfig](API_ClientCertificateConfig.md) object
Required: No

 ** [domainName](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-domainName"></a>
The name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[\s\S]*`
Required: No

 ** [serverCertificateArns](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-serverCertificateArns"></a>
The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for AWS-managed domains.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\d{1}:\d{12}:certificate/[a-zA-Z0-9/-]+`
Required: No

 ** [serverCertificateConfig](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-serverCertificateConfig"></a>
The server certificate configuration.
Type: [ServerCertificateConfig](API_ServerCertificateConfig.md) object
Required: No

 ** [serviceType](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-serviceType"></a>
The type of service delivered by the endpoint.
 AWS IoT Core currently supports only the `DATA` service type.
Type: String
Valid Values: `DATA | CREDENTIAL_PROVIDER | JOBS`
Required: No

 ** [tags](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-tags"></a>
Metadata which can be used to manage the domain configuration.
For URI Request parameters use format: ...key1=value1&key2=value2...
For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."
For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [tlsConfig](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-tlsConfig"></a>
An object that specifies the TLS configuration for a domain.
Type: [TlsConfig](API_TlsConfig.md) object
Required: No

 ** [validationCertificateArn](#API_CreateDomainConfiguration_RequestSyntax) **   <a name="iot-CreateDomainConfiguration-request-validationCertificateArn"></a>
The certificate used to validate the server certificate and prove domain name ownership. This certificate must be signed by a public certificate authority. This value is not required for AWS-managed domains.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\d{1}:\d{12}:certificate/[a-zA-Z0-9/-]+`
Required: No

## Response Syntax
<a name="API_CreateDomainConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainConfigurationArn": "string",
   "domainConfigurationName": "string"
}
```

## Response Elements
<a name="API_CreateDomainConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainConfigurationArn](#API_CreateDomainConfiguration_ResponseSyntax) **   <a name="iot-CreateDomainConfiguration-response-domainConfigurationArn"></a>
The ARN of the domain configuration.
Type: String

 ** [domainConfigurationName](#API_CreateDomainConfiguration_ResponseSyntax) **   <a name="iot-CreateDomainConfiguration-response-domainConfigurationName"></a>
The name of the domain configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w.-]+`

## Errors
<a name="API_CreateDomainConfiguration_Errors"></a>

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

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

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
<a name="API_CreateDomainConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateDomainConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateDomainConfiguration)
