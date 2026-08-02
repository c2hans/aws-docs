---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_CreatePartner.html
---

# CreatePartner
<a name="API_account_CreatePartner"></a>

Creates a new partner account in the AWS Partner Network with the specified details and configuration.

## Request Syntax
<a name="API_account_CreatePartner_RequestSyntax"></a>

```
{
   "AllianceLeadContact": {
      "BusinessTitle": "{{string}}",
      "Email": "{{string}}",
      "FirstName": "{{string}}",
      "LastName": "{{string}}"
   },
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "EmailVerificationCode": "{{string}}",
   "LegalName": "{{string}}",
   "PrimarySolutionType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_account_CreatePartner_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AllianceLeadContact](#API_account_CreatePartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-request-AllianceLeadContact"></a>
The primary contact person for alliance and partnership matters.
Type: [AllianceLeadContact](API_account_AllianceLeadContact.md) object
Required: Yes

 ** [Catalog](#API_account_CreatePartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-request-Catalog"></a>
The catalog identifier where the partner account will be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [EmailVerificationCode](#API_account_CreatePartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-request-EmailVerificationCode"></a>
The verification code sent to the alliance lead contact's email to confirm account creation.
Type: String
Length Constraints: Fixed length of 6.
Pattern: `[0-9]+`
Required: Yes

 ** [LegalName](#API_account_CreatePartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-request-LegalName"></a>
The legal name of the organization becoming a partner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** [PrimarySolutionType](#API_account_CreatePartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-request-PrimarySolutionType"></a>
The primary type of solution or service the partner provides (e.g., consulting, software, managed services).
Type: String
Valid Values: `SOFTWARE_PRODUCTS | CONSULTING_SERVICES | PROFESSIONAL_SERVICES | MANAGED_SERVICES | HARDWARE_PRODUCTS | COMMUNICATION_SERVICES | VALUE_ADDED_RESALE_AWS_SERVICES | TRAINING_SERVICES`
Required: Yes

 ** [ClientToken](#API_account_CreatePartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** [Tags](#API_account_CreatePartner_RequestSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-request-Tags"></a>
A list of tags to associate with the partner account for organization and billing purposes.
Type: Array of [Tag](API_account_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_account_CreatePartner_ResponseSyntax"></a>

```
{
   "AllianceLeadContact": {
      "BusinessTitle": "string",
      "Email": "string",
      "FirstName": "string",
      "LastName": "string"
   },
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
<a name="API_account_CreatePartner_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AllianceLeadContact](#API_account_CreatePartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-response-AllianceLeadContact"></a>
The alliance lead contact information for the partner account.
Type: [AllianceLeadContact](API_account_AllianceLeadContact.md) object

 ** [Arn](#API_account_CreatePartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-response-Arn"></a>
The Amazon Resource Name (ARN) of the created partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13}`

 ** [Catalog](#API_account_CreatePartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-response-Catalog"></a>
The catalog identifier where the partner account was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [CreatedAt](#API_account_CreatePartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-response-CreatedAt"></a>
The timestamp when the partner account was created.
Type: Timestamp

 ** [Id](#API_account_CreatePartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-response-Id"></a>
The unique identifier of the created partner account.
Type: String
Pattern: `partner-[A-Za-z0-9]{13}`

 ** [LegalName](#API_account_CreatePartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-response-LegalName"></a>
The legal name of the partner organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`

 ** [Profile](#API_account_CreatePartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-response-Profile"></a>
The partner profile information including display name, description, and other public details.
Type: [PartnerProfile](API_account_PartnerProfile.md) object

 ** [AwsTrainingCertificationEmailDomains](#API_account_CreatePartner_ResponseSyntax) **   <a name="AWSPartnerCentral-account_CreatePartner-response-AwsTrainingCertificationEmailDomains"></a>
The list of verified email domains associated with AWS training and certification credentials for the partner organization.
Type: Array of [PartnerDomain](API_account_PartnerDomain.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_account_CreatePartner_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.
 ** Reason **
The specific reason for the access denial.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.
 ** Reason **
The specific reason for the conflict.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.
HTTP Status Code: 500

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
<a name="API_account_CreatePartner_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/CreatePartner)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/CreatePartner)
