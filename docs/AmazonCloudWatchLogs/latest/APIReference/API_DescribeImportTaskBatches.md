---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeImportTaskBatches.html
---

# DescribeImportTaskBatches
<a name="API_DescribeImportTaskBatches"></a>

Gets detailed information about the individual batches within an import task, including their status and any error messages. For CloudTrail Event Data Store sources, a batch refers to a subset of stored events grouped by their eventTime.

## Request Syntax
<a name="API_DescribeImportTaskBatches_RequestSyntax"></a>

```
{
   "batchImportStatus": [ "{{string}}" ],
   "importId": "{{string}}",
   "limit": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImportTaskBatches_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [batchImportStatus](#API_DescribeImportTaskBatches_RequestSyntax) **   <a name="CWL-DescribeImportTaskBatches-request-batchImportStatus"></a>
Optional filter to list import batches by their status. Accepts multiple status values: IN\_PROGRESS, CANCELLED, COMPLETED and FAILED.
Type: Array of strings
Valid Values: `IN_PROGRESS | CANCELLED | COMPLETED | FAILED`
Required: No

 ** [importId](#API_DescribeImportTaskBatches_RequestSyntax) **   <a name="CWL-DescribeImportTaskBatches-request-importId"></a>
The ID of the import task to get batch information for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\-a-zA-Z0-9]+`
Required: Yes

 ** [limit](#API_DescribeImportTaskBatches_RequestSyntax) **   <a name="CWL-DescribeImportTaskBatches-request-limit"></a>
The maximum number of import batches to return in the response. Default: 10
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_DescribeImportTaskBatches_RequestSyntax) **   <a name="CWL-DescribeImportTaskBatches-request-nextToken"></a>
The pagination token for the next set of results.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeImportTaskBatches_ResponseSyntax"></a>

```
{
   "importBatches": [
      {
         "batchId": "string",
         "errorMessage": "string",
         "status": "string"
      }
   ],
   "importId": "string",
   "importSourceArn": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeImportTaskBatches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [importBatches](#API_DescribeImportTaskBatches_ResponseSyntax) **   <a name="CWL-DescribeImportTaskBatches-response-importBatches"></a>
The list of import batches that match the request filters.
Type: Array of [ImportBatch](API_ImportBatch.md) objects

 ** [importId](#API_DescribeImportTaskBatches_ResponseSyntax) **   <a name="CWL-DescribeImportTaskBatches-response-importId"></a>
The ID of the import task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\-a-zA-Z0-9]+`

 ** [importSourceArn](#API_DescribeImportTaskBatches_ResponseSyntax) **   <a name="CWL-DescribeImportTaskBatches-response-importSourceArn"></a>
The ARN of the source being imported from.
Type: String

 ** [nextToken](#API_DescribeImportTaskBatches_ResponseSyntax) **   <a name="CWL-DescribeImportTaskBatches-response-nextToken"></a>
The token to use when requesting the next set of results. Not present if there are no additional results to retrieve.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeImportTaskBatches_Errors"></a>

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
<a name="API_DescribeImportTaskBatches_Examples"></a>

### To describe import task batches
<a name="API_DescribeImportTaskBatches_Example_1"></a>

The following example retrieves batch-level details for an import task with status filtering.

#### Sample Request
<a name="API_DescribeImportTaskBatches_Example_1_Request"></a>

```
POST / HTTP/1.1
          Host: logs.<region>.<domain>
          X-Amz-Target: Logs_20140328.DescribeImportTaskBatches
          {
          "importId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
          "batchImportStatus": ["IN_PROGRESS", "COMPLETED"],
          "limit": 25,
          "nextToken": "eyJOZXh0VG9rZW4iOiJudWxsIiwiYm90b190cnVuY2F0ZV9hbW91bnQiOjF9"
          }
```

#### Sample Response
<a name="API_DescribeImportTaskBatches_Example_1_Response"></a>

```
HTTP/1.1 200 OK
          {
          "importSourceArn": "arn:aws:cloudtrail:us-west-2:123456789012:eventdatastore/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb",
          "importId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
          "importBatches": [
          {
          "batchId": "b1c2d3e4-f5g6-7890-hijk-lm1234567890",
          "status": "COMPLETED"
          },
          {
          "batchId": "c2d3e4f5-g6h7-8901-ijkl-mn2345678901",
          "status": "IN_PROGRESS"
          },
          {
          "batchId": "d3e4f5g6-h7i8-9012-jklm-no3456789012",
          "status": "FAILED",
          "errorMessage": "Access denied to CloudTrail event data store"
          }
          ],
          "nextToken": "eyJOZXh0VG9rZW4iOiJudWxsIiwiYm90b190cnVuY2F0ZV9hbW91bnQiOjJ9"
          }
```

## See Also
<a name="API_DescribeImportTaskBatches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeImportTaskBatches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeImportTaskBatches)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
