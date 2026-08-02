---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetApiKey.html
---

# GetApiKey
<a name="API_GetApiKey"></a>

Gets information about the current ApiKey resource.

## Request Syntax
<a name="API_GetApiKey_RequestSyntax"></a>

```
GET /apikeys/{{api_Key}}?includeValue={{includeValue}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApiKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [api\_Key](#API_GetApiKey_RequestSyntax) **   <a name="apigw-GetApiKey-request-uri-apiKey"></a>
The identifier of the ApiKey resource.
Required: Yes

 ** [includeValue](#API_GetApiKey_RequestSyntax) **   <a name="apigw-GetApiKey-request-uri-includeValue"></a>
A boolean flag to specify whether (`true`) or not (`false`) the result contains the key value.

## Request Body
<a name="API_GetApiKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApiKey_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetApiKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-createdDate"></a>
The timestamp when the API Key was created.
Type: Timestamp

 ** [customerId](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-customerId"></a>
An AWS Marketplace customer identifier, when integrating with the AWS SaaS Marketplace.
Type: String

 ** [description](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-description"></a>
The description of the API Key.
Type: String

 ** [enabled](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-enabled"></a>
Specifies whether the API Key can be used by callers.
Type: Boolean

 ** [id](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-id"></a>
The identifier of the API Key.
Type: String

 ** [lastUpdatedDate](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-lastUpdatedDate"></a>
The timestamp when the API Key was last updated.
Type: Timestamp

 ** [name](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-name"></a>
The name of the API Key.
Type: String

 ** [stageKeys](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-stageKeys"></a>
A list of Stage resources that are associated with the ApiKey resource.
Type: Array of strings

 ** [tags](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [value](#API_GetApiKey_ResponseSyntax) **   <a name="apigw-GetApiKey-response-value"></a>
The value of the API Key.
Type: String

## Errors
<a name="API_GetApiKey_Errors"></a>

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
<a name="API_GetApiKey_Examples"></a>

### Retrieve an API Key
<a name="API_GetApiKey_Example_1"></a>

 The following example request retrieves an API key.

 The successful response returns `200 OK` status code and a payload similar to the following:

#### Sample Request
<a name="API_GetApiKey_Example_1_Request"></a>

```
GET /apikeys/hzYAVO9Sg98nsNh65VfX81M84O2kyXVy6K1xwHD76 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T221142Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetApiKey_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-apikey-{rel}.html",
      "name": "apikey",
      "templated": true
    },
    "self": {
      "href": "/apikeys/hzYAVO9Sg98nsNh65VfX81M84O2kyXVy6K1xwHD76"
    },
    "apikey:delete": {
      "href": "/apikeys/hzYAVO9Sg98nsNh65VfX81M84O2kyXVy6K1xwHD76"
    },
    "apikey:update": {
      "href": "/apikeys/hzYAVO9Sg98nsNh65VfX81M84O2kyXVy6K1xwHD76"
    }
  },
  "createdDate": "2015-11-06T23:51:03Z",
  "enabled": true,
  "id": "hzYAVO9Sg98nsNh65VfX81M84O2kyXVy6K1xwHD76",
  "lastUpdatedDate": "2016-06-06T23:44:43Z",
  "name": "my_test_gateway_service",
  "stageKeys": [
    "h4ah70cvmb/beta",
    "fugvjdxtri/stage2"
  ]
}
```

## See Also
<a name="API_GetApiKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetApiKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetApiKey)
