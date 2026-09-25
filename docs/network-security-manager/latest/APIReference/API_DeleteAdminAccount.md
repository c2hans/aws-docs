---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_DeleteAdminAccount.html
---

# DeleteAdminAccount
<a name="API_DeleteAdminAccount"></a>

Removes the specified AWS Network Security Manager administrator account.

## Request Syntax
<a name="API_DeleteAdminAccount_RequestSyntax"></a>

```
DELETE /admin-account/{{accountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAdminAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_DeleteAdminAccount_RequestSyntax) **   <a name="networksecuritymanager-DeleteAdminAccount-request-uri-accountId"></a>
The AWS account ID of the administrator account to remove.
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: Yes

## Request Body
<a name="API_DeleteAdminAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAdminAccount_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteAdminAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteAdminAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing failed because of an internal error in the service. This is a retryable error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because of request throttling. Reduce your request rate and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation. For details, see the `reason` and `fieldList` members of the response.
 ** fieldList **
The list of request fields that failed validation, if any.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/DeleteAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/DeleteAdminAccount)
