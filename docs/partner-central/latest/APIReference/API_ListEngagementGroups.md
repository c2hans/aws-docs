---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementGroups.html
---

# ListEngagementGroups

Lists the active, fully curated AWS Partner Central engagement groups that are available to you in the specified catalog. An engagement group is a curated set of engagements that share common characteristics, such as customer geography, industry, or solution category. To retrieve the engagements in a group, pass the group `Id` to `SearchEngagements` as `GroupId`, and use `NextToken` to retrieve additional pages of groups.

## Request Syntax
<a name="API_ListEngagementGroups_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "EngagementGroupIdentifiers": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ReadinessLevel": "{{string}}",
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListEngagementGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListEngagementGroups_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementGroups-request-Catalog"></a>
Specifies the catalog in which to list engagement groups. The following values are valid:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [EngagementGroupIdentifiers](#API_ListEngagementGroups_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementGroups-request-EngagementGroupIdentifiers"></a>
Filters the results to the specified engagement groups. Each entry can be an engagement group identifier or an engagement group ARN. You can specify 1 to 10 entries. Identifiers that don't match an active group available to you are ignored.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(arn:.*|eng-grp-[0-9a-z]{14})`
Required: No

 ** [MaxResults](#API_ListEngagementGroups_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementGroups-request-MaxResults"></a>
Specifies the maximum number of results to return in a single call. If you omit this value, the operation returns up to 20 results. Use this value to control pagination together with `NextToken`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListEngagementGroups_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementGroups-request-NextToken"></a>
A pagination token returned by a previous call. Pass it in a subsequent call to retrieve the next page of results. Omit it on the first call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [ReadinessLevel](#API_ListEngagementGroups_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementGroups-request-ReadinessLevel"></a>
Filters the results to engagement groups with the specified readiness level. If you omit this field, the operation returns groups of all readiness levels.
Type: String
Valid Values: `SalesReady | MarketingReady | LowPotential`
Required: No

 ** [Sort](#API_ListEngagementGroups_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementGroups-request-Sort"></a>
Specifies the field and direction used to sort the results. You can sort by `Count` or `UpdatedAt`. If you omit this field, the operation returns groups in recommended order.
Type: [EngagementGroupSort](API_EngagementGroupSort.md) object
Required: No

## Response Syntax
<a name="API_ListEngagementGroups_ResponseSyntax"></a>

```
{
   "EngagementGroupSummaries": [
      {
         "Arn": "string",
         "Catalog": "string",
         "Count": number,
         "Description": "string",
         "Id": "string",
         "Name": "string",
         "ReadinessLevel": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEngagementGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngagementGroupSummaries](#API_ListEngagementGroups_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagementGroups-response-EngagementGroupSummaries"></a>
An array of engagement groups that are available to you in the specified catalog. The array is empty when no groups are available.
Type: Array of [EngagementGroupSummary](API_EngagementGroupSummary.md) objects

 ** [NextToken](#API_ListEngagementGroups_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagementGroups-response-NextToken"></a>
A pagination token used to retrieve the next set of results in subsequent calls. The response includes this token only when additional result pages are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListEngagementGroups_Errors"></a>

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
<a name="API_ListEngagementGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListEngagementGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListEngagementGroups)
