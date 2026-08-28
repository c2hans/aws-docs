---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_ListBenefits.html
---

# ListBenefits
<a name="API_benefits_ListBenefits"></a>

Retrieves a paginated list of available benefits based on specified filter criteria.

## Request Syntax
<a name="API_benefits_ListBenefits_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "FulfillmentTypes": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Programs": [ "{{string}}" ],
   "Status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_benefits_ListBenefits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_benefits_ListBenefits_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefits-request-Catalog"></a>
The catalog identifier to filter benefits by catalog.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [FulfillmentTypes](#API_benefits_ListBenefits_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefits-request-FulfillmentTypes"></a>
Filter benefits by specific fulfillment types.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `CREDITS | CASH | ACCESS`
Required: No

 ** [MaxResults](#API_benefits_ListBenefits_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefits-request-MaxResults"></a>
The maximum number of benefits to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_benefits_ListBenefits_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefits-request-NextToken"></a>
A pagination token to retrieve the next set of results from a previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** [Programs](#API_benefits_ListBenefits_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefits-request-Programs"></a>
Filter benefits by specific AWS partner programs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** [Status](#API_benefits_ListBenefits_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefits-request-Status"></a>
Filter benefits by their current status.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Syntax
<a name="API_benefits_ListBenefits_ResponseSyntax"></a>

```
{
   "BenefitSummaries": [
      {
         "Arn": "string",
         "Catalog": "string",
         "Description": "string",
         "FulfillmentTypes": [ "string" ],
         "Id": "string",
         "Name": "string",
         "Programs": [ "string" ],
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_benefits_ListBenefits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BenefitSummaries](#API_benefits_ListBenefits_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefits-response-BenefitSummaries"></a>
A list of benefit summaries matching the specified criteria.
Type: Array of [BenefitSummary](API_benefits_BenefitSummary.md) objects

 ** [NextToken](#API_benefits_ListBenefits_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_ListBenefits-response-NextToken"></a>
A pagination token to retrieve the next set of results, if more results are available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_benefits_ListBenefits_Errors"></a>

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
<a name="API_benefits_ListBenefits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/ListBenefits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/ListBenefits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
