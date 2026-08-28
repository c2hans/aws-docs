---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetPartner.html
---

# GetPartner
<a name="API_account_GetPartner"></a>

Retrieves detailed information about a specific partner account.

## Request Syntax
<a name="API_account_GetPartner_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_account_GetPartner_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_account_GetPartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-request-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Identifier](#API_account_GetPartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-request-Identifier"></a>
The unique identifier of the partner account to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(partner-[A-Za-z0-9]{13}|arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13})`
Required: Yes

## Response Syntax
<a name="API_account_GetPartner_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "AwsTrainingCertificationEmailDomains": [
      {
         "DomainName": "string",
         "RegisteredAt": "string"
      }
   ],
   "Catalog": "string",
   "CreatedAt": "string",
   "Id": "string",
   "LegalName": "string",
   "Profile": {
      "Description": "string",
      "DisplayName": "string",
      "Headquarters": {
         "CountryCode": "string",
         "SubdivisionCode": "string"
      },
      "IndustrySegments": [ "string" ],
      "LocalizedContents": [
         {
            "Description": "string",
            "DisplayName": "string",
            "Locale": "string",
            "LogoUrl": "string",
            "WebsiteUrl": "string"
         }
      ],
      "LogoUrl": "string",
      "PrimarySolutionType": "string",
      "ProfileId": "string",
      "TranslationSourceLocale": "string",
      "WebsiteUrl": "string"
   }
}
```

## Response Elements
<a name="API_account_GetPartner_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_account_GetPartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-response-Arn"></a>
The Amazon Resource Name (ARN) of the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13}`

 ** [Catalog](#API_account_GetPartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-response-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [CreatedAt](#API_account_GetPartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-response-CreatedAt"></a>
The timestamp when the partner account was created.
Type: Timestamp

 ** [Id](#API_account_GetPartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-response-Id"></a>
The unique identifier of the partner account.
Type: String
Pattern: `partner-[A-Za-z0-9]{13}`

 ** [LegalName](#API_account_GetPartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-response-LegalName"></a>
The legal name of the partner organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`

 ** [Profile](#API_account_GetPartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-response-Profile"></a>
The partner profile information including display name, description, and other public details.
Type: [PartnerProfile](API_account_PartnerProfile.md) object

 ** [AwsTrainingCertificationEmailDomains](#API_account_GetPartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetPartner-response-AwsTrainingCertificationEmailDomains"></a>
The list of verified email domains associated with AWS training and certification credentials for the partner organization.
Type: Array of [PartnerDomain](API_account_PartnerDomain.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_account_GetPartner_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.
 ** Reason **
The specific reason for the access denial.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.
 ** Reason **
The specific reason why the resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.
 ** QuotaCode **
The quota code associated with the throttling error.
 ** ServiceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.
 ** ErrorDetails **
A list of detailed validation errors that occurred during request processing.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_account_GetPartner_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/GetPartner)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/GetPartner)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
