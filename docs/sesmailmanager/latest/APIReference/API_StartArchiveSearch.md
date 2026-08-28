---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StartArchiveSearch.html
---

# StartArchiveSearch
<a name="API_StartArchiveSearch"></a>

Initiates a search across emails in the specified archive.

## Request Syntax
<a name="API_StartArchiveSearch_RequestSyntax"></a>

```
{
   "ArchiveId": "{{string}}",
   "Filters": {
      "Include": [
         { ... }
      ],
      "Unless": [
         { ... }
      ]
   },
   "FromTimestamp": {{number}},
   "MaxResults": {{number}},
   "ToTimestamp": {{number}}
}
```

## Request Parameters
<a name="API_StartArchiveSearch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchiveId](#API_StartArchiveSearch_RequestSyntax) **   <a name="sesmailmanager-StartArchiveSearch-request-ArchiveId"></a>
The identifier of the archive to search emails in.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 66.
Pattern: `a-[\w]{1,64}`
Required: Yes

 ** [Filters](#API_StartArchiveSearch_RequestSyntax) **   <a name="sesmailmanager-StartArchiveSearch-request-Filters"></a>
Criteria to filter which emails are included in the search results.
Type: [ArchiveFilters](API_ArchiveFilters.md) object
Required: No

 ** [FromTimestamp](#API_StartArchiveSearch_RequestSyntax) **   <a name="sesmailmanager-StartArchiveSearch-request-FromTimestamp"></a>
The start timestamp of the range to search emails from.
Type: Timestamp
Required: Yes

 ** [MaxResults](#API_StartArchiveSearch_RequestSyntax) **   <a name="sesmailmanager-StartArchiveSearch-request-MaxResults"></a>
The maximum number of search results to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: Yes

 ** [ToTimestamp](#API_StartArchiveSearch_RequestSyntax) **   <a name="sesmailmanager-StartArchiveSearch-request-ToTimestamp"></a>
The end timestamp of the range to search emails from.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_StartArchiveSearch_ResponseSyntax"></a>

```
{
   "SearchId": "string"
}
```

## Response Elements
<a name="API_StartArchiveSearch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SearchId](#API_StartArchiveSearch_ResponseSyntax) **   <a name="sesmailmanager-StartArchiveSearch-response-SearchId"></a>
The unique identifier for the initiated search job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_StartArchiveSearch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when an operation exceeds a predefined service quota or limit.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_StartArchiveSearch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/StartArchiveSearch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/StartArchiveSearch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
