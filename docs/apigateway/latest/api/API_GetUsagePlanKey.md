---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetUsagePlanKey.html
---

# GetUsagePlanKey
<a name="API_GetUsagePlanKey"></a>

Gets a usage plan key of a given key identifier.

## Request Syntax
<a name="API_GetUsagePlanKey_RequestSyntax"></a>

```
GET /usageplans/{{usageplanId}}/keys/{{keyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUsagePlanKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [keyId](#API_GetUsagePlanKey_RequestSyntax) **   <a name="apigw-GetUsagePlanKey-request-uri-keyId"></a>
The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer.
Required: Yes

 ** [usageplanId](#API_GetUsagePlanKey_RequestSyntax) **   <a name="apigw-GetUsagePlanKey-request-uri-usagePlanId"></a>
The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
Required: Yes

## Request Body
<a name="API_GetUsagePlanKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUsagePlanKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "name": "string",
   "type": "string",
   "value": "string"
}
```

## Response Elements
<a name="API_GetUsagePlanKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_GetUsagePlanKey_ResponseSyntax) **   <a name="apigw-GetUsagePlanKey-response-id"></a>
The Id of a usage plan key.
Type: String

 ** [name](#API_GetUsagePlanKey_ResponseSyntax) **   <a name="apigw-GetUsagePlanKey-response-name"></a>
The name of a usage plan key.
Type: String

 ** [type](#API_GetUsagePlanKey_ResponseSyntax) **   <a name="apigw-GetUsagePlanKey-response-type"></a>
The type of a usage plan key. Currently, the valid key type is `API_KEY`.
Type: String

 ** [value](#API_GetUsagePlanKey_ResponseSyntax) **   <a name="apigw-GetUsagePlanKey-response-value"></a>
The value of a usage plan key.
Type: String

## Errors
<a name="API_GetUsagePlanKey_Errors"></a>

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
<a name="API_GetUsagePlanKey_Examples"></a>

### Retrieve a usage plan key
<a name="API_GetUsagePlanKey_Example_1"></a>

This example illustrates one usage of GetUsagePlanKey.

#### Sample Request
<a name="API_GetUsagePlanKey_Example_1_Request"></a>

```
GET /usageplans/n371pt/keys/4wj0d1lt91 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
Content-Length: 58
X-Amz-Date: 20160805T180524Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160805/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sigv4_hash}
Response
```

#### Sample Response
<a name="API_GetUsagePlanKey_Example_1_Response"></a>

```
{
  "_links": {
    "self": {
      "href": "/usageplans/n371pt/keys/4wj0d1lt91"
    }
  },
  "id": "4wj0d1lt91",
  "name": "MyApiKey",
  "type": "API_KEY"
}
```

## See Also
<a name="API_GetUsagePlanKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetUsagePlanKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetUsagePlanKey)
