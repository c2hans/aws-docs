---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateAwsAccountFromPartnerAccount.html
---

# DisassociateAwsAccountFromPartnerAccount
<a name="API_DisassociateAwsAccountFromPartnerAccount"></a>

Disassociates your AWS account from a partner account. If `PartnerAccountId` and `PartnerType` are `null`, disassociates your AWS account from all partner accounts.

## Request Syntax
<a name="API_DisassociateAwsAccountFromPartnerAccount_RequestSyntax"></a>

```
DELETE /partner-accounts/{{PartnerAccountId}}?partnerType={{PartnerType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateAwsAccountFromPartnerAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PartnerAccountId](#API_DisassociateAwsAccountFromPartnerAccount_RequestSyntax) **   <a name="iotwireless-DisassociateAwsAccountFromPartnerAccount-request-uri-PartnerAccountId"></a>
The partner account ID to disassociate from the AWS account.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [PartnerType](#API_DisassociateAwsAccountFromPartnerAccount_RequestSyntax) **   <a name="iotwireless-DisassociateAwsAccountFromPartnerAccount-request-uri-PartnerType"></a>
The partner type.
Valid Values: `Sidewalk`
Required: Yes

## Request Body
<a name="API_DisassociateAwsAccountFromPartnerAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateAwsAccountFromPartnerAccount_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DisassociateAwsAccountFromPartnerAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DisassociateAwsAccountFromPartnerAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateAwsAccountFromPartnerAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/DisassociateAwsAccountFromPartnerAccount)
