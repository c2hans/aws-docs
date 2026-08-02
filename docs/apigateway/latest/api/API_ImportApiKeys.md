---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_ImportApiKeys.html
---

# ImportApiKeys
<a name="API_ImportApiKeys"></a>

Import API keys from an external source, such as a CSV-formatted file.

## Request Syntax
<a name="API_ImportApiKeys_RequestSyntax"></a>

```
POST /apikeys?mode=import&failonwarnings={{failOnWarnings}}&format={{format}} HTTP/1.1

{{body}}
```

## URI Request Parameters
<a name="API_ImportApiKeys_RequestParameters"></a>

The request uses the following URI parameters.

 ** [failOnWarnings](#API_ImportApiKeys_RequestSyntax) **   <a name="apigw-ImportApiKeys-request-uri-failOnWarnings"></a>
A query parameter to indicate whether to rollback ApiKey importation (`true`) or not (`false`) when error is encountered.

 ** [format](#API_ImportApiKeys_RequestSyntax) **   <a name="apigw-ImportApiKeys-request-uri-format"></a>
A query parameter to specify the input format to imported API keys. Currently, only the `csv` format is supported.
Valid Values: `csv`
Required: Yes

## Request Body
<a name="API_ImportApiKeys_RequestBody"></a>

The request accepts the following binary data.

 ** [body](#API_ImportApiKeys_RequestSyntax) **   <a name="apigw-ImportApiKeys-request-body"></a>
The payload of the POST request to import API keys. For the payload format, see API Key File Format.
Required: Yes

## Response Syntax
<a name="API_ImportApiKeys_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ids": [ "string" ],
   "warnings": [ "string" ]
}
```

## Response Elements
<a name="API_ImportApiKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ids](#API_ImportApiKeys_ResponseSyntax) **   <a name="apigw-ImportApiKeys-response-ids"></a>
A list of all the ApiKey identifiers.
Type: Array of strings

 ** [warnings](#API_ImportApiKeys_ResponseSyntax) **   <a name="apigw-ImportApiKeys-response-warnings"></a>
A list of warning messages.
Type: Array of strings

## Errors
<a name="API_ImportApiKeys_Errors"></a>

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

## See Also
<a name="API_ImportApiKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/ImportApiKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/ImportApiKeys)
