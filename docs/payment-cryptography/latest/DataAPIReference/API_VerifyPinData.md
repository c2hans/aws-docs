---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyPinData.html
---

# VerifyPinData
<a name="API_VerifyPinData"></a>

Verifies pin-related data such as PIN and PIN Offset using algorithms including VISA PVV and IBM3624. For more information, see [Verify PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-pin-data.html) in the * AWS Payment Cryptography User Guide*.

This operation verifies PIN data for user payment card. A card holder PIN data is never transmitted in clear to or from AWS Payment Cryptography. This operation uses PIN Verification Key (PVK) for PIN or PIN Offset generation and then encrypts it using PIN Encryption Key (PEK) to create an `EncryptedPinBlock` for transmission from AWS Payment Cryptography.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [GeneratePinData](API_GeneratePinData.md)
+  [TranslatePinData](API_TranslatePinData.md)

## Request Syntax
<a name="API_VerifyPinData_RequestSyntax"></a>

```
POST /pindata/verify HTTP/1.1
Content-type: application/json

{
   "DukptAttributes": {
      "DukptDerivationType": "{{string}}",
      "KeySerialNumber": "{{string}}"
   },
   "EncryptedPinBlock": "{{string}}",
   "EncryptionKeyIdentifier": "{{string}}",
   "EncryptionWrappedKey": {
      "KeyCheckValueAlgorithm": "{{string}}",
      "WrappedKeyMaterial": { ... }
   },
   "PinBlockFormat": "{{string}}",
   "PinDataLength": {{number}},
   "PrimaryAccountNumber": "{{string}}",
   "VerificationAttributes": { ... },
   "VerificationKeyIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_VerifyPinData_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_VerifyPinData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DukptAttributes](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-DukptAttributes"></a>
The attributes and values for the DUKPT encrypted PIN block data.
Type: [DukptAttributes](API_DukptAttributes.md) object
Required: No

 ** [EncryptedPinBlock](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-EncryptedPinBlock"></a>
The encrypted PIN block data that AWS Payment Cryptography verifies.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** [EncryptionKeyIdentifier](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-EncryptionKeyIdentifier"></a>
The `keyARN` of the encryption key under which the PIN block data is encrypted. This key type can be PEK or BDK.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [EncryptionWrappedKey](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-EncryptionWrappedKey"></a>
Parameter information of a WrappedKeyBlock for encryption key exchange.
Type: [WrappedKey](API_WrappedKey.md) object
Required: No

 ** [PinBlockFormat](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-PinBlockFormat"></a>
The PIN encoding format for pin data generation as specified in ISO 9564. AWS Payment Cryptography supports `ISO_Format_0` and `ISO_Format_3`.
The `ISO_Format_0` PIN block format is equivalent to the ANSI X9.8, VISA-1, and ECI-1 PIN block formats. It is similar to a VISA-4 PIN block format. It supports a PIN from 4 to 12 digits in length.
The `ISO_Format_3` PIN block format is the same as `ISO_Format_0` except that the fill digits are random values from 10 to 15.
Type: String
Valid Values: `ISO_FORMAT_0 | ISO_FORMAT_1 | ISO_FORMAT_3 | ISO_FORMAT_4`
Required: Yes

 ** [PinDataLength](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-PinDataLength"></a>
The length of PIN being verified.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 12.
Required: No

 ** [PrimaryAccountNumber](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-PrimaryAccountNumber"></a>
The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: No

 ** [VerificationAttributes](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-VerificationAttributes"></a>
The attributes and values for PIN data verification.
Type: [PinVerificationAttributes](API_PinVerificationAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [VerificationKeyIdentifier](#API_VerifyPinData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyPinData-request-VerificationKeyIdentifier"></a>
The `keyARN` of the PIN verification key.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## Response Syntax
<a name="API_VerifyPinData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EncryptionKeyArn": "string",
   "EncryptionKeyCheckValue": "string",
   "VerificationKeyArn": "string",
   "VerificationKeyCheckValue": "string"
}
```

## Response Elements
<a name="API_VerifyPinData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncryptionKeyArn](#API_VerifyPinData_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyPinData-response-EncryptionKeyArn"></a>
The `keyARN` of the PEK that AWS Payment Cryptography uses for encrypted pin block generation.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [EncryptionKeyCheckValue](#API_VerifyPinData_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyPinData-response-EncryptionKeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [VerificationKeyArn](#API_VerifyPinData_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyPinData-response-VerificationKeyArn"></a>
The `keyARN` of the PIN encryption key that AWS Payment Cryptography uses for PIN or PIN Offset verification.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [VerificationKeyCheckValue](#API_VerifyPinData_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyPinData-response-VerificationKeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

## Errors
<a name="API_VerifyPinData_Errors"></a>

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

 ** VerificationFailedException **
This request failed verification.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_VerifyPinData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/VerifyPinData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/VerifyPinData)
