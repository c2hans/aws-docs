---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteDomain.html
---

# DeleteDomain
<a name="API_DeleteDomain"></a>

Deletes a Amazon DataZone domain.

## Request Syntax
<a name="API_DeleteDomain_RequestSyntax"></a>

```
DELETE /v2/domains/{{identifier}}?clientToken={{clientToken}}&skipDeletionCheck={{skipDeletionCheck}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteDomain_RequestSyntax) **   <a name="datazone-DeleteDomain-request-uri-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.

 ** [identifier](#API_DeleteDomain_RequestSyntax) **   <a name="datazone-DeleteDomain-request-uri-identifier"></a>
The identifier of the AWS domain that is to be deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [skipDeletionCheck](#API_DeleteDomain_RequestSyntax) **   <a name="datazone-DeleteDomain-request-uri-skipDeletionCheck"></a>
Specifies the optional flag to delete all child entities within the domain.

## Request Body
<a name="API_DeleteDomain_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDomain_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DeleteDomain_ResponseSyntax) **   <a name="datazone-DeleteDomain-response-status"></a>
The status of the domain.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATION_FAILED | DELETING | DELETED | DELETION_FAILED`

## Errors
<a name="API_DeleteDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteDomain)
