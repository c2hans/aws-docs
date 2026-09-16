---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html
---

# ListDetectors
<a name="API_ListDetectors"></a>

Lists detectorIds of all the existing Amazon GuardDuty detector resources.

## Request Syntax
<a name="API_ListDetectors_RequestSyntax"></a>

```
GET /detector?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDetectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListDetectors_RequestSyntax) **   <a name="guardduty-ListDetectors-request-uri-MaxResults"></a>
You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListDetectors_RequestSyntax) **   <a name="guardduty-ListDetectors-request-uri-NextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

## Request Body
<a name="API_ListDetectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDetectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "detectorIds": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDetectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [detectorIds](#API_ListDetectors_ResponseSyntax) **   <a name="guardduty-ListDetectors-response-detectorIds"></a>
A list of detector IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [nextToken](#API_ListDetectors_ResponseSyntax) **   <a name="guardduty-ListDetectors-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String

## Errors
<a name="API_ListDetectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_ListDetectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListDetectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListDetectors)
