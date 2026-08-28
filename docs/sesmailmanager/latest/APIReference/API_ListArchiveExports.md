---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListArchiveExports.html
---

# ListArchiveExports
<a name="API_ListArchiveExports"></a>

Returns a list of email archive export jobs.

## Request Syntax
<a name="API_ListArchiveExports_RequestSyntax"></a>

```
{
   "ArchiveId": "{{string}}",
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## Request Parameters
<a name="API_ListArchiveExports_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchiveId](#API_ListArchiveExports_RequestSyntax) **   <a name="sesmailmanager-ListArchiveExports-request-ArchiveId"></a>
The identifier of the archive.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 66.
Pattern: `a-[\w]{1,64}`
Required: Yes

 ** [NextToken](#API_ListArchiveExports_RequestSyntax) **   <a name="sesmailmanager-ListArchiveExports-request-NextToken"></a>
If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PageSize](#API_ListArchiveExports_RequestSyntax) **   <a name="sesmailmanager-ListArchiveExports-request-PageSize"></a>
The maximum number of archive export jobs that are returned per call. You can use NextToken to obtain further pages of archives.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

## Response Syntax
<a name="API_ListArchiveExports_ResponseSyntax"></a>

```
{
   "Exports": [
      {
         "ExportId": "string",
         "Status": {
            "CompletionTimestamp": number,
            "ErrorMessage": "string",
            "State": "string",
            "SubmissionTimestamp": number
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListArchiveExports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Exports](#API_ListArchiveExports_ResponseSyntax) **   <a name="sesmailmanager-ListArchiveExports-response-Exports"></a>
The list of export job identifiers and statuses.
Type: Array of [ExportSummary](API_ExportSummary.md) objects

 ** [NextToken](#API_ListArchiveExports_ResponseSyntax) **   <a name="sesmailmanager-ListArchiveExports-response-NextToken"></a>
If present, use to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListArchiveExports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_ListArchiveExports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/ListArchiveExports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ListArchiveExports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
