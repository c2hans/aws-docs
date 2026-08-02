---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetBasePathMapping.html
---

# GetBasePathMapping
<a name="API_GetBasePathMapping"></a>

Describe a BasePathMapping resource.

## Request Syntax
<a name="API_GetBasePathMapping_RequestSyntax"></a>

```
GET /domainnames/{{domain_name}}/basepathmappings/{{base_path}}?domainNameId={{domainNameId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBasePathMapping_RequestParameters"></a>

The request uses the following URI parameters.

 ** [base\_path](#API_GetBasePathMapping_RequestSyntax) **   <a name="apigw-GetBasePathMapping-request-uri-basePath"></a>
The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do not want callers to specify any base path name after the domain name.
Required: Yes

 ** [domain\_name](#API_GetBasePathMapping_RequestSyntax) **   <a name="apigw-GetBasePathMapping-request-uri-domainName"></a>
The domain name of the BasePathMapping resource to be described.
Required: Yes

 ** [domainNameId](#API_GetBasePathMapping_RequestSyntax) **   <a name="apigw-GetBasePathMapping-request-uri-domainNameId"></a>
The identifier for the domain name resource. Supported only for private custom domain names.

## Request Body
<a name="API_GetBasePathMapping_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBasePathMapping_ResponseSyntax"></a>

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
<a name="API_GetBasePathMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [basePath](#API_GetBasePathMapping_ResponseSyntax) **   <a name="apigw-GetBasePathMapping-response-basePath"></a>
The base path name that callers of the API must provide as part of the URL after the domain name.
Type: String

 ** [restApiId](#API_GetBasePathMapping_ResponseSyntax) **   <a name="apigw-GetBasePathMapping-response-restApiId"></a>
The string identifier of the associated RestApi.
Type: String

 ** [stage](#API_GetBasePathMapping_ResponseSyntax) **   <a name="apigw-GetBasePathMapping-response-stage"></a>
The name of the associated stage.
Type: String

## Errors
<a name="API_GetBasePathMapping_Errors"></a>

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

## See Also
<a name="API_GetBasePathMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetBasePathMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetBasePathMapping)
