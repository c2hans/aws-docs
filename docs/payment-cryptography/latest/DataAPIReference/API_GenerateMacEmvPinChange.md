---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateMacEmvPinChange.html
---

# GenerateMacEmvPinChange
<a name="API_GenerateMacEmvPinChange"></a>

Generates an issuer script mac for EMV payment cards that use offline PINs as the cardholder verification method (CVM).

This operation generates an authenticated issuer script response by appending the incoming message data (APDU command) with the target encrypted PIN block in ISO2 format. The command structure and method to send the issuer script update to the card is not defined by this operation and is typically determined by the applicable payment card scheme.

The primary inputs to this operation include the incoming new encrypted pinblock, PIN encryption key (PEK), issuer master key (IMK), primary account number (PAN), and the payment card derivation method.

The operation uses two issuer master keys - secure messaging for confidentiality (IMK-SMC) and secure messaging for integrity (IMK-SMI). The SMC key is used to internally derive a key to secure the pin, while SMI key is used to internally derive a key to authenticate the script reponse as per the [EMV 4.4 - Book 2 - Security and Key Management](https://www.emvco.com/specifications/) specification.

This operation supports Amex, EMV2000, EMVCommon, Mastercard and Visa derivation methods, each requiring specific input parameters. Users must follow the specific derivation method and input parameters defined by the respective payment card scheme.

**Note**
Use [GenerateMac](API_GenerateMac.md) operation when sending a script update to an EMV card that does not involve PIN change. When assigning IAM permissions, it is important to understand that [EncryptData](API_EncryptData.md) using EMV keys and [GenerateMac](API_GenerateMac.md) perform similar functions to this command.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [EncryptData](API_EncryptData.md)
+  [GenerateMac](API_GenerateMac.md)

## Request Syntax
<a name="API_GenerateMacEmvPinChange_RequestSyntax"></a>

```
POST /macemvpinchange/generate HTTP/1.1
Content-type: application/json

{
   "DerivationMethodAttributes": { ... },
   "MessageData": "{{string}}",
   "NewEncryptedPinBlock": "{{string}}",
   "NewPinPekIdentifier": "{{string}}",
   "PinBlockFormat": "{{string}}",
   "SecureMessagingConfidentialityKeyIdentifier": "{{string}}",
   "SecureMessagingIntegrityKeyIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GenerateMacEmvPinChange_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GenerateMacEmvPinChange_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DerivationMethodAttributes](#API_GenerateMacEmvPinChange_RequestSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-request-DerivationMethodAttributes"></a>
The attributes and data values to derive payment card specific confidentiality and integrity keys.
Type: [DerivationMethodAttributes](API_DerivationMethodAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [MessageData](#API_GenerateMacEmvPinChange_RequestSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-request-MessageData"></a>
The message data is the APDU command from the card reader or terminal. The target encrypted PIN block, after translation to ISO2 format, is appended to this message data to generate an issuer script response.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1024.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: Yes

 ** [NewEncryptedPinBlock](#API_GenerateMacEmvPinChange_RequestSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-request-NewEncryptedPinBlock"></a>
The incoming new encrypted PIN block data for offline pin change on an EMV card.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** [NewPinPekIdentifier](#API_GenerateMacEmvPinChange_RequestSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-request-NewPinPekIdentifier"></a>
The `keyARN` of the PEK protecting the incoming new encrypted PIN block.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [PinBlockFormat](#API_GenerateMacEmvPinChange_RequestSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-request-PinBlockFormat"></a>
The PIN encoding format of the incoming new encrypted PIN block as specified in ISO 9564.
Type: String
Valid Values: `ISO_FORMAT_0 | ISO_FORMAT_1 | ISO_FORMAT_3`
Required: Yes

 ** [SecureMessagingConfidentialityKeyIdentifier](#API_GenerateMacEmvPinChange_RequestSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-request-SecureMessagingConfidentialityKeyIdentifier"></a>
The `keyARN` of the issuer master key (IMK-SMC) used to protect the PIN block data in the issuer script response.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [SecureMessagingIntegrityKeyIdentifier](#API_GenerateMacEmvPinChange_RequestSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-request-SecureMessagingIntegrityKeyIdentifier"></a>
The `keyARN` of the issuer master key (IMK-SMI) used to authenticate the issuer script response.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## Response Syntax
<a name="API_GenerateMacEmvPinChange_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EncryptedPinBlock": "string",
   "Mac": "string",
   "NewPinPekArn": "string",
   "NewPinPekKeyCheckValue": "string",
   "SecureMessagingConfidentialityKeyArn": "string",
   "SecureMessagingConfidentialityKeyCheckValue": "string",
   "SecureMessagingIntegrityKeyArn": "string",
   "SecureMessagingIntegrityKeyCheckValue": "string",
   "VisaAmexDerivationOutputs": {
      "AuthorizationRequestKeyArn": "string",
      "AuthorizationRequestKeyCheckValue": "string",
      "CurrentPinPekArn": "string",
      "CurrentPinPekKeyCheckValue": "string"
   }
}
```

## Response Elements
<a name="API_GenerateMacEmvPinChange_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncryptedPinBlock](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-EncryptedPinBlock"></a>
Returns the incoming new encrpted PIN block.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `[0-9a-fA-F]+`

 ** [Mac](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-Mac"></a>
Returns the mac of the issuer script containing message data and appended target encrypted pin block in ISO2 format.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [NewPinPekArn](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-NewPinPekArn"></a>
Returns the `keyArn` of the PEK protecting the incoming new encrypted PIN block.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [NewPinPekKeyCheckValue](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-NewPinPekKeyCheckValue"></a>
The key check value (KCV) of the PEK uprotecting the incoming new encrypted PIN block.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [SecureMessagingConfidentialityKeyArn](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-SecureMessagingConfidentialityKeyArn"></a>
Returns the `keyArn` of the IMK-SMC used by the operation.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [SecureMessagingConfidentialityKeyCheckValue](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-SecureMessagingConfidentialityKeyCheckValue"></a>
The key check value (KCV) of the SMC issuer master key used by the operation.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [SecureMessagingIntegrityKeyArn](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-SecureMessagingIntegrityKeyArn"></a>
Returns the `keyArn` of the IMK-SMI used by the operation.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [SecureMessagingIntegrityKeyCheckValue](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-SecureMessagingIntegrityKeyCheckValue"></a>
The key check value (KCV) of the SMI issuer master key used by the operation.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

 ** [VisaAmexDerivationOutputs](#API_GenerateMacEmvPinChange_ResponseSyntax) **   <a name="paymentcryptographydata-GenerateMacEmvPinChange-response-VisaAmexDerivationOutputs"></a>
The attribute values used for Amex and Visa derivation methods.
Type: [VisaAmexDerivationOutputs](API_VisaAmexDerivationOutputs.md) object

## Errors
<a name="API_GenerateMacEmvPinChange_Errors"></a>

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
<a name="API_GenerateMacEmvPinChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
