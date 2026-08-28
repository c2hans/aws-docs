---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStoreAlias.html
---

# GetPolicyStoreAlias
<a name="API_GetPolicyStoreAlias"></a>

Retrieves details about the specified policy store alias.

## Request Syntax
<a name="API_GetPolicyStoreAlias_RequestSyntax"></a>

```
{
   "aliasName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPolicyStoreAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [aliasName](#API_GetPolicyStoreAlias_RequestSyntax) **   <a name="verifiedpermissions-GetPolicyStoreAlias-request-aliasName"></a>
Specifies the name of the policy store alias that you want information about.
The alias name must always be prefixed with `policy-store-alias/`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

## Response Syntax
<a name="API_GetPolicyStoreAlias_ResponseSyntax"></a>

```
{
   "aliasArn": "string",
   "aliasName": "string",
   "createdAt": "string",
   "policyStoreId": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_GetPolicyStoreAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aliasArn](#API_GetPolicyStoreAlias_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStoreAlias-response-aliasArn"></a>
The Amazon Resource Name (ARN) of the policy store alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

 ** [aliasName](#API_GetPolicyStoreAlias_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStoreAlias-response-aliasName"></a>
The name of the policy store alias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [createdAt](#API_GetPolicyStoreAlias_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStoreAlias-response-createdAt"></a>
The date and time the policy store alias was created.
Type: Timestamp

 ** [policyStoreId](#API_GetPolicyStoreAlias_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStoreAlias-response-policyStoreId"></a>
The ID of the policy store associated with the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [state](#API_GetPolicyStoreAlias_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStoreAlias-response-state"></a>
The state of the policy store alias. Policy Store Aliases in the Active state can be used normally. When a policy store alias is deleted, it enters the PendingDeletion state. Policy Store Aliases in the PendingDeletion cannot be used, and creating a policy store alias with the same alias name will fail.
Type: String
Valid Values: `Active | PendingDeletion`

## Errors
<a name="API_GetPolicyStoreAlias_Errors"></a>

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
<a name="API_GetPolicyStoreAlias_Examples"></a>

### Example
<a name="API_GetPolicyStoreAlias_Example_1"></a>

The following example retrieves details about the policy store alias with the name `example-policy-store`.

#### Sample Request
<a name="API_GetPolicyStoreAlias_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.GetPolicyStoreAlias
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "aliasName": "policy-store-alias/example-policy-store"
}
```

#### Sample Response
<a name="API_GetPolicyStoreAlias_Example_1_Response"></a>

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
    "aliasName": "policy-store-alias/example-policy-store",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "aliasArn": "arn:aws:verifiedpermissions:us-east-1:123456789012:policy-store-alias/example-policy-store",
    "createdAt": "2024-01-15T12:30:00.000000+00:00",
    "state": "Active"
}
```

## See Also
<a name="API_GetPolicyStoreAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/GetPolicyStoreAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
