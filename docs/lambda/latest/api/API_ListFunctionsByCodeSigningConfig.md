---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctionsByCodeSigningConfig.html
---

# ListFunctionsByCodeSigningConfig
<a name="API_ListFunctionsByCodeSigningConfig"></a>

List the functions that use the specified code signing configuration. You can use this method prior to deleting a code signing configuration, to verify that no functions are using it.

## Request Syntax
<a name="API_ListFunctionsByCodeSigningConfig_RequestSyntax"></a>

```
GET /2020-04-22/code-signing-configs/{{CodeSigningConfigArn}}/functions?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFunctionsByCodeSigningConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CodeSigningConfigArn](#API_ListFunctionsByCodeSigningConfig_RequestSyntax) **   <a name="lambda-ListFunctionsByCodeSigningConfig-request-uri-CodeSigningConfigArn"></a>
The The Amazon Resource Name (ARN) of the code signing configuration.
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:code-signing-config:csc-[a-z0-9]{17}`
Required: Yes

 ** [Marker](#API_ListFunctionsByCodeSigningConfig_RequestSyntax) **   <a name="lambda-ListFunctionsByCodeSigningConfig-request-uri-Marker"></a>
Specify the pagination token that's returned by a previous request to retrieve the next page of results.

 ** [MaxItems](#API_ListFunctionsByCodeSigningConfig_RequestSyntax) **   <a name="lambda-ListFunctionsByCodeSigningConfig-request-uri-MaxItems"></a>
Maximum number of items to return.
Valid Range: Minimum value of 1. Maximum value of 10000.

## Request Body
<a name="API_ListFunctionsByCodeSigningConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFunctionsByCodeSigningConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FunctionArns": [ "string" ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListFunctionsByCodeSigningConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FunctionArns](#API_ListFunctionsByCodeSigningConfig_ResponseSyntax) **   <a name="lambda-ListFunctionsByCodeSigningConfig-response-FunctionArns"></a>
The function ARNs.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`

 ** [NextMarker](#API_ListFunctionsByCodeSigningConfig_ResponseSyntax) **   <a name="lambda-ListFunctionsByCodeSigningConfig-response-NextMarker"></a>
The pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ListFunctionsByCodeSigningConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

## See Also
<a name="API_ListFunctionsByCodeSigningConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ListFunctionsByCodeSigningConfig)
