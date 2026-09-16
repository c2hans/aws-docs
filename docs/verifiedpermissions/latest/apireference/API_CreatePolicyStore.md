---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html
---

# CreatePolicyStore
<a name="API_CreatePolicyStore"></a>

Creates a policy store. A policy store is a container for policy resources.

**Note**
As of May 2026, Verified Permissions has aligned with Cedar and now supports multiple namespaces.

**Note**
Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) *. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

## Request Syntax
<a name="API_CreatePolicyStore_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "deletionProtection": "{{string}}",
   "description": "{{string}}",
   "encryptionSettings": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "validationSettings": {
      "mode": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreatePolicyStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [validationSettings](#API_CreatePolicyStore_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-request-validationSettings"></a>
Specifies the validation setting for this policy store.
Currently, the only valid and required value is `Mode`.
We recommend that you turn on `STRICT` mode only after you define a schema. If a schema doesn't exist, then `STRICT` mode causes any policy to fail validation, and Verified Permissions rejects the policy. You can turn off validation by using the [UpdatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore). Then, when you have a schema defined, use [UpdatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore) again to turn validation back on.
Type: [ValidationSettings](API_ValidationSettings.md) object
Required: Yes

 ** [clientToken](#API_CreatePolicyStore_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-request-clientToken"></a>
Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `ConflictException` error.
Verified Permissions recognizes a `ClientToken` for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of `ClientToken`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** [deletionProtection](#API_CreatePolicyStore_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-request-deletionProtection"></a>
Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.
The default state is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [description](#API_CreatePolicyStore_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-request-description"></a>
Descriptive text that you can provide to help with identification of the current policy store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

 ** [encryptionSettings](#API_CreatePolicyStore_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-request-encryptionSettings"></a>
Specifies the encryption settings used to encrypt the policy store and their child resources. Allows for the ability to use a customer owned KMS key for encryption of data.
This is an optional field to be used when providing a customer-managed KMS key for encryption.
Type: [EncryptionSettings](API_EncryptionSettings.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_CreatePolicyStore_RequestSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-request-tags"></a>
The list of key-value pairs to associate with the policy store.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePolicyStore_ResponseSyntax"></a>

```
{
   "arn": "string",
   "createdDate": "string",
   "lastUpdatedDate": "string",
   "policyStoreId": "string"
}
```

## Response Elements
<a name="API_CreatePolicyStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreatePolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-response-arn"></a>
The Amazon Resource Name (ARN) of the new policy store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

 ** [createdDate](#API_CreatePolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-response-createdDate"></a>
The date and time the policy store was originally created.
Type: Timestamp

 ** [lastUpdatedDate](#API_CreatePolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-response-lastUpdatedDate"></a>
The date and time the policy store was last updated.
Type: Timestamp

 ** [policyStoreId](#API_CreatePolicyStore_ResponseSyntax) **   <a name="verifiedpermissions-CreatePolicyStore-response-policyStoreId"></a>
The unique ID of the new policy store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`

## Errors
<a name="API_CreatePolicyStore_Errors"></a>

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
<a name="API_CreatePolicyStore_Examples"></a>

### Example
<a name="API_CreatePolicyStore_Example_1"></a>

The following example creates a new policy store with strict validation turned on.

#### Sample Request
<a name="API_CreatePolicyStore_Example_1_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.CreatePolicyStore
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "validationSettings": {"mode": "STRICT"},
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111"
}
```

#### Sample Response
<a name="API_CreatePolicyStore_Example_1_Response"></a>

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
    "arn":"arn:aws::verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111",
    "createdDate":"2023-05-16T17:41:29.103459Z",
    "lastUpdatedDate":"2023-05-16T17:41:29.103459Z"
}
```

### Example
<a name="API_CreatePolicyStore_Example_2"></a>

The following example creates a new encrypted policy store with strict validation turned on.

#### Sample Request
<a name="API_CreatePolicyStore_Example_2_Request"></a>

```
POST HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: identity
X-Amz-Target: VerifiedPermissions.CreatePolicyStore
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "validationSettings": {"mode": "STRICT"},
    "clientToken": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111",
    "encryptionSettings": {
        "kmsEncryptionSettings": {
            "key": "arn:aws::kms:us-east-1:123456789012:key/abcdefgh-ijkl-mnop-qrst-uvwxyz123456",
            "encryptionContext": {
                "test_key": "test_value"
            }
        }
    }
}
```

#### Sample Response
<a name="API_CreatePolicyStore_Example_2_Response"></a>

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
    "arn":"arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111",
    "createdDate":"2023-05-16T17:41:29.103459Z",
    "lastUpdatedDate":"2023-05-16T17:41:29.103459Z"
}
```

## See Also
<a name="API_CreatePolicyStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/verifiedpermissions-2021-12-01/CreatePolicyStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CreatePolicyStore)
