---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_DeletePermissionVersion.html
---

# DeletePermissionVersion
<a name="API_DeletePermissionVersion"></a>

Deletes one version of a customer managed permission. The version you specify must not be attached to any resource share and must not be the default version for the permission.

If a customer managed permission has the maximum of 5 versions, then you must delete at least one version before you can create another.

## Request Syntax
<a name="API_DeletePermissionVersion_RequestSyntax"></a>

```
DELETE /deletepermissionversion?clientToken={{clientToken}}&permissionArn={{permissionArn}}&permissionVersion={{permissionVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePermissionVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeletePermissionVersion_RequestSyntax) **   <a name="ram-DeletePermissionVersion-request-uri-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.

 ** [permissionArn](#API_DeletePermissionVersion_RequestSyntax) **   <a name="ram-DeletePermissionVersion-request-uri-permissionArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the permission with the version you want to delete.
Required: Yes

 ** [permissionVersion](#API_DeletePermissionVersion_RequestSyntax) **   <a name="ram-DeletePermissionVersion-request-uri-permissionVersion"></a>
Specifies the version number to delete.
You can't delete the default version for a customer managed permission.
You can't delete a version if it's the only version of the permission. You must either first create another version, or delete the permission completely.
You can't delete a version if it is attached to any resource shares. If the version is the default, you must first use [SetDefaultPermissionVersion](API_SetDefaultPermissionVersion.md) to set a different version as the default for the customer managed permission, and then use [AssociateResourceSharePermission](API_AssociateResourceSharePermission.md) to update your resource shares to use the new default version.
Required: Yes

## Request Body
<a name="API_DeletePermissionVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePermissionVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "permissionStatus": "string",
   "returnValue": boolean
}
```

## Response Elements
<a name="API_DeletePermissionVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_DeletePermissionVersion_ResponseSyntax) **   <a name="ram-DeletePermissionVersion-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [permissionStatus](#API_DeletePermissionVersion_ResponseSyntax) **   <a name="ram-DeletePermissionVersion-response-permissionStatus"></a>
This operation is performed asynchronously, and this response parameter indicates the current status.
Type: String
Valid Values: `ATTACHABLE | UNATTACHABLE | DELETING | DELETED`

 ** [returnValue](#API_DeletePermissionVersion_ResponseSyntax) **   <a name="ram-DeletePermissionVersion-response-returnValue"></a>
A boolean value that indicates whether the operation is successful.
Type: Boolean

## Errors
<a name="API_DeletePermissionVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.
HTTP Status Code: 400

 ** InvalidClientTokenException **
The operation failed because the specified client token isn't valid.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

## See Also
<a name="API_DeletePermissionVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/DeletePermissionVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/DeletePermissionVersion)
