---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyTemplate.html
---

# CreatePolicyTemplate
<a name="API_CreatePolicyTemplate"></a>

Creates a policy template. A template can use placeholders for the principal and resource. A template must be instantiated into a policy by associating it with specific principals and resources to use for the placeholders. That instantiated policy can then be considered in authorization decisions. The instantiated policy works identically to any other policy, except that it is dynamically linked to the template. If the template changes, then any policies that are linked to that template are immediately updated as well.

**Note**
Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) *. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

## Request Syntax
<a name="API_CreatePolicyTemplate_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "policyStoreId": "{{string}}",
   "statement": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePolicyTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_CreatePolicyTemplate_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-request-policyStoreId"></a>
The ID of the policy store in which to create the policy template.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [statement](#API_CreatePolicyTemplate_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-request-statement"></a>
Specifies the content that you want to use for the new policy template, written in the Cedar policy language.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [clientToken](#API_CreatePolicyTemplate_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-request-clientToken"></a>
Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `ConflictException` error.
Verified Permissions recognizes a `ClientToken` for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of `ClientToken`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** [description](#API_CreatePolicyTemplate_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-request-description"></a>
Specifies a description for the policy template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

 ** [name](#API_CreatePolicyTemplate_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-request-name"></a>
Specifies a name for the policy template that is unique among all policy templates within the policy store. You can use the name in place of the policy template ID in API operations that reference the policy template. The name must be prefixed with `name/`.
If you specify a name that is already associated with another policy template in the policy store, you receive a `ConflictException` error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`
Required: No

## Response Syntax
<a name="API_CreatePolicyTemplate_ResponseSyntax"></a>

```
{
   "createdDate": "string",
   "lastUpdatedDate": "string",
   "policyStoreId": "string",
   "policyTemplateId": "string"
}
```

## Response Elements
<a name="API_CreatePolicyTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdDate](#API_CreatePolicyTemplate_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-response-createdDate"></a>
The date and time the policy template was originally created.
Type: Timestamp

 ** [lastUpdatedDate](#API_CreatePolicyTemplate_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-response-lastUpdatedDate"></a>
The date and time the policy template was most recently updated.
Type: Timestamp

 ** [policyStoreId](#API_CreatePolicyTemplate_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-response-policyStoreId"></a>
The ID of the policy store that contains the policy template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [policyTemplateId](#API_CreatePolicyTemplate_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicyTemplate-response-policyTemplateId"></a>
The unique ID of the new policy template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

## Errors
<a name="API_CreatePolicyTemplate_Errors"></a>

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
<a name="API_CreatePolicyTemplate_Examples"></a>

### Example
<a name="API_CreatePolicyTemplate_Example_1"></a>

The following example creates a policy template that has a placeholder for the principal.

**Note**
The JSON in the parameters of this operation are strings that can contain embedded quotation marks (`"`) within the outermost quotation mark pair. When you are calling the API directly, using a tool like the AWS CLI or Postman, you have to *stringify* the JSON object by preceding all embedded quotation marks with a backslash character ( `\"` ) and combining all lines into a single text line with no line breaks.
Example strings are displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings.

#### Sample Request
<a name="API_CreatePolicyTemplate_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.CreatePolicyTemplate
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "description": "Template for research dept",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "statement": "\"AccessVacation\"\npermit(\n    principal in ?principal,\n    action == Action::\"view\",\n    resource == Photo::\"VacationPhoto94.jpg\"\n)\nwhen {\n    principal has department && principal.department == \"research\"\n};",
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"}
```

#### Sample Response
<a name="API_CreatePolicyTemplate_Example_1_Response"></a>

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
    "policyStoreId":"PSEXAMPLEabcdefg111111",
    "policyTemplateId":"PTEXAMPLEabcdefg111111",
    "createdDate":"2023-05-17T18:58:48.795411Z",
    "lastUpdatedDate":"2023-05-17T18:58:48.795411Z"
}
```

## See Also
<a name="API_CreatePolicyTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CreatePolicyTemplate)
