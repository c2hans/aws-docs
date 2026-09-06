---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetRequestValidators.html
---

# GetRequestValidators
<a name="API_GetRequestValidators"></a>

Gets the RequestValidators collection of a given RestApi.

## Request Syntax
<a name="API_GetRequestValidators_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/requestvalidators?limit={{limit}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRequestValidators_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_GetRequestValidators_RequestSyntax) **   <a name="apigw-GetRequestValidators-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [position](#API_GetRequestValidators_RequestSyntax) **   <a name="apigw-GetRequestValidators-request-uri-position"></a>
The current pagination position in the paged result set.

 ** [restapi\_id](#API_GetRequestValidators_RequestSyntax) **   <a name="apigw-GetRequestValidators-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetRequestValidators_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRequestValidators_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "id": "string",
         "name": "string",
         "validateRequestBody": boolean,
         "validateRequestParameters": boolean
      }
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetRequestValidators_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetRequestValidators_ResponseSyntax) **   <a name="apigw-GetRequestValidators-response-item"></a>
The current page of elements from this collection.
Type: Array of [RequestValidator](API_RequestValidator.md) objects

 ** [position](#API_GetRequestValidators_ResponseSyntax) **   <a name="apigw-GetRequestValidators-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetRequestValidators_Errors"></a>

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
<a name="API_GetRequestValidators_Examples"></a>

### Get the RequestValidators collection of an API
<a name="API_GetRequestValidators_Example_1"></a>

This example illustrates one usage of GetRequestValidators.

#### Sample Request
<a name="API_GetRequestValidators_Example_1_Request"></a>

```
GET /restapis/mkhqppt4e4/requestvalidators HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T172652Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetRequestValidators_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-requestvalidator-{rel}.html",
      "name": "requestvalidator",
      "templated": true
    },
    "self": {
      "href": "/restapis/mkhqppt4e4/requestvalidators"
    },
    "item": [
      {
        "href": "/restapis/mkhqppt4e4/requestvalidators/1t3hul"
      },
      {
        "href": "/restapis/mkhqppt4e4/requestvalidators/8sbwvf"
      }
    ],
    "requestvalidator:by-id": {
      "href": "/restapis/mkhqppt4e4/requestvalidators/{requestvalidator_id}",
      "templated": true
    },
    "requestvalidator:create": {
      "href": "/restapis/mkhqppt4e4/requestvalidators"
    }
  },
  "_embedded": {
    "item": [
      {
        "_links": {
          "self": {
            "href": "/restapis/mkhqppt4e4/requestvalidators/1t3hul"
          },
          "request-validator-delete": {
            "href": "/restapis/mkhqppt4e4/requestvalidators/1t3hul"
          },
          "request-validator-update": {
            "href": "/restapis/mkhqppt4e4/requestvalidators/1t3hul"
          }
        },
        "id": "1t3hul",
        "name": "params-only",
        "validateRequestBody": false,
        "validateRequestParameters": true
      },
      {
        "_links": {
          "self": {
            "href": "/restapis/mkhqppt4e4/requestvalidators/8sbwvf"
          },
          "request-validator-delete": {
            "href": "/restapis/mkhqppt4e4/requestvalidators/8sbwvf"
          },
          "request-validator-update": {
            "href": "/restapis/mkhqppt4e4/requestvalidators/8sbwvf"
          }
        },
        "id": "8sbwvf",
        "name": "all",
        "validateRequestBody": true,
        "validateRequestParameters": true
      }
    ]
  }
}
```

## See Also
<a name="API_GetRequestValidators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetRequestValidators)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetRequestValidators)
