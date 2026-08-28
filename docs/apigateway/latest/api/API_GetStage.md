---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetStage.html
---

# GetStage
<a name="API_GetStage"></a>

Gets information about a Stage resource.

## Request Syntax
<a name="API_GetStage_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/stages/{{stage_name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetStage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [restapi\_id](#API_GetStage_RequestSyntax) **   <a name="apigw-GetStage-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

 ** [stage\_name](#API_GetStage_RequestSyntax) **   <a name="apigw-GetStage-request-uri-stageName"></a>
The name of the Stage resource to get information about.
Required: Yes

## Request Body
<a name="API_GetStage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetStage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetStage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessLogSettings](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-accessLogSettings"></a>
Settings for logging access in this stage.
Type: [AccessLogSettings](API_AccessLogSettings.md) object

 ** [cacheClusterEnabled](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-cacheClusterEnabled"></a>
Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set `CachingEnabled` to `true` for a method.
Type: Boolean

 ** [cacheClusterSize](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-cacheClusterSize"></a>
The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
Type: String
Valid Values: `0.5 | 1.6 | 6.1 | 13.5 | 28.4 | 58.2 | 118 | 237`

 ** [cacheClusterStatus](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-cacheClusterStatus"></a>
The status of the cache cluster for the stage, if enabled.
Type: String
Valid Values: `CREATE_IN_PROGRESS | AVAILABLE | DELETE_IN_PROGRESS | NOT_AVAILABLE | FLUSH_IN_PROGRESS`

 ** [canarySettings](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-canarySettings"></a>
Settings for the canary deployment in this stage.
Type: [CanarySettings](API_CanarySettings.md) object

 ** [clientCertificateId](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-clientCertificateId"></a>
The identifier of a client certificate for an API stage.
Type: String

 ** [createdDate](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-createdDate"></a>
The timestamp when the stage was created.
Type: Timestamp

 ** [deploymentId](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-deploymentId"></a>
The identifier of the Deployment that the stage points to.
Type: String

 ** [description](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-description"></a>
The stage's description.
Type: String

 ** [documentationVersion](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-documentationVersion"></a>
The version of the associated API documentation.
Type: String

 ** [lastUpdatedDate](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-lastUpdatedDate"></a>
The timestamp when the stage last updated.
Type: Timestamp

 ** [methodSettings](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-methodSettings"></a>
A map that defines the method settings for a Stage resource. Keys (designated as `/{method_setting_key` below) are method paths defined as `{resource_path}/{http_method}` for an individual method override, or `/\*/\*` for overriding all methods in the stage.
Type: String to [MethodSetting](API_MethodSetting.md) object map

 ** [stageName](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-stageName"></a>
The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
Type: String

 ** [tags](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [tracingEnabled](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-tracingEnabled"></a>
Specifies whether active tracing with X-ray is enabled for the Stage.
Type: Boolean

 ** [variables](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-variables"></a>
A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9-._~:/?#&=,]+`.
Type: String to string map

 ** [webAclArn](#API_GetStage_ResponseSyntax) **   <a name="apigw-GetStage-response-webAclArn"></a>
The ARN of the WebAcl associated with the Stage.
Type: String

## Errors
<a name="API_GetStage_Errors"></a>

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
<a name="API_GetStage_Examples"></a>

### Get a named stage of an API
<a name="API_GetStage_Example_1"></a>

This example illustrates one usage of GetStage.

#### Sample Request
<a name="API_GetStage_Example_1_Request"></a>

```
GET /restapis/uycll6xg9a/stages/prod HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T194603Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetStage_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-stage-{rel}.html",
      "name": "stage",
      "templated": true
    },
    "self": {
      "href": "/restapis/uycll6xg9a/stages/prod"
    },
    "stage:delete": {
      "href": "/restapis/uycll6xg9a/stages/prod"
    },
    "stage:flush-authorizer-cache": {
      "href": "/restapis/uycll6xg9a/stages/prod/cache/authorizers"
    },
    "stage:update": {
      "href": "/restapis/uycll6xg9a/stages/prod"
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
```

## See Also
<a name="API_GetStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetStage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetStage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetStage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetStage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetStage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetStage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetStage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetStage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
