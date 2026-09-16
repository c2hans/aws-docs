---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html
---

# ListSinks
<a name="API_ListSinks"></a>

Use this operation in a monitoring account to return the list of sinks created in that account.

## Request Syntax
<a name="API_ListSinks_RequestSyntax"></a>

```
POST /ListSinks HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSinks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSinks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListSinks_RequestSyntax) **   <a name="OAM-ListSinks-request-MaxResults"></a>
Limits the number of returned links to the specified number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListSinks_RequestSyntax) **   <a name="OAM-ListSinks-request-NextToken"></a>
The token for the next set of items to return. You received this token from a previous call.
Type: String
Required: No

## Response Syntax
<a name="API_ListSinks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "Id": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListSinks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListSinks_ResponseSyntax) **   <a name="OAM-ListSinks-response-Items"></a>
An array of structures that contain the information about the returned sinks.
Type: Array of [ListSinksItem](API_ListSinksItem.md) objects

 ** [NextToken](#API_ListSinks_ResponseSyntax) **   <a name="OAM-ListSinks-response-NextToken"></a>
The token to use when requesting the next set of sinks.
Type: String

## Errors
<a name="API_ListSinks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceFault **
Unexpected error while processing the request. Retry the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 500

 ** InvalidParameterException **
A parameter is specified incorrectly.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 404

## See Also
<a name="API_ListSinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/ListSinks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/ListSinks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/ListSinks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/ListSinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/ListSinks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/ListSinks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/ListSinks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/ListSinks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/ListSinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/ListSinks)
