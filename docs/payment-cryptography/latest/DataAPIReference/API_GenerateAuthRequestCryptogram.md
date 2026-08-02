---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateAuthRequestCryptogram.html
---

# GenerateAuthRequestCryptogram
<a name="API_GenerateAuthRequestCryptogram"></a>

Generates an Authorization Request Cryptogram (ARQC) for an EMV chip payment card authorization. For more information, see [Generate auth request cryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.generateauthrequestcryptogram.html) in the * AWS Payment Cryptography User Guide*.

ARQC generation uses an Issuer Master Key (IMK) for application cryptograms (TR31\_E0\_EMV\_MKEY\_APP\_CRYPTOGRAMS) to derive a session key, which is then used to generate the cryptogram from the provided transaction data (when applicable). To use this operation, you must first create or import an IMK-AC key by calling [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) or [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html). The `KeyModesOfUse` should be set to `DeriveKey` for the IMK-AC encryption key.

**Important**
This operation is intended for development and testing scenarios only. It is not recommended to use this operation as a substitute for card-based cryptogram generation in production payment flows.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [VerifyAuthRequestCryptogram](API_VerifyAuthRequestCryptogram.md)

## Request Syntax
<a name="API_GenerateAuthRequestCryptogram_RequestSyntax"></a>

```
POST /cryptogram/generate HTTP/1.1
Content-type: application/json

{
   "KeyIdentifier": "{{string}}",
   "MajorKeyDerivationMode": "{{string}}",
   "SessionKeyDerivationAttributes": { ... },
   "TransactionData": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GenerateAuthRequestCryptogram_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GenerateAuthRequestCryptogram_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KeyIdentifier](#API_GenerateAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-GenerateAuthRequestCryptogram-request-KeyIdentifier"></a>
The `keyARN` of the IMK-AC (TR31\_E0\_EMV\_MKEY\_APP\_CRYPTOGRAMS) that AWS Payment Cryptography uses to generate the ARQC.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [MajorKeyDerivationMode](#API_GenerateAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-GenerateAuthRequestCryptogram-request-MajorKeyDerivationMode"></a>
The method to use when deriving the major encryption key for ARQC generation within AWS Payment Cryptography.
Type: String
Valid Values: `EMV_OPTION_A | EMV_OPTION_B`
Required: Yes

 ** [SessionKeyDerivationAttributes](#API_GenerateAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-GenerateAuthRequestCryptogram-request-SessionKeyDerivationAttributes"></a>
The attributes and values to use for deriving a session key for ARQC generation within AWS Payment Cryptography.
Type: [SessionKeyDerivation](API_SessionKeyDerivation.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [TransactionData](#API_GenerateAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-GenerateAuthRequestCryptogram-request-TransactionData"></a>
The transaction data that AWS Payment Cryptography uses for ARQC generation. The same transaction data is used for ARQC verification by the issuer using [VerifyAuthRequestCryptogram](API_VerifyAuthRequestCryptogram.md).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 1024.
Pattern: `[0-9a-fA-F]+`
Required: Yes

## Response Syntax
<a name="API_GenerateAuthRequestCryptogram_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthRequestCryptogram": "string",
   "KeyArn": "string",
   "KeyCheckValue": "string"
}
```

## Response Elements
<a name="API_GenerateAuthRequestCryptogram_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthRequestCryptogram](#API_GenerateAuthRequestCryptogram_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateAuthRequestCryptogram-response-AuthRequestCryptogram"></a>
The Authorization Request Cryptogram (ARQC) generated by AWS Payment Cryptography using the specified key and transaction data.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [KeyArn](#API_GenerateAuthRequestCryptogram_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateAuthRequestCryptogram-response-KeyArn"></a>
The `keyARN` of the IMK-AC that AWS Payment Cryptography uses for ARQC generation.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [KeyCheckValue](#API_GenerateAuthRequestCryptogram_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateAuthRequestCryptogram-response-KeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

## Errors
<a name="API_GenerateAuthRequestCryptogram_Errors"></a>

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
<a name="API_GenerateAuthRequestCryptogram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/GenerateAuthRequestCryptogram)
