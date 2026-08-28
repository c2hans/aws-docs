---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetStages.html
---

# GetStages
<a name="API_GetStages"></a>

Gets information about one or more Stage resources.

## Request Syntax
<a name="API_GetStages_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/stages?deploymentId={{deploymentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetStages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deploymentId](#API_GetStages_RequestSyntax) **   <a name="apigw-GetStages-request-uri-deploymentId"></a>
The stages' deployment identifiers.

 ** [restapi\_id](#API_GetStages_RequestSyntax) **   <a name="apigw-GetStages-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetStages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetStages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "accessLogSettings": {
            "destinationArn": "string",
            "format": "string"
         },
         "cacheClusterEnabled": boolean,
         "cacheClusterSize": "string",
         "cacheClusterStatus": "string",
         "canarySettings": {
            "deploymentId": "string",
            "percentTraffic": number,
            "stageVariableOverrides": {
               "string" : "string"
            },
            "useStageCache": boolean
         },
         "clientCertificateId": "string",
         "createdDate": number,
         "deploymentId": "string",
         "description": "string",
         "documentationVersion": "string",
         "lastUpdatedDate": number,
         "methodSettings": {
            "string" : {
               "cacheDataEncrypted": boolean,
               "cacheTtlInSeconds": number,
               "cachingEnabled": boolean,
               "dataTraceEnabled": boolean,
               "loggingLevel": "string",
               "metricsEnabled": boolean,
               "requireAuthorizationForCacheControl": boolean,
               "throttlingBurstLimit": number,
               "throttlingRateLimit": number,
               "unauthorizedCacheControlHeaderStrategy": "string"
            }
         },
         "stageName": "string",
         "tags": {
            "string" : "string"
         },
         "tracingEnabled": boolean,
         "variables": {
            "string" : "string"
         },
         "webAclArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetStages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetStages_ResponseSyntax) **   <a name="apigw-GetStages-response-item"></a>
The current page of elements from this collection.
Type: Array of [Stage](API_Stage.md) objects

## Errors
<a name="API_GetStages_Errors"></a>

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
<a name="API_GetStages_Examples"></a>

### Get Stages
<a name="API_GetStages_Example_1"></a>

This example illustrates one usage of GetStages.

#### Sample Request
<a name="API_GetStages_Example_1_Request"></a>

```
GET /restapis/{restapi_id}/stages?deployment_id=vakw79 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160524T061752Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160524/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig-hash}
Cache-Control: no-cache
```

#### Sample Response
<a name="API_GetStages_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-stage-{rel}.html",
      "name": "stage",
      "templated": true
    },
    "self": {
      "href": "/restapis/{restapi_id}/stages{?deployment_id}",
      "templated": true
    },
    "item": [
      {
        "href": "/restapis/{restapi_id}/stages/beta"
      },
      {
        "href": "/restapis/{restapi_id}/stages/prod"
      }
    ],
    "stage:by-name": {
      "href": "/restapis/{restapi_id}/stages/{stage_name}",
      "templated": true
    },
    "stage:create": {
      "href": "/restapis/{restapi_id}/stages"
    }
  },
  "_embedded": {
    "item": [
      {
        "_links": {
          "self": {
            "href": "/restapis/{restapi_id}/stages/beta"
          },
          "stage:delete": {
            "href": "/restapis/{restapi_id}/stages/beta"
          },
          "stage:flush-authorizer-cache": {
            "href": "/restapis/{restapi_id}/stages/beta/cache/authorizers"
          },
          "stage:update": {
            "href": "/restapis/{restapi_id}/stages/beta"
          }
        },
        "cacheClusterEnabled": false,
        "cacheClusterStatus": "NOT_AVAILABLE",
        "createdDate": "2016-04-15T17:38:08Z",
        "deploymentId": "vakw79",
        "lastUpdatedDate": "2016-04-15T17:45:48Z",
        "methodSettings": {},
        "stageName": "beta",
        "variables": {
          "version": "v-beta",
          "url": "myDomain.com",
          "function": "HelloWorld"
        }
      },
      {
        "_links": {
          "self": {
            "href": "/restapis/{restapi_id}/stages/prod"
          },
          "stage:delete": {
            "href": "/restapis/{restapi_id}/stages/prod"
          },
          "stage:flush-authorizer-cache": {
            "href": "/restapis/{restapi_id}/stages/prod/cache/authorizers"
          },
          "stage:update": {
            "href": "/restapis/{restapi_id}/stages/prod"
          }
        },
        "cacheClusterEnabled": false,
        "cacheClusterStatus": "NOT_AVAILABLE",
        "createdDate": "2016-04-15T17:53:35Z",
        "deploymentId": "vakw79",
        "lastUpdatedDate": "2016-04-15T18:30:10Z",
        "methodSettings": {},
        "stageName": "prod",
        "variables": {
          "version": "v-prod",
          "url": "petstore-demo-endpoint.execute-api.com/petstore/pets",
          "function": "HelloEveryone"
        }
      }
    ]
  }
}
```

## See Also
<a name="API_GetStages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetStages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetStages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetStages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetStages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetStages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetStages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetStages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetStages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetStages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetStages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
