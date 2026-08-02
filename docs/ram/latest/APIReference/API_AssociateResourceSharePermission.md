---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceSharePermission.html
---

# AssociateResourceSharePermission
<a name="API_AssociateResourceSharePermission"></a>

Adds or replaces the AWS RAM permission for a resource type included in a resource share. You can have exactly one permission associated with each resource type in the resource share. You can add a new AWS RAM permission only if there are currently no resources of that resource type currently in the resource share.

## Request Syntax
<a name="API_AssociateResourceSharePermission_RequestSyntax"></a>

```
POST /associateresourcesharepermission HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "permissionArn": "{{string}}",
   "permissionVersion": {{number}},
   "replace": {{boolean}},
   "resourceShareArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateResourceSharePermission_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateResourceSharePermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [permissionArn](#API_AssociateResourceSharePermission_RequestSyntax) **   <a name="ram-AssociateResourceSharePermission-request-permissionArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS RAM permission to associate with the resource share. To find the ARN for a permission, use either the [ListPermissions](API_ListPermissions.md) operation or go to the [Permissions library](https://console.aws.amazon.com/ram/home#Permissions:) page in the AWS RAM console and then choose the name of the permission. The ARN is displayed on the detail page.
Type: String
Required: Yes

 ** [resourceShareArn](#API_AssociateResourceSharePermission_RequestSyntax) **   <a name="ram-AssociateResourceSharePermission-request-resourceShareArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share to which you want to add or replace permissions.
Type: String
Required: Yes

 ** [clientToken](#API_AssociateResourceSharePermission_RequestSyntax) **   <a name="ram-AssociateResourceSharePermission-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

 ** [permissionVersion](#API_AssociateResourceSharePermission_RequestSyntax) **   <a name="ram-AssociateResourceSharePermission-request-permissionVersion"></a>
Specifies the version of the AWS RAM permission to associate with the resource share. You can specify *only* the version that is currently set as the default version for the permission. If you also set the `replace` pararameter to `true`, then this operation updates an outdated version of the permission to the current default version.
You don't need to specify this parameter because the default behavior is to use the version that is currently set as the default version for the permission. This parameter is supported for backwards compatibility.
Type: Integer
Required: No

 ** [replace](#API_AssociateResourceSharePermission_RequestSyntax) **   <a name="ram-AssociateResourceSharePermission-request-replace"></a>
Specifies whether the specified permission should replace the existing permission associated with the resource share. Use `true` to replace the current permissions. Use `false` to add the permission to a resource share that currently doesn't have a permission. The default value is `false`.
A resource share can have only one permission per resource type. If a resource share already has a permission for the specified resource type and you don't set `replace` to `true` then the operation returns an error. This helps prevent accidental overwriting of a permission.
Type: Boolean
Required: No

## Response Syntax
<a name="API_AssociateResourceSharePermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "returnValue": boolean
}
```

## Response Elements
<a name="API_AssociateResourceSharePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_AssociateResourceSharePermission_ResponseSyntax) **   <a name="ram-AssociateResourceSharePermission-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [returnValue](#API_AssociateResourceSharePermission_ResponseSyntax) **   <a name="ram-AssociateResourceSharePermission-response-returnValue"></a>
A return value of `true` indicates that the request succeeded. A value of `false` indicates that the request failed.
Type: Boolean

## Errors
<a name="API_AssociateResourceSharePermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## Examples
<a name="API_AssociateResourceSharePermission_Examples"></a>

**Note**
The examples show the JSON payloads of the request and response pretty printed with white spaces and line breaks for ease for ease of reading.

### Example
<a name="API_AssociateResourceSharePermission_Example_1"></a>

The following example command replaces the permission for the relevant resource type in the specified resource share. You don't need to specify the resource type, it is automatically inferred from the specified permission.

#### Sample Request
<a name="API_AssociateResourceSharePermission_Example_1_Request"></a>

```
            POST /associateresourcesharepermission HTTP/1.1
X-Amz-Date: 20210924T194101Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>>

{
    "resourceShareArn": "arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE",
    "permissionArn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueDatabaseReadWrite",
    "replace": true
}
```

#### Sample Response
<a name="API_AssociateResourceSharePermission_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Fri, 24 Sep 2021 19:41:02 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "returnValue":true
}
```

## See Also
<a name="API_AssociateResourceSharePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/AssociateResourceSharePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/AssociateResourceSharePermission)
