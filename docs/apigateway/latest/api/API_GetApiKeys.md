---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetApiKeys.html
---

# GetApiKeys
<a name="API_GetApiKeys"></a>

Gets information about the current ApiKeys resource.

## Request Syntax
<a name="API_GetApiKeys_RequestSyntax"></a>

```
GET /apikeys?customerId={{customerId}}&includeValues={{includeValues}}&limit={{limit}}&name={{nameQuery}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApiKeys_RequestParameters"></a>

The request uses the following URI parameters.

 ** [customerId](#API_GetApiKeys_RequestSyntax) **   <a name="apigw-GetApiKeys-request-uri-customerId"></a>
The identifier of a customer in AWS Marketplace or an external system, such as a developer portal.

 ** [includeValues](#API_GetApiKeys_RequestSyntax) **   <a name="apigw-GetApiKeys-request-uri-includeValues"></a>
A boolean flag to specify whether (`true`) or not (`false`) the result contains key values.

 ** [limit](#API_GetApiKeys_RequestSyntax) **   <a name="apigw-GetApiKeys-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [nameQuery](#API_GetApiKeys_RequestSyntax) **   <a name="apigw-GetApiKeys-request-uri-nameQuery"></a>
The name of queried API keys.

 ** [position](#API_GetApiKeys_RequestSyntax) **   <a name="apigw-GetApiKeys-request-uri-position"></a>
The current pagination position in the paged result set.

## Request Body
<a name="API_GetApiKeys_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApiKeys_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
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
   ],
   "position": "string",
   "warnings": [ "string" ]
}
```

## Response Elements
<a name="API_GetApiKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetApiKeys_ResponseSyntax) **   <a name="apigw-GetApiKeys-response-item"></a>
The current page of elements from this collection.
Type: Array of [ApiKey](API_ApiKey.md) objects

 ** [position](#API_GetApiKeys_ResponseSyntax) **   <a name="apigw-GetApiKeys-response-position"></a>
The current pagination position in the paged result set.
Type: String

 ** [warnings](#API_GetApiKeys_ResponseSyntax) **   <a name="apigw-GetApiKeys-response-warnings"></a>
A list of warning messages logged during the import of API keys when the `failOnWarnings` option is set to true.
Type: Array of strings

## Errors
<a name="API_GetApiKeys_Errors"></a>

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
<a name="API_GetApiKeys_Examples"></a>

### Retrieve an API key
<a name="API_GetApiKeys_Example_1"></a>

The following example request retrieves the available API keys in the caller's AWS account.

A successful response returns the requested `ApiKey` resources that can be navigated to by following the linked item or examining the embedded item resource.

#### Sample Request
<a name="API_GetApiKeys_Example_1_Request"></a>

```
GET /apikeys HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160601T180431Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160601/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetApiKeys_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-apikey-{rel}.html",
        "name": "apikey",
        "templated": true
      }
    ],
    "self": {
      "href": "/apikeys"
    },
    "apikey:by-key": {
      "href": "/apikeys/{api_Key}",
      "templated": true
    },
    "apikey:create": {
      "href": "/apikeys"
    },
    "apikey:delete": {
      "href": "/apikeys/{api_Key}",
      "templated": true
    },
    "item": {
      "href": "/apikeys/hzYAVO9Sg98nsNh45VfX81M84O2kyXVy6K1xwHD76"
    }
  },
  "_embedded": {
    "item": {
      "_links": {
        "self": {
          "href": "/apikeys/hzYAVO9Sg98nsNh45VfX81M84O2kyXVy6K1xwHD76"
        },
        "apikey:delete": {
          "href": "/apikeys/hzYAVO9Sg98nsNh45VfX81M84O2kyXVy6K1xwHD76"
        },
        "apikey:update": {
          "href": "/apikeys/hzYAVO9Sg98nsNh45VfX81M84O2kyXVy6K1xwHD76"
        }
      },
      "createdDate": "2015-11-06T23:51:03Z",
      "enabled": true,
      "id": "hzYAVO9Sg98nsNh45VfX81M84O2kyXVy6K1xwHD76",
      "lastUpdatedDate": "2016-01-26T20:05:38Z",
      "name": "my_test_gateway_service",
      "stageKeys": "h4ah70cvmb/beta"
    }
  }
}
```

## See Also
<a name="API_GetApiKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetApiKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetApiKeys)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
