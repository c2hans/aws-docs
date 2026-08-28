---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPartnerAccount.html
---

# GetPartnerAccount
<a name="API_GetPartnerAccount"></a>

Gets information about a partner account. If `PartnerAccountId` and `PartnerType` are `null`, returns all partner accounts.

## Request Syntax
<a name="API_GetPartnerAccount_RequestSyntax"></a>

```
GET /partner-accounts/{{PartnerAccountId}}?partnerType={{PartnerType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPartnerAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PartnerAccountId](#API_GetPartnerAccount_RequestSyntax) **   <a name="iotwireless-GetPartnerAccount-request-uri-PartnerAccountId"></a>
The partner account ID to disassociate from the AWS account.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [PartnerType](#API_GetPartnerAccount_RequestSyntax) **   <a name="iotwireless-GetPartnerAccount-request-uri-PartnerType"></a>
The partner type.
Valid Values: `Sidewalk`
Required: Yes

## Request Body
<a name="API_GetPartnerAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPartnerAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountLinked": boolean,
   "Sidewalk": {
      "AmazonId": "string",
      "Arn": "string",
      "Fingerprint": "string"
   }
}
```

## Response Elements
<a name="API_GetPartnerAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountLinked](#API_GetPartnerAccount_ResponseSyntax) **   <a name="iotwireless-GetPartnerAccount-response-AccountLinked"></a>
Whether the partner account is linked to the AWS account.
Type: Boolean

 ** [Sidewalk](#API_GetPartnerAccount_ResponseSyntax) **   <a name="iotwireless-GetPartnerAccount-response-Sidewalk"></a>
The Sidewalk account credentials.
Type: [SidewalkAccountInfoWithFingerprint](API_SidewalkAccountInfoWithFingerprint.md) object

## Errors
<a name="API_GetPartnerAccount_Errors"></a>

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
<a name="API_GetPartnerAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetPartnerAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetPartnerAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
