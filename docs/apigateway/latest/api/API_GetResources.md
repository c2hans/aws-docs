---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetResources.html
---

# GetResources
<a name="API_GetResources"></a>

Lists information about a collection of Resource resources.

## Request Syntax
<a name="API_GetResources_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/resources?embed={{embed}}&limit={{limit}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [embed](#API_GetResources_RequestSyntax) **   <a name="apigw-GetResources-request-uri-embed"></a>
A query parameter used to retrieve the specified resources embedded in the returned Resources resource in the response. This `embed` parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the `"methods"` string. For example, `GET /restapis/{restapi_id}/resources?embed=methods`.

 ** [limit](#API_GetResources_RequestSyntax) **   <a name="apigw-GetResources-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [position](#API_GetResources_RequestSyntax) **   <a name="apigw-GetResources-request-uri-position"></a>
The current pagination position in the paged result set.

 ** [restapi\_id](#API_GetResources_RequestSyntax) **   <a name="apigw-GetResources-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetResources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "id": "string",
         "parentId": "string",
         "path": "string",
         "pathPart": "string",
         "resourceMethods": {
            "string" : {
               "apiKeyRequired": boolean,
               "authorizationScopes": [ "string" ],
               "authorizationType": "string",
               "authorizerId": "string",
               "httpMethod": "string",
               "methodIntegration": {
                  "cacheKeyParameters": [ "string" ],
                  "cacheNamespace": "string",
                  "connectionId": "string",
                  "connectionType": "string",
                  "contentHandling": "string",
                  "credentials": "string",
                  "httpMethod": "string",
                  "integrationResponses": {
                     "string" : {
                        "contentHandling": "string",
                        "responseParameters": {
                           "string" : "string"
                        },
                        "responseTemplates": {
                           "string" : "string"
                        },
                        "selectionPattern": "string",
                        "statusCode": "string"
                     }
                  },
                  "integrationTarget": "string",
                  "passthroughBehavior": "string",
                  "requestParameters": {
                     "string" : "string"
                  },
                  "requestTemplates": {
                     "string" : "string"
                  },
                  "responseTransferMode": "string",
                  "timeoutInMillis": number,
                  "tlsConfig": {
                     "insecureSkipVerification": boolean
                  },
                  "type": "string",
                  "uri": "string"
               },
               "methodResponses": {
                  "string" : {
                     "responseModels": {
                        "string" : "string"
                     },
                     "responseParameters": {
                        "string" : boolean
                     },
                     "statusCode": "string"
                  }
               },
               "operationName": "string",
               "requestModels": {
                  "string" : "string"
               },
               "requestParameters": {
                  "string" : boolean
               },
               "requestValidatorId": "string"
            }
         }
      }
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetResources_ResponseSyntax) **   <a name="apigw-GetResources-response-item"></a>
The current page of elements from this collection.
Type: Array of [Resource](API_Resource.md) objects

 ** [position](#API_GetResources_ResponseSyntax) **   <a name="apigw-GetResources-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetResources_Errors"></a>

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
<a name="API_GetResources_Examples"></a>

### Get an API resource collection
<a name="API_GetResources_Example_1"></a>

This example illustrates one usage of GetResources.

#### Sample Request
<a name="API_GetResources_Example_1_Request"></a>

```
GET /restapis/fugvjdxtri/resources HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160602T173305Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160602/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
Response
```

#### Sample Response
<a name="API_GetResources_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html",
        "name": "method",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-resource-{rel}.html",
        "name": "resource",
        "templated": true
      }
    ],
    "self": {
      "href": "/restapis/fugvjdxtri/resources"
    },
    "item": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2"
    },
    "resource:by-id": {
      "href": "/restapis/fugvjdxtri/resources/{resource_id}{?embed}",
      "templated": true
    },
    "resource:create": {
      "href": "/restapis/fugvjdxtri/resources/{parent_id}",
      "templated": true
    }
  },
  "_embedded": {
    "item": {
      "_links": {
        "self": {
          "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2"
        },
        "method:by-http-method": {
          "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/{http_method}",
          "templated": true
        },
        "method:put": {
          "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/{http_method}",
          "templated": true
        },
        "resource:create-child": {
          "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2"
        },
        "resource:update": {
          "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2"
        }
      },
      "id": "3kzxbg5sa2",
      "path": "/"
    }
  }
}
```

## See Also
<a name="API_GetResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetResources)
