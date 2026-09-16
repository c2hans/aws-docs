---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetNotebookMetadata.html
---

# GetNotebookMetadata
<a name="API_GetNotebookMetadata"></a>

Retrieves notebook metadata for the specified notebook ID.

## Request Syntax
<a name="API_GetNotebookMetadata_RequestSyntax"></a>

```
{
   "NotebookId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetNotebookMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotebookId](#API_GetNotebookMetadata_RequestSyntax) **   <a name="athena-GetNotebookMetadata-request-NotebookId"></a>
The ID of the notebook whose metadata is to be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_GetNotebookMetadata_ResponseSyntax"></a>

```
{
   "NotebookMetadata": {
      "CreationTime": number,
      "LastModifiedTime": number,
      "Name": "string",
      "NotebookId": "string",
      "Type": "string",
      "WorkGroup": "string"
   }
}
```

## Response Elements
<a name="API_GetNotebookMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NotebookMetadata](#API_GetNotebookMetadata_ResponseSyntax) **   <a name="athena-GetNotebookMetadata-response-NotebookMetadata"></a>
The metadata that is returned for the specified notebook ID.
Type: [NotebookMetadata](API_NotebookMetadata.md) object

## Errors
<a name="API_GetNotebookMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** TooManyRequestsException **
Indicates that the request was throttled.
 ** Reason **
The reason for the query throttling, for example, when it exceeds the concurrent query limit.
HTTP Status Code: 400

## See Also
<a name="API_GetNotebookMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetNotebookMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetNotebookMetadata)
