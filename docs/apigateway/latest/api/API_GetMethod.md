---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetMethod.html
---

# GetMethod
<a name="API_GetMethod"></a>

Describe an existing Method resource.

## Request Syntax
<a name="API_GetMethod_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/resources/{{resource_id}}/methods/{{http_method}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMethod_RequestParameters"></a>

The request uses the following URI parameters.

 ** [http\_method](#API_GetMethod_RequestSyntax) **   <a name="apigw-GetMethod-request-uri-httpMethod"></a>
Specifies the method request's HTTP method type.
Required: Yes

 ** [resource\_id](#API_GetMethod_RequestSyntax) **   <a name="apigw-GetMethod-request-uri-resourceId"></a>
The Resource identifier for the Method resource.
Required: Yes

 ** [restapi\_id](#API_GetMethod_RequestSyntax) **   <a name="apigw-GetMethod-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetMethod_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMethod_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
```

## Response Elements
<a name="API_GetMethod_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiKeyRequired](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-apiKeyRequired"></a>
A boolean flag specifying whether a valid ApiKey is required to invoke this method.
Type: Boolean

 ** [authorizationScopes](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-authorizationScopes"></a>
A list of authorization scopes configured on the method. The scopes are used with a `COGNITO_USER_POOLS` authorizer to authorize the method invocation. The authorization works by matching the method scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any method scopes matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the method scope is configured, the client must provide an access token instead of an identity token for authorization purposes.
Type: Array of strings

 ** [authorizationType](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-authorizationType"></a>
The method's authorization type. Valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, `CUSTOM` for using a custom authorizer, or `COGNITO_USER_POOLS` for using a Cognito user pool.
Type: String

 ** [authorizerId](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-authorizerId"></a>
The identifier of an authorizer to use on this method. The method's authorization type must be `CUSTOM` or `COGNITO_USER_POOLS`.
Type: String

 ** [httpMethod](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-httpMethod"></a>
The method's HTTP verb.
Type: String

 ** [methodIntegration](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-methodIntegration"></a>
Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.
Type: [Integration](API_Integration.md) object

 ** [methodResponses](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-methodResponses"></a>
Gets a method response associated with a given HTTP status code.
Type: String to [MethodResponse](API_MethodResponse.md) object map

 ** [operationName](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-operationName"></a>
A human-friendly operation identifier for the method. For example, you can assign the `operationName` of `ListPets` for the `GET /pets` method in the `PetStore` example.
Type: String

 ** [requestModels](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-requestModels"></a>
A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).
Type: String to string map

 ** [requestParameters](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-requestParameters"></a>
A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of `method.request.{location}.{name}`, where `location` is `querystring`, `path`, or `header` and `name` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (`true`) or optional (`false`). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or templates.
Type: String to boolean map

 ** [requestValidatorId](#API_GetMethod_ResponseSyntax) **   <a name="apigw-GetMethod-response-requestValidatorId"></a>
The identifier of a RequestValidator for request validation.
Type: String

## Errors
<a name="API_GetMethod_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetMethod_Examples"></a>

### View the detailed information about the GET method on an API resource
<a name="API_GetMethod_Example_1"></a>

This example illustrates one usage of GetMethod.

#### Sample Request
<a name="API_GetMethod_Example_1_Request"></a>

```
GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
Content-Length: 117
X-Amz-Date: 20160613T205752Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetMethod_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html",
        "name": "integration",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
        "name": "integrationresponse",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html",
        "name": "method",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
        "name": "methodresponse",
        "templated": true
      }
    ],
    "self": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET",
      "name": "GET",
      "title": "GET"
    },
    "integration:put": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration"
    },
    "method:delete": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET"
    },
    "method:integration": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration"
    },
    "method:responses": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200",
      "name": "200",
      "title": "200"
    },
    "method:update": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET"
    },
    "methodresponse:put": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/{status_code}",
      "templated": true
    }
  },
  "apiKeyRequired": false,
  "authorizationType": "NONE",
  "httpMethod": "GET",
  "requestParameters": {
    "method.request.querystring.operand2": false,
    "method.request.querystring.operator": false,
    "method.request.querystring.operand1": false
  },
  "_embedded": {
    "method:integration": {
      "_links": {
        "self": {
          "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration"
        },
        "integration:delete": {
          "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration"
        },
        "integration:responses": {
          "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200",
          "name": "200",
          "title": "200"
        },
        "integration:update": {
          "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration"
        },
        "integrationresponse:put": {
          "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}",
          "templated": true
        }
      },
      "cacheKeyParameters": [],
      "cacheNamespace": "0cjtch",
      "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole",
      "httpMethod": "POST",
      "passthroughBehavior": "WHEN_NO_MATCH",
      "requestTemplates": {
        "application/json": "{\n    \"a\":  \"$input.params('operand1')\",\n    \"b\":  \"$input.params('operand2')\", \n    \"op\": \"$input.params('operator')\"   \n}"
      },
      "type": "AWS",
      "uri": "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations",
      "_embedded": {
        "integration:responses": {
          "_links": {
            "self": {
              "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200",
              "name": "200",
              "title": "200"
            },
            "integrationresponse:delete": {
              "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200"
            },
            "integrationresponse:update": {
              "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200"
            }
          },
          "responseParameters": {
            "method.response.header.operator": "integration.response.body.op",
            "method.response.header.operand_2": "integration.response.body.b",
            "method.response.header.operand_1": "integration.response.body.a"
          },
          "responseTemplates": {
            "application/json": "#set($res = $input.path('$'))\n{\n    \"result\": \"$res.a, $res.b, $res.op => $res.c\",\n  \"a\" : \"$res.a\",\n  \"b\" : \"$res.b\",\n  \"op\" : \"$res.op\",\n  \"c\" : \"$res.c\"\n}"
          },
          "selectionPattern": "",
          "statusCode": "200"
        }
      }
    },
    "method:responses": {
      "_links": {
        "self": {
          "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200",
          "name": "200",
          "title": "200"
        },
        "methodresponse:delete": {
          "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200"
        },
        "methodresponse:update": {
          "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200"
        }
      },
      "responseModels": {
        "application/json": "Empty"
      },
      "responseParameters": {
        "method.response.header.operator": false,
        "method.response.header.operand_2": false,
        "method.response.header.operand_1": false
      },
      "statusCode": "200"
    }
  }
}
```

## See Also
<a name="API_GetMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetMethod)
