---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxUser.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# DeleteKxUser
<a name="API_DeleteKxUser"></a>

Deletes a user in the specified kdb environment.

## Request Syntax
<a name="API_DeleteKxUser_RequestSyntax"></a>

```
DELETE /kx/environments/{{environmentId}}/users/{{userName}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteKxUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteKxUser_RequestSyntax) **   <a name="finspace-DeleteKxUser-request-uri-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `.*\S.*`

 ** [environmentId](#API_DeleteKxUser_RequestSyntax) **   <a name="finspace-DeleteKxUser-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: Yes

 ** [userName](#API_DeleteKxUser_RequestSyntax) **   <a name="finspace-DeleteKxUser-request-uri-userName"></a>
A unique identifier for the user that you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[0-9A-Za-z_-]{1,50}$`
Required: Yes

## Request Body
<a name="API_DeleteKxUser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteKxUser_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteKxUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteKxUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteKxUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/DeleteKxUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/DeleteKxUser)
