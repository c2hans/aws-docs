---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetClientCertificates.html
---

# GetClientCertificates
<a name="API_GetClientCertificates"></a>

Gets a collection of ClientCertificate resources.

## Request Syntax
<a name="API_GetClientCertificates_RequestSyntax"></a>

```
GET /clientcertificates?limit={{limit}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetClientCertificates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_GetClientCertificates_RequestSyntax) **   <a name="apigw-GetClientCertificates-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [position](#API_GetClientCertificates_RequestSyntax) **   <a name="apigw-GetClientCertificates-request-uri-position"></a>
The current pagination position in the paged result set.

## Request Body
<a name="API_GetClientCertificates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetClientCertificates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
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
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetClientCertificates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetClientCertificates_ResponseSyntax) **   <a name="apigw-GetClientCertificates-response-item"></a>
The current page of elements from this collection.
Type: Array of [ClientCertificate](API_ClientCertificate.md) objects

 ** [position](#API_GetClientCertificates_ResponseSyntax) **   <a name="apigw-GetClientCertificates-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetClientCertificates_Errors"></a>

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
<a name="API_GetClientCertificates_Examples"></a>

### Retrieve client certificates
<a name="API_GetClientCertificates_Example_1"></a>

The following example request retrieves the available client certificates in the caller's AWS account.

A successful response returns the requested `ClientCertificate` resources that can be navigated to by following the linked item or examining the embedded item resource.

#### Sample Request
<a name="API_GetClientCertificates_Example_1_Request"></a>

```
GET /clientcertificates HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160601T175605Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetClientCertificates_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-clientcertificate-{rel}.html",
      "name": "clientcertificate",
      "templated": true
    },
    "self": {
      "href": "/clientcertificates"
    },
    "clientcertificate:by-id": {
      "href": "/clientcertificates/{clientcertificate_id}",
      "templated": true
    },
    "clientcertificate:generate": {
      "href": "/clientcertificates"
    },
    "item": {
      "href": "/clientcertificates/xmbiqp"
    }
  },
  "_embedded": {
    "item": {
      "_links": {
        "self": {
          "href": "/clientcertificates/xmbiqp"
        },
        "clientcertificate:delete": {
          "href": "/clientcertificates/xmbiqp"
        },
        "clientcertificate:update": {
          "href": "/clientcertificates/xmbiqp"
        }
      },
      "clientCertificateId": "xmbiqp",get
      "createdDate": "2015-12-08T18:02:16Z",
      "description": "test-client-cert-2",
      "expirationDate": "2016-12-07T18:02:16Z",
      "pemEncodedCertificate": "-----BEGIN CERTIFICATE-----\r\nMIIC6DC...XuHVdZ5r27XRRXEjg==\r\n-----END CERTIFICATE-----"
    }
  }
}
```

## See Also
<a name="API_GetClientCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetClientCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetClientCertificates)
