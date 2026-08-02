---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html
---

# GetPolicy
<a name="API_GetPolicy"></a>

Retrieves information about the specified policy.

## Request Syntax
<a name="API_GetPolicy_RequestSyntax"></a>

```
{
   "policyId": "{{string}}",
   "policyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyId](#API_GetPolicy_RequestSyntax) **   <a name="verifiedpermissions-GetPolicy-request-policyId"></a>
Specifies the ID of the policy you want information about.
You can use the policy name in place of the policy ID. When using a name, prefix it with `name/`. For example:
+ ID: `SPEXAMPLEabcdefg111111`
+ Name: `name/example-policy`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [policyStoreId](#API_GetPolicy_RequestSyntax) **   <a name="verifiedpermissions-GetPolicy-request-policyStoreId"></a>
Specifies the ID of the policy store that contains the policy that you want information about.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

## Response Syntax
<a name="API_GetPolicy_ResponseSyntax"></a>

```
{
   "actions": [
      {
         "actionId": "string",
         "actionType": "string"
      }
   ],
   "createdDate": "string",
   "definition": { ... },
   "effect": "string",
   "lastUpdatedDate": "string",
   "name": "string",
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
<a name="API_GetPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-createdDate"></a>
The date and time that the policy was originally created.
Type: Timestamp

 ** [definition](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-definition"></a>
The definition of the requested policy.
Type: [PolicyDefinitionDetail](API_PolicyDefinitionDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [lastUpdatedDate](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-lastUpdatedDate"></a>
The date and time that the policy was last updated.
Type: Timestamp

 ** [policyId](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-policyId"></a>
The unique ID of the policy that you want information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [policyStoreId](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-policyStoreId"></a>
The ID of the policy store that contains the policy that you want information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [policyType](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-policyType"></a>
The type of the policy.
Type: String
Valid Values: `STATIC | TEMPLATE_LINKED`

 ** [actions](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-actions"></a>
The action that a policy permits or forbids. For example, `{"actions": [{"actionId": "ViewPhoto", "actionType": "PhotoFlash::Action"}, {"entityID": "SharePhoto", "entityType": "PhotoFlash::Action"}]}`.
Type: Array of [ActionIdentifier](API_ActionIdentifier.md) objects

 ** [effect](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-effect"></a>
The effect of the decision that a policy returns to an authorization request. For example, `"effect": "Permit"`.
Type: String
Valid Values: `Permit | Forbid`

 ** [name](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-name"></a>
The name of the policy, if one was assigned when the policy was created or last updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [principal](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-principal"></a>
The principal specified in the policy's scope. This element isn't included in the response when `Principal` isn't present in the policy content.
Type: [EntityIdentifier](API_EntityIdentifier.md) object

 ** [resource](#API_GetPolicy_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicy-response-resource"></a>
The resource specified in the policy's scope. This element isn't included in the response when `Resource` isn't present in the policy content.
Type: [EntityIdentifier](API_EntityIdentifier.md) object

## Errors
<a name="API_GetPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
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
<a name="API_GetPolicy_Examples"></a>

### Example
<a name="API_GetPolicy_Example_1"></a>

The following example retrieves information about the specified policy contained in the specified policy store. In this example, the requested policy is a template-linked policy, so it returns the ID of the policy template, and the specific principal and resource used by this policy.

#### Sample Request
<a name="API_GetPolicy_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.GetPolicy
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
   "policyId": "SPEXAMPLEabcdefg111111",
   "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_GetPolicy_Example_1_Response"></a>

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
            "actionId": "SharePhoto",
            "actionType": "PhotoFlash::Action"
        }
    ],
    "createdDate":"2023-05-16T20:33:01.730817Z",
    "definition": {
        "static": {
            "description": "Grant everyone of janeFriends UserGroup permission to share photos in the vacationFolder Album",
            "statement": "permit(principal in PhotoFlash::UserGroup::\"janeFriends\", action in PhotoFlash::Action::\"SharePhoto\", resource in PhotoFlash::Album::\"vacationFolder\");"
        }
    },
    "effect": "Permit",
    "lastUpdatedDate":"2023-05-16T20:33:01.730817Z",
    "policyId":"SPEXAMPLEabcdefg111111",
    "policyStoreId":"PSEXAMPLEabcdefg111111",
    "policyType":"STATIC",
    "principal": {
        "entityId": "PhotoFlash::UserGroup",
        "entityType": "janeFriends"
    },
    "resource": {
        "entityId": "vacationFolder",
        "entityType": "PhotoFlash::Album"
    }
}
```

## See Also
<a name="API_GetPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/GetPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/GetPolicy)
