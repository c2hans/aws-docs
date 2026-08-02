---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_UpdateBenefitApplication.html
---

# UpdateBenefitApplication
<a name="API_benefits_UpdateBenefitApplication"></a>

Updates an existing benefit application with new information while maintaining revision control.

## Request Syntax
<a name="API_benefits_UpdateBenefitApplication_RequestSyntax"></a>

```
{
   "BenefitApplicationDetails": {{JSON value}},
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "FileDetails": [
      {
         "BusinessUseCase": "{{string}}",
         "FileURI": "{{string}}"
      }
   ],
   "Identifier": "{{string}}",
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
   "Revision": "{{string}}"
}
```

## Request Parameters
<a name="API_benefits_UpdateBenefitApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-Catalog"></a>
The catalog identifier that specifies which benefit catalog the application belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [ClientToken](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-ClientToken"></a>
A unique, case-sensitive identifier to ensure idempotent processing of the update request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]{1,64}`
Required: Yes

 ** [Identifier](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-Identifier"></a>
The unique identifier of the benefit application to update.
Type: String
Pattern: `(arn:.+|benappl-[0-9a-z]{14})`
Required: Yes

 ** [Revision](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-Revision"></a>
The current revision number of the benefit application to ensure optimistic concurrency control.
Type: String
Required: Yes

 ** [BenefitApplicationDetails](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-BenefitApplicationDetails"></a>
Updated detailed information and requirements specific to the benefit being requested.
Type: JSON value
Required: No

 ** [Description](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-Description"></a>
The updated detailed description of the benefit application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [FileDetails](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-FileDetails"></a>
Updated supporting documents and files attached to the benefit application.
Type: Array of [FileInput](API_benefits_FileInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** [Name](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-Name"></a>
The updated human-readable name for the benefit application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [PartnerContacts](#API_benefits_UpdateBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-request-PartnerContacts"></a>
Updated contact information for partner representatives responsible for this benefit application.
Type: Array of [Contact](API_benefits_Contact.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_benefits_UpdateBenefitApplication_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Id": "string",
   "Revision": "string"
}
```

## Response Elements
<a name="API_benefits_UpdateBenefitApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_benefits_UpdateBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the updated benefit application.
Type: String

 ** [Id](#API_benefits_UpdateBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-response-Id"></a>
The unique identifier of the updated benefit application.
Type: String
Pattern: `benappl-[0-9a-z]{14}`

 ** [Revision](#API_benefits_UpdateBenefitApplication_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_UpdateBenefitApplication-response-Revision"></a>
The new revision number of the benefit application after the update.
Type: String

## Errors
<a name="API_benefits_UpdateBenefitApplication_Errors"></a>

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
<a name="API_benefits_UpdateBenefitApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/UpdateBenefitApplication)
