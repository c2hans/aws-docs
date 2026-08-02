---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListDatasetExportJobs.html
---

# ListDatasetExportJobs
<a name="API_ListDatasetExportJobs"></a>

Retrieves a paginated list of dataset export jobs for a workspace.

## Request Syntax
<a name="API_ListDatasetExportJobs_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/dataset-export-jobs?filter={{filter}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDatasetExportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [filter](#API_ListDatasetExportJobs_RequestSyntax) **   <a name="iotsitewise-ListDatasetExportJobs-request-uri-filter"></a>
The optional filter that returns only jobs matching the given filter value. Defaults to ALL.
Valid Values: `ALL | SUBMITTED | RUNNING | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`

 ** [maxResults](#API_ListDatasetExportJobs_RequestSyntax) **   <a name="iotsitewise-ListDatasetExportJobs-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListDatasetExportJobs_RequestSyntax) **   <a name="iotsitewise-ListDatasetExportJobs-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [workspaceName](#API_ListDatasetExportJobs_RequestSyntax) **   <a name="iotsitewise-ListDatasetExportJobs-request-uri-workspaceName"></a>
The name of the workspace whose dataset export jobs should be listed.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_ListDatasetExportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDatasetExportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [
      {
         "completedAt": number,
         "destinationS3Uri": "string",
         "jobId": "string",
         "startedAt": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasetExportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListDatasetExportJobs_ResponseSyntax) **   <a name="iotsitewise-ListDatasetExportJobs-response-jobs"></a>
A list of dataset export job summaries.
Type: Array of [ExportJobSummary](API_ExportJobSummary.md) objects

 ** [nextToken](#API_ListDatasetExportJobs_ResponseSyntax) **   <a name="iotsitewise-ListDatasetExportJobs-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_ListDatasetExportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_ListDatasetExportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListDatasetExportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListDatasetExportJobs)
