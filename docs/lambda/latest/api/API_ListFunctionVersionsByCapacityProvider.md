---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctionVersionsByCapacityProvider.html
---

# ListFunctionVersionsByCapacityProvider
<a name="API_ListFunctionVersionsByCapacityProvider"></a>

Returns a list of function versions that are configured to use a specific capacity provider.

## Request Syntax
<a name="API_ListFunctionVersionsByCapacityProvider_RequestSyntax"></a>

```
GET /2025-11-30/capacity-providers/{{CapacityProviderName}}/function-versions?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFunctionVersionsByCapacityProvider_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CapacityProviderName](#API_ListFunctionVersionsByCapacityProvider_RequestSyntax) **   <a name="lambda-ListFunctionVersionsByCapacityProvider-request-uri-CapacityProviderName"></a>
The name of the capacity provider to list function versions for.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:aws[a-zA-Z-]*:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: Yes

 ** [Marker](#API_ListFunctionVersionsByCapacityProvider_RequestSyntax) **   <a name="lambda-ListFunctionVersionsByCapacityProvider-request-uri-Marker"></a>
Specify the pagination token that's returned by a previous request to retrieve the next page of results.

 ** [MaxItems](#API_ListFunctionVersionsByCapacityProvider_RequestSyntax) **   <a name="lambda-ListFunctionVersionsByCapacityProvider-request-uri-MaxItems"></a>
The maximum number of function versions to return in the response.
Valid Range: Minimum value of 1. Maximum value of 50.

## Request Body
<a name="API_ListFunctionVersionsByCapacityProvider_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFunctionVersionsByCapacityProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CapacityProviderArn": "string",
   "FunctionVersions": [
      {
         "FunctionArn": "string",
         "State": "string"
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListFunctionVersionsByCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CapacityProviderArn](#API_ListFunctionVersionsByCapacityProvider_ResponseSyntax) **   <a name="lambda-ListFunctionVersionsByCapacityProvider-response-CapacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:aws[a-zA-Z-]*:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+`

 ** [FunctionVersions](#API_ListFunctionVersionsByCapacityProvider_ResponseSyntax) **   <a name="lambda-ListFunctionVersionsByCapacityProvider-response-FunctionVersions"></a>
A list of function versions that use the specified capacity provider.
Type: Array of [FunctionVersionsByCapacityProviderListItem](API_FunctionVersionsByCapacityProviderListItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [NextMarker](#API_ListFunctionVersionsByCapacityProvider_ResponseSyntax) **   <a name="lambda-ListFunctionVersionsByCapacityProvider-response-NextMarker"></a>
The pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ListFunctionVersionsByCapacityProvider_Errors"></a>

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

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_ListFunctionVersionsByCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ListFunctionVersionsByCapacityProvider)
