---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_GetBenefitApplication.html
---

# GetBenefitApplication
<a name="API_benefits_GetBenefitApplication"></a>

Retrieves detailed information about a specific benefit application.

## Request Syntax
<a name="API_benefits_GetBenefitApplication_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_benefits_GetBenefitApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_benefits_GetBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-request-Catalog"></a>
The catalog identifier that specifies which benefit catalog to query.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [Identifier](#API_benefits_GetBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-request-Identifier"></a>
The unique identifier of the benefit application to retrieve.
Type: String
Pattern: `(arn:.+|benappl-[0-9a-z]{14})`
Required: Yes

## Response Syntax
<a name="API_benefits_GetBenefitApplication_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "AssociatedResources": [ "string" ],
   "BenefitApplicationDetails": JSON value,
   "BenefitId": "string",
   "Catalog": "string",
   "CreatedAt": "string",
   "Description": "string",
   "FileDetails": [
      {
         "BusinessUseCase": "string",
         "CreatedAt": "string",
         "CreatedBy": "string",
         "FileName": "string",
         "FileStatus": "string",
         "FileStatusReason": "string",
         "FileType": "string",
         "FileURI": "string"
      }
   ],
   "FulfillmentTypes": [ "string" ],
   "Id": "string",
   "Name": "string",
   "PartnerContacts": [
      {
         "BusinessTitle": "string",
         "Email": "string",
         "FirstName": "string",
         "LastName": "string",
         "Phone": "string"
      }
   ],
   "Programs": [ "string" ],
   "Revision": "string",
   "Stage": "string",
   "Status": "string",
   "StatusReason": "string",
   "StatusReasonCode": "string",
   "StatusReasonCodes": [ "string" ],
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_benefits_GetBenefitApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the benefit application.
Type: String
Pattern: `arn:aws:([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.+)`

 ** [AssociatedResources](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-AssociatedResources"></a>
AWS resources that are associated with this benefit application.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Pattern: `arn:aws:([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.+)`

 ** [BenefitApplicationDetails](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-BenefitApplicationDetails"></a>
Detailed information and requirements specific to the benefit being requested.
Type: JSON value

 ** [BenefitId](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-BenefitId"></a>
The identifier of the benefit being requested in this application.
Type: String
Pattern: `(arn:.+|ben-[0-9a-z]{14})`

 ** [Catalog](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Catalog"></a>
The catalog identifier that the benefit application belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`

 ** [CreatedAt](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-CreatedAt"></a>
The timestamp when the benefit application was created.
Type: Timestamp

 ** [Description](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Description"></a>
A detailed description of the benefit application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [FileDetails](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-FileDetails"></a>
Supporting documents and files attached to the benefit application.
Type: Array of [FileDetail](API_benefits_FileDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.

 ** [FulfillmentTypes](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-FulfillmentTypes"></a>
The fulfillment types requested for this benefit application.
Type: Array of strings
Valid Values: `CREDITS | CASH | ACCESS`

 ** [Id](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Id"></a>
The unique identifier of the benefit application.
Type: String
Pattern: `benappl-[0-9a-z]{14}`

 ** [Name](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Name"></a>
The human-readable name of the benefit application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [PartnerContacts](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-PartnerContacts"></a>
Contact information for partner representatives responsible for this benefit application.
Type: Array of [Contact](API_benefits_Contact.md) objects

 ** [Programs](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Programs"></a>
The AWS partner programs associated with this benefit application.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9_-]+`

 ** [Revision](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Revision"></a>
The current revision number of the benefit application.
Type: String

 ** [Stage](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Stage"></a>
The current stage in the benefit application processing workflow.
Type: String

 ** [Status](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-Status"></a>
The current processing status of the benefit application.
Type: String
Valid Values: `PENDING_SUBMISSION | IN_REVIEW | ACTION_REQUIRED | APPROVED | REJECTED | CANCELED`

 ** [StatusReason](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-StatusReason"></a>
Additional information explaining the current status of the benefit application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [StatusReasonCode](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-StatusReasonCode"></a>
 *This parameter has been deprecated.*
A standardized code representing the reason for the current status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [StatusReasonCodes](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-StatusReasonCodes"></a>
The list of standardized codes representing the reason for the current status.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [UpdatedAt](#API_benefits_GetBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitApplication-response-UpdatedAt"></a>
The timestamp when the benefit application was last updated.
Type: Timestamp

## Errors
<a name="API_benefits_GetBenefitApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Thrown when the caller does not have sufficient permissions to perform the requested operation.
 ** Message **
A message describing the access denial.
HTTP Status Code: 400

 ** ConflictException **
Thrown when the request conflicts with the current state of the resource, such as attempting to modify a resource that has been changed by another process.
 ** Message **
A message describing the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an unexpected error occurs on the server side during request processing.
 ** Message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when the requested resource cannot be found or does not exist.
 ** Message **
A message describing the resource not found error.
HTTP Status Code: 400

 ** ThrottlingException **
Thrown when the request rate exceeds the allowed limits and the request is being throttled.
 ** Message **
A message describing the throttling error.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the request contains invalid parameters or fails input validation requirements.
 ** FieldList **
A list of fields that failed validation.
 ** Message **
A message describing the validation error.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_benefits_GetBenefitApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/GetBenefitApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/GetBenefitApplication)
