---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateApiKey.html
---

# CreateApiKey
<a name="API_CreateApiKey"></a>

Create an ApiKey resource.

## Request Syntax
<a name="API_CreateApiKey_RequestSyntax"></a>

```
POST /apikeys HTTP/1.1
Content-type: application/json

{
   "customerId": "{{string}}",
   "description": "{{string}}",
   "enabled": {{boolean}},
   "generateDistinctId": {{boolean}},
   "name": "{{string}}",
   "stageKeys": [
      {
         "restApiId": "{{string}}",
         "stageName": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "value": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateApiKey_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApiKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [customerId](#API_CreateApiKey_RequestSyntax) **   <a name="apigw-CreateApiKey-request-customerId"></a>
An AWS Marketplace customer identifier, when integrating with the AWS SaaS Marketplace.
Type: String
Required: No

 ** [description](#API_CreateApiKey_RequestSyntax) **   <a name="apigw-CreateApiKey-request-description"></a>
The description of the ApiKey.
Type: String
Required: No

 ** [enabled](#API_CreateApiKey_RequestSyntax) **   <a name="apigw-CreateApiKey-request-enabled"></a>
Specifies whether the ApiKey can be used by callers.
Type: Boolean
Required: No

 ** [generateDistinctId](#API_CreateApiKey_RequestSyntax) **   <a name="apigw-CreateApiKey-request-generateDistinctId"></a>
Specifies whether (`true`) or not (`false`) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.
Type: Boolean
Required: No

 ** [name](#API_CreateApiKey_RequestSyntax) **   <a name="apigw-CreateApiKey-request-name"></a>
The name of the ApiKey.
Type: String
Required: No

 ** [stageKeys](#API_CreateApiKey_RequestSyntax) **   <a name="apigw-CreateApiKey-request-stageKeys"></a>
DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
Type: Array of [StageKey](API_StageKey.md) objects
Required: No

 ** [tags](#API_CreateApiKey_RequestSyntax) **   <a name="apigw-CreateApiKey-request-tags"></a>
The key-value map of strings. The valid character set is [a-zA-Z\+-=.\_:/]. The tag key can be up to 128 characters and must not start with `aws:`. The tag value can be up to 256 characters.
Type: String to string map
Required: No

 ** [value](#API_CreateApiKey_RequestSyntax) **   <a name="apigw-CreateApiKey-request-value"></a>
Specifies a value of the API key.
Type: String
Required: No

## Response Syntax
<a name="API_CreateApiKey_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdDate": number,
   "customerId": "string",
   "description": "string",
   "enabled": boolean,
   "id": "string",
   "lastUpdatedDate": number,
   "name": "string",
   "stageKeys": [ "string" ],
   "tags": {
      "string" : "string"
   },
   "value": "string"
}
```

## Response Elements
<a name="API_CreateApiKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-createdDate"></a>
The timestamp when the API Key was created.
Type: Timestamp

 ** [customerId](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-customerId"></a>
An AWS Marketplace customer identifier, when integrating with the AWS SaaS Marketplace.
Type: String

 ** [description](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-description"></a>
The description of the API Key.
Type: String

 ** [enabled](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-enabled"></a>
Specifies whether the API Key can be used by callers.
Type: Boolean

 ** [id](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-id"></a>
The identifier of the API Key.
Type: String

 ** [lastUpdatedDate](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-lastUpdatedDate"></a>
The timestamp when the API Key was last updated.
Type: Timestamp

 ** [name](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-name"></a>
The name of the API Key.
Type: String

 ** [stageKeys](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-stageKeys"></a>
A list of Stage resources that are associated with the ApiKey resource.
Type: Array of strings

 ** [tags](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [value](#API_CreateApiKey_ResponseSyntax) **   <a name="apigw-CreateApiKey-response-value"></a>
The value of the API Key.
Type: String

## Errors
<a name="API_CreateApiKey_Errors"></a>

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

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_CreateApiKey_Examples"></a>

### Create an API key
<a name="API_CreateApiKey_Example_1"></a>

 The following example creates an API key.

#### Sample Request
<a name="API_CreateApiKey_Example_1_Request"></a>

```
POST /apikeys HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T222156Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "name" : "my_api_key",
  "description" : "My API key",
  "enabled" : "false",
  "stageKeys" : [ {
    "restApiId" : "uycll6xg9a",
    "stageName" : "beta"
  } ]
}
```

#### Sample Response
<a name="API_CreateApiKey_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-apikey-{rel}.html",
      "name": "apikey",
      "templated": true
    },
    "self": {
      "href": "/apikeys/a2TprUZuzf2EKbbmMUotDaHYGg8kgxFypcarGved6"
    },
    "apikey:delete": {
      "href": "/apikeys/a2TprUZuzf2EKbbmMUotDaHYGg8kgxFypcarGved6"
    },
    "apikey:update": {
      "href": "/apikeys/a2TprUZuzf2EKbbmMUotDaHYGg8kgxFypcarGved6"
    }
  },
  "createdDate": "2016-06-08T22:21:56Z",
  "description": "My API key",
  "enabled": false,
  "id": "a2TprUZuzf2EKbbmMUotDaHYGg8kgxFypcarGved6",
  "lastUpdatedDate": "2016-06-08T22:21:56Z",
  "name": "my_api_key",
  "stageKeys": "uycll6xg9a/beta"
}
```

## See Also
<a name="API_CreateApiKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateApiKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateApiKey)
