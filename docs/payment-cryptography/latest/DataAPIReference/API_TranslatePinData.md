---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslatePinData.html
---

# TranslatePinData
<a name="API_TranslatePinData"></a>

Translates encrypted PIN block from and to ISO 9564 formats 0,1,3,4. For more information, see [Translate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/translate-pin-data.html) in the * AWS Payment Cryptography User Guide*.

PIN block translation involves changing a PIN block from one encryption key to another and optionally change its format. PIN block translation occurs entirely within the HSM boundary and PIN data never enters or leaves AWS Payment Cryptography in clear text. The encryption key transformation can be from PEK (Pin Encryption Key) to BDK (Base Derivation Key) for DUKPT or from BDK for DUKPT to PEK.

 AWS Payment Cryptography also supports use of dynamic keys and ECDH (Elliptic Curve Diffie-Hellman) based key exchange for this operation.

Dynamic keys allow you to pass a PEK as a TR-31 WrappedKeyBlock. They can be used when key material is frequently rotated, such as during every card transaction, and there is need to avoid importing short-lived keys into AWS Payment Cryptography. To translate PIN block using dynamic keys, the `keyARN` is the Key Encryption Key (KEK) of the TR-31 wrapped PEK. The incoming wrapped key shall have a key purpose of P0 with a mode of use of B or D. For more information, see [Using Dynamic Keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html) in the * AWS Payment Cryptography User Guide*.

Using ECDH key exchange, you can receive cardholder selectable PINs into AWS Payment Cryptography. The ECDH derived key protects the incoming PIN block, which is translated to a PEK encrypted PIN block for use within the service. You can also use ECDH for reveal PIN, wherein the service translates the PIN block from PEK to a ECDH derived encryption key. For more information on establishing ECDH derived keys, see the [Creating keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html) in the * AWS Payment Cryptography User Guide*.

The allowed combinations of PIN block format translations are guided by PCI. It is important to note that not all encrypted PIN block formats (example, format 1) require PAN (Primary Account Number) as input. And as such, PIN block format that requires PAN (example, formats 0,3,4) cannot be translated to a format (format 1) that does not require a PAN for generation.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

**Note**
 AWS Payment Cryptography currently supports ISO PIN block 4 translation for PIN block built using legacy PAN length. That is, PAN is the right most 12 digits excluding the check digits.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [GeneratePinData](API_GeneratePinData.md)
+  [VerifyPinData](API_VerifyPinData.md)

## Request Syntax
<a name="API_TranslatePinData_RequestSyntax"></a>

```
POST /pindata/translate HTTP/1.1
Content-type: application/json

{
   "EncryptedPinBlock": "{{string}}",
   "IncomingAs2805Attributes": {
      "SystemTraceAuditNumber": "{{string}}",
      "TransactionAmount": "{{string}}"
   },
   "IncomingDukptAttributes": {
      "DukptKeyDerivationType": "{{string}}",
      "DukptKeyVariant": "{{string}}",
      "KeySerialNumber": "{{string}}"
   },
   "IncomingKeyIdentifier": "{{string}}",
   "IncomingTranslationAttributes": { ... },
   "IncomingWrappedKey": {
      "KeyCheckValueAlgorithm": "{{string}}",
      "WrappedKeyMaterial": { ... }
   },
   "OutgoingDukptAttributes": {
      "DukptKeyDerivationType": "{{string}}",
      "DukptKeyVariant": "{{string}}",
      "KeySerialNumber": "{{string}}"
   },
   "OutgoingKeyIdentifier": "{{string}}",
   "OutgoingTranslationAttributes": { ... },
   "OutgoingWrappedKey": {
      "KeyCheckValueAlgorithm": "{{string}}",
      "WrappedKeyMaterial": { ... }
   }
}
```

## URI Request Parameters
<a name="API_TranslatePinData_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TranslatePinData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EncryptedPinBlock](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-EncryptedPinBlock"></a>
The encrypted PIN block data that AWS Payment Cryptography translates.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: Yes

 ** [IncomingAs2805Attributes](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-IncomingAs2805Attributes"></a>
The attributes and values to use for incoming AS2805 encryption key for PIN block translation.
Type: [As2805PekDerivationAttributes](API_As2805PekDerivationAttributes.md) object
Required: No

 ** [IncomingDukptAttributes](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-IncomingDukptAttributes"></a>
The attributes and values to use for incoming DUKPT encryption key for PIN block translation.
Type: [DukptDerivationAttributes](API_DukptDerivationAttributes.md) object
Required: No

 ** [IncomingKeyIdentifier](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-IncomingKeyIdentifier"></a>
The `keyARN` of the encryption key under which incoming PIN block data is encrypted. This key type can be PEK or BDK.
For dynamic keys, it is the `keyARN` of KEK of the TR-31 wrapped PEK. For ECDH, it is the `keyARN` of the asymmetric ECC key.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [IncomingTranslationAttributes](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-IncomingTranslationAttributes"></a>
The format of the incoming PIN block data for translation within AWS Payment Cryptography.
Type: [TranslationIsoFormats](API_TranslationIsoFormats.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [IncomingWrappedKey](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-IncomingWrappedKey"></a>
The WrappedKeyBlock containing the encryption key under which incoming PIN block data is encrypted.
Type: [WrappedKey](API_WrappedKey.md) object
Required: No

 ** [OutgoingDukptAttributes](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-OutgoingDukptAttributes"></a>
The attributes and values to use for outgoing DUKPT encryption key after PIN block translation.
Type: [DukptDerivationAttributes](API_DukptDerivationAttributes.md) object
Required: No

 ** [OutgoingKeyIdentifier](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-OutgoingKeyIdentifier"></a>
The `keyARN` of the encryption key for encrypting outgoing PIN block data. This key type can be PEK or BDK.
For ECDH, it is the `keyARN` of the asymmetric ECC key.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [OutgoingTranslationAttributes](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-OutgoingTranslationAttributes"></a>
The format of the outgoing PIN block data after translation by AWS Payment Cryptography.
Type: [TranslationIsoFormats](API_TranslationIsoFormats.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [OutgoingWrappedKey](#API_TranslatePinData_RequestSyntax) **   <a name="paymentcryptographydata-TranslatePinData-request-OutgoingWrappedKey"></a>
The WrappedKeyBlock containing the encryption key for encrypting outgoing PIN block data.
Type: [WrappedKey](API_WrappedKey.md) object
Required: No

## Response Syntax
<a name="API_TranslatePinData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "KeyArn": "string",
   "KeyCheckValue": "string",
   "PinBlock": "string"
}
```

## Response Elements
<a name="API_TranslatePinData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyArn](#API_TranslatePinData_ResponseSyntax) **   <a name="paymentcryptographydata-TranslatePinData-response-KeyArn"></a>
The `keyARN` of the encryption key that AWS Payment Cryptography uses to encrypt outgoing PIN block data after translation.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [KeyCheckValue](#API_TranslatePinData_ResponseSyntax) **   <a name="paymentcryptographydata-TranslatePinData-response-KeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [PinBlock](#API_TranslatePinData_ResponseSyntax) **   <a name="paymentcryptographydata-TranslatePinData-response-PinBlock"></a>
The outgoing encrypted PIN block data after translation.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `[0-9a-fA-F]+`

## Errors
<a name="API_TranslatePinData_Errors"></a>

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
<a name="API_TranslatePinData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/TranslatePinData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/TranslatePinData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
