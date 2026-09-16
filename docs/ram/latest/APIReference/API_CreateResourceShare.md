---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html
---

# CreateResourceShare
<a name="API_CreateResourceShare"></a>

Creates a resource share. You can provide a list of the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for the resources that you want to share, a list of principals you want to share the resources with, the permissions to grant those principals, and optionally source constraints to enhance security for service principal sharing.

**Note**
Sharing a resource makes it available for use by principals outside of the AWS account that created the resource. Sharing doesn't change any permissions or quotas that apply to the resource in the account that created it.

## Request Syntax
<a name="API_CreateResourceShare_RequestSyntax"></a>

```
POST /createresourceshare HTTP/1.1
Content-type: application/json

{
   "allowExternalPrincipals": {{boolean}},
   "clientToken": "{{string}}",
   "name": "{{string}}",
   "permissionArns": [ "{{string}}" ],
   "principals": [ "{{string}}" ],
   "resourceArns": [ "{{string}}" ],
   "resourceShareConfiguration": {
      "retainSharingOnAccountLeaveOrganization": {{boolean}}
   },
   "sources": [ "{{string}}" ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateResourceShare_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateResourceShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-name"></a>
Specifies the name of the resource share.
Type: String
Required: Yes

 ** [allowExternalPrincipals](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-allowExternalPrincipals"></a>
Specifies whether principals outside your organization in AWS Organizations can be associated with a resource share. A value of `true` lets you share with individual AWS accounts that are *not* in your organization. A value of `false` only has meaning if your account is a member of an AWS Organization. The default value is `true`.
Type: Boolean
Required: No

 ** [clientToken](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

 ** [permissionArns](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-permissionArns"></a>
Specifies the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS RAM permission to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.
Type: Array of strings
Required: No

 ** [principals](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-principals"></a>
Specifies a list of one or more principals to associate with the resource share.
You can include the following values:
+ An AWS account ID, for example: `123456789012`
+ An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an organization in AWS Organizations, for example: `arn:aws:organizations::123456789012:organization/o-exampleorgid`
+ An ARN of an organizational unit (OU) in AWS Organizations, for example: `arn:aws:organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123`
+ An ARN of an IAM role, for example: `arn:aws:iam::123456789012:role/rolename`
+ An ARN of an IAM user, for example: `arn:aws:iam::123456789012user/username`
+ A service principal name, for example: `service-id.amazonaws.com`
Not all resource types can be shared with IAM roles and users. For more information, see [Sharing with IAM roles and users](https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types) in the * AWS Resource Access Manager User Guide*.
Type: Array of strings
Required: No

 ** [resourceArns](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-resourceArns"></a>
Specifies a list of one or more ARNs of the resources to associate with the resource share.
Type: Array of strings
Required: No

 ** [resourceShareConfiguration](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-resourceShareConfiguration"></a>
Specifies the configuration of this resource share.
Type: [ResourceShareConfiguration](API_ResourceShareConfiguration.md) object
Required: No

 ** [sources](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-sources"></a>
Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) that limit when service principals can access resources in this resource share. When a service principal attempts to access a shared resource, validation is performed to ensure the request originates from one of the specified sources. This helps prevent confused deputy attacks by applying constraints on where service principals can access resources from.
Type: Array of strings
Required: No

 ** [tags](#API_CreateResourceShare_RequestSyntax) **   <a name="ram-CreateResourceShare-request-tags"></a>
Specifies one or more tags to attach to the resource share itself. It doesn't attach the tags to the resources associated with the resource share.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateResourceShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "resourceShare": {
      "allowExternalPrincipals": boolean,
      "creationTime": number,
      "featureSet": "string",
      "lastUpdatedTime": number,
      "name": "string",
      "owningAccountId": "string",
      "resourceShareArn": "string",
      "resourceShareConfiguration": {
         "retainSharingOnAccountLeaveOrganization": boolean
      },
      "status": "string",
      "statusMessage": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateResourceShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateResourceShare_ResponseSyntax) **   <a name="ram-CreateResourceShare-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [resourceShare](#API_CreateResourceShare_ResponseSyntax) **   <a name="ram-CreateResourceShare-response-resourceShare"></a>
An object with information about the new resource share.
Type: [ResourceShare](API_ResourceShare.md) object

## Errors
<a name="API_CreateResourceShare_Errors"></a>

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

 ** InvalidStateTransitionException **
The operation failed because the requested operation isn't valid for the resource share in its current state.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** ResourceShareLimitExceededException **
The operation failed because it would exceed the limit for resource shares for your account. You can associate up to 100 resources per call. To view the limits for your AWS account, see the [AWS RAM page in the Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas).
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** TagLimitExceededException **
The operation failed because it would exceed the limit for tags for your AWS account.
HTTP Status Code: 400

 ** TagPolicyViolationException **
The operation failed because the specified tag key is a reserved word and can't be used.
HTTP Status Code: 400

 ** ThrottlingException **
The operation failed because it exceeded the rate at which you are allowed to perform this operation. Please try again later.
HTTP Status Code: 429

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

## See Also
<a name="API_CreateResourceShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/CreateResourceShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/CreateResourceShare)
