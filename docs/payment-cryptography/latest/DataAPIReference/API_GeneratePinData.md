---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GeneratePinData.html
---

# GeneratePinData
<a name="API_GeneratePinData"></a>

Generates pin-related data such as PIN, PIN Verification Value (PVV), PIN Block, and PIN Offset during new card issuance or reissuance. For more information, see [Generate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-pin-data.html) in the * AWS Payment Cryptography User Guide*.

PIN data is never transmitted in clear to or from AWS Payment Cryptography. This operation generates PIN, PVV, or PIN Offset and then encrypts it using Pin Encryption Key (PEK) to create an `EncryptedPinBlock` for transmission from AWS Payment Cryptography. This operation uses a separate Pin Verification Key (PVK) for VISA PVV generation.

Using ECDH key exchange, you can receive cardholder selectable PINs into AWS Payment Cryptography. The ECDH derived key protects the incoming PIN block. You can also use it for reveal PIN, wherein the generated PIN block is protected by the ECDH derived key before transmission from AWS Payment Cryptography. For more information on establishing ECDH derived keys, see the [Generating keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html) in the * AWS Payment Cryptography User Guide*.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [GenerateCardValidationData](API_GenerateCardValidationData.md)
+  [TranslatePinData](API_TranslatePinData.md)
+  [VerifyPinData](API_VerifyPinData.md)

## Request Syntax
<a name="API_GeneratePinData_RequestSyntax"></a>

```
POST /pindata/generate HTTP/1.1
Content-type: application/json

{
   "EncryptionKeyIdentifier": "{{string}}",
   "EncryptionWrappedKey": {
      "KeyCheckValueAlgorithm": "{{string}}",
      "WrappedKeyMaterial": { ... }
   },
   "GenerationAttributes": { ... },
   "GenerationKeyIdentifier": "{{string}}",
   "PinBlockFormat": "{{string}}",
   "PinDataLength": {{number}},
   "PrimaryAccountNumber": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GeneratePinData_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GeneratePinData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EncryptionKeyIdentifier](#API_GeneratePinData_RequestSyntax) **   <a name="paymentcryptographydata-GeneratePinData-request-EncryptionKeyIdentifier"></a>
The `keyARN` of the PEK that AWS Payment Cryptography uses to encrypt the PIN Block. For ECDH, it is the `keyARN` of the asymmetric ECC key.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [EncryptionWrappedKey](#API_GeneratePinData_RequestSyntax) **   <a name="paymentcryptographydata-GeneratePinData-request-EncryptionWrappedKey"></a>
Parameter information of a WrappedKeyBlock for encryption key exchange.
Type: [WrappedKey](API_WrappedKey.md) object
Required: No

 ** [GenerationAttributes](#API_GeneratePinData_RequestSyntax) **   <a name="paymentcryptographydata-GeneratePinData-request-GenerationAttributes"></a>
The attributes and values to use for PIN, PVV, or PIN Offset generation.
Type: [PinGenerationAttributes](API_PinGenerationAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [GenerationKeyIdentifier](#API_GeneratePinData_RequestSyntax) **   <a name="paymentcryptographydata-GeneratePinData-request-GenerationKeyIdentifier"></a>
The `keyARN` of the PEK that AWS Payment Cryptography uses for pin data generation.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [PinBlockFormat](#API_GeneratePinData_RequestSyntax) **   <a name="paymentcryptographydata-GeneratePinData-request-PinBlockFormat"></a>
The PIN encoding format for pin data generation as specified in ISO 9564. AWS Payment Cryptography supports `ISO_Format_0`, `ISO_Format_3` and `ISO_Format_4`.
The `ISO_Format_0` PIN block format is equivalent to the ANSI X9.8, VISA-1, and ECI-1 PIN block formats. It is similar to a VISA-4 PIN block format. It supports a PIN from 4 to 12 digits in length.
The `ISO_Format_3` PIN block format is the same as `ISO_Format_0` except that the fill digits are random values from 10 to 15.
The `ISO_Format_4` PIN block format is the only one supporting AES encryption.
Type: String
Valid Values: `ISO_FORMAT_0 | ISO_FORMAT_1 | ISO_FORMAT_3 | ISO_FORMAT_4`
Required: Yes

 ** [PinDataLength](#API_GeneratePinData_RequestSyntax) **   <a name="paymentcryptographydata-GeneratePinData-request-PinDataLength"></a>
The length of PIN under generation.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 12.
Required: No

 ** [PrimaryAccountNumber](#API_GeneratePinData_RequestSyntax) **   <a name="paymentcryptographydata-GeneratePinData-request-PrimaryAccountNumber"></a>
The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: No

## Response Syntax
<a name="API_GeneratePinData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EncryptedPinBlock": "string",
   "EncryptionKeyArn": "string",
   "EncryptionKeyCheckValue": "string",
   "GenerationKeyArn": "string",
   "GenerationKeyCheckValue": "string",
   "PinData": { ... }
}
```

## Response Elements
<a name="API_GeneratePinData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncryptedPinBlock](#API_GeneratePinData_ResponseSyntax) **   <a name="paymentcryptographydata-GeneratePinData-response-EncryptedPinBlock"></a>
The PIN block encrypted under PEK from AWS Payment Cryptography. The encrypted PIN block is a composite of PAN (Primary Account Number) and PIN (Personal Identification Number), generated in accordance with ISO 9564 standard.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `[0-9a-fA-F]+`

 ** [EncryptionKeyArn](#API_GeneratePinData_ResponseSyntax) **   <a name="paymentcryptographydata-GeneratePinData-response-EncryptionKeyArn"></a>
The `keyARN` of the PEK that AWS Payment Cryptography uses for encrypted pin block generation. For ECDH, it is the `keyARN` of the asymmetric ECC key.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [EncryptionKeyCheckValue](#API_GeneratePinData_ResponseSyntax) **   <a name="paymentcryptographydata-GeneratePinData-response-EncryptionKeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [GenerationKeyArn](#API_GeneratePinData_ResponseSyntax) **   <a name="paymentcryptographydata-GeneratePinData-response-GenerationKeyArn"></a>
The `keyARN` of the pin data generation key that AWS Payment Cryptography uses for PIN, PVV or PIN Offset generation.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [GenerationKeyCheckValue](#API_GeneratePinData_ResponseSyntax) **   <a name="paymentcryptographydata-GeneratePinData-response-GenerationKeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [PinData](#API_GeneratePinData_ResponseSyntax) **   <a name="paymentcryptographydata-GeneratePinData-response-PinData"></a>
The attributes and values AWS Payment Cryptography uses for pin data generation.
Type: [PinData](API_PinData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_GeneratePinData_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied due to an invalid resource error.
 ** ResourceId **
The resource that is missing.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied due to an invalid request error.
 ** fieldList **
The request was denied due to an invalid request error.
HTTP Status Code: 400

## See Also
<a name="API_GeneratePinData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/GeneratePinData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/GeneratePinData)
