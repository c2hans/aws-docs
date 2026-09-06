---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateMethodResponse.html
---

# UpdateMethodResponse
<a name="API_UpdateMethodResponse"></a>

Updates an existing MethodResponse resource.

## Request Syntax
<a name="API_UpdateMethodResponse_RequestSyntax"></a>

```
PATCH /restapis/{{restapi_id}}/resources/{{resource_id}}/methods/{{http_method}}/responses/{{status_code}} HTTP/1.1
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
<a name="API_UpdateMethodResponse_RequestParameters"></a>

The request uses the following URI parameters.

 ** [http\_method](#API_UpdateMethodResponse_RequestSyntax) **   <a name="apigw-UpdateMethodResponse-request-uri-httpMethod"></a>
The HTTP verb of the Method resource.
Required: Yes

 ** [resource\_id](#API_UpdateMethodResponse_RequestSyntax) **   <a name="apigw-UpdateMethodResponse-request-uri-resourceId"></a>
The Resource identifier for the MethodResponse resource.
Required: Yes

 ** [restapi\_id](#API_UpdateMethodResponse_RequestSyntax) **   <a name="apigw-UpdateMethodResponse-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

 ** [status\_code](#API_UpdateMethodResponse_RequestSyntax) **   <a name="apigw-UpdateMethodResponse-request-uri-statusCode"></a>
The status code for the MethodResponse resource.
Pattern: `[1-5]\d\d`
Required: Yes

## Request Body
<a name="API_UpdateMethodResponse_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateMethodResponse_RequestSyntax) **   <a name="apigw-UpdateMethodResponse-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateMethodResponse_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "responseModels": {
      "string" : "string"
   },
   "responseParameters": {
      "string" : boolean
   },
   "statusCode": "string"
}
```

## Response Elements
<a name="API_UpdateMethodResponse_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [responseModels](#API_UpdateMethodResponse_ResponseSyntax) **   <a name="apigw-UpdateMethodResponse-response-responseModels"></a>
Specifies the Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a Model name as the value.
Type: String to string map

 ** [responseParameters](#API_UpdateMethodResponse_ResponseSyntax) **   <a name="apigw-UpdateMethodResponse-response-responseParameters"></a>
A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern `method.response.header.{name}`, where `name` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's IntegrationResponse. The integration response data that can be mapped include an integration response header expressed in `integration.response.header.{name}`, a static value enclosed within a pair of single quotes (e.g., `'application/json'`), or a JSON expression from the back-end response payload in the form of `integration.response.body.{JSON-expression}`, where `JSON-expression` is a valid JSON expression without the `$` prefix.)
Type: String to boolean map

 ** [statusCode](#API_UpdateMethodResponse_ResponseSyntax) **   <a name="apigw-UpdateMethodResponse-response-statusCode"></a>
The method response's status code.
Type: String
Pattern: `[1-5]\d\d`

## Errors
<a name="API_UpdateMethodResponse_Errors"></a>

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
<a name="API_UpdateMethodResponse_Examples"></a>

### Update response parameters and models
<a name="API_UpdateMethodResponse_Example_1"></a>

This example illustrates one usage of UpdateMethodResponse.

#### Sample Request
<a name="API_UpdateMethodResponse_Example_1_Request"></a>

```
PATCH /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200 HTTP/1.1
Content-Type: application/x-amz-json-1.1
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160613T233140Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160613/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "patchOperations" : [ {
    "op" : "replace",
    "path" : "/responseParameters/method.response.header.operator",
    "value" : "true"
  },
  {
    "op" : "replace",
    "path" : "/responseModels/application~1json",
    "value" : "output"
  } ]
}
```

#### Sample Response
<a name="API_UpdateMethodResponse_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
      "name": "methodresponse",
      "templated": true
    },
    "self": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200",
      "title": "200"
    },
    "methodresponse:delete": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200"
    },
    "methodresponse:update": {
      "href": "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200"
    }
  },
  "responseModels": {
    "application/json": "output"
  },
  "responseParameters": {
    "method.response.header.operator": true,
    "method.response.header.operand_2": false,
    "method.response.header.operand_1": false
  },
  "statusCode": "200"
}
```

## See Also
<a name="API_UpdateMethodResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateMethodResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateMethodResponse)
