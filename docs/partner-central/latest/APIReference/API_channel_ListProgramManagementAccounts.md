---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ListProgramManagementAccounts.html
---

# ListProgramManagementAccounts
<a name="API_channel_ListProgramManagementAccounts"></a>

Lists program management accounts based on specified criteria.

## Request Syntax
<a name="API_channel_ListProgramManagementAccounts_RequestSyntax"></a>

```
{
   "accountIds": [ "{{string}}" ],
   "catalog": "{{string}}",
   "displayNames": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "programs": [ "{{string}}" ],
   "sort": {
      "sortBy": "{{string}}",
      "sortOrder": "{{string}}"
   },
   "statuses": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_channel_ListProgramManagementAccounts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [catalog](#API_channel_ListProgramManagementAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-request-catalog"></a>
The catalog identifier to filter accounts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** [accountIds](#API_channel_ListProgramManagementAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-request-accountIds"></a>
Filter by AWS account IDs.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

 ** [displayNames](#API_channel_ListProgramManagementAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-request-displayNames"></a>
Filter by display names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** [maxResults](#API_channel_ListProgramManagementAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_channel_ListProgramManagementAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-request-nextToken"></a>
Token for retrieving the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\x00-\x1F\x7F\x20]*`
Required: No

 ** [programs](#API_channel_ListProgramManagementAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-request-programs"></a>
Filter by program types.
Type: Array of strings
Valid Values: `SOLUTION_PROVIDER | DISTRIBUTION | DISTRIBUTION_SELLER`
Required: No

 ** [sort](#API_channel_ListProgramManagementAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-request-sort"></a>
Sorting options for the results.
Type: [ListProgramManagementAccountsSortBase](API_channel_ListProgramManagementAccountsSortBase.md) object
Required: No

 ** [statuses](#API_channel_ListProgramManagementAccounts_RequestSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-request-statuses"></a>
Filter by program management account statuses.
Type: Array of strings
Valid Values: `PENDING | ACTIVE | INACTIVE`
Required: No

## Response Syntax
<a name="API_channel_ListProgramManagementAccounts_ResponseSyntax"></a>

```
{
   "items": [
      {
         "accountId": "string",
         "arn": "string",
         "catalog": "string",
         "createdAt": "string",
         "displayName": "string",
         "id": "string",
         "program": "string",
         "revision": "string",
         "startDate": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_channel_ListProgramManagementAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_channel_ListProgramManagementAccounts_ResponseSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-response-items"></a>
List of program management accounts matching the criteria.
Type: Array of [ProgramManagementAccountSummary](API_channel_ProgramManagementAccountSummary.md) objects

 ** [nextToken](#API_channel_ListProgramManagementAccounts_ResponseSyntax) **   <a name="AWSPartnerCentral-channel_ListProgramManagementAccounts-response-nextToken"></a>
Token for retrieving the next page of results, if available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\x00-\x1F\x7F\x20]*`

## Errors
<a name="API_channel_ListProgramManagementAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** message **
A message describing the access denial.
 ** reason **
The reason for the access denial.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
 ** message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** message **
A message describing the resource not found error.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period.
 ** message **
A message describing the throttling error.
 ** quotaCode **
The quota code associated with the throttling error.
 ** serviceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** fieldList **
A list of fields that failed validation.
 ** message **
A message describing the validation error.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_channel_ListProgramManagementAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ListProgramManagementAccounts)
