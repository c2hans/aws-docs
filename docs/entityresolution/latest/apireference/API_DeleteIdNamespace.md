---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteIdNamespace.html
---

# DeleteIdNamespace
<a name="API_DeleteIdNamespace"></a>

Deletes the `IdNamespace` with a given name. This operation returns a `ResourceNotFoundException` if an ID namespace with the given name does not exist.

## Request Syntax
<a name="API_DeleteIdNamespace_RequestSyntax"></a>

```
DELETE /idnamespaces/{{idNamespaceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteIdNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [idNamespaceName](#API_DeleteIdNamespace_RequestSyntax) **   <a name="API-DeleteIdNamespace-request-uri-idNamespaceName"></a>
The name of the ID namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_DeleteIdNamespace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteIdNamespace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "message": "string"
}
```

## Response Elements
<a name="API_DeleteIdNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [message](#API_DeleteIdNamespace_ResponseSyntax) **   <a name="API-DeleteIdNamespace-response-message"></a>
A successful operation message.
Type: String

## Errors
<a name="API_DeleteIdNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_DeleteIdNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/DeleteIdNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/DeleteIdNamespace)
