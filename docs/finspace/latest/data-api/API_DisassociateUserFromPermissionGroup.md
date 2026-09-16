---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_DisassociateUserFromPermissionGroup.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# DisassociateUserFromPermissionGroup
<a name="API_DisassociateUserFromPermissionGroup"></a>

Removes a user from a permission group.

## Request Syntax
<a name="API_DisassociateUserFromPermissionGroup_RequestSyntax"></a>

```
DELETE /permission-group/{{permissionGroupId}}/users/{{userId}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateUserFromPermissionGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DisassociateUserFromPermissionGroup_RequestSyntax) **   <a name="finspace-DisassociateUserFromPermissionGroup-request-uri-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`

 ** [permissionGroupId](#API_DisassociateUserFromPermissionGroup_RequestSyntax) **   <a name="finspace-DisassociateUserFromPermissionGroup-request-uri-permissionGroupId"></a>
The unique identifier for the permission group.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`
Required: Yes

 ** [userId](#API_DisassociateUserFromPermissionGroup_RequestSyntax) **   <a name="finspace-DisassociateUserFromPermissionGroup-request-uri-userId"></a>
The unique identifier for the user.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_DisassociateUserFromPermissionGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateUserFromPermissionGroup_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
```

## Response Elements
<a name="API_DisassociateUserFromPermissionGroup_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_DisassociateUserFromPermissionGroup_ResponseSyntax) **   <a name="finspace-DisassociateUserFromPermissionGroup-response-statusCode"></a>
The returned status code of the response.

## Errors
<a name="API_DisassociateUserFromPermissionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with an existing resource.
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
<a name="API_DisassociateUserFromPermissionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/DisassociateUserFromPermissionGroup)
