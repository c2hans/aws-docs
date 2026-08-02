---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateUsage.html
---

# UpdateUsage
<a name="API_UpdateUsage"></a>

Grants a temporary extension to the remaining quota of a usage plan associated with a specified API key.

## Request Syntax
<a name="API_UpdateUsage_RequestSyntax"></a>

```
PATCH /usageplans/{{usageplanId}}/keys/{{keyId}}/usage HTTP/1.1
Content-type: application/json

{
   "patchOperations": [
      {
         "from": "{{string}}",
         "op": "{{string}}",
         "path": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateUsage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [keyId](#API_UpdateUsage_RequestSyntax) **   <a name="apigw-UpdateUsage-request-uri-keyId"></a>
The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.
Required: Yes

 ** [usageplanId](#API_UpdateUsage_RequestSyntax) **   <a name="apigw-UpdateUsage-request-uri-usagePlanId"></a>
The Id of the usage plan associated with the usage data.
Required: Yes

## Request Body
<a name="API_UpdateUsage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateUsage_RequestSyntax) **   <a name="apigw-UpdateUsage-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateUsage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endDate": "string",
   "values": {
      "string" : [
         [ number ]
      ]
   },
   "position": "string",
   "startDate": "string",
   "usagePlanId": "string"
}
```

## Response Elements
<a name="API_UpdateUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endDate](#API_UpdateUsage_ResponseSyntax) **   <a name="apigw-UpdateUsage-response-endDate"></a>
The ending date of the usage data.
Type: String

 ** [values](#API_UpdateUsage_ResponseSyntax) **   <a name="apigw-UpdateUsage-response-values"></a>
The usage data, as daily logs of used and remaining quotas, over the specified time interval indexed over the API keys in a usage plan. For example, `{..., "values" : { "{api_key}" : [ [0, 100], [10, 90], [100, 10]]}`, where `{api_key}` stands for an API key ID and the daily log entry is of the format `[used quota, remaining quota]`.
Type: String to array of arrays of longs map

 ** [position](#API_UpdateUsage_ResponseSyntax) **   <a name="apigw-UpdateUsage-response-position"></a>
The current pagination position in the paged result set.
Type: String

 ** [startDate](#API_UpdateUsage_ResponseSyntax) **   <a name="apigw-UpdateUsage-response-startDate"></a>
The starting date of the usage data.
Type: String

 ** [usagePlanId](#API_UpdateUsage_ResponseSyntax) **   <a name="apigw-UpdateUsage-response-usagePlanId"></a>
The plan Id associated with this usage data.
Type: String

## Errors
<a name="API_UpdateUsage_Errors"></a>

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
<a name="API_UpdateUsage_Examples"></a>

### Update usage
<a name="API_UpdateUsage_Example_1"></a>

This example illustrates one usage of UpdateUsage.

#### Sample Request
<a name="API_UpdateUsage_Example_1_Request"></a>

```
PATCH /usageplans/ywbqww/keys/3JX4ISs7Ik23cDsgiaJdu6SiLffQpIsU7AyTMALs6/usage HTTP/1.1
Content-Type: application/json
Host: apigateway.ap-southeast-1.amazonaws.com
Content-Length: 114
X-Amz-Date: 20160801T235803Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160801/ap-southeast-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sigv4_hash}

{
    "patchOperation" : [ {
       "op": "replace",
       "path": "/remaining",
       "value": "10"
    } ]
}
```

#### Sample Response
<a name="API_UpdateUsage_Example_1_Response"></a>

```
{
  "_links": {
    "self": {
      "href": "/usageplans/ywbqww/keys/3JX4ISs7Ik23cDsgiaJdu6SiLffQpIsU7AyTMALs6/usage"
    }
  },
  "endDate": "2016-08-08",
  "startDate": "2016-08-08",
  "usagePlanId": "ywbqww",
  "values": {
    "3JX4ISs7Ik23cDsgiaJdu6SiLffQpIsU7AyTMALs6": [
      0,
      10
    ]
  }
}
```

## See Also
<a name="API_UpdateUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateUsage)
