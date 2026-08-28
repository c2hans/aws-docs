---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateUsagePlanKey.html
---

# CreateUsagePlanKey
<a name="API_CreateUsagePlanKey"></a>

Creates a usage plan key for adding an existing API key to a usage plan.

## Request Syntax
<a name="API_CreateUsagePlanKey_RequestSyntax"></a>

```
POST /usageplans/{{usageplanId}}/keys HTTP/1.1
Content-type: application/json

{
   "keyId": "{{string}}",
   "keyType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateUsagePlanKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [usageplanId](#API_CreateUsagePlanKey_RequestSyntax) **   <a name="apigw-CreateUsagePlanKey-request-uri-usagePlanId"></a>
The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.
Required: Yes

## Request Body
<a name="API_CreateUsagePlanKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [keyId](#API_CreateUsagePlanKey_RequestSyntax) **   <a name="apigw-CreateUsagePlanKey-request-keyId"></a>
The identifier of a UsagePlanKey resource for a plan customer.
Type: String
Required: Yes

 ** [keyType](#API_CreateUsagePlanKey_RequestSyntax) **   <a name="apigw-CreateUsagePlanKey-request-keyType"></a>
The type of a UsagePlanKey resource for a plan customer.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateUsagePlanKey_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "id": "string",
   "name": "string",
   "type": "string",
   "value": "string"
}
```

## Response Elements
<a name="API_CreateUsagePlanKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [id](#API_CreateUsagePlanKey_ResponseSyntax) **   <a name="apigw-CreateUsagePlanKey-response-id"></a>
The Id of a usage plan key.
Type: String

 ** [name](#API_CreateUsagePlanKey_ResponseSyntax) **   <a name="apigw-CreateUsagePlanKey-response-name"></a>
The name of a usage plan key.
Type: String

 ** [type](#API_CreateUsagePlanKey_ResponseSyntax) **   <a name="apigw-CreateUsagePlanKey-response-type"></a>
The type of a usage plan key. Currently, the valid key type is `API_KEY`.
Type: String

 ** [value](#API_CreateUsagePlanKey_ResponseSyntax) **   <a name="apigw-CreateUsagePlanKey-response-value"></a>
The value of a usage plan key.
Type: String

## Errors
<a name="API_CreateUsagePlanKey_Errors"></a>

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
<a name="API_CreateUsagePlanKey_Examples"></a>

### Create a usage plan key
<a name="API_CreateUsagePlanKey_Example_1"></a>

This example illustrates one usage of CreateUsagePlanKey.

#### Sample Request
<a name="API_CreateUsagePlanKey_Example_1_Request"></a>

```
POST /usageplans/n371pt/keys HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160805T181755Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160805/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sigv4_hash}

{
    "keyId": "q5ugs7qjjh",
    "keyType": "API_KEY"
}
```

#### Sample Response
<a name="API_CreateUsagePlanKey_Example_1_Response"></a>

```
{
  "_links": {
    "self": {
      "href": "/usageplans/n371pt/keys/q5ugs7qjjh"
    }
  },
  "id": "q5ugs7qjjh",
  "name": " importedKey_2",
  "type": "API_KEY"
}
```

## See Also
<a name="API_CreateUsagePlanKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateUsagePlanKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateUsagePlanKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
