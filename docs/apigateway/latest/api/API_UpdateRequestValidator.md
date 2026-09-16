---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateRequestValidator.html
---

# UpdateRequestValidator
<a name="API_UpdateRequestValidator"></a>

Updates a RequestValidator of a given RestApi.

## Request Syntax
<a name="API_UpdateRequestValidator_RequestSyntax"></a>

```
PATCH /restapis/{{restapi_id}}/requestvalidators/{{requestvalidator_id}} HTTP/1.1
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
<a name="API_UpdateRequestValidator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [requestvalidator\_id](#API_UpdateRequestValidator_RequestSyntax) **   <a name="apigw-UpdateRequestValidator-request-uri-requestValidatorId"></a>
The identifier of RequestValidator to be updated.
Required: Yes

 ** [restapi\_id](#API_UpdateRequestValidator_RequestSyntax) **   <a name="apigw-UpdateRequestValidator-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_UpdateRequestValidator_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateRequestValidator_RequestSyntax) **   <a name="apigw-UpdateRequestValidator-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateRequestValidator_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "name": "string",
   "validateRequestBody": boolean,
   "validateRequestParameters": boolean
}
```

## Response Elements
<a name="API_UpdateRequestValidator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_UpdateRequestValidator_ResponseSyntax) **   <a name="apigw-UpdateRequestValidator-response-id"></a>
The identifier of this RequestValidator.
Type: String

 ** [name](#API_UpdateRequestValidator_ResponseSyntax) **   <a name="apigw-UpdateRequestValidator-response-name"></a>
The name of this RequestValidator
Type: String

 ** [validateRequestBody](#API_UpdateRequestValidator_ResponseSyntax) **   <a name="apigw-UpdateRequestValidator-response-validateRequestBody"></a>
A Boolean flag to indicate whether to validate a request body according to the configured Model schema.
Type: Boolean

 ** [validateRequestParameters](#API_UpdateRequestValidator_ResponseSyntax) **   <a name="apigw-UpdateRequestValidator-response-validateRequestParameters"></a>
A Boolean flag to indicate whether to validate request parameters (`true`) or not (`false`).
Type: Boolean

## Errors
<a name="API_UpdateRequestValidator_Errors"></a>

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
<a name="API_UpdateRequestValidator_Examples"></a>

### Update a RequestValidator for an API
<a name="API_UpdateRequestValidator_Example_1"></a>

This example illustrates one usage of UpdateRequestValidator.

#### Sample Request
<a name="API_UpdateRequestValidator_Example_1_Request"></a>

```
PATCH /restapis/mkhqppt4e4/requestvalidators/3n5aa0 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T172652Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}

{
  "patchOperations" : [ {
    "op" : "replace",
    "path" : "/name",
    "value" : "body-parameters-switched"
  }, {
    "op" : "replace",
    "path" : "/validateRequestBody",
    "value" : "false"
  }, {
    "op" : "replace",
    "path" : "/validateRequestParameters",
    "value" : "true"
  } ]
}
```

#### Sample Response
<a name="API_UpdateRequestValidator_Example_1_Response"></a>

```
{
  "_links": {
    "self": {
      "href": "/restapis/mkhqppt4e4/requestvalidators/3n5aa0"
    },
    "request-validator-delete": {
      "href": "/restapis/mkhqppt4e4/requestvalidators/3n5aa0"
    },
    "request-validator-update": {
      "href": "/restapis/mkhqppt4e4/requestvalidators/3n5aa0"
    }
  },
  "id": "3n5aa0",
  "name": "body-parameters-switched",
  "validateRequestBody": false,
  "validateRequestParameters": true
}
```

## See Also
<a name="API_UpdateRequestValidator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateRequestValidator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateRequestValidator)
