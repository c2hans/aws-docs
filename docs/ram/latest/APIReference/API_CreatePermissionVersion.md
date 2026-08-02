---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_CreatePermissionVersion.html
---

# CreatePermissionVersion
<a name="API_CreatePermissionVersion"></a>

Creates a new version of the specified customer managed permission. The new version is automatically set as the default version of the customer managed permission. New resource shares automatically use the default permission. Existing resource shares continue to use their original permission versions, but you can use [ReplacePermissionAssociations](API_ReplacePermissionAssociations.md) to update them.

If the specified customer managed permission already has the maximum of 5 versions, then you must delete one of the existing versions before you can create a new one.

## Request Syntax
<a name="API_CreatePermissionVersion_RequestSyntax"></a>

```
POST /createpermissionversion HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "permissionArn": "{{string}}",
   "policyTemplate": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePermissionVersion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePermissionVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [permissionArn](#API_CreatePermissionVersion_RequestSyntax) **   <a name="ram-CreatePermissionVersion-request-permissionArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the customer managed permission you're creating a new version for.
Type: String
Required: Yes

 ** [policyTemplate](#API_CreatePermissionVersion_RequestSyntax) **   <a name="ram-CreatePermissionVersion-request-policyTemplate"></a>
A string in JSON format string that contains the following elements of a resource-based policy:
+  **Effect**: must be set to `ALLOW`.
+  **Action**: specifies the actions that are allowed by this customer managed permission. The list must contain only actions that are supported by the specified resource type. For a list of all actions supported by each resource type, see [Actions, resources, and condition keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) in the * AWS Identity and Access Management User Guide*.
+  **Condition**: (optional) specifies conditional parameters that must evaluate to true when a user attempts an action for that action to be allowed. For more information about the Condition element, see [IAM policies: Condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the * AWS Identity and Access Management User Guide*.
This template can't include either the `Resource` or `Principal` elements. Those are both filled in by AWS RAM when it instantiates the resource-based policy on each resource shared using this managed permission. The `Resource` comes from the ARN of the specific resource that you are sharing. The `Principal` comes from the list of identities added to the resource share.
Type: String
Required: Yes

 ** [clientToken](#API_CreatePermissionVersion_RequestSyntax) **   <a name="ram-CreatePermissionVersion-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

## Response Syntax
<a name="API_CreatePermissionVersion_ResponseSyntax"></a>

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
      "permission": "string",
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
<a name="API_CreatePermissionVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreatePermissionVersion_ResponseSyntax) **   <a name="ram-CreatePermissionVersion-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [permission](#API_CreatePermissionVersion_ResponseSyntax) **   <a name="ram-CreatePermissionVersion-response-permission"></a>
Information about a AWS RAM managed permission.
Type: [ResourceSharePermissionDetail](API_ResourceSharePermissionDetail.md) object

## Errors
<a name="API_CreatePermissionVersion_Errors"></a>

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

 ** InvalidPolicyException **
The operation failed because a policy you specified isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** MalformedPolicyTemplateException **
The operation failed because the policy template that you provided isn't valid.
HTTP Status Code: 400

 ** PermissionVersionsLimitExceededException **
The operation failed because it would exceed the limit for the number of versions you can have for a permission. To view the limits for your AWS account, see the [AWS RAM page in the Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas).
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
<a name="API_CreatePermissionVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/CreatePermissionVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/CreatePermissionVersion)
