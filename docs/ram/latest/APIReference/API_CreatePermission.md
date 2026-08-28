---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_CreatePermission.html
---

# CreatePermission
<a name="API_CreatePermission"></a>

Creates a customer managed permission for a specified resource type that you can attach to resource shares. It is created in the AWS Region in which you call the operation.

## Request Syntax
<a name="API_CreatePermission_RequestSyntax"></a>

```
POST /createpermission HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "name": "{{string}}",
   "policyTemplate": "{{string}}",
   "resourceType": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreatePermission_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreatePermission_RequestSyntax) **   <a name="ram-CreatePermission-request-name"></a>
Specifies the name of the customer managed permission. The name must be unique within the AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[\w.-]*`
Required: Yes

 ** [policyTemplate](#API_CreatePermission_RequestSyntax) **   <a name="ram-CreatePermission-request-policyTemplate"></a>
A string in JSON format string that contains the following elements of a resource-based policy:
+  **Effect**: must be set to `ALLOW`.
+  **Action**: specifies the actions that are allowed by this customer managed permission. The list must contain only actions that are supported by the specified resource type. For a list of all actions supported by each resource type, see [Actions, resources, and condition keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) in the * AWS Identity and Access Management User Guide*.
+  **Condition**: (optional) specifies conditional parameters that must evaluate to true when a user attempts an action for that action to be allowed. For more information about the Condition element, see [IAM policies: Condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the * AWS Identity and Access Management User Guide*.
This template can't include either the `Resource` or `Principal` elements. Those are both filled in by AWS RAM when it instantiates the resource-based policy on each resource shared using this managed permission. The `Resource` comes from the ARN of the specific resource that you are sharing. The `Principal` comes from the list of identities added to the resource share.
Type: String
Required: Yes

 ** [resourceType](#API_CreatePermission_RequestSyntax) **   <a name="ram-CreatePermission-request-resourceType"></a>
Specifies the name of the resource type that this customer managed permission applies to.
The format is ` <service-code>:<resource-type> ` and is case sensitive. For example, to specify an Amazon EC2 Subnet, you can use the string `ec2:Subnet`. To see the list of valid values for this parameter, query the [ListResourceTypes](API_ListResourceTypes.md) operation. This value must match the display name of the resource (available in `ListResourceTypes`).
Type: String
Required: Yes

 ** [clientToken](#API_CreatePermission_RequestSyntax) **   <a name="ram-CreatePermission-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

 ** [tags](#API_CreatePermission_RequestSyntax) **   <a name="ram-CreatePermission-request-tags"></a>
Specifies a list of one or more tag key and value pairs to attach to the permission.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreatePermission_ResponseSyntax"></a>

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
<a name="API_CreatePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreatePermission_ResponseSyntax) **   <a name="ram-CreatePermission-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [permission](#API_CreatePermission_ResponseSyntax) **   <a name="ram-CreatePermission-response-permission"></a>
A structure with information about this customer managed permission.
Type: [ResourceSharePermissionSummary](API_ResourceSharePermissionSummary.md) object

## Errors
<a name="API_CreatePermission_Errors"></a>

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

 ** MalformedPolicyTemplateException **
The operation failed because the policy template that you provided isn't valid.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** PermissionAlreadyExistsException **
The operation failed because a permission with the specified name already exists in the requested AWS Region. Choose a different name.
HTTP Status Code: 409

 ** PermissionLimitExceededException **
The operation failed because it would exceed the maximum number of permissions you can create in each AWS Region. To view the limits for your AWS account, see the [AWS RAM page in the Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas).
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

## See Also
<a name="API_CreatePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/CreatePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/CreatePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/CreatePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/CreatePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/CreatePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/CreatePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/CreatePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/CreatePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/CreatePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/CreatePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
