---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html
---

# IsAuthorizedWithToken
<a name="API_IsAuthorizedWithToken"></a>

Makes an authorization decision about a service request described in the parameters. The principal in this request comes from an external identity source in the form of an identity token formatted as a [JSON web token (JWT)](https://wikipedia.org/wiki/JSON_Web_Token). The information in the parameters can also define additional context that Verified Permissions can include in the evaluation. The request is evaluated against all matching policies in the specified policy store. The result of the decision is either `Allow` or `Deny`, along with a list of the policies that resulted in the decision.

Verified Permissions validates each token that is specified in a request by checking its expiration date and its signature.

**Important**
Tokens from an identity source user continue to be usable until they expire. Token revocation and resource deletion have no effect on the validity of a token in your policy store

## Request Syntax
<a name="API_IsAuthorizedWithToken_RequestSyntax"></a>

```
{
   "accessToken": "{{string}}",
   "action": {
      "actionId": "{{string}}",
      "actionType": "{{string}}"
   },
   "context": { ... },
   "entities": { ... },
   "identityToken": "{{string}}",
   "policyStoreId": "{{string}}",
   "resource": {
      "entityId": "{{string}}",
      "entityType": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_IsAuthorizedWithToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_IsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-request-policyStoreId"></a>
Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [accessToken](#API_IsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-request-accessToken"></a>
Specifies an access token for the principal to be authorized. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an `accessToken`, an `identityToken`, or both.
Must be an access token. Verified Permissions returns an error if the `token_use` claim in the submitted token isn't `access`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`
Required: No

 ** [action](#API_IsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-request-action"></a>
Specifies the requested action to be authorized. Is the specified principal authorized to perform this action on the specified resource.
Type: [ActionIdentifier](API_ActionIdentifier.md) object
Required: No

 ** [context](#API_IsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-request-context"></a>
Specifies additional context that can be used to make more granular authorization decisions.
Type: [ContextDefinition](API_ContextDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [entities](#API_IsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-request-entities"></a>
(Optional) Specifies the list of resources and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.
You can't include principals in this parameter, only resource and action entities. This parameter can't include any entities of a type that matches the user or group entity types that you defined in your identity source.
+ The `IsAuthorizedWithToken` operation takes principal attributes from ** *only* ** the `identityToken` or `accessToken` passed to the operation.
+ For action entities, you can include only their `Identifier` and `EntityType`.
Type: [EntitiesDefinition](API_EntitiesDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [identityToken](#API_IsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-request-identityToken"></a>
Specifies an identity token for the principal to be authorized. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an `accessToken`, an `identityToken`, or both.
Must be an ID token. Verified Permissions returns an error if the `token_use` claim in the submitted token isn't `id`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`
Required: No

 ** [resource](#API_IsAuthorizedWithToken_RequestSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-request-resource"></a>
Specifies the resource for which the authorization decision is made. For example, is the principal allowed to perform the action on the resource?
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

## Response Syntax
<a name="API_IsAuthorizedWithToken_ResponseSyntax"></a>

```
{
   "decision": "string",
   "determiningPolicies": [
      {
         "policyId": "string"
      }
   ],
   "errors": [
      {
         "errorDescription": "string"
      }
   ],
   "principal": {
      "entityId": "string",
      "entityType": "string"
   }
}
```

## Response Elements
<a name="API_IsAuthorizedWithToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [decision](#API_IsAuthorizedWithToken_ResponseSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-response-decision"></a>
An authorization decision that indicates if the authorization request should be allowed or denied.
Type: String
Valid Values: `ALLOW | DENY`

 ** [determiningPolicies](#API_IsAuthorizedWithToken_ResponseSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-response-determiningPolicies"></a>
The list of determining policies used to make the authorization decision. For example, if there are multiple matching policies, where at least one is a forbid policy, then because forbid always overrides permit the forbid policies are the determining policies. If all matching policies are permit policies, then those policies are the determining policies. When no policies match and the response is the default DENY, there are no determining policies.
Type: Array of [DeterminingPolicyItem](API_DeterminingPolicyItem.md) objects

 ** [errors](#API_IsAuthorizedWithToken_ResponseSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-response-errors"></a>
Errors that occurred while making an authorization decision. For example, a policy references an entity or entity attribute that does not exist in the slice.
Type: Array of [EvaluationErrorItem](API_EvaluationErrorItem.md) objects

 ** [principal](#API_IsAuthorizedWithToken_ResponseSyntax) **   <a name="verifiedpermissions-IsAuthorizedWithToken-response-principal"></a>
The identifier of the principal in the ID or access token.
Type: [EntityIdentifier](API_EntityIdentifier.md) object

## Errors
<a name="API_IsAuthorizedWithToken_Errors"></a>

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
<a name="API_IsAuthorizedWithToken_Examples"></a>

### Example
<a name="API_IsAuthorizedWithToken_Example_1"></a>

The following example requests an authorization decision for a user who was authenticated by Amazon Cognito. The request uses the identity token provided by Amazon Cognito instead of the access token. In this example, the specified information store is configured to return principals as entities of type `CognitoUser`. The policy store contains a policy with the following statement.

```
permit(
    principal == CognitoUser::"us-east-1_1a2b3c4d5|a1b2c3d4e5f6g7h8i9j0kalbmc",
    action,
    resource == PhotoFlash::Photo::"VacationPhoto94.jpg"
);
```

#### Sample Request
<a name="API_IsAuthorizedWithToken_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.IsAuthorizedWithToken
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "action": {
        "actionId": "View",
        "actionType": "Action"
    },
    "resource": {
        "entityId": "vacationPhoto94.jpg",
        "entityType": "PhotoFlash::Photo"
    }
    "identityToken": "AbCdE12345...long.string...54321EdCbA",
}
```

#### Sample Response
<a name="API_IsAuthorizedWithToken_Example_1_Response"></a>

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
    "decision":"Allow",
    "determiningPolicies":[
        {
        "determiningPolicyId":"SPEXAMPLEabcdefg111111"
        }
    ],
    "errors":[]
}
```

## See Also
<a name="API_IsAuthorizedWithToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/IsAuthorizedWithToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
