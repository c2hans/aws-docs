---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html
---

# GenerateMac
<a name="API_GenerateMac"></a>

Generates a hash-based message authentication code (HMAC) for a message using an HMAC KMS key and a MAC algorithm that the key supports. HMAC KMS keys and the HMAC algorithms that AWS KMS uses conform to industry standards defined in [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104).

You can use value that GenerateMac returns in the [VerifyMac](API_VerifyMac.md) operation to demonstrate that the original message has not changed. Also, because a secret key is used to create the hash, you can verify that the party that generated the hash has the required secret key. You can also use the raw result to implement HMAC-based algorithms such as key derivation functions. This operation is part of AWS KMS support for HMAC KMS keys. For details, see [HMAC keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html) in the * * AWS Key Management Service Developer Guide* *.

**Note**
Best practices recommend that you limit the time during which any signing mechanism, including an HMAC, is effective. This deters an attack where the actor uses a signed message to establish validity repeatedly or long after the message is superseded. HMAC tags do not include a timestamp, but you can include a timestamp in the token or message to help you detect when its time to refresh the HMAC.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations**: [VerifyMac](API_VerifyMac.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GenerateMac_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}",
   "MacAlgorithm": "{{string}}",
   "Message": {{blob}}
}
```

## Request Parameters
<a name="API_GenerateMac_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_GenerateMac_RequestSyntax) **   <a name="KMS-GenerateMac-request-KeyId"></a>
The HMAC KMS key to use in the operation. The MAC algorithm computes the HMAC for the message and the key as described in [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104).
To identify an HMAC KMS key, use the [DescribeKey](API_DescribeKey.md) operation and see the `KeySpec` field in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [MacAlgorithm](#API_GenerateMac_RequestSyntax) **   <a name="KMS-GenerateMac-request-MacAlgorithm"></a>
The MAC algorithm used in the operation.
 The algorithm must be compatible with the HMAC KMS key that you specify. To find the MAC algorithms that your HMAC KMS key supports, use the [DescribeKey](API_DescribeKey.md) operation and see the `MacAlgorithms` field in the `DescribeKey` response.
Type: String
Valid Values: `HMAC_SHA_224 | HMAC_SHA_256 | HMAC_SHA_384 | HMAC_SHA_512`
Required: Yes

 ** [Message](#API_GenerateMac_RequestSyntax) **   <a name="KMS-GenerateMac-request-Message"></a>
The message to be hashed. Specify a message of up to 4,096 bytes.
 `GenerateMac` and [VerifyMac](API_VerifyMac.md) do not provide special handling for message digests. If you generate an HMAC for a hash digest of a message, you must verify the HMAC of the same hash digest.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** [DryRun](#API_GenerateMac_RequestSyntax) **   <a name="KMS-GenerateMac-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** [GrantTokens](#API_GenerateMac_RequestSyntax) **   <a name="KMS-GenerateMac-request-GrantTokens"></a>
A list of grant tokens.
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_GenerateMac_ResponseSyntax"></a>

```
{
   "KeyId": "string",
   "Mac": blob,
   "MacAlgorithm": "string"
}
```

## Response Elements
<a name="API_GenerateMac_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyId](#API_GenerateMac_ResponseSyntax) **   <a name="KMS-GenerateMac-response-KeyId"></a>
The HMAC KMS key used in the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Mac](#API_GenerateMac_ResponseSyntax) **   <a name="KMS-GenerateMac-response-Mac"></a>
The hash-based message authentication code (HMAC) that was generated for the specified message, HMAC KMS key, and MAC algorithm.
This is the standard, raw HMAC defined in [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [MacAlgorithm](#API_GenerateMac_ResponseSyntax) **   <a name="KMS-GenerateMac-response-MacAlgorithm"></a>
The MAC algorithm that was used to generate the HMAC.
Type: String
Valid Values: `HMAC_SHA_224 | HMAC_SHA_256 | HMAC_SHA_384 | HMAC_SHA_512`

## Errors
<a name="API_GenerateMac_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledException **
The request was rejected because the specified KMS key is not enabled.
HTTP Status Code: 400

 ** DryRunOperationException **
 The request was rejected because the DryRun parameter was specified.
HTTP Status Code: 400

 ** InvalidGrantTokenException **
The request was rejected because the specified grant token is not valid.
HTTP Status Code: 400

 ** InvalidKeyUsageException **
The request was rejected for one of the following reasons:
+ The `KeyUsage` value of the KMS key is incompatible with the API operation.
+ The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key `(KeySpec`).
For encrypting, decrypting, re-encrypting, and generating data keys, the `KeyUsage` must be `ENCRYPT_DECRYPT`. For signing and verifying messages, the `KeyUsage` must be `SIGN_VERIFY`. For generating and verifying message authentication codes (MACs), the `KeyUsage` must be `GENERATE_VERIFY_MAC`. For deriving key agreement secrets, the `KeyUsage` must be `KEY_AGREEMENT`. To find the `KeyUsage` of a KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
To find the encryption or signing algorithms supported for a particular KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
HTTP Status Code: 400

 ** KeyUnavailableException **
The request was rejected because the specified KMS key was not available. You can retry the request.
HTTP Status Code: 500

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** KMSInvalidStateException **
The request was rejected because the state of the specified resource is not valid for this request.
This exceptions means one of the following:
+ The key state of the KMS key is not compatible with the operation.

  To find the key state, use the [DescribeKey](API_DescribeKey.md) operation. For more information about which key states are compatible with each AWS KMS operation, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * * AWS Key Management Service Developer Guide* *.
+ For cryptographic operations on KMS keys in custom key stores, this exception represents a general failure with many possible causes. To identify the cause, see the error message that accompanies the exception.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

## See Also
<a name="API_GenerateMac_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GenerateMac)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GenerateMac)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GenerateMac)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GenerateMac)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GenerateMac)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GenerateMac)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GenerateMac)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GenerateMac)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GenerateMac)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GenerateMac)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
