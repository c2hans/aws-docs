---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetUsagePlanKeys.html
---

# GetUsagePlanKeys
<a name="API_GetUsagePlanKeys"></a>

Gets all the usage plan keys representing the API keys added to a specified usage plan.

## Request Syntax
<a name="API_GetUsagePlanKeys_RequestSyntax"></a>

```
GET /usageplans/{{usageplanId}}/keys?limit={{limit}}&name={{nameQuery}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUsagePlanKeys_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_GetUsagePlanKeys_RequestSyntax) **   <a name="apigw-GetUsagePlanKeys-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [nameQuery](#API_GetUsagePlanKeys_RequestSyntax) **   <a name="apigw-GetUsagePlanKeys-request-uri-nameQuery"></a>
A query parameter specifying the name of the to-be-returned usage plan keys.

 ** [position](#API_GetUsagePlanKeys_RequestSyntax) **   <a name="apigw-GetUsagePlanKeys-request-uri-position"></a>
The current pagination position in the paged result set.

 ** [usageplanId](#API_GetUsagePlanKeys_RequestSyntax) **   <a name="apigw-GetUsagePlanKeys-request-uri-usagePlanId"></a>
The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
Required: Yes

## Request Body
<a name="API_GetUsagePlanKeys_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUsagePlanKeys_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "id": "string",
         "name": "string",
         "type": "string",
         "value": "string"
      }
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetUsagePlanKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetUsagePlanKeys_ResponseSyntax) **   <a name="apigw-GetUsagePlanKeys-response-item"></a>
The current page of elements from this collection.
Type: Array of [UsagePlanKey](API_UsagePlanKey.md) objects

 ** [position](#API_GetUsagePlanKeys_ResponseSyntax) **   <a name="apigw-GetUsagePlanKeys-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetUsagePlanKeys_Errors"></a>

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
<a name="API_GetUsagePlanKeys_Examples"></a>

### Retrieve usage plan keys
<a name="API_GetUsagePlanKeys_Example_1"></a>

This example illustrates one usage of GetUsagePlanKeys.

#### Sample Request
<a name="API_GetUsagePlanKeys_Example_1_Request"></a>

```
GET /usageplans/n371pt/keys HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
Content-Length: 58
X-Amz-Date: 20160805T185459Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160805/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sigv4_hash}
Response
```

#### Sample Response
<a name="API_GetUsagePlanKeys_Example_1_Response"></a>

```
{
  "_links": {
    "self": {
      "href": "/usageplans/n371pt/keys"
    },
    "item": {
      "href": "/usageplans/n371pt/keys/4wj0d1lt91"
    }
  },
  "_embedded": {
    "item": {
      "_links": {
        "self": {
          "href": "/usageplans/n371pt/keys/4wj0d1lt91"
        }
      },
      "id": "4wj0d1lt91",
      "name": "MyApiKey",
      "type": "API_KEY"
    }
  }
}
```

## See Also
<a name="API_GetUsagePlanKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetUsagePlanKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetUsagePlanKeys)
