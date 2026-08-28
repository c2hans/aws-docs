---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateBasePathMapping.html
---

# UpdateBasePathMapping
<a name="API_UpdateBasePathMapping"></a>

Changes information about the BasePathMapping resource.

## Request Syntax
<a name="API_UpdateBasePathMapping_RequestSyntax"></a>

```
PATCH /domainnames/{{domain_name}}/basepathmappings/{{base_path}}?domainNameId={{domainNameId}} HTTP/1.1
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
<a name="API_UpdateBasePathMapping_RequestParameters"></a>

The request uses the following URI parameters.

 ** [base\_path](#API_UpdateBasePathMapping_RequestSyntax) **   <a name="apigw-UpdateBasePathMapping-request-uri-basePath"></a>
The base path of the BasePathMapping resource to change.
To specify an empty base path, set this parameter to `'(none)'`.
Required: Yes

 ** [domain\_name](#API_UpdateBasePathMapping_RequestSyntax) **   <a name="apigw-UpdateBasePathMapping-request-uri-domainName"></a>
The domain name of the BasePathMapping resource to change.
Required: Yes

 ** [domainNameId](#API_UpdateBasePathMapping_RequestSyntax) **   <a name="apigw-UpdateBasePathMapping-request-uri-domainNameId"></a>
 The identifier for the domain name resource. Supported only for private custom domain names.

## Request Body
<a name="API_UpdateBasePathMapping_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateBasePathMapping_RequestSyntax) **   <a name="apigw-UpdateBasePathMapping-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateBasePathMapping_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "basePath": "string",
   "restApiId": "string",
   "stage": "string"
}
```

## Response Elements
<a name="API_UpdateBasePathMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [basePath](#API_UpdateBasePathMapping_ResponseSyntax) **   <a name="apigw-UpdateBasePathMapping-response-basePath"></a>
The base path name that callers of the API must provide as part of the URL after the domain name.
Type: String

 ** [restApiId](#API_UpdateBasePathMapping_ResponseSyntax) **   <a name="apigw-UpdateBasePathMapping-response-restApiId"></a>
The string identifier of the associated RestApi.
Type: String

 ** [stage](#API_UpdateBasePathMapping_ResponseSyntax) **   <a name="apigw-UpdateBasePathMapping-response-stage"></a>
The name of the associated stage.
Type: String

## Errors
<a name="API_UpdateBasePathMapping_Errors"></a>

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
<a name="API_UpdateBasePathMapping_Examples"></a>

### Update the base path mapping of an API
<a name="API_UpdateBasePathMapping_Example_1"></a>

 The following example request updates the base path (`TestApi`) of a custom domain name (`a.b.c.com`) to map to a different deployment stage (`stage2 `of an API (`fugvjdxtri`).

#### Sample Request
<a name="API_UpdateBasePathMapping_Example_1_Request"></a>

```
PATCH /domainnames/a.b.c.com/basepathmappings/TestApi HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160615T025216Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160615/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "patchOperations" : [ {
    "op" : "replace",
    "path" : "/stage",
    "value" : "stage2"
  } ]
}
```

#### Sample Response
<a name="API_UpdateBasePathMapping_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-basepathmapping-{rel}.html",
      "name": "basepathmapping",
      "templated": true
    },
    "self": {
      "href": "/domainnames/a.b.c.com/basepathmappings/TestApi"
    },
    "basepathmapping:create": {
      "href": "/domainnames/a.b.c.com/basepathmappings"
    },
    "basepathmapping:delete": {
      "href": "/domainnames/a.b.c.com/basepathmappings/TestApi"
    },
    "basepathmapping:update": {
      "href": "/domainnames/a.b.c.com/basepathmappings/TestApi"
    }
  },
  "basepath": "TestApi",
  "restApiId": "fugvjdxtri",
  "stage": "stage2"
}
```

## See Also
<a name="API_UpdateBasePathMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateBasePathMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateBasePathMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
