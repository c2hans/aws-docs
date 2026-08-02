---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html
---

# UpdatePolicy
<a name="API_UpdatePolicy"></a>

Modifies a Cedar static policy in the specified policy store. You can change only certain elements of the [UpdatePolicyDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyInput.html#amazonverifiedpermissions-UpdatePolicy-request-UpdatePolicyDefinition) parameter. You can directly update only static policies. To change a template-linked policy, you must update the template instead, using [UpdatePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html).

**Note**
If policy validation is enabled in the policy store, then updating a static policy causes Verified Permissions to validate the policy against the schema in the policy store. If the updated static policy doesn't pass validation, the operation fails and the update isn't stored.
When you edit a static policy, you can change only certain elements of a static policy:
The action referenced by the policy.
A condition clause, such as when and unless.
You can't change these elements of a static policy:
Changing a policy from a static policy to a template-linked policy.
Changing the effect of a static policy from permit or forbid.
The principal referenced by a static policy.
The resource referenced by a static policy.
To update a template-linked policy, you must update the template instead.

**Note**
Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) *. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

## Request Syntax
<a name="API_UpdatePolicy_RequestSyntax"></a>

```
{
   "definition": { ... },
   "name": "{{string}}",
   "policyId": "{{string}}",
   "policyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyId](#API_UpdatePolicy_RequestSyntax) **   <a name="verifiedpermissions-UpdatePolicy-request-policyId"></a>
Specifies the ID of the policy that you want to update. To find this value, you can use [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html).
You can use the policy name in place of the policy ID. When using a name, prefix it with `name/`. For example:
+ ID: `SPEXAMPLEabcdefg111111`
+ Name: `name/example-policy`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [policyStoreId](#API_UpdatePolicy_RequestSyntax) **   <a name="verifiedpermissions-UpdatePolicy-request-policyStoreId"></a>
Specifies the ID of the policy store that contains the policy that you want to update.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [definition](#API_UpdatePolicy_RequestSyntax) **   <a name="verifiedpermissions-UpdatePolicy-request-definition"></a>
Specifies the updated policy content that you want to replace on the specified policy. The content must be valid Cedar policy language text.
If you don't specify this parameter, the existing policy definition remains unchanged.
You can change only the following elements from the policy definition:
+ The `action` referenced by the policy.
+ Any conditional clauses, such as `when` or `unless` clauses.
You **can't** change the following elements:
+ Changing from `static` to `templateLinked`.
+ Changing the effect of the policy from `permit` or `forbid`.
+ The `principal` referenced by the policy.
+ The `resource` referenced by the policy.
Type: [UpdatePolicyDefinition](API_UpdatePolicyDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [name](#API_UpdatePolicy_RequestSyntax) **   <a name="verifiedpermissions-UpdatePolicy-request-name"></a>
Specifies a name for the policy that is unique among all policies within the policy store. You can use the name in place of the policy ID in API operations that reference the policy. The name must be prefixed with `name/`.
If you don't include the name in an update request, the existing name is unchanged. To remove a name, set it to an empty string (`""`).
If you specify a name that is already associated with another policy in the policy store, you receive a `ConflictException` error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`
Required: No

## Response Syntax
<a name="API_UpdatePolicy_ResponseSyntax"></a>

```
{
   "actions": [
      {
         "actionId": "string",
         "actionType": "string"
      }
   ],
   "createdDate": "string",
   "effect": "string",
   "lastUpdatedDate": "string",
   "policyId": "string",
   "policyStoreId": "string",
   "policyType": "string",
   "principal": {
      "entityId": "string",
      "entityType": "string"
   },
   "resource": {
      "entityId": "string",
      "entityType": "string"
   }
}
```

## Response Elements
<a name="API_UpdatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-createdDate"></a>
The date and time that the policy was originally created.
Type: Timestamp

 ** [lastUpdatedDate](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-lastUpdatedDate"></a>
The date and time that the policy was most recently updated.
Type: Timestamp

 ** [policyId](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-policyId"></a>
The ID of the policy that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [policyStoreId](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-policyStoreId"></a>
The ID of the policy store that contains the policy that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [policyType](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-policyType"></a>
The type of the policy that was updated.
Type: String
Valid Values: `STATIC | TEMPLATE_LINKED`

 ** [actions](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-actions"></a>
The action that a policy permits or forbids. For example, `{"actions": [{"actionId": "ViewPhoto", "actionType": "PhotoFlash::Action"}, {"entityID": "SharePhoto", "entityType": "PhotoFlash::Action"}]}`.
Type: Array of [ActionIdentifier](API_ActionIdentifier.md) objects

 ** [effect](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-effect"></a>
The effect of the decision that a policy returns to an authorization request. For example, `"effect": "Permit"`.
Type: String
Valid Values: `Permit | Forbid`

 ** [principal](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-principal"></a>
The principal specified in the policy's scope. This element isn't included in the response when `Principal` isn't present in the policy content.
Type: [EntityIdentifier](API_EntityIdentifier.md) object

 ** [resource](#API_UpdatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-UpdatePolicy-response-resource"></a>
The resource specified in the policy's scope. This element isn't included in the response when `Resource` isn't present in the policy content.
Type: [EntityIdentifier](API_EntityIdentifier.md) object

## Errors
<a name="API_UpdatePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request failed because another request to modify a resource occurred at the same time.
 ** resources **
The list of resources referenced with this failed request.
HTTP Status Code: 400

 ** InternalServerException **
The request failed because of an internal error. Try your request again later
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request failed because it references a resource that doesn't exist.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request failed because it would cause a service quota to be exceeded.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request failed because it exceeded a throttling quota.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 400

 ** ValidationException **
The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.
The possible reasons include the following:
+  **UnrecognizedEntityType**

  The policy includes an entity type that isn't found in the schema.
+  **UnrecognizedActionId**

  The policy includes an action id that isn't found in the schema.
+  **InvalidActionApplication**

  The policy includes an action that, according to the schema, doesn't support the specified principal and resource.
+  **UnexpectedType**

  The policy included an operand that isn't a valid type for the specified operation.
+  **IncompatibleTypes**

  The types of elements included in a `set`, or the types of expressions used in an `if...then...else` clause aren't compatible in this context.
+  **MissingAttribute**

  The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the [has (presence of attribute test) operator](https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test) in the *Cedar Policy Language Guide*.
+  **UnsafeOptionalAttributeAccess**

  The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the [has (presence of attribute test) operator](https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test) in the *Cedar Policy Language Guide*.
+  **ImpossiblePolicy**

  Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.
+  **WrongNumberArguments**

  The policy references an extension type with the wrong number of arguments.
+  **FunctionArgumentValidationError**

  Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.
 ** fieldList **
The list of fields that aren't valid.
HTTP Status Code: 400

## Examples
<a name="API_UpdatePolicy_Examples"></a>

### Example
<a name="API_UpdatePolicy_Example_1"></a>

The following example replaces the definition of the specified static policy with a new one.

#### Sample Request
<a name="API_UpdatePolicy_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.UpdatePolicy
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "policyId": "SPEXAMPLEabcdefg111111",
    "definition": {
        "static": {
            "statement": "permit(principal, action in PhotoFlash::Action::\"ViewPhoto\", resource in PhotoFlash::Album::\"public_folder\");"
        }
    }
}
```

#### Sample Response
<a name="API_UpdatePolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
vary: origin
vary: access-control-request-method
vary: access-control-request-headers
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{

    "actions": [
        {
            "actionId": "ViewPhoto",
            "actionType": "PhotoFlash::Action"
        }
    ],
    "createdDate": "20230613T22:56:48.020321Z",
    "effect": "Permit",
    "lastUpdatedDate": "20230613T23:26:09.764859Z",
    "policyId": "SPEXAMPLEabcdefg111111",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "policyType": "STATIC",
    "resource": {
        "entityType": "PhotoFlash::Album",
        "entityId": "public_folder"
    }
}
```

## See Also
<a name="API_UpdatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/UpdatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/UpdatePolicy)
