---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyMac.html
---

# VerifyMac
<a name="API_VerifyMac"></a>

Verifies a Message Authentication Code (MAC).

You can use this operation to verify MAC for message data authentication such as . In this operation, you must use the same message data, secret encryption key and MAC algorithm that was used to generate MAC. You can use this operation to verify a DUPKT, CMAC, HMAC or EMV MAC by setting generation attributes and algorithm to the associated values.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [GenerateMac](API_GenerateMac.md)

## Request Syntax
<a name="API_VerifyMac_RequestSyntax"></a>

```
POST /mac/verify HTTP/1.1
Content-type: application/json

{
   "KeyIdentifier": "{{string}}",
   "Mac": "{{string}}",
   "MacLength": {{number}},
   "MessageData": "{{string}}",
   "VerificationAttributes": { ... }
}
```

## URI Request Parameters
<a name="API_VerifyMac_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_VerifyMac_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KeyIdentifier](#API_VerifyMac_RequestSyntax) **   <a name="paymentcryptographydata-VerifyMac-request-KeyIdentifier"></a>
The `keyARN` of the encryption key that AWS Payment Cryptography uses to verify MAC data.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [Mac](#API_VerifyMac_RequestSyntax) **   <a name="paymentcryptographydata-VerifyMac-request-Mac"></a>
The MAC being verified.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 128.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: Yes

 ** [MacLength](#API_VerifyMac_RequestSyntax) **   <a name="paymentcryptographydata-VerifyMac-request-MacLength"></a>
The length of the MAC.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 32.
Required: No

 ** [MessageData](#API_VerifyMac_RequestSyntax) **   <a name="paymentcryptographydata-VerifyMac-request-MessageData"></a>
The data on for which MAC is under verification. This value must be hexBinary.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 8192.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: Yes

 ** [VerificationAttributes](#API_VerifyMac_RequestSyntax) **   <a name="paymentcryptographydata-VerifyMac-request-VerificationAttributes"></a>
The attributes and data values to use for MAC verification within AWS Payment Cryptography.
Type: [MacAttributes](API_MacAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_VerifyMac_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "KeyArn": "string",
   "KeyCheckValue": "string"
}
```

## Response Elements
<a name="API_VerifyMac_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyArn](#API_VerifyMac_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyMac-response-KeyArn"></a>
The `keyARN` of the encryption key that AWS Payment Cryptography uses for MAC verification.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [KeyCheckValue](#API_VerifyMac_ResponseSyntax) **   <a name="paymentcryptographydata-VerifyMac-response-KeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

## Errors
<a name="API_VerifyMac_Errors"></a>

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
<a name="API_VerifyMac_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/VerifyMac)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/VerifyMac)
