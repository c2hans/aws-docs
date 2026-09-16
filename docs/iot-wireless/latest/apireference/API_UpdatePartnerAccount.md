---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdatePartnerAccount.html
---

# UpdatePartnerAccount
<a name="API_UpdatePartnerAccount"></a>

Updates properties of a partner account.

## Request Syntax
<a name="API_UpdatePartnerAccount_RequestSyntax"></a>

```
PATCH /partner-accounts/{{PartnerAccountId}}?partnerType={{PartnerType}} HTTP/1.1
Content-type: application/json

{
   "Sidewalk": {
      "AppServerPrivateKey": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdatePartnerAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PartnerAccountId](#API_UpdatePartnerAccount_RequestSyntax) **   <a name="iotwireless-UpdatePartnerAccount-request-uri-PartnerAccountId"></a>
The ID of the partner account to update.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [PartnerType](#API_UpdatePartnerAccount_RequestSyntax) **   <a name="iotwireless-UpdatePartnerAccount-request-uri-PartnerType"></a>
The partner type.
Valid Values: `Sidewalk`
Required: Yes

## Request Body
<a name="API_UpdatePartnerAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Sidewalk](#API_UpdatePartnerAccount_RequestSyntax) **   <a name="iotwireless-UpdatePartnerAccount-request-Sidewalk"></a>
The Sidewalk account credentials.
Type: [SidewalkUpdateAccount](API_SidewalkUpdateAccount.md) object
Required: Yes

## Response Syntax
<a name="API_UpdatePartnerAccount_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdatePartnerAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdatePartnerAccount_Errors"></a>

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
<a name="API_UpdatePartnerAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdatePartnerAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdatePartnerAccount)
