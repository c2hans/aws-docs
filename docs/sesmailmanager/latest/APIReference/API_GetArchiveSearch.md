---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveSearch.html
---

# GetArchiveSearch
<a name="API_GetArchiveSearch"></a>

Retrieves the details and current status of a specific email archive search job.

## Request Syntax
<a name="API_GetArchiveSearch_RequestSyntax"></a>

```
{
   "SearchId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetArchiveSearch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SearchId](#API_GetArchiveSearch_RequestSyntax) **   <a name="sesmailmanager-GetArchiveSearch-request-SearchId"></a>
The identifier of the search job to get details for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_GetArchiveSearch_ResponseSyntax"></a>

```
{
   "ArchiveId": "string",
   "Filters": {
      "Include": [
         { ... }
      ],
      "Unless": [
         { ... }
      ]
   },
   "FromTimestamp": number,
   "MaxResults": number,
   "Status": {
      "CompletionTimestamp": number,
      "ErrorMessage": "string",
      "State": "string",
      "SubmissionTimestamp": number
   },
   "ToTimestamp": number
}
```

## Response Elements
<a name="API_GetArchiveSearch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArchiveId](#API_GetArchiveSearch_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveSearch-response-ArchiveId"></a>
The identifier of the archive the email search was performed in.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 66.
Pattern: `a-[\w]{1,64}`

 ** [Filters](#API_GetArchiveSearch_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveSearch-response-Filters"></a>
The criteria used to filter emails included in the search.
Type: [ArchiveFilters](API_ArchiveFilters.md) object

 ** [FromTimestamp](#API_GetArchiveSearch_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveSearch-response-FromTimestamp"></a>
The start timestamp of the range the searched emails cover.
Type: Timestamp

 ** [MaxResults](#API_GetArchiveSearch_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveSearch-response-MaxResults"></a>
The maximum number of search results to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [Status](#API_GetArchiveSearch_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveSearch-response-Status"></a>
The current status of the search job.
Type: [SearchStatus](API_SearchStatus.md) object

 ** [ToTimestamp](#API_GetArchiveSearch_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveSearch-response-ToTimestamp"></a>
The end timestamp of the range the searched emails cover.
Type: Timestamp

## Errors
<a name="API_GetArchiveSearch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetArchiveSearch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetArchiveSearch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetArchiveSearch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
