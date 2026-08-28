---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateResource.html
---

# CreateResource
<a name="API_CreateResource"></a>

Creates a Resource resource.

## Request Syntax
<a name="API_CreateResource_RequestSyntax"></a>

```
POST /restapis/{{restapi_id}}/resources/{{parent_id}} HTTP/1.1
Content-type: application/json

{
   "pathPart": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [parent\_id](#API_CreateResource_RequestSyntax) **   <a name="apigw-CreateResource-request-uri-parentId"></a>
The parent resource's identifier.
Required: Yes

 ** [restapi\_id](#API_CreateResource_RequestSyntax) **   <a name="apigw-CreateResource-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_CreateResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [pathPart](#API_CreateResource_RequestSyntax) **   <a name="apigw-CreateResource-request-pathPart"></a>
The last path segment for this resource.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateResource_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

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
```

## Response Elements
<a name="API_CreateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [id](#API_CreateResource_ResponseSyntax) **   <a name="apigw-CreateResource-response-id"></a>
The resource's identifier.
Type: String

 ** [parentId](#API_CreateResource_ResponseSyntax) **   <a name="apigw-CreateResource-response-parentId"></a>
The parent resource's identifier.
Type: String

 ** [path](#API_CreateResource_ResponseSyntax) **   <a name="apigw-CreateResource-response-path"></a>
The full path for this resource.
Type: String

 ** [pathPart](#API_CreateResource_ResponseSyntax) **   <a name="apigw-CreateResource-response-pathPart"></a>
The last path segment for this resource.
Type: String

 ** [resourceMethods](#API_CreateResource_ResponseSyntax) **   <a name="apigw-CreateResource-response-resourceMethods"></a>
Gets an API resource's method of a given HTTP verb.
Type: String to [Method](API_Method.md) object map

## Errors
<a name="API_CreateResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** LimitExceededException **
The request exceeded the rate limit. Retry after the specified time period.
HTTP Status Code: 429

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
<a name="API_CreateResource_Examples"></a>

### Create a child resource under an API's root resource
<a name="API_CreateResource_Example_1"></a>

This example illustrates one usage of CreateResource.

#### Sample Request
<a name="API_CreateResource_Example_1_Request"></a>

```
POST /restapis/fugvjdxtri/resources/3kzxbg5sa2 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T010429Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
    "pathPart" : "res1"
}
```

#### Sample Response
<a name="API_CreateResource_Example_1_Response"></a>

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
      "href": "/restapis/fugvjdxtri/resources/47rxl6"
    },
    "method:by-http-method": {
      "href": "/restapis/fugvjdxtri/resources/47rxl6/methods/{http_method}",
      "templated": true
    },
    "method:put": {
      "href": "/restapis/fugvjdxtri/resources/47rxl6/methods/{http_method}",
      "templated": true
    },
    "resource:create-child": {
      "href": "/restapis/fugvjdxtri/resources/47rxl6"
    },
    "resource:delete": {
      "href": "/restapis/fugvjdxtri/resources/47rxl6"
    },
    "resource:update": {
      "href": "/restapis/fugvjdxtri/resources/47rxl6"
    }
  },
  "id": "47rxl6",
  "parentId": "3kzxbg5sa2",
  "path": "/res1",
  "pathPart": "res1"
}
```

## See Also
<a name="API_CreateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
