---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html
---

# CreateKey
<a name="API_CreateKey"></a>

Creates an AWS Payment Cryptography key, a logical representation of a cryptographic key, that is unique in your account and AWS Region. You use keys for cryptographic functions such as encryption and decryption.

In addition to the key material used in cryptographic operations, an AWS Payment Cryptography key includes metadata such as the key ARN, key usage, key origin, creation date, description, and key state.

When you create a key, you specify both immutable and mutable data about the key. The immutable data contains key attributes that define the scope and cryptographic operations that you can perform using the key, for example key class (example: `SYMMETRIC_KEY`), key algorithm (example: `TDES_2KEY`), key usage (example: `TR31_P0_PIN_ENCRYPTION_KEY`) and key modes of use (example: `Encrypt`). AWS Payment Cryptography binds key attributes to keys using key blocks when you store or export them. AWS Payment Cryptography stores the key contents wrapped and never stores or transmits them in the clear.

For information about valid combinations of key attributes, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) in the * AWS Payment Cryptography User Guide*. The mutable data contained within a key includes usage timestamp and key deletion timestamp and can be modified after creation.

You can use the `CreateKey` operation to generate an ECC (Elliptic Curve Cryptography) key pair used for establishing an ECDH (Elliptic Curve Diffie-Hellman) key agreement between two parties. In the ECDH key agreement process, both parties generate their own ECC key pair with key usage K3 and exchange the public keys. Each party then use their private key, the received public key from the other party, and the key derivation parameters including key derivation function, hash algorithm, derivation data, and key algorithm to derive a shared key.

To maintain the single-use principle of cryptographic keys in payments, ECDH derived keys should not be used for multiple purposes, such as a `TR31_P0_PIN_ENCRYPTION_KEY` and `TR31_K1_KEY_BLOCK_PROTECTION_KEY`. When creating ECC key pairs in AWS Payment Cryptography you can optionally set the `DeriveKeyUsage` parameter, which defines the key usage bound to the symmetric key that will be derived using the ECC key pair.

 **Cross-account use**: This operation can't be used across different AWS accounts.

 **Related operations:**
+  [DeleteKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html)
+  [GetKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html)
+  [ListKeys](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html)

## Request Syntax
<a name="API_CreateKey_RequestSyntax"></a>

```
{
   "DeriveKeyUsage": "{{string}}",
   "Enabled": {{boolean}},
   "Exportable": {{boolean}},
   "KeyAttributes": {
      "KeyAlgorithm": "{{string}}",
      "KeyClass": "{{string}}",
      "KeyModesOfUse": {
         "Decrypt": {{boolean}},
         "DeriveKey": {{boolean}},
         "Encrypt": {{boolean}},
         "Generate": {{boolean}},
         "NoRestrictions": {{boolean}},
         "Sign": {{boolean}},
         "Unwrap": {{boolean}},
         "Verify": {{boolean}},
         "Wrap": {{boolean}}
      },
      "KeyUsage": "{{string}}"
   },
   "KeyCheckValueAlgorithm": "{{string}}",
   "ReplicationRegions": [ "{{string}}" ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateKey_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeriveKeyUsage](#API_CreateKey_RequestSyntax) **   <a name="paymentcryptography-CreateKey-request-DeriveKeyUsage"></a>
The intended cryptographic usage of keys derived from the ECC key pair to be created.
After creating an ECC key pair, you cannot change the intended cryptographic usage of keys derived from it using ECDH.
Type: String
Valid Values: `TR31_B0_BASE_DERIVATION_KEY | TR31_C0_CARD_VERIFICATION_KEY | TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY | TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS | TR31_E1_EMV_MKEY_CONFIDENTIALITY | TR31_E2_EMV_MKEY_INTEGRITY | TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS | TR31_E5_EMV_MKEY_CARD_PERSONALIZATION | TR31_E6_EMV_MKEY_OTHER | TR31_K0_KEY_ENCRYPTION_KEY | TR31_K1_KEY_BLOCK_PROTECTION_KEY | TR31_M3_ISO_9797_3_MAC_KEY | TR31_M1_ISO_9797_1_MAC_KEY | TR31_M6_ISO_9797_5_CMAC_KEY | TR31_M7_HMAC_KEY | TR31_P0_PIN_ENCRYPTION_KEY | TR31_P1_PIN_GENERATION_KEY | TR31_V1_IBM3624_PIN_VERIFICATION_KEY | TR31_V2_VISA_PIN_VERIFICATION_KEY`
Required: No

 ** [Enabled](#API_CreateKey_RequestSyntax) **   <a name="paymentcryptography-CreateKey-request-Enabled"></a>
Specifies whether to enable the key. If the key is enabled, it is activated for use within the service. If the key is not enabled, then it is created but not activated. The default value is enabled.
Type: Boolean
Required: No

 ** [Exportable](#API_CreateKey_RequestSyntax) **   <a name="paymentcryptography-CreateKey-request-Exportable"></a>
Specifies whether the key is exportable from the service.
Type: Boolean
Required: Yes

 ** [KeyAttributes](#API_CreateKey_RequestSyntax) **   <a name="paymentcryptography-CreateKey-request-KeyAttributes"></a>
The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.
Type: [KeyAttributes](API_KeyAttributes.md) object
Required: Yes

 ** [KeyCheckValueAlgorithm](#API_CreateKey_RequestSyntax) **   <a name="paymentcryptography-CreateKey-request-KeyCheckValueAlgorithm"></a>
The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.
For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.
Type: String
Valid Values: `CMAC | ANSI_X9_24 | HMAC | SHA_1`
Required: No

 ** [ReplicationRegions](#API_CreateKey_RequestSyntax) **   <a name="paymentcryptography-CreateKey-request-ReplicationRegions"></a>
A list of AWS Regions for key replication operations.
Each region in the list must be a valid AWS Region identifier where AWS Payment Cryptography is available. This list is used to specify which regions should be added to or removed from a key's replication configuration.
Type: Array of strings
Pattern: `[a-z]{2}-[a-z]{1,16}-[0-9]+`
Required: No

 ** [Tags](#API_CreateKey_RequestSyntax) **   <a name="paymentcryptography-CreateKey-request-Tags"></a>
Assigns one or more tags to the AWS Payment Cryptography key. Use this parameter to tag a key when it is created. To tag an existing AWS Payment Cryptography key, use the [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html) operation.
Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You can't have more than one tag on an AWS Payment Cryptography key with the same tag key.
Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
Tagging or untagging an AWS Payment Cryptography key can allow or deny permission to the key.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateKey_ResponseSyntax"></a>

```
{
   "Key": {
      "CreateTimestamp": number,
      "DeletePendingTimestamp": number,
      "DeleteTimestamp": number,
      "DeriveKeyUsage": "string",
      "Enabled": boolean,
      "Exportable": boolean,
      "KeyArn": "string",
      "KeyAttributes": {
         "KeyAlgorithm": "string",
         "KeyClass": "string",
         "KeyModesOfUse": {
            "Decrypt": boolean,
            "DeriveKey": boolean,
            "Encrypt": boolean,
            "Generate": boolean,
            "NoRestrictions": boolean,
            "Sign": boolean,
            "Unwrap": boolean,
            "Verify": boolean,
            "Wrap": boolean
         },
         "KeyUsage": "string"
      },
      "KeyCheckValue": "string",
      "KeyCheckValueAlgorithm": "string",
      "KeyOrigin": "string",
      "KeyState": "string",
      "MpaStatus": {
         "InitiationDate": number,
         "MpaSessionArn": "string",
         "Status": "string",
         "StatusMessage": "string"
      },
      "MultiRegionKeyType": "string",
      "PrimaryRegion": "string",
      "ReplicationStatus": {
         "string" : {
            "Status": "string",
            "StatusMessage": "string"
         }
      },
      "UsageStartTimestamp": number,
      "UsageStopTimestamp": number,
      "UsingDefaultReplicationRegions": boolean
   }
}
```

## Response Elements
<a name="API_CreateKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Key](#API_CreateKey_ResponseSyntax) **   <a name="paymentcryptography-CreateKey-response-Key"></a>
The key material that contains all the key attributes.
Type: [Key](API_Key.md) object

## Errors
<a name="API_CreateKey_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific AWS Payment Cryptography action you're attempting.
HTTP Status Code: 400

 ** ConflictException **
This request can cause an inconsistent state for the resource.
The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
This indicates a server-side error within the AWS Payment Cryptography service. If this error persists, contact support for assistance.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied due to resource not found.
The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.
 ** ResourceId **
The identifier of the resource that was not found.
This field contains the specific resource identifier (such as a key ARN or alias name) that could not be located.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
This request would cause a service quota to be exceeded.
You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
The AWS Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
You have exceeded the rate limits for AWS Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.
HTTP Status Code: 400

 ** ValidationException **
The request was denied due to an invalid request error.
One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.
HTTP Status Code: 400

## See Also
<a name="API_CreateKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/CreateKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/CreateKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
