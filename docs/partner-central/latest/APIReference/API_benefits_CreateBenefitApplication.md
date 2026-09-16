---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_CreateBenefitApplication.html
---

# CreateBenefitApplication
<a name="API_benefits_CreateBenefitApplication"></a>

Creates a new benefit application for a partner to request access to AWS benefits and programs.

## Request Syntax
<a name="API_benefits_CreateBenefitApplication_RequestSyntax"></a>

```
{
   "AssociatedResources": [ "{{string}}" ],
   "BenefitApplicationDetails": {{JSON value}},
   "BenefitIdentifier": "{{string}}",
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "FileDetails": [
      {
         "BusinessUseCase": "{{string}}",
         "FileURI": "{{string}}"
      }
   ],
   "FulfillmentTypes": [ "{{string}}" ],
   "Name": "{{string}}",
   "PartnerContacts": [
      {
         "BusinessTitle": "{{string}}",
         "Email": "{{string}}",
         "FirstName": "{{string}}",
         "LastName": "{{string}}",
         "Phone": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_benefits_CreateBenefitApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BenefitIdentifier](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-BenefitIdentifier"></a>
The unique identifier of the benefit being requested in this application.
Type: String
Pattern: `(arn:.+|ben-[0-9a-z]{14})`
Required: Yes

 ** [Catalog](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-Catalog"></a>
The catalog identifier that specifies which benefit catalog to create the application in.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [ClientToken](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-ClientToken"></a>
A unique, case-sensitive identifier to ensure idempotent processing of the creation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]{1,64}`
Required: Yes

 ** [AssociatedResources](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-AssociatedResources"></a>
AWS resources that are associated with this benefit application.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Pattern: `arn:aws:([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.+)`
Required: No

 ** [BenefitApplicationDetails](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-BenefitApplicationDetails"></a>
Detailed information and requirements specific to the benefit being requested. To retrieve the detailed specifications for any benefit, make a `GetBenefit` API call using the benefit identifier.
Type: JSON value
Required: No

 ** [Description](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-Description"></a>
A detailed description of the benefit application and its intended use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [FileDetails](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-FileDetails"></a>
Supporting documents and files attached to the benefit application.
Type: Array of [FileInput](API_benefits_FileInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** [FulfillmentTypes](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-FulfillmentTypes"></a>
The types of fulfillment requested for this benefit application (e.g., credits, access, disbursement).
Type: Array of strings
Valid Values: `CREDITS | CASH | ACCESS`
Required: No

 ** [Name](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-Name"></a>
A human-readable name for the benefit application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [PartnerContacts](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-PartnerContacts"></a>
Contact information for partner representatives responsible for this benefit application.
Type: Array of [Contact](API_benefits_Contact.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [Tags](#API_benefits_CreateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-request-Tags"></a>
Key-value pairs to categorize and organize the benefit application.
Type: Array of [Tag](API_benefits_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_benefits_CreateBenefitApplication_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Id": "string",
   "Revision": "string"
}
```

## Response Elements
<a name="API_benefits_CreateBenefitApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_benefits_CreateBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the newly created benefit application.
Type: String

 ** [Id](#API_benefits_CreateBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-response-Id"></a>
The unique identifier assigned to the newly created benefit application.
Type: String
Pattern: `benappl-[0-9a-z]{14}`

 ** [Revision](#API_benefits_CreateBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_CreateBenefitApplication-response-Revision"></a>
The initial revision number of the newly created benefit application.
Type: String

## Errors
<a name="API_benefits_CreateBenefitApplication_Errors"></a>

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
<a name="API_benefits_CreateBenefitApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/CreateBenefitApplication)
