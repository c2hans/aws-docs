---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SearchEngagements.html
---

# SearchEngagements

Searches the engagements in AWS Partner Central that match your criteria, such as customer industry or geography. You can combine a free-text `Keyword`, a structured `Filter` tree, an engagement group (`GroupId`), and `Sort` options, and each search criterion that you specify narrows the results. Results are paginated, so use `NextToken` to retrieve additional results.

## Request Syntax
<a name="API_SearchEngagements_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Filter": {
      "AndAllFilters": [
         "EngagementSearchFilter"
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
      "NotFilter": "EngagementSearchFilter",
      "OrAllFilters": [
         "EngagementSearchFilter"
      ]
   },
   "GroupId": "{{string}}",
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
<a name="API_SearchEngagements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_SearchEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-request-Catalog"></a>
Specifies the catalog to search. The following values are valid:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Filter](#API_SearchEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-request-Filter"></a>
A recursive, structured filter tree. Each node is either a boolean combinator (`AndAllFilters`, `OrAllFilters`, or `NotFilter`) or a leaf predicate (a single comparison such as `EqualsTo`). When provided together with `Keyword` or `GroupId`, each one narrows the result set.
Type: [EngagementSearchFilter](API_EngagementSearchFilter.md) object
Required: No

 ** [GroupId](#API_SearchEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-request-GroupId"></a>
The identifier of an engagement group that `ListEngagementGroups` returns. When you specify a group, the operation returns only the engagements that match the criteria that define the group. The group must be active and available to you in the specified catalog. Otherwise, the request fails with a `ValidationException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `eng-grp-[0-9a-z]{14}`
Required: No

 ** [Keyword](#API_SearchEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-request-Keyword"></a>
An optional free-text query string matched against the engagement title, description, customer company name, and member company names. When provided together with `Filter` or `GroupId`, each one narrows the result set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [MaxResults](#API_SearchEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-request-MaxResults"></a>
Specifies the maximum number of results to return in a single call. If you omit this value, the operation returns up to 20 results. Use this value to control pagination together with `NextToken`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-request-NextToken"></a>
A pagination token returned by a previous call. Pass it in a subsequent call to retrieve the next page of results. Omit it on the first call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Sort](#API_SearchEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-request-Sort"></a>
Specifies the field and direction used to sort the search results. If you omit this field, results are sorted by creation time, newest first.
Type: [EngagementSearchSort](API_EngagementSearchSort.md) object
Required: No

## Response Syntax
<a name="API_SearchEngagements_ResponseSyntax"></a>

```
{
   "EngagementSearchSummaries": [
      {
         "Arn": "string",
         "Contexts": [
            {
               "Id": "string",
               "Payload": { ... },
               "Type": "string"
            }
         ],
         "CreatedAt": "string",
         "CreatedBy": "string",
         "Description": "string",
         "Id": "string",
         "MemberCount": number,
         "ModifiedAt": "string",
         "ModifiedBy": "string",
         "Title": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchEngagements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngagementSearchSummaries](#API_SearchEngagements_ResponseSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-response-EngagementSearchSummaries"></a>
An array of summaries, one for each engagement that matches the request criteria.
Type: Array of [EngagementSearchSummary](API_EngagementSearchSummary.md) objects

 ** [NextToken](#API_SearchEngagements_ResponseSyntax) **   <a name="AWSPartnerCentral-SearchEngagements-response-NextToken"></a>
A pagination token used to retrieve the next set of results in subsequent calls. The response includes this token only when additional result pages are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_SearchEngagements_Errors"></a>

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
<a name="API_SearchEngagements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/SearchEngagements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/SearchEngagements)
