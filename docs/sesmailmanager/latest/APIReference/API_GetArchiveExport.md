---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveExport.html
---

# GetArchiveExport
<a name="API_GetArchiveExport"></a>

Retrieves the details and current status of a specific email archive export job.

## Request Syntax
<a name="API_GetArchiveExport_RequestSyntax"></a>

```
{
   "ExportId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetArchiveExport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExportId](#API_GetArchiveExport_RequestSyntax) **   <a name="sesmailmanager-GetArchiveExport-request-ExportId"></a>
The identifier of the export job to get details for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_GetArchiveExport_ResponseSyntax"></a>

```
{
   "ArchiveId": "string",
   "ExportDestinationConfiguration": { ... },
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
<a name="API_GetArchiveExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArchiveId](#API_GetArchiveExport_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveExport-response-ArchiveId"></a>
The identifier of the archive the email export was performed from.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 66.
Pattern: `a-[\w]{1,64}`

 ** [ExportDestinationConfiguration](#API_GetArchiveExport_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveExport-response-ExportDestinationConfiguration"></a>
Where the exported emails are being delivered.
Type: [ExportDestinationConfiguration](API_ExportDestinationConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Filters](#API_GetArchiveExport_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveExport-response-Filters"></a>
The criteria used to filter emails included in the export.
Type: [ArchiveFilters](API_ArchiveFilters.md) object

 ** [FromTimestamp](#API_GetArchiveExport_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveExport-response-FromTimestamp"></a>
The start of the timestamp range the exported emails cover.
Type: Timestamp

 ** [MaxResults](#API_GetArchiveExport_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveExport-response-MaxResults"></a>
The maximum number of email items included in the export.
Type: Integer

 ** [Status](#API_GetArchiveExport_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveExport-response-Status"></a>
The current status of the export job.
Type: [ExportStatus](API_ExportStatus.md) object

 ** [ToTimestamp](#API_GetArchiveExport_ResponseSyntax) **   <a name="sesmailmanager-GetArchiveExport-response-ToTimestamp"></a>
The end of the date range the exported emails cover.
Type: Timestamp

## Errors
<a name="API_GetArchiveExport_Errors"></a>

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
<a name="API_GetArchiveExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetArchiveExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetArchiveExport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
