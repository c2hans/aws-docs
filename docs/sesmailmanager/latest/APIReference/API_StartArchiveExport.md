---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StartArchiveExport.html
---

# StartArchiveExport
<a name="API_StartArchiveExport"></a>

Initiates an export of emails from the specified archive.

## Request Syntax
<a name="API_StartArchiveExport_RequestSyntax"></a>

```
{
   "ArchiveId": "{{string}}",
   "ExportDestinationConfiguration": { ... },
   "Filters": {
      "Include": [
         { ... }
      ],
      "Unless": [
         { ... }
      ]
   },
   "FromTimestamp": {{number}},
   "IncludeMetadata": {{boolean}},
   "MaxResults": {{number}},
   "ToTimestamp": {{number}}
}
```

## Request Parameters
<a name="API_StartArchiveExport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchiveId](#API_StartArchiveExport_RequestSyntax) **   <a name="sesmailmanager-StartArchiveExport-request-ArchiveId"></a>
The identifier of the archive to export emails from.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 66.
Pattern: `a-[\w]{1,64}`
Required: Yes

 ** [ExportDestinationConfiguration](#API_StartArchiveExport_RequestSyntax) **   <a name="sesmailmanager-StartArchiveExport-request-ExportDestinationConfiguration"></a>
Details on where to deliver the exported email data.
Type: [ExportDestinationConfiguration](API_ExportDestinationConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Filters](#API_StartArchiveExport_RequestSyntax) **   <a name="sesmailmanager-StartArchiveExport-request-Filters"></a>
Criteria to filter which emails are included in the export.
Type: [ArchiveFilters](API_ArchiveFilters.md) object
Required: No

 ** [FromTimestamp](#API_StartArchiveExport_RequestSyntax) **   <a name="sesmailmanager-StartArchiveExport-request-FromTimestamp"></a>
The start of the timestamp range to include emails from.
Type: Timestamp
Required: Yes

 ** [IncludeMetadata](#API_StartArchiveExport_RequestSyntax) **   <a name="sesmailmanager-StartArchiveExport-request-IncludeMetadata"></a>
Whether to include message metadata as JSON files in the export.
Type: Boolean
Required: No

 ** [MaxResults](#API_StartArchiveExport_RequestSyntax) **   <a name="sesmailmanager-StartArchiveExport-request-MaxResults"></a>
The maximum number of email items to include in the export.
Type: Integer
Required: No

 ** [ToTimestamp](#API_StartArchiveExport_RequestSyntax) **   <a name="sesmailmanager-StartArchiveExport-request-ToTimestamp"></a>
The end of the timestamp range to include emails from.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_StartArchiveExport_ResponseSyntax"></a>

```
{
   "ExportId": "string"
}
```

## Response Elements
<a name="API_StartArchiveExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportId](#API_StartArchiveExport_ResponseSyntax) **   <a name="sesmailmanager-StartArchiveExport-response-ExportId"></a>
The unique identifier for the initiated export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_StartArchiveExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
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
<a name="API_StartArchiveExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/StartArchiveExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/StartArchiveExport)
