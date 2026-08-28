---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStore.html
---

# GetPolicyStore
<a name="API_GetPolicyStore"></a>

Retrieves details about a policy store.

## Request Syntax
<a name="API_GetPolicyStore_RequestSyntax"></a>

```
{
   "policyStoreId": "{{string}}",
   "tags": {{boolean}}
}
```

## Request Parameters
<a name="API_GetPolicyStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [policyStoreId](#API_GetPolicyStore_RequestSyntax) **   <a name="verifiedpermissions-GetPolicyStore-request-policyStoreId"></a>
Specifies the policy store that you want information about.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** [tags](#API_GetPolicyStore_RequestSyntax) **   <a name="verifiedpermissions-GetPolicyStore-request-tags"></a>
Specifies whether to return the tags that are attached to the policy store. If this parameter is included in the API call, the tags are returned, otherwise they are not returned.
If this parameter is included in the API call but there are no tags attached to the policy store, the `tags` response parameter is omitted from the response.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetPolicyStore_ResponseSyntax"></a>

```
{
   "arn": "string",
   "cedarVersion": "string",
   "createdDate": "string",
   "deletionProtection": "string",
   "description": "string",
   "encryptionState": { ... },
   "lastUpdatedDate": "string",
   "policyStoreId": "string",
   "tags": {
      "string" : "string"
   },
   "validationSettings": {
      "mode": "string"
   }
}
```

## Response Elements
<a name="API_GetPolicyStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-arn"></a>
The Amazon Resource Name (ARN) of the policy store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

 ** [createdDate](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-createdDate"></a>
The date and time that the policy store was originally created.
Type: Timestamp

 ** [lastUpdatedDate](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-lastUpdatedDate"></a>
The date and time that the policy store was last updated.
Type: Timestamp

 ** [policyStoreId](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-policyStoreId"></a>
The ID of the policy store;
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

 ** [validationSettings](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-validationSettings"></a>
The current validation settings for the policy store.
Type: [ValidationSettings](API_ValidationSettings.md) object

 ** [cedarVersion](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-cedarVersion"></a>
The version of the Cedar language used with policies, policy templates, and schemas in this policy store. For more information, see [Amazon Verified Permissions upgrade to Cedar v4 FAQ](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/cedar4-faq.html).
Type: String
Valid Values: `CEDAR_2 | CEDAR_4`

 ** [deletionProtection](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-deletionProtection"></a>
Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.
The default state is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [description](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-description"></a>
Descriptive text that you can provide to help with identification of the current policy store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.

 ** [encryptionState](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-encryptionState"></a>
A structure that contains the encryption configuration for the policy store.
Type: [EncryptionState](API_EncryptionState.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [tags](#API_GetPolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-GetPolicyStore-response-tags"></a>
The list of tags associated with the policy store.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetPolicyStore_Errors"></a>

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
<a name="API_GetPolicyStore_Examples"></a>

### Example
<a name="API_GetPolicyStore_Example_1"></a>

The following example retrieves details about the specified policy store.

#### Sample Request
<a name="API_GetPolicyStore_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.GetPolicyStore
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_GetPolicyStore_Example_1_Response"></a>

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
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111",
    "validationSettings": {"mode":"STRICT"},
    "createdDate": "2023-05-17T16:20:22.75472Z",
    "lastUpdatedDate": "2023-05-17T16:20:22.75472Z",
    "encryptionState": {
        "default": {}
    }
}
```

### Example
<a name="API_GetPolicyStore_Example_2"></a>

The following example retrieves details about the specified encrypted policy store.

#### Sample Request
<a name="API_GetPolicyStore_Example_2_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.GetPolicyStore
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

#### Sample Response
<a name="API_GetPolicyStore_Example_2_Response"></a>

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
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111",
    "validationSettings": {"mode":"STRICT"},
    "createdDate": "2023-05-17T16:20:22.75472Z",
    "lastUpdatedDate": "2023-05-17T16:20:22.75472Z",
    "encryptionState": {
        "kmsEncryptionState": {
            "encryptionContext": {
                "aws:verifiedpermissions:policy-store-arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111",
                "test_context_key": "test_context_value"
            },
            "key": "arn:aws::kms:us-east-1:123456789012:key/abcdefgh-ijkl-mnop-qrst-uvwxyz123456"
        }
    }
}
```

## See Also
<a name="API_GetPolicyStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/GetPolicyStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/GetPolicyStore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
