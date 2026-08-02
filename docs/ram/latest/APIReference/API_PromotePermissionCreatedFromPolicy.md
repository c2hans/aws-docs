---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_PromotePermissionCreatedFromPolicy.html
---

# PromotePermissionCreatedFromPolicy
<a name="API_PromotePermissionCreatedFromPolicy"></a>

When you attach a resource-based policy to a resource, AWS RAM automatically creates a resource share of `featureSet`=`CREATED_FROM_POLICY` with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share can't be modified by using AWS RAM.

This operation creates a separate, fully manageable customer managed permission that has the same IAM permissions as the original resource-based policy. You can associate this customer managed permission to any resource shares.

Before you use [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md), you should first run this operation to ensure that you have an appropriate customer managed permission that can be associated with the promoted resource share.

**Note**
The original `CREATED_FROM_POLICY` policy isn't deleted, and resource shares using that original policy aren't automatically updated.
You can't modify a `CREATED_FROM_POLICY` resource share so you can't associate the new customer managed permission by using `ReplacePermsissionAssociations`. However, if you use [PromoteResourceShareCreatedFromPolicy](API_PromoteResourceShareCreatedFromPolicy.md), that operation automatically associates the fully manageable customer managed permission to the newly promoted `STANDARD` resource share.
After you promote a resource share, if the original `CREATED_FROM_POLICY` managed permission has no other associations to A resource share, then AWS RAM automatically deletes it.

## Request Syntax
<a name="API_PromotePermissionCreatedFromPolicy_RequestSyntax"></a>

```
POST /promotepermissioncreatedfrompolicy HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "name": "{{string}}",
   "permissionArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PromotePermissionCreatedFromPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PromotePermissionCreatedFromPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_PromotePermissionCreatedFromPolicy_RequestSyntax) **   <a name="ram-PromotePermissionCreatedFromPolicy-request-name"></a>
Specifies a name for the promoted customer managed permission.
Type: String
Required: Yes

 ** [permissionArn](#API_PromotePermissionCreatedFromPolicy_RequestSyntax) **   <a name="ram-PromotePermissionCreatedFromPolicy-request-permissionArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the `CREATED_FROM_POLICY` permission that you want to promote. You can get this [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) by calling the [ListResourceSharePermissions](API_ListResourceSharePermissions.md) operation.
Type: String
Required: Yes

 ** [clientToken](#API_PromotePermissionCreatedFromPolicy_RequestSyntax) **   <a name="ram-PromotePermissionCreatedFromPolicy-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

## Response Syntax
<a name="API_PromotePermissionCreatedFromPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "permission": {
      "arn": "string",
      "creationTime": number,
      "defaultVersion": boolean,
      "featureSet": "string",
      "isResourceTypeDefault": boolean,
      "lastUpdatedTime": number,
      "name": "string",
      "permissionType": "string",
      "resourceType": "string",
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "version": "string"
   }
}
```

## Response Elements
<a name="API_PromotePermissionCreatedFromPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_PromotePermissionCreatedFromPolicy_ResponseSyntax) **   <a name="ram-PromotePermissionCreatedFromPolicy-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [permission](#API_PromotePermissionCreatedFromPolicy_ResponseSyntax) **   <a name="ram-PromotePermissionCreatedFromPolicy-response-permission"></a>
Information about an AWS RAM permission.
Type: [ResourceSharePermissionSummary](API_ResourceSharePermissionSummary.md) object

## Errors
<a name="API_PromotePermissionCreatedFromPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** InvalidPolicyException **
The operation failed because a policy you specified isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** MissingRequiredParameterException **
The operation failed because a required input parameter is missing.
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
<a name="API_PromotePermissionCreatedFromPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/PromotePermissionCreatedFromPolicy)
