---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyCardValidationData.html
---

# VerifyCardValidationData
<a name="API_VerifyCardValidationData"></a>

Verifies card-related validation data using algorithms such as Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2) and Card Security Codes (CSC). For more information, see [Verify card data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-card-data.html) in the * AWS Payment Cryptography User Guide*.

This operation validates the CVV or CSC codes that is printed on a payment credit or debit card during card payment transaction. The input values are typically provided as part of an inbound transaction to an issuer or supporting platform partner. AWS Payment Cryptography uses CVV or CSC, PAN (Primary Account Number) and expiration date of the card to check its validity during transaction processing. In this operation, the CVK (Card Verification Key) encryption key for use with card data verification is same as the one in used for [GenerateCardValidationData](API_GenerateCardValidationData.md).

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [GenerateCardValidationData](API_GenerateCardValidationData.md)
+  [VerifyAuthRequestCryptogram](API_VerifyAuthRequestCryptogram.md)
+  [VerifyPinData](API_VerifyPinData.md)

## Request Syntax
<a name="API_VerifyCardValidationData_RequestSyntax"></a>

```
POST /cardvalidationdata/verify HTTP/1.1
Content-type: application/json

{
   "KeyIdentifier": "{{string}}",
   "PrimaryAccountNumber": "{{string}}",
   "ValidationData": "{{string}}",
   "VerificationAttributes": { ... }
}
```

## URI Request Parameters
<a name="API_VerifyCardValidationData_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_VerifyCardValidationData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KeyIdentifier](#API_VerifyCardValidationData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyCardValidationData-request-KeyIdentifier"></a>
The `keyARN` of the CVK encryption key that AWS Payment Cryptography uses to verify card data.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [PrimaryAccountNumber](#API_VerifyCardValidationData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyCardValidationData-request-PrimaryAccountNumber"></a>
The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

 ** [ValidationData](#API_VerifyCardValidationData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyCardValidationData-request-ValidationData"></a>
The CVV or CSC value for use for card data verification within AWS Payment Cryptography.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 5.
Pattern: `[0-9]+`
Required: Yes

 ** [VerificationAttributes](#API_VerifyCardValidationData_RequestSyntax) **   <a name="paymentcryptographydata-VerifyCardValidationData-request-VerificationAttributes"></a>
The algorithm to use for verification of card data within AWS Payment Cryptography.
Type: [CardVerificationAttributes](API_CardVerificationAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_VerifyCardValidationData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "KeyArn": "string",
   "KeyCheckValue": "string"
}
```

## Response Elements
<a name="API_VerifyCardValidationData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyArn](#API_VerifyCardValidationData_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyCardValidationData-response-KeyArn"></a>
The `keyARN` of the CVK encryption key that AWS Payment Cryptography uses to verify CVV or CSC.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [KeyCheckValue](#API_VerifyCardValidationData_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyCardValidationData-response-KeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

## Errors
<a name="API_VerifyCardValidationData_Errors"></a>

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
<a name="API_VerifyCardValidationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/VerifyCardValidationData)
