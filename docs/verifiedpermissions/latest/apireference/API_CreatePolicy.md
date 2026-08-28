---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html
---

# CreatePolicy
<a name="API_CreatePolicy"></a>

Creates a Cedar policy and saves it in the specified policy store. You can create either a static policy or a policy linked to a policy template.
+ To create a static policy, provide the Cedar policy text in the `StaticPolicy` section of the `PolicyDefinition`.
+ To create a policy that is dynamically linked to a policy template, specify the policy template ID and the principal and resource to associate with this policy in the `templateLinked` section of the `PolicyDefinition`. If the policy template is ever updated, any policies linked to the policy template automatically use the updated template.

**Note**
Creating a policy causes it to be validated against the schema in the policy store. If the policy doesn't pass validation, the operation fails and the policy isn't stored.

**Note**
Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) *. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

## Request Syntax
<a name="API_CreatePolicy_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "definition": { ... },
   "name": "{{string}}",
   "policyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [definition](#API_CreatePolicy_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicy-request-definition"></a>
A structure that specifies the policy type and content to use for the new policy. You must include either a static or a templateLinked element. The policy content must be written in the Cedar policy language.
Type: [PolicyDefinition](API_PolicyDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [policyStoreId](#API_CreatePolicy_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicy-request-policyStoreId"></a>
Specifies the `PolicyStoreId` of the policy store you want to store the policy in.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [clientToken](#API_CreatePolicy_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicy-request-clientToken"></a>
Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `ConflictException` error.
Verified Permissions recognizes a `ClientToken` for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of `ClientToken`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** [name](#API_CreatePolicy_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicy-request-name"></a>
Specifies a name for the policy that is unique among all policies within the policy store. You can use the name in place of the policy ID in API operations that reference the policy. The name must be prefixed with `name/`.
If you specify a name that is already associated with another policy in the policy store, you receive a `ConflictException` error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`
Required: No

## Response Syntax
<a name="API_CreatePolicy_ResponseSyntax"></a>

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
<a name="API_CreatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-createdDate"></a>
The date and time the policy was originally created.
Type: Timestamp

 ** [lastUpdatedDate](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-lastUpdatedDate"></a>
The date and time the policy was last updated.
Type: Timestamp

 ** [policyId](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-policyId"></a>
The unique ID of the new policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [policyStoreId](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-policyStoreId"></a>
The ID of the policy store that contains the new policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [policyType](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-policyType"></a>
The policy type of the new policy.
Type: String
Valid Values: `STATIC | TEMPLATE_LINKED`

 ** [actions](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-actions"></a>
The action that a policy permits or forbids. For example, `{"actions": [{"actionId": "ViewPhoto", "actionType": "PhotoFlash::Action"}, {"entityID": "SharePhoto", "entityType": "PhotoFlash::Action"}]}`.
Type: Array of [ActionIdentifier](API_ActionIdentifier.md) objects

 ** [effect](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-effect"></a>
The effect of the decision that a policy returns to an authorization request. For example, `"effect": "Permit"`.
Type: String
Valid Values: `Permit | Forbid`

 ** [principal](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-principal"></a>
The principal specified in the new policy's scope. This response element isn't present when `principal` isn't specified in the policy content.
Type: [EntityIdentifier](API_EntityIdentifier.md) object

 ** [resource](#API_CreatePolicy_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicy-response-resource"></a>
The resource specified in the new policy's scope. This response element isn't present when the `resource` isn't specified in the policy content.
Type: [EntityIdentifier](API_EntityIdentifier.md) object

## Errors
<a name="API_CreatePolicy_Errors"></a>

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
<a name="API_CreatePolicy_Examples"></a>

### Example 1
<a name="API_CreatePolicy_Example_1"></a>

The following example request creates a static policy with a policy scope that specifies both a principal and a resource. The response includes both the `Principal` and `Resource` elements because both were specified in the request policy scope.

**Note**
The JSON in the parameters of this operation are strings that can contain embedded quotation marks (`"`) within the outermost quotation mark pair. When you are calling the API directly, using a tool like the AWS CLI or Postman, you have to *stringify* the JSON object by preceding all embedded quotation marks with a backslash character ( `\"` ) and combining all lines into a single text line with no line breaks.
Example strings are displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

#### Sample Request
<a name="API_CreatePolicy_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.CreatePolicy
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "definition": {
        "static": {
            "description":  "Grant members of janeFriends UserGroup view and share access to the vacationFolder Album",
            "statement": "permit( principal in PhotoFlash::UserGroup::\"janeFriends\", action in [PhotoFlash::Action::\"ViewPhoto\", PhotoFlash::Action::\"SharePhoto\"], resource in PhotoFlash::Album::\"vacationFolder\" );"
        }
    },
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"
}
```

#### Sample Response
<a name="API_CreatePolicy_Example_1_Response"></a>

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
        },
        {
            "actionId": "SharePhoto",
            "actionType": "PhotoFlash::Action"
        }
    ],
    "createdDate":"2023-05-16T20:33:01.730817Z",
    "effect": "Permit",
    "lastUpdatedDate":"2023-05-16T20:33:01.730817Z",
    "policyId":"SPEXAMPLEabcdefg111111",
    "policyStoreId":"PSEXAMPLEabcdefg111111",
    "policyType": "STATIC",
    "principal": {
        "entityId": "janeFriends",
        "entityType": "PhotoFlash::UserGroup"
    },
    "resource": {
        "entityId": "vacationFolder",
        "entityType": "PhotoFlash::Album"
    }
}
```

### Example 2
<a name="API_CreatePolicy_Example_2"></a>

The following example creates a static policy with a policy scope that identifies a specific resource but does not specify a principal. Therefore, the response does not include a `Principal` element.

**Note**
The JSON in the parameters of this operation are strings that can contain embedded quotation marks (`"`) within the outermost quotation mark pair. When you are calling the API directly, using a tool like the AWS CLI or Postman, you have to *stringify* the JSON object by preceding all embedded quotation marks with a backslash character ( `\"` ) and combining all lines into a single text line with no line breaks.
Example strings are displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

#### Sample Request
<a name="API_CreatePolicy_Example_2_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.CreatePolicy
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "definition": {
        "static": {
            "description": "Grant everyone full access to the publicFolder Album",
            "statement": "permit(principal, action, resource in PhotoFlash::Album::\"publicFolder\");"
        }
    },
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"
}
```

#### Sample Response
<a name="API_CreatePolicy_Example_2_Response"></a>

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
    "createdDate": "2023-05-16T21:19:44.528576+00:00",
    "effect": "Permit",
    "lastUpdatedDate": "2023-05-16T21:19:44.528576+00:00",
    "policyId": "SPEXAMPLEabcdefg222222",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "policyType": "STATIC",
    "resource": {
        "entityId": "publicFolder",
        "entityType": "PhotoFlash::Album"
    }
}
```

### Example 3
<a name="API_CreatePolicy_Example_3"></a>

The following example creates a template-linked policy using the following policy template and associates the specified principal to use with the new template-linked policy.

```
permit (
    principal in ?principal,
    action == PhotoFlash::Action::"ViewPhoto",
    resource == PhotoFlash::Photo::"VacationPhoto94.jpg"
);
```

#### Sample Request
<a name="API_CreatePolicy_Example_3_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.CreatePolicy
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "definition": {
        "templateLinked": {
            "policyTemplateId": "PTEXAMPLEabcdefg111111",
            "principal": {
                "entityType": "PhotoFlash::User",
                "entityId": "alice"
            }
        }
    },
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"
}
```

#### Sample Response
<a name="API_CreatePolicy_Example_3_Response"></a>

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
            "actionId": "FullPhotoAccess",
            "actionType": "PhotoFlash::Action"
        }
    ],
    "createdDate":"2023-05-22T18:57:53.298278Z",
    "effect": "Permit",
    "lastUpdatedDate":"2023-05-22T18:57:53.298278Z",
    "policyId": "TPEXAMPLEabcdefg111111",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "policyType": "TEMPLATE_LINKED",
    "principal": {
        "entityType": "PhotoFlash::User",
        "entityId": "alice"
    },
    "resource": {
        "entityType": "PhotoFlash::Photo",
        "entityId": "VacationPhoto94.jpg"
    }
}
```

## See Also
<a name="API_CreatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/CreatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CreatePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
