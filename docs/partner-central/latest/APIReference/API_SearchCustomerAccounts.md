---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SearchCustomerAccounts.html
---

# SearchCustomerAccounts

Use `SearchCustomerAccounts` to find customer accounts in the specified catalog. You can filter the results by fields such as enrichment status, industry, geography, and creation date, and sort them by company name, date, or score.

Results are paginated. Use `NextToken` to retrieve additional results.

## Request Syntax
<a name="API_SearchCustomerAccounts_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Filter": {
      "AndAllFilters": [
         "Filter"
      ],
      "ContainsAll": {
         "Key": "{{string}}",
         "Value": { ... }
      },
      "ContainsAny": {
         "Key": "{{string}}",
         "Value": { ... }
      },
      "EqualsTo": {
         "Key": "{{string}}",
         "Value": { ... }
      },
      "GreaterThan": {
         "Key": "{{string}}",
         "Value": { ... }
      },
      "GreaterThanOrEquals": {
         "Key": "{{string}}",
         "Value": { ... }
      },
      "LessThan": {
         "Key": "{{string}}",
         "Value": { ... }
      },
      "LessThanOrEquals": {
         "Key": "{{string}}",
         "Value": { ... }
      },
      "NotFilter": "Filter",
      "OrAllFilters": [
         "Filter"
      ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_SearchCustomerAccounts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_SearchCustomerAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-SearchCustomerAccounts-request-Catalog"></a>
Specifies the catalog for the request. Valid values:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Filter](#API_SearchCustomerAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-SearchCustomerAccounts-request-Filter"></a>
Specifies a filter tree that narrows the customer accounts. Each node either combines child filters or compares a single field to a value.
Type: [Filter](API_Filter.md) object
Required: No

 ** [MaxResults](#API_SearchCustomerAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-SearchCustomerAccounts-request-MaxResults"></a>
Specifies the maximum number of results to return in a single call. Use this value together with `NextToken` to control pagination.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchCustomerAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-SearchCustomerAccounts-request-NextToken"></a>
Specifies the token for the next page of results. Use the `NextToken` value from a previous response to retrieve the next page.
Type: String
Required: No

 ** [Sort](#API_SearchCustomerAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-SearchCustomerAccounts-request-Sort"></a>
Specifies the field and direction used to sort the results.
Type: [CustomerAccountSort](API_CustomerAccountSort.md) object
Required: No

## Response Syntax
<a name="API_SearchCustomerAccounts_ResponseSyntax"></a>

```
{
   "CustomerAccountSummaries": [
      {
         "Arn": "string",
         "AwsEnrichment": {
            "Customer": {
               "AccountPlanningQualification": "string",
               "Country": "string",
               "EligiblePrograms": [ "string" ],
               "Geo": "string",
               "Industry": "string",
               "Segment": "string"
            },
            "Insights": {
               "MarketplaceEngagementScore": "string",
               "SolutionCategory": "string",
               "SolutionScore": "string"
            }
         },
         "Catalog": "string",
         "CreatedDate": "string",
         "CustomerAccount": {
            "CompanyName": "string"
         },
         "EnrichmentStatus": "string",
         "Id": "string",
         "LastModifiedDate": "string",
         "PartnerAccountIdentifier": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchCustomerAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomerAccountSummaries](#API_SearchCustomerAccounts_ResponseSyntax) **   <a name="AWSPartnerCentral-SearchCustomerAccounts-response-CustomerAccountSummaries"></a>
The customer accounts that match the request.
Type: Array of [CustomerAccountSummary](API_CustomerAccountSummary.md) objects

 ** [NextToken](#API_SearchCustomerAccounts_ResponseSyntax) **   <a name="AWSPartnerCentral-SearchCustomerAccounts-response-NextToken"></a>
The token to retrieve the next page of results. This value is absent when there are no more results.
Type: String

## Errors
<a name="API_SearchCustomerAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
 ** Message **
A message that describes the internal error.
HTTP Status Code: 500

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
 ** Message **
A message that describes why the service throttled the request.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Message **
A message that describes the validation error.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_SearchCustomerAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/SearchCustomerAccounts)
