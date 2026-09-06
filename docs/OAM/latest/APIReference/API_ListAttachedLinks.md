---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinks.html
---

# ListAttachedLinks
<a name="API_ListAttachedLinks"></a>

Returns a list of source account links that are linked to this monitoring account sink.

To use this operation, provide the sink ARN. To retrieve a list of sink ARNs, use [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html).

To find a list of links for one source account, use [ListLinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html).

## Request Syntax
<a name="API_ListAttachedLinks_RequestSyntax"></a>

```
POST /ListAttachedLinks HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SinkIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAttachedLinks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAttachedLinks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListAttachedLinks_RequestSyntax) **   <a name="OAM-ListAttachedLinks-request-MaxResults"></a>
Limits the number of returned links to the specified number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListAttachedLinks_RequestSyntax) **   <a name="OAM-ListAttachedLinks-request-NextToken"></a>
The token for the next set of items to return. You received this token from a previous call.
Type: String
Required: No

 ** [SinkIdentifier](#API_ListAttachedLinks_RequestSyntax) **   <a name="OAM-ListAttachedLinks-request-SinkIdentifier"></a>
The ARN of the sink that you want to retrieve links for.
Type: String
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_:\.\-\/]{0,2047}`
Required: Yes

## Response Syntax
<a name="API_ListAttachedLinks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Label": "string",
         "LinkArn": "string",
         "ResourceTypes": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAttachedLinks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListAttachedLinks_ResponseSyntax) **   <a name="OAM-ListAttachedLinks-response-Items"></a>
An array of structures that contain the information about the attached links.
Type: Array of [ListAttachedLinksItem](API_ListAttachedLinksItem.md) objects

 ** [NextToken](#API_ListAttachedLinks_ResponseSyntax) **   <a name="OAM-ListAttachedLinks-response-NextToken"></a>
The token to use when requesting the next set of links.
Type: String

## Errors
<a name="API_ListAttachedLinks_Errors"></a>

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

 ** MissingRequiredParameterException **
A required parameter is missing from the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 404

## See Also
<a name="API_ListAttachedLinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/ListAttachedLinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/ListAttachedLinks)
