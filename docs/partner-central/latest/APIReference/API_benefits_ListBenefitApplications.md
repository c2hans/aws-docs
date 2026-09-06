---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_ListBenefitApplications.html
---

# ListBenefitApplications
<a name="API_benefits_ListBenefitApplications"></a>

Retrieves a paginated list of benefit applications based on specified filter criteria.

## Request Syntax
<a name="API_benefits_ListBenefitApplications_RequestSyntax"></a>

```
{
   "AssociatedResourceArns": [ "{{string}}" ],
   "AssociatedResources": [
      {
         "ResourceArn": "{{string}}",
         "ResourceIdentifier": "{{string}}",
         "ResourceType": "{{string}}"
      }
   ],
   "BenefitIdentifiers": [ "{{string}}" ],
   "Catalog": "{{string}}",
   "FulfillmentTypes": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Programs": [ "{{string}}" ],
   "Stages": [ "{{string}}" ],
   "Status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_benefits_ListBenefitApplications_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-Catalog"></a>
The catalog identifier to filter benefit applications by catalog.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [AssociatedResourceArns](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-AssociatedResourceArns"></a>
Filter benefit applications by specific AWS resource ARNs.
Type: Array of strings
Pattern: `arn:aws:([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.+)`
Required: No

 ** [AssociatedResources](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-AssociatedResources"></a>
 *This parameter has been deprecated.*
Filter benefit applications by associated AWS resources.
Type: Array of [AssociatedResource](API_benefits_AssociatedResource.md) objects
Required: No

 ** [BenefitIdentifiers](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-BenefitIdentifiers"></a>
Filter benefit applications by specific benefit identifiers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Pattern: `(arn:.+|ben-[0-9a-z]{14})`
Required: No

 ** [FulfillmentTypes](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-FulfillmentTypes"></a>
Filter benefit applications by specific fulfillment types.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `CREDITS | CASH | ACCESS`
Required: No

 ** [MaxResults](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-MaxResults"></a>
The maximum number of benefit applications to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-NextToken"></a>
A pagination token to retrieve the next set of results from a previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** [Programs](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-Programs"></a>
Filter benefit applications by specific AWS partner programs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** [Stages](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-Stages"></a>
Filter benefit applications by their current processing stage.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [Status](#API_benefits_ListBenefitApplications_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-request-Status"></a>
Filter benefit applications by their current processing status.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `PENDING_SUBMISSION | IN_REVIEW | ACTION_REQUIRED | APPROVED | REJECTED | CANCELED`
Required: No

## Response Syntax
<a name="API_benefits_ListBenefitApplications_ResponseSyntax"></a>

```
{
   "BenefitApplicationSummaries": [
      {
         "Arn": "string",
         "AssociatedResources": [ "string" ],
         "BenefitApplicationDetails": {
            "string" : "string"
         },
         "BenefitId": "string",
         "Catalog": "string",
         "CreatedAt": "string",
         "FulfillmentTypes": [ "string" ],
         "Id": "string",
         "Name": "string",
         "Programs": [ "string" ],
         "Stage": "string",
         "Status": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_benefits_ListBenefitApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BenefitApplicationSummaries](#API_benefits_ListBenefitApplications_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-response-BenefitApplicationSummaries"></a>
A list of benefit application summaries matching the specified criteria.
Type: Array of [BenefitApplicationSummary](API_benefits_BenefitApplicationSummary.md) objects

 ** [NextToken](#API_benefits_ListBenefitApplications_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefitApplications-response-NextToken"></a>
A pagination token to retrieve the next set of results, if more results are available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_benefits_ListBenefitApplications_Errors"></a>

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
<a name="API_benefits_ListBenefitApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/ListBenefitApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/ListBenefitApplications)
