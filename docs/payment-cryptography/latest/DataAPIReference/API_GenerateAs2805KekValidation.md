---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateAs2805KekValidation.html
---

# GenerateAs2805KekValidation
<a name="API_GenerateAs2805KekValidation"></a>

Generates a `KekValidationRequest` or a `KekValidationResponse` for node-to-node initialization between payment processing nodes using [Australian Standard 2805 (AS2805)](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.html).

During node-to-node initialization, both communicating nodes must validate that they possess the correct Key Encrypting Keys (KEKs) before proceeding with session key exchange. In AS2805, the sending KEK (KEKs) of one node corresponds to the receiving KEK (KEKr) of its partner node. Each node uses its KEK to encrypt and decrypt session keys exchanged between the nodes. A KEK can be created or imported into AWS Payment Cryptography using either the [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) or [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) operations.

To use `GenerateAs2805KekValidation` to generate a KEK validation request, set `KekValidationType` to `KekValidationRequest`. This operation returns both `RandomKeySend` (KRs) and `RandomKeyReceive` (KRr) as response values. The partnering node receives the KRs, uses its KEKr to decrypt it, and generates a KRr which is an inverted value of KRs. The node receiving the KRr validates it against its own KRr generated during KEK validation request outside of AWS Payment Cryptography.

You can also use this operation to generate a KEK validation response, by setting `KekValidationType` to `KekValidationResponse` and providing the incoming KRs. This operation then calculates a KRr. To learn more about more about node-to-node initialization, see [Validation of KEK](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.kekvalidation.html) in the * AWS Payment Cryptography User Guide*.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

## Request Syntax
<a name="API_GenerateAs2805KekValidation_RequestSyntax"></a>

```
POST /as2805kekvalidation/generate HTTP/1.1
Content-type: application/json

{
   "KekValidationType": { ... },
   "KeyIdentifier": "{{string}}",
   "RandomKeySendVariantMask": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GenerateAs2805KekValidation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GenerateAs2805KekValidation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KekValidationType](#API_GenerateAs2805KekValidation_RequestSyntax) **   <a name="paymentcryptographydata-GenerateAs2805KekValidation-request-KekValidationType"></a>
Defines whether to generate a KEK validation request or KEK validation response for node-to-node initialization.
Type: [As2805KekValidationType](API_As2805KekValidationType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [KeyIdentifier](#API_GenerateAs2805KekValidation_RequestSyntax) **   <a name="paymentcryptographydata-GenerateAs2805KekValidation-request-KeyIdentifier"></a>
The `keyARN` of sending KEK that AWS Payment Cryptography uses for node-to-node initialization
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [RandomKeySendVariantMask](#API_GenerateAs2805KekValidation_RequestSyntax) **   <a name="paymentcryptographydata-GenerateAs2805KekValidation-request-RandomKeySendVariantMask"></a>
The key variant to use for generating a random key for KEK validation during node-to-node initialization.
Type: String
Valid Values: `VARIANT_MASK_82C0 | VARIANT_MASK_82`
Required: Yes

## Response Syntax
<a name="API_GenerateAs2805KekValidation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "KeyArn": "string",
   "KeyCheckValue": "string",
   "RandomKeyReceive": "string",
   "RandomKeySend": "string"
}
```

## Response Elements
<a name="API_GenerateAs2805KekValidation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyArn](#API_GenerateAs2805KekValidation_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateAs2805KekValidation-response-KeyArn"></a>
The `keyARN` of sending KEK that AWS Payment Cryptography validates for node-to-node initialization
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [KeyCheckValue](#API_GenerateAs2805KekValidation_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateAs2805KekValidation-response-KeyCheckValue"></a>
The key check value (KCV) of the sending KEK that AWS Payment Cryptography validates for node-to-node initialization.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [RandomKeyReceive](#API_GenerateAs2805KekValidation_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateAs2805KekValidation-response-RandomKeyReceive"></a>
The random key generated for receiving KEK validation. The initiating node sends this key to its partner node for validation.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 48.
Pattern: `(?:[0-9a-fA-F]{16}|[0-9a-fA-F]{32}|[0-9a-fA-F]{48})`

 ** [RandomKeySend](#API_GenerateAs2805KekValidation_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateAs2805KekValidation-response-RandomKeySend"></a>
The random key generated for sending KEK validation.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 48.
Pattern: `(?:[0-9a-fA-F]{16}|[0-9a-fA-F]{32}|[0-9a-fA-F]{48})`

## Errors
<a name="API_GenerateAs2805KekValidation_Errors"></a>

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
<a name="API_GenerateAs2805KekValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/GenerateAs2805KekValidation)
