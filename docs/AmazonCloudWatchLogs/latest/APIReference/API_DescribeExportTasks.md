---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.html
---

# DescribeExportTasks
<a name="API_DescribeExportTasks"></a>

Lists the specified export tasks. You can list all your export tasks or filter the results based on task ID or task status.

## Request Syntax
<a name="API_DescribeExportTasks_RequestSyntax"></a>

```
{
   "limit": {{number}},
   "nextToken": "{{string}}",
   "statusCode": "{{string}}",
   "taskId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeExportTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [limit](#API_DescribeExportTasks_RequestSyntax) **   <a name="CWL-DescribeExportTasks-request-limit"></a>
The maximum number of items returned. If you don't specify a value, the default is up to 50 items.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_DescribeExportTasks_RequestSyntax) **   <a name="CWL-DescribeExportTasks-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [statusCode](#API_DescribeExportTasks_RequestSyntax) **   <a name="CWL-DescribeExportTasks-request-statusCode"></a>
The status code of the export task. Specifying a status code filters the results to zero or more export tasks.
Type: String
Valid Values: `CANCELLED | COMPLETED | FAILED | PENDING | PENDING_CANCEL | RUNNING`
Required: No

 ** [taskId](#API_DescribeExportTasks_RequestSyntax) **   <a name="CWL-DescribeExportTasks-request-taskId"></a>
The ID of the export task. Specifying a task ID filters the results to one or zero export tasks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_DescribeExportTasks_ResponseSyntax"></a>

```
{
   "exportTasks": [
      {
         "destination": "string",
         "destinationPrefix": "string",
         "executionInfo": {
            "completionTime": number,
            "creationTime": number
         },
         "from": number,
         "logGroupName": "string",
         "status": {
            "code": "string",
            "message": "string"
         },
         "taskId": "string",
         "taskName": "string",
         "to": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeExportTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exportTasks](#API_DescribeExportTasks_ResponseSyntax) **   <a name="CWL-DescribeExportTasks-response-exportTasks"></a>
The export tasks.
Type: Array of [ExportTask](API_ExportTask.md) objects

 ** [nextToken](#API_DescribeExportTasks_ResponseSyntax) **   <a name="CWL-DescribeExportTasks-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeExportTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_DescribeExportTasks_Examples"></a>

### To list the export tasks that are complete
<a name="API_DescribeExportTasks_Example_1"></a>

The following example lists the export tasks with the `COMPLETE` status.

#### Sample Request
<a name="API_DescribeExportTasks_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.DescribeExportTasks
{
  "statusCode": "COMPLETE"
}
```

#### Sample Response
<a name="API_DescribeExportTasks_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "exportTasks": [
    {
      "taskId": "exampleTaskId",
      "taskName": "my-task-1",
      "logGroupName": "my-log-group",
      "from": 1437584472382,
      "to": 1437584472833,
      "destination": "my-destination",
      "destinationPrefix": "my-prefix",
      "status":
        {
          "code": "COMPLETE",
          "message": "Example message"
        },
      "executionInfo":
        {
          "creationTime": 1437584472856,
          "completionTime" : 1437584472986
        }
    },
    {
      "taskId": "exampleTaskId",
      "taskName": "my-task-2",
      "logGroupName": "my-log-group",
      "from": 1437584472382,
      "to": 1437584472833,
      "destination": "my-destination",
      "destinationPrefix": "my-prefix",
      "status":
        {
          "code": "COMPLETE",
          "message": "Example message"
        },
      "executionInfo":
        {
          "creationTime": 1437584472856,
          "completionTime" : 1437584472986
        }
    }
  ]
}
```

## See Also
<a name="API_DescribeExportTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeExportTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeExportTasks)
