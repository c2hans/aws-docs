---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileHistoryRecords.html
---

# ListProfileHistoryRecords
<a name="API_connect-customer-profiles_ListProfileHistoryRecords"></a>

Returns a list of history records for a specific profile, for a specific domain.

## Request Syntax
<a name="API_connect-customer-profiles_ListProfileHistoryRecords_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/profiles/history-records?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "ActionType": "{{string}}",
   "ObjectTypeName": "{{string}}",
   "PerformedBy": "{{string}}",
   "ProfileId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListProfileHistoryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListProfileHistoryRecords_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-request-uri-DomainName"></a>
The unique name of the domain for which to return profile history records.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListProfileHistoryRecords_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListProfileHistoryRecords_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListProfileHistoryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ActionType](#API_connect-customer-profiles_ListProfileHistoryRecords_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-request-ActionType"></a>
Applies a filter to include profile history records only with the specified `ActionType` value in the response.
Type: String
Valid Values: `ADDED_PROFILE_KEY | DELETED_PROFILE_KEY | CREATED | UPDATED | INGESTED | DELETED_BY_CUSTOMER | EXPIRED | MERGED | DELETED_BY_MERGE`
Required: No

 ** [ObjectTypeName](#API_connect-customer-profiles_ListProfileHistoryRecords_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-request-ObjectTypeName"></a>
Applies a filter to include profile history records only with the specified `ObjectTypeName` value in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** [PerformedBy](#API_connect-customer-profiles_ListProfileHistoryRecords_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-request-PerformedBy"></a>
Applies a filter to include profile history records only with the specified `PerformedBy` value in the response. The `PerformedBy` value can be the Amazon Resource Name (ARN) of the person or service principal who performed the action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [ProfileId](#API_connect-customer-profiles_ListProfileHistoryRecords_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-request-ProfileId"></a>
The identifier of the profile to be taken.
Type: String
Pattern: `[a-f0-9]{32}`
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_ListProfileHistoryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProfileHistoryRecords": [
      {
         "ActionType": "string",
         "CreatedAt": number,
         "Id": "string",
         "LastUpdatedAt": number,
         "ObjectTypeName": "string",
         "PerformedBy": "string",
         "ProfileObjectUniqueKey": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListProfileHistoryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_connect-customer-profiles_ListProfileHistoryRecords_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [ProfileHistoryRecords](#API_connect-customer-profiles_ListProfileHistoryRecords_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileHistoryRecords-response-ProfileHistoryRecords"></a>
The list of profile history records.
Type: Array of [ProfileHistoryRecord](API_connect-customer-profiles_ProfileHistoryRecord.md) objects

## Errors
<a name="API_connect-customer-profiles_ListProfileHistoryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_ListProfileHistoryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListProfileHistoryRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListProfileHistoryRecords)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
