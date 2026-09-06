---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetClientCertificate.html
---

# GetClientCertificate
<a name="API_GetClientCertificate"></a>

Gets information about the current ClientCertificate resource.

## Request Syntax
<a name="API_GetClientCertificate_RequestSyntax"></a>

```
GET /clientcertificates/{{clientcertificate_id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetClientCertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientcertificate\_id](#API_GetClientCertificate_RequestSyntax) **   <a name="apigw-GetClientCertificate-request-uri-clientCertificateId"></a>
The identifier of the ClientCertificate resource to be described.
Required: Yes

## Request Body
<a name="API_GetClientCertificate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetClientCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientCertificateId": "string",
   "createdDate": number,
   "description": "string",
   "expirationDate": number,
   "pemEncodedCertificate": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetClientCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientCertificateId](#API_GetClientCertificate_ResponseSyntax) **   <a name="apigw-GetClientCertificate-response-clientCertificateId"></a>
The identifier of the client certificate.
Type: String

 ** [createdDate](#API_GetClientCertificate_ResponseSyntax) **   <a name="apigw-GetClientCertificate-response-createdDate"></a>
The timestamp when the client certificate was created.
Type: Timestamp

 ** [description](#API_GetClientCertificate_ResponseSyntax) **   <a name="apigw-GetClientCertificate-response-description"></a>
The description of the client certificate.
Type: String

 ** [expirationDate](#API_GetClientCertificate_ResponseSyntax) **   <a name="apigw-GetClientCertificate-response-expirationDate"></a>
The timestamp when the client certificate will expire.
Type: Timestamp

 ** [pemEncodedCertificate](#API_GetClientCertificate_ResponseSyntax) **   <a name="apigw-GetClientCertificate-response-pemEncodedCertificate"></a>
The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .
Type: String

 ** [tags](#API_GetClientCertificate_ResponseSyntax) **   <a name="apigw-GetClientCertificate-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

## Errors
<a name="API_GetClientCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_GetClientCertificate_Examples"></a>

### Get the client certificate of a given identifier
<a name="API_GetClientCertificate_Example_1"></a>

This example illustrates one usage of GetClientCertificate.

#### Sample Request
<a name="API_GetClientCertificate_Example_1_Request"></a>

```
GET /clientcertificates/9ao60f HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160615T225614Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160615/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetClientCertificate_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-clientcertificate-{rel}.html",
      "name": "clientcertificate",
      "templated": true
    },
    "self": {
      "href": "/clientcertificates/9ao60f"
    },
    "clientcertificate:delete": {
      "href": "/clientcertificates/9ao60f"
    },
    "clientcertificate:update": {
      "href": "/clientcertificates/9ao60f"
    }
  },
  "clientCertificateId": "9ao60f",
  "createdDate": "2016-06-15T22:33:13Z",
  "description": "my second client-side cert",
  "expirationDate": "2017-06-15T22:33:13Z",
  "pemEncodedCertificate": "-----BEGIN CERTIFICATE-----\r\nMIIC6TC...yQAGEHvs=\r\n-----END CERTIFICATE-----"
}
```

## See Also
<a name="API_GetClientCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetClientCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetClientCertificate)
