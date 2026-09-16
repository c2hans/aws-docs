---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateStage.html
---

# CreateStage
<a name="API_CreateStage"></a>

Creates a new Stage resource that references a pre-existing Deployment for the API.

## Request Syntax
<a name="API_CreateStage_RequestSyntax"></a>

```
POST /restapis/{{restapi_id}}/stages HTTP/1.1
Content-type: application/json

{
   "cacheClusterEnabled": {{boolean}},
   "cacheClusterSize": "{{string}}",
   "canarySettings": {
      "deploymentId": "{{string}}",
      "percentTraffic": {{number}},
      "stageVariableOverrides": {
         "{{string}}" : "{{string}}"
      },
      "useStageCache": {{boolean}}
   },
   "deploymentId": "{{string}}",
   "description": "{{string}}",
   "documentationVersion": "{{string}}",
   "stageName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "tracingEnabled": {{boolean}},
   "variables": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateStage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [restapi\_id](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_CreateStage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cacheClusterEnabled](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-cacheClusterEnabled"></a>
Whether cache clustering is enabled for the stage.
Type: Boolean
Required: No

 ** [cacheClusterSize](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-cacheClusterSize"></a>
The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
Type: String
Valid Values: `0.5 | 1.6 | 6.1 | 13.5 | 28.4 | 58.2 | 118 | 237`
Required: No

 ** [canarySettings](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-canarySettings"></a>
The canary deployment settings of this stage.
Type: [CanarySettings](API_CanarySettings.md) object
Required: No

 ** [deploymentId](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-deploymentId"></a>
The identifier of the Deployment resource for the Stage resource.
Type: String
Required: Yes

 ** [description](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-description"></a>
The description of the Stage resource.
Type: String
Required: No

 ** [documentationVersion](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-documentationVersion"></a>
The version of the associated API documentation.
Type: String
Required: No

 ** [stageName](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-stageName"></a>
The name for the Stage resource. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
Type: String
Required: Yes

 ** [tags](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-tags"></a>
The key-value map of strings. The valid character set is [a-zA-Z\+-=.\_:/]. The tag key can be up to 128 characters and must not start with `aws:`. The tag value can be up to 256 characters.
Type: String to string map
Required: No

 ** [tracingEnabled](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-tracingEnabled"></a>
Specifies whether active tracing with X-ray is enabled for the Stage.
Type: Boolean
Required: No

 ** [variables](#API_CreateStage_RequestSyntax) **   <a name="apigw-CreateStage-request-variables"></a>
A map that defines the stage variables for the new Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9-._~:/?#&=,]+`.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateStage_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateStage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [accessLogSettings](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-accessLogSettings"></a>
Settings for logging access in this stage.
Type: [AccessLogSettings](API_AccessLogSettings.md) object

 ** [cacheClusterEnabled](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-cacheClusterEnabled"></a>
Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set `CachingEnabled` to `true` for a method.
Type: Boolean

 ** [cacheClusterSize](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-cacheClusterSize"></a>
The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
Type: String
Valid Values: `0.5 | 1.6 | 6.1 | 13.5 | 28.4 | 58.2 | 118 | 237`

 ** [cacheClusterStatus](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-cacheClusterStatus"></a>
The status of the cache cluster for the stage, if enabled.
Type: String
Valid Values: `CREATE_IN_PROGRESS | AVAILABLE | DELETE_IN_PROGRESS | NOT_AVAILABLE | FLUSH_IN_PROGRESS`

 ** [canarySettings](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-canarySettings"></a>
Settings for the canary deployment in this stage.
Type: [CanarySettings](API_CanarySettings.md) object

 ** [clientCertificateId](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-clientCertificateId"></a>
The identifier of a client certificate for an API stage.
Type: String

 ** [createdDate](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-createdDate"></a>
The timestamp when the stage was created.
Type: Timestamp

 ** [deploymentId](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-deploymentId"></a>
The identifier of the Deployment that the stage points to.
Type: String

 ** [description](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-description"></a>
The stage's description.
Type: String

 ** [documentationVersion](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-documentationVersion"></a>
The version of the associated API documentation.
Type: String

 ** [lastUpdatedDate](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-lastUpdatedDate"></a>
The timestamp when the stage last updated.
Type: Timestamp

 ** [methodSettings](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-methodSettings"></a>
A map that defines the method settings for a Stage resource. Keys (designated as `/{method_setting_key` below) are method paths defined as `{resource_path}/{http_method}` for an individual method override, or `/\*/\*` for overriding all methods in the stage.
Type: String to [MethodSetting](API_MethodSetting.md) object map

 ** [stageName](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-stageName"></a>
The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
Type: String

 ** [tags](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [tracingEnabled](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-tracingEnabled"></a>
Specifies whether active tracing with X-ray is enabled for the Stage.
Type: Boolean

 ** [variables](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-variables"></a>
A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9-._~:/?#&=,]+`.
Type: String to string map

 ** [webAclArn](#API_CreateStage_ResponseSyntax) **   <a name="apigw-CreateStage-response-webAclArn"></a>
The ARN of the WebAcl associated with the Stage.
Type: String

## Errors
<a name="API_CreateStage_Errors"></a>

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
<a name="API_CreateStage_Examples"></a>

### Create a new stage for a deployed API
<a name="API_CreateStage_Example_1"></a>

This example illustrates one usage of CreateStage.

#### Sample Request
<a name="API_CreateStage_Example_1_Request"></a>

```
POST /restapis/uycll6xg9a/stages HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T200249Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "stageName" : "alpha",
  "deploymentId" : "vakw79",
  "description" : "alpha stage",
  "cacheClusterEnabled" : "true",
  "cacheClusterSize" : "0.5",
  "variables" : {
    "sv_1" : "value_1",
    "sv_2" : "value_2"
  }
}
```

#### Sample Response
<a name="API_CreateStage_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-stage-{rel}.html",
      "name": "stage",
      "templated": true
    },
    "self": {
      "href": "/restapis/uycll6xg9a/stages/alpha"
    },
    "stage:delete": {
      "href": "/restapis/uycll6xg9a/stages/alpha"
    },
    "stage:flush-authorizer-cache": {
      "href": "/restapis/uycll6xg9a/stages/alpha/cache/authorizers"
    },
    "stage:flush-cache": {
      "href": "/restapis/uycll6xg9a/stages/alpha/cache/data"
    },
    "stage:update": {
      "href": "/restapis/uycll6xg9a/stages/alpha"
    }
  },
  "cacheClusterEnabled": true,
  "cacheClusterSize": "0.5",
  "cacheClusterStatus": "CREATE_IN_PROGRESS",
  "createdDate": "2016-06-08T20:02:50Z",
  "deploymentId": "vakw79",
  "description": "alpha stage",
  "lastUpdatedDate": "2016-06-08T20:02:50Z",
  "methodSettings": {},
  "stageName": "alpha",
  "variables": {
    "sv_2": "value_2",
    "sv_1": "value_1"
  }
}
```

## See Also
<a name="API_CreateStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateStage)
