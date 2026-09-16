---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_GetBenefitAllocation.html
---

# GetBenefitAllocation
<a name="API_benefits_GetBenefitAllocation"></a>

Retrieves detailed information about a specific benefit allocation that has been granted to a partner.

## Request Syntax
<a name="API_benefits_GetBenefitAllocation_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_benefits_GetBenefitAllocation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_benefits_GetBenefitAllocation_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-request-Catalog"></a>
The catalog identifier that specifies which benefit catalog to query.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [Identifier](#API_benefits_GetBenefitAllocation_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-request-Identifier"></a>
The unique identifier of the benefit allocation to retrieve.
Type: String
Pattern: `(arn:.+|benalloc-[0-9a-z]{14})`
Required: Yes

## Response Syntax
<a name="API_benefits_GetBenefitAllocation_ResponseSyntax"></a>

```
{
   "ApplicableBenefitIds": [ "string" ],
   "Arn": "string",
   "BenefitApplicationId": "string",
   "BenefitId": "string",
   "Catalog": "string",
   "CreatedAt": "string",
   "Description": "string",
   "ExpiresAt": "string",
   "FulfillmentDetail": { ... },
   "FulfillmentType": "string",
   "Id": "string",
   "Name": "string",
   "StartsAt": "string",
   "Status": "string",
   "StatusReason": "string",
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_benefits_GetBenefitAllocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicableBenefitIds](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-ApplicableBenefitIds"></a>
A list of benefit identifiers that this allocation can be applied to.
Type: Array of strings
Pattern: `(arn:.+|ben-[0-9a-z]{14})`

 ** [Arn](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-Arn"></a>
The Amazon Resource Name (ARN) of the benefit allocation.
Type: String
Pattern: `(arn:.+benalloc-[0-9a-z]{14})`

 ** [BenefitApplicationId](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-BenefitApplicationId"></a>
The identifier of the benefit application that resulted in this allocation.
Type: String
Pattern: `benappl-[0-9a-z]{14}`

 ** [BenefitId](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-BenefitId"></a>
The identifier of the benefit that this allocation is based on.
Type: String
Pattern: `(arn:.+|ben-[0-9a-z]{14})`

 ** [Catalog](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-Catalog"></a>
The catalog identifier that the benefit allocation belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`

 ** [CreatedAt](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-CreatedAt"></a>
The timestamp when the benefit allocation was created.
Type: Timestamp

 ** [Description](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-Description"></a>
A detailed description of the benefit allocation.
Type: String

 ** [ExpiresAt](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-ExpiresAt"></a>
The timestamp when the benefit allocation expires and is no longer usable.
Type: Timestamp

 ** [FulfillmentDetail](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-FulfillmentDetail"></a>
Detailed information about how the benefit allocation is fulfilled.
Type: [FulfillmentDetails](API_benefits_FulfillmentDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [FulfillmentType](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-FulfillmentType"></a>
The fulfillment type used for this benefit allocation.
Type: String
Valid Values: `CREDITS | CASH | ACCESS`

 ** [Id](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-Id"></a>
The unique identifier of the benefit allocation.
Type: String
Pattern: `benalloc-[0-9a-z]{14}`

 ** [Name](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-Name"></a>
The human-readable name of the benefit allocation.
Type: String

 ** [StartsAt](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-StartsAt"></a>
The timestamp when the benefit allocation becomes active and usable.
Type: Timestamp

 ** [Status](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-Status"></a>
The current status of the benefit allocation (e.g., active, expired, consumed).
Type: String
Valid Values: `ACTIVE | INACTIVE | FULFILLED`

 ** [StatusReason](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-StatusReason"></a>
Additional information explaining the current status of the benefit allocation.
Type: String

 ** [UpdatedAt](#API_benefits_GetBenefitAllocation_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_GetBenefitAllocation-response-UpdatedAt"></a>
The timestamp when the benefit allocation was last updated.
Type: Timestamp

## Errors
<a name="API_benefits_GetBenefitAllocation_Errors"></a>

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
<a name="API_benefits_GetBenefitAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/GetBenefitAllocation)
