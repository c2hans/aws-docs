---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateBasePathMapping.html
---

# CreateBasePathMapping
<a name="API_CreateBasePathMapping"></a>

Creates a new BasePathMapping resource.

## Request Syntax
<a name="API_CreateBasePathMapping_RequestSyntax"></a>

```
POST /domainnames/{{domain_name}}/basepathmappings?domainNameId={{domainNameId}} HTTP/1.1
Content-type: application/json

{
   "basePath": "{{string}}",
   "restApiId": "{{string}}",
   "stage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBasePathMapping_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain\_name](#API_CreateBasePathMapping_RequestSyntax) **   <a name="apigw-CreateBasePathMapping-request-uri-domainName"></a>
The domain name of the BasePathMapping resource to create.
Required: Yes

 ** [domainNameId](#API_CreateBasePathMapping_RequestSyntax) **   <a name="apigw-CreateBasePathMapping-request-uri-domainNameId"></a>
The identifier for the domain name resource. Required for private custom domain names.

## Request Body
<a name="API_CreateBasePathMapping_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [basePath](#API_CreateBasePathMapping_RequestSyntax) **   <a name="apigw-CreateBasePathMapping-request-basePath"></a>
The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do not want callers to specify a base path name after the domain name.
Type: String
Required: No

 ** [restApiId](#API_CreateBasePathMapping_RequestSyntax) **   <a name="apigw-CreateBasePathMapping-request-restApiId"></a>
The string identifier of the associated RestApi.
Type: String
Required: Yes

 ** [stage](#API_CreateBasePathMapping_RequestSyntax) **   <a name="apigw-CreateBasePathMapping-request-stage"></a>
The name of the API's stage that you want to use for this mapping. Specify '(none)' if you want callers to explicitly specify the stage name after any base path name.
Type: String
Required: No

## Response Syntax
<a name="API_CreateBasePathMapping_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "basePath": "string",
   "restApiId": "string",
   "stage": "string"
}
```

## Response Elements
<a name="API_CreateBasePathMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [basePath](#API_CreateBasePathMapping_ResponseSyntax) **   <a name="apigw-CreateBasePathMapping-response-basePath"></a>
The base path name that callers of the API must provide as part of the URL after the domain name.
Type: String

 ** [restApiId](#API_CreateBasePathMapping_ResponseSyntax) **   <a name="apigw-CreateBasePathMapping-response-restApiId"></a>
The string identifier of the associated RestApi.
Type: String

 ** [stage](#API_CreateBasePathMapping_ResponseSyntax) **   <a name="apigw-CreateBasePathMapping-response-stage"></a>
The name of the associated stage.
Type: String

## Errors
<a name="API_CreateBasePathMapping_Errors"></a>

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
<a name="API_CreateBasePathMapping_Examples"></a>

### Creates base path mapping for an API
<a name="API_CreateBasePathMapping_Example_1"></a>

 The following example request creates a `TestApi` base path that is mapped the `fugvjdxtri` API in the `stage1` stage.

#### Sample Request
<a name="API_CreateBasePathMapping_Example_1_Request"></a>

```
POST /domainnames/a.b.c.com/basepathmappings HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160615T012033Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160615/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "basepath" : "TestApi",
  "restApiId" : "fugvjdxtri",
  "stage" : "stage1"
}
```

#### Sample Response
<a name="API_CreateBasePathMapping_Example_1_Response"></a>

```
{
  "_links": {upd
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
  "stage": "stage1"
}
```

## See Also
<a name="API_CreateBasePathMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateBasePathMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateBasePathMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
