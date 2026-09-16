---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSourceSyncJobs.html
---

# ListDataSourceSyncJobs
<a name="API_ListDataSourceSyncJobs"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Get information about an Amazon Q Business data source connector synchronization.

## Request Syntax
<a name="API_ListDataSourceSyncJobs_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/indices/{{indexId}}/datasources/{{dataSourceId}}/syncjobs?endTime={{endTime}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startTime={{startTime}}&syncStatus={{statusFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSourceSyncJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application connected to the data source.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [dataSourceId](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-request-uri-dataSourceId"></a>
 The identifier of the data source connector.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [endTime](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-request-uri-endTime"></a>
 The end time of the data source connector sync.

 ** [indexId](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-request-uri-indexId"></a>
The identifier of the index used with the Amazon Q Business data source connector.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [maxResults](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-request-uri-maxResults"></a>
The maximum number of synchronization jobs to return in the response.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [nextToken](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-request-uri-nextToken"></a>
If the `maxResults` response was incpmplete because there is more data to retriever, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of responses.
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [startTime](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-request-uri-startTime"></a>
 The start time of the data source connector sync.

 ** [statusFilter](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-request-uri-statusFilter"></a>
Only returns synchronization jobs with the `Status` field equal to the specified status.
Valid Values: `FAILED | SUCCEEDED | SYNCING | INCOMPLETE | STOPPING | ABORTED | SYNCING_INDEXING`

## Request Body
<a name="API_ListDataSourceSyncJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSourceSyncJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "history": [
      {
         "dataSourceErrorCode": "string",
         "endTime": number,
         "error": {
            "errorCode": "string",
            "errorMessage": "string"
         },
         "executionId": "string",
         "metrics": {
            "documentsAdded": "string",
            "documentsDeleted": "string",
            "documentsFailed": "string",
            "documentsModified": "string",
            "documentsScanned": "string"
         },
         "startTime": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataSourceSyncJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [history](#API_ListDataSourceSyncJobs_ResponseSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-response-history"></a>
A history of synchronization jobs for the data source connector.
Type: Array of [DataSourceSyncJob](API_DataSourceSyncJob.md) objects

 ** [nextToken](#API_ListDataSourceSyncJobs_ResponseSyntax) **   <a name="qbusiness-ListDataSourceSyncJobs-response-nextToken"></a>
If the response is truncated, Amazon Q Business returns this token. You can use this token in any subsequent request to retrieve the next set of jobs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

## Errors
<a name="API_ListDataSourceSyncJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_ListDataSourceSyncJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/ListDataSourceSyncJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ListDataSourceSyncJobs)
