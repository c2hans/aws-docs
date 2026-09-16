---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeImportTasks.html
---

# DescribeImportTasks
<a name="API_DescribeImportTasks"></a>

Lists and describes import tasks, with optional filtering by import status and source ARN.

## Request Syntax
<a name="API_DescribeImportTasks_RequestSyntax"></a>

```
{
   "importId": "{{string}}",
   "importSourceArn": "{{string}}",
   "importStatus": "{{string}}",
   "limit": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImportTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [importId](#API_DescribeImportTasks_RequestSyntax) **   <a name="CWL-DescribeImportTasks-request-importId"></a>
Optional filter to describe a specific import task by its ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\-a-zA-Z0-9]+`
Required: No

 ** [importSourceArn](#API_DescribeImportTasks_RequestSyntax) **   <a name="CWL-DescribeImportTasks-request-importSourceArn"></a>
Optional filter to list imports from a specific source
Type: String
Required: No

 ** [importStatus](#API_DescribeImportTasks_RequestSyntax) **   <a name="CWL-DescribeImportTasks-request-importStatus"></a>
Optional filter to list imports by their status. Valid values are IN\_PROGRESS, CANCELLED, COMPLETED and FAILED.
Type: String
Valid Values: `IN_PROGRESS | CANCELLED | COMPLETED | FAILED`
Required: No

 ** [limit](#API_DescribeImportTasks_RequestSyntax) **   <a name="CWL-DescribeImportTasks-request-limit"></a>
The maximum number of import tasks to return in the response. Default: 50
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_DescribeImportTasks_RequestSyntax) **   <a name="CWL-DescribeImportTasks-request-nextToken"></a>
The pagination token for the next set of results.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeImportTasks_ResponseSyntax"></a>

```
{
   "imports": [
      {
         "creationTime": number,
         "errorMessage": "string",
         "importDestinationArn": "string",
         "importFilter": {
            "endEventTime": number,
            "startEventTime": number
         },
         "importId": "string",
         "importSourceArn": "string",
         "importStatistics": {
            "bytesImported": number
         },
         "importStatus": "string",
         "lastUpdatedTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeImportTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imports](#API_DescribeImportTasks_ResponseSyntax) **   <a name="CWL-DescribeImportTasks-response-imports"></a>
The list of import tasks that match the request filters.
Type: Array of [Import](API_Import.md) objects

 ** [nextToken](#API_DescribeImportTasks_ResponseSyntax) **   <a name="CWL-DescribeImportTasks-response-nextToken"></a>
The token to use when requesting the next set of results. Not present if there are no additional results to retrieve.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeImportTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

## Examples
<a name="API_DescribeImportTasks_Examples"></a>

### To describe import tasks
<a name="API_DescribeImportTasks_Example_1"></a>

The following example retrieves a list of import tasks with filters.

#### Sample Request
<a name="API_DescribeImportTasks_Example_1_Request"></a>

```
POST / HTTP/1.1
          Host: logs.<region>.<domain>
          X-Amz-Target: Logs_20140328.DescribeImportTasks
          {
          "importId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
          "importStatus": "IN_PROGRESS",
          "importSourceArn": "arn:aws:cloudtrail:us-west-2:123456789012:eventdatastore/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb",
          "limit": 50,
          "nextToken": "eyJOZXh0VG9rZW4iOiJudWxsIiwiYm90b190cnVuY2F0ZV9hbW91bnQiOjF9"
          }
```

#### Sample Response
<a name="API_DescribeImportTasks_Example_1_Response"></a>

```
HTTP/1.1 200 OK
          {
          "imports": [
          {
          "importId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
          "importSourceArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb",
          "importStatus": "IN_PROGRESS",
          "importDestinationArn": "arn:aws:logs:us-east-1:123456789012:log-group:aws/cloudtrail/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb",
          "importStatistics": {
          "bytesImported": 1048576
          },
          "importFilter": {
          "startEventTime": 1640995200000,
          "endEventTime": 1641081600000
          },
          "creationTime": 1641168000000,
          "lastUpdatedTime": 1641171600000
          }
          ],
          "nextToken": "eyJOZXh0VG9rZW4iOiJudWxsIiwiYm90b190cnVuY2F0ZV9hbW91bnQiOjJ9"
          }
```

## See Also
<a name="API_DescribeImportTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeImportTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeImportTasks)
