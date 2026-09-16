---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteLink.html
---

# DeleteLink
<a name="API_DeleteLink"></a>

Deletes a link between a monitoring account sink and a source account. You must run this operation in the source account.

## Request Syntax
<a name="API_DeleteLink_RequestSyntax"></a>

```
POST /DeleteLink HTTP/1.1
Content-type: application/json

{
   "Identifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteLink_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteLink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Identifier](#API_DeleteLink_RequestSyntax) **   <a name="OAM-DeleteLink-request-Identifier"></a>
The ARN of the link to delete.
Type: String
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_:\.\-\/]{0,2047}`
Required: Yes

## Response Syntax
<a name="API_DeleteLink_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteLink_Errors"></a>

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
<a name="API_DeleteLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/DeleteLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/DeleteLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/DeleteLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/DeleteLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/DeleteLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/DeleteLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/DeleteLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/DeleteLink)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/DeleteLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/DeleteLink)
