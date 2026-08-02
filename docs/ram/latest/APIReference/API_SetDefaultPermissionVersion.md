---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_SetDefaultPermissionVersion.html
---

# SetDefaultPermissionVersion
<a name="API_SetDefaultPermissionVersion"></a>

Designates the specified version number as the default version for the specified customer managed permission. New resource shares automatically use this new default permission. Existing resource shares continue to use their original permission version, but you can use [ReplacePermissionAssociations](API_ReplacePermissionAssociations.md) to update them.

## Request Syntax
<a name="API_SetDefaultPermissionVersion_RequestSyntax"></a>

```
POST /setdefaultpermissionversion HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "permissionArn": "{{string}}",
   "permissionVersion": {{number}}
}
```

## URI Request Parameters
<a name="API_SetDefaultPermissionVersion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SetDefaultPermissionVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [permissionArn](#API_SetDefaultPermissionVersion_RequestSyntax) **   <a name="ram-SetDefaultPermissionVersion-request-permissionArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the customer managed permission whose default version you want to change.
Type: String
Required: Yes

 ** [permissionVersion](#API_SetDefaultPermissionVersion_RequestSyntax) **   <a name="ram-SetDefaultPermissionVersion-request-permissionVersion"></a>
Specifies the version number that you want to designate as the default for customer managed permission. To see a list of all available version numbers, use [ListPermissionVersions](API_ListPermissionVersions.md).
Type: Integer
Required: Yes

 ** [clientToken](#API_SetDefaultPermissionVersion_RequestSyntax) **   <a name="ram-SetDefaultPermissionVersion-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

## Response Syntax
<a name="API_SetDefaultPermissionVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "returnValue": boolean
}
```

## Response Elements
<a name="API_SetDefaultPermissionVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_SetDefaultPermissionVersion_ResponseSyntax) **   <a name="ram-SetDefaultPermissionVersion-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [returnValue](#API_SetDefaultPermissionVersion_ResponseSyntax) **   <a name="ram-SetDefaultPermissionVersion-response-returnValue"></a>
A boolean value that indicates whether the operation was successful.
Type: Boolean

## Errors
<a name="API_SetDefaultPermissionVersion_Errors"></a>

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
<a name="API_SetDefaultPermissionVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/SetDefaultPermissionVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/SetDefaultPermissionVersion)
