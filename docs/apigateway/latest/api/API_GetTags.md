---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetTags.html
---

# GetTags
<a name="API_GetTags"></a>

Gets the Tags collection for a given resource.

## Request Syntax
<a name="API_GetTags_RequestSyntax"></a>

```
GET /tags/{{resource_arn}}?limit={{limit}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTags_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_GetTags_RequestSyntax) **   <a name="apigw-GetTags-request-uri-limit"></a>
(Not currently supported) The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [position](#API_GetTags_RequestSyntax) **   <a name="apigw-GetTags-request-uri-position"></a>
(Not currently supported) The current pagination position in the paged result set.

 ** [resource\_arn](#API_GetTags_RequestSyntax) **   <a name="apigw-GetTags-request-uri-resourceArn"></a>
The ARN of a resource that can be tagged.
Required: Yes

## Request Body
<a name="API_GetTags_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTags_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_GetTags_ResponseSyntax) **   <a name="apigw-GetTags-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

## Errors
<a name="API_GetTags_Errors"></a>

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
<a name="API_GetTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetTags)
