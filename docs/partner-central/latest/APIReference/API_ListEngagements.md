---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagements.html
---

# ListEngagements
<a name="API_ListEngagements"></a>

This action allows users to retrieve a list of Engagement records from Partner Central. This action can be used to manage and track various engagements across different stages of the partner selling process.

## Request Syntax
<a name="API_ListEngagements_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ContextTypes": [ "{{string}}" ],
   "CreatedBy": [ "{{string}}" ],
   "EngagementIdentifier": [ "{{string}}" ],
   "ExcludeContextTypes": [ "{{string}}" ],
   "ExcludeCreatedBy": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListEngagements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-Catalog"></a>
 Specifies the catalog related to the request.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ContextTypes](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-ContextTypes"></a>
Filters engagements to include only those containing the specified context types, such as "CustomerProject" or "Lead". Use this to find engagements that have specific types of contextual information associated with them.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `CustomerProject | Lead | ProspectingResult`
Required: No

 ** [CreatedBy](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-CreatedBy"></a>
 A list of AWS account IDs. When specified, the response includes engagements created by these accounts. This filter is useful for finding engagements created by specific team members.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** [EngagementIdentifier](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-EngagementIdentifier"></a>
An array of strings representing engagement identifiers to retrieve.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `(arn:.*|eng-[0-9a-z]{14})`
Required: No

 ** [ExcludeContextTypes](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-ExcludeContextTypes"></a>
Filters engagements to exclude those containing the specified context types. Use this to find engagements that do not have certain types of contextual information, helping to narrow results based on context exclusion criteria.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `CustomerProject | Lead | ProspectingResult`
Required: No

 ** [ExcludeCreatedBy](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-ExcludeCreatedBy"></a>
An array of strings representing AWS Account IDs. Use this to exclude engagements created by specific users.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** [MaxResults](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-MaxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-NextToken"></a>
The token for the next set of results. This value is returned from a previous call.
Type: String
Required: No

 ** [Sort](#API_ListEngagements_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagements-request-Sort"></a>
Specifies the sorting parameters for listing Engagements.
Type: [EngagementSort](API_EngagementSort.md) object
Required: No

## Response Syntax
<a name="API_ListEngagements_ResponseSyntax"></a>

```
{
   "EngagementSummaryList": [
      {
         "Arn": "string",
         "ContextTypes": [ "string" ],
         "CreatedAt": "string",
         "CreatedBy": "string",
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
<a name="API_ListEngagements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngagementSummaryList](#API_ListEngagements_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagements-response-EngagementSummaryList"></a>
An array of engagement summary objects.
Type: Array of [EngagementSummary](API_EngagementSummary.md) objects

 ** [NextToken](#API_ListEngagements_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagements-response-NextToken"></a>
The token to retrieve the next set of results. This field will be null if there are no more results.
Type: String

## Errors
<a name="API_ListEngagements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
HTTP Status Code: 400

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_ListEngagements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListEngagements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListEngagements)
