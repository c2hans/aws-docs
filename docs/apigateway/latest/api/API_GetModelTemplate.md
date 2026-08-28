---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetModelTemplate.html
---

# GetModelTemplate
<a name="API_GetModelTemplate"></a>

Generates a sample mapping template that can be used to transform a payload into the structure of a model.

## Request Syntax
<a name="API_GetModelTemplate_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/models/{{model_name}}/default_template HTTP/1.1
```

## URI Request Parameters
<a name="API_GetModelTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [model\_name](#API_GetModelTemplate_RequestSyntax) **   <a name="apigw-GetModelTemplate-request-uri-modelName"></a>
The name of the model for which to generate a template.
Required: Yes

 ** [restapi\_id](#API_GetModelTemplate_RequestSyntax) **   <a name="apigw-GetModelTemplate-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetModelTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetModelTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "value": "string"
}
```

## Response Elements
<a name="API_GetModelTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [value](#API_GetModelTemplate_ResponseSyntax) **   <a name="apigw-GetModelTemplate-response-value"></a>
The Apache Velocity Template Language (VTL) template content used for the template resource.
Type: String

## Errors
<a name="API_GetModelTemplate_Errors"></a>

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
<a name="API_GetModelTemplate_Examples"></a>

### Generate the sample template from a model
<a name="API_GetModelTemplate_Example_1"></a>

This example illustrates one usage of GetModelTemplate.

#### Sample Request
<a name="API_GetModelTemplate_Example_1_Request"></a>

```
GET /restapis/uojnr9hd57/models/output/default_template HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160614T202448Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160614/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
Response
```

#### Sample Response
<a name="API_GetModelTemplate_Example_1_Response"></a>

```
{
  "_links": {
    "self": {
      "href": "/restapis/uojnr9hd57/models/output/default_template"
    }
  },
  "value": "#set($inputRoot = $input.path('$'))\n{\n  \"a\" : 3.1415,\n  \"b\" : 3.1415,\n  \"op\" : \"foo\",\n  \"c\" : 3.1415\n}"
}
```

## See Also
<a name="API_GetModelTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetModelTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetModelTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
