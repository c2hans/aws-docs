---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetAuthorizers.html
---

# GetAuthorizers
<a name="API_GetAuthorizers"></a>

Describe an existing Authorizers resource.

## Request Syntax
<a name="API_GetAuthorizers_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/authorizers?limit={{limit}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAuthorizers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_GetAuthorizers_RequestSyntax) **   <a name="apigw-GetAuthorizers-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [position](#API_GetAuthorizers_RequestSyntax) **   <a name="apigw-GetAuthorizers-request-uri-position"></a>
The current pagination position in the paged result set.

 ** [restapi\_id](#API_GetAuthorizers_RequestSyntax) **   <a name="apigw-GetAuthorizers-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetAuthorizers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAuthorizers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "authorizerCredentials": "string",
         "authorizerResultTtlInSeconds": number,
         "authorizerUri": "string",
         "authType": "string",
         "id": "string",
         "identitySource": "string",
         "identityValidationExpression": "string",
         "name": "string",
         "providerARNs": [ "string" ],
         "type": "string"
      }
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetAuthorizers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetAuthorizers_ResponseSyntax) **   <a name="apigw-GetAuthorizers-response-item"></a>
The current page of elements from this collection.
Type: Array of [Authorizer](API_Authorizer.md) objects

 ** [position](#API_GetAuthorizers_ResponseSyntax) **   <a name="apigw-GetAuthorizers-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetAuthorizers_Errors"></a>

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
<a name="API_GetAuthorizers_Examples"></a>

### Get the collection of custom authorizers defined for an API
<a name="API_GetAuthorizers_Example_1"></a>

This example illustrates one usage of GetAuthorizers.

#### Sample Request
<a name="API_GetAuthorizers_Example_1_Request"></a>

```
GET /restapis/86l3267lf6/authorizers HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
Content-Length: 60
X-Amz-Date: 20170223T175134Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetAuthorizers_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-authorizer-{rel}.html",
      "name": "authorizer",
      "templated": true
    },
    "self": {
      "href": "/restapis/86l3267lf6/authorizers"
    },
    "authorizer:by-id": {
      "href": "/restapis/86l3267lf6/authorizers/{authorizer_id}",
      "templated": true
    },
    "authorizer:create": {
      "href": "/restapis/86l3267lf6/authorizers"
    },
    "item": {
      "href": "/restapis/86l3267lf6/authorizers/bs9803"
    }
  },
  "_embedded": {
    "item": {
      "_links": {
        "self": {
          "href": "/restapis/86l3267lf6/authorizers/bs9803"
        },
        "authorizer:delete": {
          "href": "/restapis/86l3267lf6/authorizers/bs9803"
        },
        "authorizer:update": {
          "href": "/restapis/86l3267lf6/authorizers/bs9803"
        }
      },
      "authType": "custom",
      "authorizerResultTtlInSeconds": 300,
      "authorizerUri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:myCustomAuthorizer/invocations",
      "id": "bs9803",
      "identitySource": "method.request.header.Authorization",
      "name": "myCustomAuth",
      "type": "TOKEN"
    }
  }
}
```

## See Also
<a name="API_GetAuthorizers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetAuthorizers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetAuthorizers)
