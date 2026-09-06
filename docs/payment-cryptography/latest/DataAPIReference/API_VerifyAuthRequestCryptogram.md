---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyAuthRequestCryptogram.html
---

# VerifyAuthRequestCryptogram
<a name="API_VerifyAuthRequestCryptogram"></a>

Verifies Authorization Request Cryptogram (ARQC) for a EMV chip payment card authorization. For more information, see [Verify auth request cryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.verifyauthrequestcryptogram.html) in the * AWS Payment Cryptography User Guide*.

ARQC generation is done outside of AWS Payment Cryptography and is typically generated on a point of sale terminal for an EMV chip card to obtain payment authorization during transaction time. For ARQC verification, you must first import the ARQC generated outside of AWS Payment Cryptography by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html). This operation uses the imported ARQC and an major encryption key (DUKPT) created by calling [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) to either provide a boolean ARQC verification result or provide an APRC (Authorization Response Cryptogram) response using Method 1 or Method 2. The `ARPC_METHOD_1` uses `AuthResponseCode` to generate ARPC and `ARPC_METHOD_2` uses `CardStatusUpdate` to generate ARPC.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [VerifyCardValidationData](API_VerifyCardValidationData.md)
+  [VerifyPinData](API_VerifyPinData.md)

## Request Syntax
<a name="API_VerifyAuthRequestCryptogram_RequestSyntax"></a>

```
POST /cryptogram/verify HTTP/1.1
Content-type: application/json

{
   "AuthRequestCryptogram": "{{string}}",
   "AuthResponseAttributes": { ... },
   "KeyIdentifier": "{{string}}",
   "MajorKeyDerivationMode": "{{string}}",
   "SessionKeyDerivationAttributes": { ... },
   "TransactionData": "{{string}}"
}
```

## URI Request Parameters
<a name="API_VerifyAuthRequestCryptogram_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_VerifyAuthRequestCryptogram_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuthRequestCryptogram](#API_VerifyAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-request-AuthRequestCryptogram"></a>
The auth request cryptogram imported into AWS Payment Cryptography for ARQC verification using a major encryption key and transaction data.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** [AuthResponseAttributes](#API_VerifyAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-request-AuthResponseAttributes"></a>
The attributes and values for auth request cryptogram verification. These parameters are required in case using ARPC Method 1 or Method 2 for ARQC verification.
Type: [CryptogramAuthResponse](API_CryptogramAuthResponse.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [KeyIdentifier](#API_VerifyAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-request-KeyIdentifier"></a>
The `keyARN` of the major encryption key that AWS Payment Cryptography uses for ARQC verification.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [MajorKeyDerivationMode](#API_VerifyAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-request-MajorKeyDerivationMode"></a>
The method to use when deriving the major encryption key for ARQC verification within AWS Payment Cryptography. The same key derivation mode was used for ARQC generation outside of AWS Payment Cryptography.
Type: String
Valid Values: `EMV_OPTION_A | EMV_OPTION_B`
Required: Yes

 ** [SessionKeyDerivationAttributes](#API_VerifyAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-request-SessionKeyDerivationAttributes"></a>
The attributes and values to use for deriving a session key for ARQC verification within AWS Payment Cryptography. The same attributes were used for ARQC generation outside of AWS Payment Cryptography.
Type: [SessionKeyDerivation](API_SessionKeyDerivation.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [TransactionData](#API_VerifyAuthRequestCryptogram_RequestSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-request-TransactionData"></a>
The transaction data that AWS Payment Cryptography uses for ARQC verification. The same transaction is used for ARQC generation outside of AWS Payment Cryptography.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 1024.
Pattern: `[0-9a-fA-F]+`
Required: Yes

## Response Syntax
<a name="API_VerifyAuthRequestCryptogram_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthResponseValue": "string",
   "KeyArn": "string",
   "KeyCheckValue": "string"
}
```

## Response Elements
<a name="API_VerifyAuthRequestCryptogram_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthResponseValue](#API_VerifyAuthRequestCryptogram_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-response-AuthResponseValue"></a>
The result for ARQC verification or ARPC generation within AWS Payment Cryptography.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [KeyArn](#API_VerifyAuthRequestCryptogram_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-response-KeyArn"></a>
The `keyARN` of the major encryption key that AWS Payment Cryptography uses for ARQC verification.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [KeyCheckValue](#API_VerifyAuthRequestCryptogram_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyAuthRequestCryptogram-response-KeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

## Errors
<a name="API_VerifyAuthRequestCryptogram_Errors"></a>

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
<a name="API_VerifyAuthRequestCryptogram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)
