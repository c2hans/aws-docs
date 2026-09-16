---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ReplacePermissionAssociations.html
---

# ReplacePermissionAssociations
<a name="API_ReplacePermissionAssociations"></a>

Updates all resource shares that use a managed permission to a different managed permission. This operation always applies the default version of the target managed permission. You can optionally specify that the update applies to only resource shares that currently use a specified version. This enables you to update to the latest version, without changing the which managed permission is used.

You can use this operation to update all of your resource shares to use the current default version of the permission by specifying the same value for the `fromPermissionArn` and `toPermissionArn` parameters.

You can use the optional `fromPermissionVersion` parameter to update only those resources that use a specified version of the managed permission to the new managed permission.

**Important**
To successfully perform this operation, you must have permission to update the resource-based policy on all affected resource types.

## Request Syntax
<a name="API_ReplacePermissionAssociations_RequestSyntax"></a>

```
POST /replacepermissionassociations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "fromPermissionArn": "{{string}}",
   "fromPermissionVersion": {{number}},
   "toPermissionArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ReplacePermissionAssociations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ReplacePermissionAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fromPermissionArn](#API_ReplacePermissionAssociations_RequestSyntax) **   <a name="ram-ReplacePermissionAssociations-request-fromPermissionArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the managed permission that you want to replace.
Type: String
Required: Yes

 ** [toPermissionArn](#API_ReplacePermissionAssociations_RequestSyntax) **   <a name="ram-ReplacePermissionAssociations-request-toPermissionArn"></a>
Specifies the ARN of the managed permission that you want to associate with resource shares in place of the one specified by `fromPerssionArn` and `fromPermissionVersion`.
The operation always associates the version that is currently the default for the specified managed permission.
Type: String
Required: Yes

 ** [clientToken](#API_ReplacePermissionAssociations_RequestSyntax) **   <a name="ram-ReplacePermissionAssociations-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

 ** [fromPermissionVersion](#API_ReplacePermissionAssociations_RequestSyntax) **   <a name="ram-ReplacePermissionAssociations-request-fromPermissionVersion"></a>
Specifies that you want to updated the permissions for only those resource shares that use the specified version of the managed permission.
Type: Integer
Required: No

## Response Syntax
<a name="API_ReplacePermissionAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "replacePermissionAssociationsWork": {
      "creationTime": number,
      "fromPermissionArn": "string",
      "fromPermissionVersion": "string",
      "id": "string",
      "lastUpdatedTime": number,
      "status": "string",
      "statusMessage": "string",
      "toPermissionArn": "string",
      "toPermissionVersion": "string"
   }
}
```

## Response Elements
<a name="API_ReplacePermissionAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_ReplacePermissionAssociations_ResponseSyntax) **   <a name="ram-ReplacePermissionAssociations-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [replacePermissionAssociationsWork](#API_ReplacePermissionAssociations_ResponseSyntax) **   <a name="ram-ReplacePermissionAssociations-response-replacePermissionAssociationsWork"></a>
Specifies a data structure that you can use to track the asynchronous tasks that AWS RAM performs to complete this operation. You can use the [ListReplacePermissionAssociationsWork](API_ListReplacePermissionAssociationsWork.md) operation and pass the `id` value returned in this structure.
Type: [ReplacePermissionAssociationsWork](API_ReplacePermissionAssociationsWork.md) object

## Errors
<a name="API_ReplacePermissionAssociations_Errors"></a>

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
<a name="API_ReplacePermissionAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/ReplacePermissionAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ReplacePermissionAssociations)
