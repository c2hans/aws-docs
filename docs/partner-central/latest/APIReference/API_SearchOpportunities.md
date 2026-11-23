---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SearchOpportunities.html
---

# SearchOpportunities

The `SearchOpportunities` operation in the AWS Partner Central Selling API searches and filters the opportunities available to you in AWS Partner Central.

You can optionally provide a free-text `Keyword`, a structured `Filter` tree, and `Sort` options. The operation returns a curated summary view of each matching opportunity. If you supply both `Keyword` and `Filter`, the operation combines them with a logical AND, so each one narrows the result set.

Results are paginated. Use the `NextToken` parameter to retrieve additional pages of results.

## Request Syntax
<a name="API_SearchOpportunities_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Filter": {
      "AndAllFilters": [
         "OpportunitySearchFilter"
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
      "NotFilter": "OpportunitySearchFilter",
      "OrAllFilters": [
         "OpportunitySearchFilter"
      ]
   },
   "Keyword": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_SearchOpportunities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_SearchOpportunities_RequestSyntax) **   <a name="AWSPartnerCentral-SearchOpportunities-request-Catalog"></a>
Specifies the catalog in which you run the search. Use `AWS` to search production opportunities, or use `Sandbox` to search opportunities in a testing environment.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Filter](#API_SearchOpportunities_RequestSyntax) **   <a name="AWSPartnerCentral-SearchOpportunities-request-Filter"></a>
A recursive, structured filter tree. Each node is either a boolean combinator (`AndAllFilters`, `OrAllFilters`, or `NotFilter`) or a leaf predicate (a single comparison such as `EqualsTo`). When provided together with `Keyword`, both narrow the result set.
Type: [OpportunitySearchFilter](API_OpportunitySearchFilter.md) object
Required: No

 ** [Keyword](#API_SearchOpportunities_RequestSyntax) **   <a name="AWSPartnerCentral-SearchOpportunities-request-Keyword"></a>
An optional free-text query string matched against opportunity fields. When provided together with `Filter`, both narrow the result set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [MaxResults](#API_SearchOpportunities_RequestSyntax) **   <a name="AWSPartnerCentral-SearchOpportunities-request-MaxResults"></a>
The maximum number of results to return in a single call. Use this value to control pagination together with `NextToken`. If you omit this parameter, the service applies a default page size and returns the remaining results on subsequent pages.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchOpportunities_RequestSyntax) **   <a name="AWSPartnerCentral-SearchOpportunities-request-NextToken"></a>
A pagination token returned by a previous call. Pass it in a subsequent call to retrieve the next page of results. Omit it on the first call.
Type: String
Required: No

 ** [Sort](#API_SearchOpportunities_RequestSyntax) **   <a name="AWSPartnerCentral-SearchOpportunities-request-Sort"></a>
Specifies the field and direction used to sort the search results.
Type: [OpportunitySearchSort](API_OpportunitySearchSort.md) object
Required: No

## Response Syntax
<a name="API_SearchOpportunities_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OpportunitySearchSummaries": [
      {
         "AwsOpportunitySummary": {
            "CosellMotion": "string",
            "Insights": {
               "EngagementScore": "string",
               "OpportunityQuality": {
                  "Score": number
               }
            },
            "Origin": "string"
         },
         "CreatedDate": "string",
         "Customer": {
            "Account": {
               "Address": {
                  "CountryCode": "string"
               },
               "AwsAccountId": "string",
               "CompanyName": "string",
               "Industry": "string"
            }
         },
         "Id": "string",
         "LastModifiedDate": "string",
         "LifeCycle": {
            "NextSteps": "string",
            "ReviewStatus": "string",
            "Stage": "string",
            "TargetCloseDate": "string"
         },
         "OpportunityTeam": [
            {
               "BusinessTitle": "string",
               "FirstName": "string",
               "LastName": "string"
            }
         ],
         "OpportunityType": "string",
         "PartnerOpportunityIdentifier": "string",
         "Project": {
            "ApnPrograms": [ "string" ],
            "ExpectedCustomerSpend": [
               {
                  "Amount": "string",
                  "CurrencyCode": "string"
               }
            ],
            "Title": "string"
         },
         "RelatedEntityIdentifiers": {
            "AwsMarketplaceOffers": [ "string" ],
            "AwsMarketplaceOfferSets": [ "string" ],
            "AwsMarketplaceSolutions": [ "string" ],
            "Solutions": [ "string" ]
         },
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_SearchOpportunities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OpportunitySearchSummaries](#API_SearchOpportunities_ResponseSyntax) **   <a name="AWSPartnerCentral-SearchOpportunities-response-OpportunitySearchSummaries"></a>
An array of curated summary views, one for each opportunity that matches the request criteria.
Type: Array of [OpportunitySearchSummary](API_OpportunitySearchSummary.md) objects

 ** [NextToken](#API_SearchOpportunities_ResponseSyntax) **   <a name="AWSPartnerCentral-SearchOpportunities-response-NextToken"></a>
A pagination token for retrieving the next set of results. Pass this token in a subsequent call to get the next page. The response includes this token only when additional result pages are available.
Type: String

## Errors
<a name="API_SearchOpportunities_Errors"></a>

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

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
 ** Message **
A message that describes which resource the service couldn't find.
HTTP Status Code: 400

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
<a name="API_SearchOpportunities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/SearchOpportunities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/SearchOpportunities)
