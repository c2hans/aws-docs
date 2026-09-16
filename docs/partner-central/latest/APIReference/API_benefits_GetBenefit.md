---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_GetBenefit.html
---

# GetBenefit
<a name="API_benefits_GetBenefit"></a>

Retrieves detailed information about a specific benefit available in the partner catalog.

## Request Syntax
<a name="API_benefits_GetBenefit_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_benefits_GetBenefit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_benefits_GetBenefit_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-request-Catalog"></a>
The catalog identifier that specifies which benefit catalog to query.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [Identifier](#API_benefits_GetBenefit_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-request-Identifier"></a>
The unique identifier of the benefit to retrieve.
Type: String
Pattern: `(arn:.+|ben-[0-9a-z]{14})`
Required: Yes

## Response Syntax
<a name="API_benefits_GetBenefit_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "BenefitRequestSchema": JSON value,
   "Catalog": "string",
   "Description": "string",
   "FulfillmentTypes": [ "string" ],
   "Id": "string",
   "Name": "string",
   "Programs": [ "string" ],
   "Status": "string"
}
```

## Response Elements
<a name="API_benefits_GetBenefit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-Arn"></a>
The Amazon Resource Name (ARN) of the benefit.
Type: String

 ** [BenefitRequestSchema](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-BenefitRequestSchema"></a>
The schema definition that describes the required fields for requesting this benefit.
Type: JSON value

 ** [Catalog](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-Catalog"></a>
The catalog identifier that the benefit belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`

 ** [Description](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-Description"></a>
A detailed description of the benefit and its purpose.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [FulfillmentTypes](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-FulfillmentTypes"></a>
The available fulfillment types for this benefit (e.g., credits, access, disbursement).
Type: Array of strings
Valid Values: `CREDITS | CASH | ACCESS`

 ** [Id](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-Id"></a>
The unique identifier of the benefit.
Type: String
Pattern: `ben-[0-9a-z]{14}`

 ** [Name](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-Name"></a>
The human-readable name of the benefit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [Programs](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-Programs"></a>
The AWS partner programs that this benefit is associated with.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9_-]+`

 ** [Status](#API_benefits_GetBenefit_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefit-response-Status"></a>
The current status of the benefit (e.g., active, inactive, deprecated).
Type: String
Valid Values: `ACTIVE | INACTIVE`

## Errors
<a name="API_benefits_GetBenefit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Thrown when the caller does not have sufficient permissions to perform the requested operation.
 ** Message **
A message describing the access denial.
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
<a name="API_benefits_GetBenefit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/GetBenefit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/GetBenefit)
