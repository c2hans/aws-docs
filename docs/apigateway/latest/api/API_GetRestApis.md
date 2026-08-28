---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetRestApis.html
---

# GetRestApis
<a name="API_GetRestApis"></a>

Lists the RestApis resources for your collection.

## Request Syntax
<a name="API_GetRestApis_RequestSyntax"></a>

```
GET /restapis?limit={{limit}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRestApis_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_GetRestApis_RequestSyntax) **   <a name="apigw-GetRestApis-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [position](#API_GetRestApis_RequestSyntax) **   <a name="apigw-GetRestApis-request-uri-position"></a>
The current pagination position in the paged result set.

## Request Body
<a name="API_GetRestApis_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRestApis_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "apiKeySource": "string",
         "apiStatus": "string",
         "apiStatusMessage": "string",
         "binaryMediaTypes": [ "string" ],
         "createdDate": number,
         "description": "string",
         "disableExecuteApiEndpoint": boolean,
         "endpointAccessMode": "string",
         "endpointConfiguration": {
            "ipAddressType": "string",
            "types": [ "string" ],
            "vpcEndpointIds": [ "string" ]
         },
         "id": "string",
         "minimumCompressionSize": number,
         "name": "string",
         "policy": "string",
         "rootResourceId": "string",
         "securityPolicy": "string",
         "tags": {
            "string" : "string"
         },
         "version": "string",
         "warnings": [ "string" ]
      }
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetRestApis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetRestApis_ResponseSyntax) **   <a name="apigw-GetRestApis-response-item"></a>
The current page of elements from this collection.
Type: Array of [RestApi](API_RestApi.md) objects

 ** [position](#API_GetRestApis_ResponseSyntax) **   <a name="apigw-GetRestApis-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetRestApis_Errors"></a>

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
<a name="API_GetRestApis_Examples"></a>

### Retrieve REST APIs
<a name="API_GetRestApis_Example_1"></a>

The following example GET request retrieves one API from an account. The `limit` query string parameter is used to limit the quantity of the returned result. For illustrative purposes, we choose `limit=1`.

 A successful response returns an API that can be navigated to by following the linked item or examining the embedded item resource.

#### Sample Request
<a name="API_GetRestApis_Example_1_Request"></a>

```
GET /restapis?limit=1 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160531T233903Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetRestApis_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-authorizer-{rel}.html",
        "name": "authorizer",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-deployment-{rel}.html",
        "name": "deployment",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-model-{rel}.html",
        "name": "model",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-resource-{rel}.html",
        "name": "resource",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-restapi-{rel}.html",
        "name": "restapi",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-stage-{rel}.html",
        "name": "stage",
        "templated": true
      }
    ],
    "self": {
      "href": "/restapis?limit=1"
    },
    "item": {
      "href": "/restapis/0n1anifwvf"
    },
    "next": {
      "href": "/restapis?position=aWQ9UzBuMWFuaWZ3dmY%3D&limit=1"
    },
    "restapi:by-id": {
      "href": "/restapis/{restapi_id}",
      "templated": true
    },
    "restapi:create": {
      "href": "/restapis"
    },
    "restapi:put": {
      "href": "/restapis/{restapi_id}?failonwarnings=false{&mode}",
      "templated": true
    }
  },
  "_embedded": {
    "item": {
      "_links": {
        "self": {
          "href": "/restapis/0n1anifwvf"
        },
        "authorizer:by-id": {
          "href": "/restapis/0n1anifwvf/authorizers/{authorizer_id}",
          "templated": true
        },
        "authorizer:create": {
          "href": "/restapis/0n1anifwvf/authorizers"
        },
        "deployment:by-id": {
          "href": "/restapis/0n1anifwvf/deployments/{deployment_id}{?embed}",
          "templated": true
        },
        "deployment:create": {
          "href": "/restapis/0n1anifwvf/deployments"
        },
        "model:by-name": {
          "href": "/restapis/0n1anifwvf/models/{model_name}?flatten=false",
          "templated": true
        },
        "model:create": {
          "href": "/restapis/0n1anifwvf/models"
        },
        "resource:by-id": {
          "href": "/restapis/0n1anifwvf/resources/{resource_id}{?embed}",
          "templated": true
        },
        "resource:create": {
          "href": "/restapis/0n1anifwvf/resources/ny9qrywoj2"
        },
        "restapi:authorizers": {
          "href": "/restapis/0n1anifwvf/authorizers"
        },
        "restapi:delete": {
          "href": "/restapis/0n1anifwvf"
        },
        "restapi:deployments": {
          "href": "/restapis/0n1anifwvf/deployments{?limit}",
          "templated": true
        },
        "restapi:models": {
          "href": "/restapis/0n1anifwvf/models"
        },
        "restapi:resources": {
          "href": "/restapis/0n1anifwvf/resources{?limit,embed}",
          "templated": trueget
        },
        "restapi:stages": {
          "href": "/restapis/0n1anifwvf/stages{?deployment_id}",
          "templated": true
        },
        "restapi:update": {
          "href": "/restapis/0n1anifwvf"
        },
        "stage:by-name": {
          "href": "/restapis/0n1anifwvf/stages/{stage_name}",
          "templated": true
        },
        "stage:create": {
          "href": "/restapis/0n1anifwvf/stages"
        }
      },
      "createdDate": "2016-04-05T19:58:27Z",
      "description": "Your first API with Amazon API Gateway. This is a sample API that integrates via HTTP with our demo Pet Store endpoints",
      "id": "0n1anifwvf",
      "name": "PetStore"
    }
  }
}
```

## See Also
<a name="API_GetRestApis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetRestApis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetRestApis)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
