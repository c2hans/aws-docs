---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDomainConfiguration.html
---

# DescribeDomainConfiguration
<a name="API_DescribeDomainConfiguration"></a>

Gets summary information about a domain configuration.

Requires permission to access the [DescribeDomainConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeDomainConfiguration_RequestSyntax"></a>

```
GET /domainConfigurations/{{domainConfigurationName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDomainConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainConfigurationName](#API_DescribeDomainConfiguration_RequestSyntax) **   <a name="iot-DescribeDomainConfiguration-request-uri-domainConfigurationName"></a>
The name of the domain configuration.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w.:-]+`
Required: Yes

## Request Body
<a name="API_DescribeDomainConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDomainConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationProtocol": "string",
   "authenticationType": "string",
   "authorizerConfig": {
      "allowAuthorizerOverride": boolean,
      "defaultAuthorizerName": "string"
   },
   "clientCertificateConfig": {
      "clientCertificateCallbackArn": "string"
   },
   "domainConfigurationArn": "string",
   "domainConfigurationName": "string",
   "domainConfigurationStatus": "string",
   "domainName": "string",
   "domainType": "string",
   "lastStatusChangeDate": number,
   "serverCertificateConfig": {
      "enableOCSPCheck": boolean,
      "ocspAuthorizedResponderArn": "string",
      "ocspLambdaArn": "string"
   },
   "serverCertificates": [
      {
         "serverCertificateArn": "string",
         "serverCertificateStatus": "string",
         "serverCertificateStatusDetail": "string"
      }
   ],
   "serviceType": "string",
   "tlsConfig": {
      "securityPolicy": "string"
   }
}
```

## Response Elements
<a name="API_DescribeDomainConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationProtocol](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-applicationProtocol"></a>
An enumerated string that speciﬁes the application-layer protocol.
+  `SECURE_MQTT` - MQTT over TLS.
+  `MQTT_WSS` - MQTT over WebSocket.
+  `HTTPS` - HTTP over TLS.
+  `DEFAULT` - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify application\_layer protocol. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html).
Type: String
Valid Values: `SECURE_MQTT | MQTT_WSS | HTTPS | DEFAULT`

 ** [authenticationType](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-authenticationType"></a>
An enumerated string that speciﬁes the authentication type.
+  `CUSTOM_AUTH_X509` - Use custom authentication and authorization with additional details from the X.509 client certificate.
+  `CUSTOM_AUTH` - Use custom authentication and authorization. For more information, see [Custom authentication and authorization](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html).
+  `AWS_X509` - Use X.509 client certificates without custom authentication and authorization. For more information, see [X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html).
+  `AWS_SIGV4` - Use AWS Signature Version 4. For more information, see [IAM users, groups, and roles](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html).
+  `DEFAULT` - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify authentication type. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html).
Type: String
Valid Values: `CUSTOM_AUTH_X509 | CUSTOM_AUTH | AWS_X509 | AWS_SIGV4 | DEFAULT`

 ** [authorizerConfig](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-authorizerConfig"></a>
An object that specifies the authorization service for a domain.
Type: [AuthorizerConfig](API_AuthorizerConfig.md) object

 ** [clientCertificateConfig](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-clientCertificateConfig"></a>
An object that speciﬁes the client certificate conﬁguration for a domain.
Type: [ClientCertificateConfig](API_ClientCertificateConfig.md) object

 ** [domainConfigurationArn](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-domainConfigurationArn"></a>
The ARN of the domain configuration.
Type: String

 ** [domainConfigurationName](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-domainConfigurationName"></a>
The name of the domain configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w.:-]+`

 ** [domainConfigurationStatus](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-domainConfigurationStatus"></a>
A Boolean value that specifies the current state of the domain configuration.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [domainName](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-domainName"></a>
The name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[\s\S]*`

 ** [domainType](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-domainType"></a>
The type of the domain.
Type: String
Valid Values: `ENDPOINT | AWS_MANAGED | CUSTOMER_MANAGED`

 ** [lastStatusChangeDate](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-lastStatusChangeDate"></a>
The date and time the domain configuration's status was last changed.
Type: Timestamp

 ** [serverCertificateConfig](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-serverCertificateConfig"></a>
The server certificate configuration.
Type: [ServerCertificateConfig](API_ServerCertificateConfig.md) object

 ** [serverCertificates](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-serverCertificates"></a>
A list containing summary information about the server certificate included in the domain configuration.
Type: Array of [ServerCertificateSummary](API_ServerCertificateSummary.md) objects

 ** [serviceType](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-serviceType"></a>
The type of service delivered by the endpoint.
Type: String
Valid Values: `DATA | CREDENTIAL_PROVIDER | JOBS`

 ** [tlsConfig](#API_DescribeDomainConfiguration_ResponseSyntax) **   <a name="iot-DescribeDomainConfiguration-response-tlsConfig"></a>
An object that specifies the TLS configuration for a domain.
Type: [TlsConfig](API_TlsConfig.md) object

## Errors
<a name="API_DescribeDomainConfiguration_Errors"></a>

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
<a name="API_DescribeDomainConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeDomainConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeDomainConfiguration)
