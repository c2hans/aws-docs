---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeFlowExecutionRecords.html
---

# DescribeFlowExecutionRecords
<a name="API_DescribeFlowExecutionRecords"></a>

 Fetches the execution history of the flow.

## Request Syntax
<a name="API_DescribeFlowExecutionRecords_RequestSyntax"></a>

```
POST /describe-flow-execution-records HTTP/1.1
Content-type: application/json

{
   "flowName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeFlowExecutionRecords_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeFlowExecutionRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [flowName](#API_DescribeFlowExecutionRecords_RequestSyntax) **   <a name="appflow-DescribeFlowExecutionRecords-request-flowName"></a>
 The specified name of the flow. Spaces are not allowed. Use underscores (\_) or hyphens (-) only.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: Yes

 ** [maxResults](#API_DescribeFlowExecutionRecords_RequestSyntax) **   <a name="appflow-DescribeFlowExecutionRecords-request-maxResults"></a>
 Specifies the maximum number of items that should be returned in the result set. The default for `maxResults` is 20 (for all paginated API operations).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeFlowExecutionRecords_RequestSyntax) **   <a name="appflow-DescribeFlowExecutionRecords-request-nextToken"></a>
 The pagination token for the next page of data.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_DescribeFlowExecutionRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowExecutions": [
      {
         "dataPullEndTime": number,
         "dataPullStartTime": number,
         "executionId": "string",
         "executionResult": {
            "bytesProcessed": number,
            "bytesWritten": number,
            "errorInfo": {
               "executionMessage": "string",
               "putFailuresCount": number
            },
            "maxPageSize": number,
            "numParallelProcesses": number,
            "recordsProcessed": number
         },
         "executionStatus": "string",
         "lastUpdatedAt": number,
         "metadataCatalogDetails": [
            {
               "catalogType": "string",
               "partitionRegistrationOutput": {
                  "message": "string",
                  "result": "string",
                  "status": "string"
               },
               "tableName": "string",
               "tableRegistrationOutput": {
                  "message": "string",
                  "result": "string",
                  "status": "string"
               }
            }
         ],
         "startedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFlowExecutionRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowExecutions](#API_DescribeFlowExecutionRecords_ResponseSyntax) **   <a name="appflow-DescribeFlowExecutionRecords-response-flowExecutions"></a>
 Returns a list of all instances when this flow was run.
Type: Array of [ExecutionRecord](API_ExecutionRecord.md) objects

 ** [nextToken](#API_DescribeFlowExecutionRecords_ResponseSyntax) **   <a name="appflow-DescribeFlowExecutionRecords-response-nextToken"></a>
 The pagination token for the next page of data.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`

## Errors
<a name="API_DescribeFlowExecutionRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_DescribeFlowExecutionRecords_Examples"></a>

### DescribeFlowExecutionRecords examples
<a name="API_DescribeFlowExecutionRecords_Example_1"></a>

This example shows sample requests and responses for the `DescribeFlowExecutionRecords` API.

#### Sample Request
<a name="API_DescribeFlowExecutionRecords_Example_1_Request"></a>

```
{
  "flowName": "name",
  "maxResults": 1
}
```

#### Sample Response
<a name="API_DescribeFlowExecutionRecords_Example_1_Response"></a>

```
{
  "flowExecutionList": [
    {
      "executionId": "Execution_ID",
      "executionMessage": "Request failed with Trendmicro Status Code 404: , RequestId: RequestId_value",
      "executionMetadata":
      {
        "bytesProcessed": 234,
        "bytesWritten": 0,
        "numFailures": 878,
        "numFilteredRecords": 0,
        "numPutFailures": 978978,
        "reason": null,
        "recordsProcessed": 23342,
        "terminateFlow": false
      },
      "executionResult":
      {
        "bytesProcessed": 234,
        "bytesWritten": 0,
        "errorInfo":
        {
          "executionMessage": "Request failed with Trendmicro Status Code 404: , RequestId: RequestId_value",
          "putFailuresCount": 978978
        },
        "recordsProcessed": 23342
      },
      "executionStartTime": "2022-02-22T15:31:41.467000-08:00",
      "executionStatus": "Error",
      "lastUpdatedAt": "2022-02-22T15:31:41.467000-08:00",
      "startedAt": "2022-02-22T15:31:41.467000-08:00"
    }
  ],
  "nextToken": "next_token_value"
}
```

#### Sample Request
<a name="API_DescribeFlowExecutionRecords_Example_1_Request"></a>

```
{
  "flowName": "test-new-create",
  "maxResults": 1,
  "nextToken": "next_token_value"
}
```

#### Sample Response
<a name="API_DescribeFlowExecutionRecords_Example_1_Response"></a>

```
{
  "flowExecutionList": [
    {
      "executionId": "execution_id_value",
      "executionMessage": "Request failed with Trendmicro Status Code 404: , RequestId: RequestId_value",
      "executionMetadata": {
        "bytesProcessed": 234,
        "bytesWritten": 0,
        "numFailures": 0,
        "numFilteredRecords": 0,
        "numPutFailures": 0,
        "reason": null,
        "recordsProcessed": 23342,
        "terminateFlow": false
      },
      "executionResult": {
        "bytesProcessed": 234,
        "bytesWritten": 0,
        "errorInfo": null,
        "recordsProcessed": 23342
      },
      "executionStartTime": "execution_start_time_value",
      "executionStatus": "Successful",
      "lastUpdatedAt": "lastupdated_at_value",
      "lastUpdatedTime": "lastupdated_time_value",
      "startedAt": "started_at_value"
    }
  ],
  "nextToken": "next_token_value"
}
```

#### Sample Request
<a name="API_DescribeFlowExecutionRecords_Example_1_Request"></a>

```
{
  "flowName": "name",
  "maxResults": 1,
  "nextToken": "next_token_value"
}
```

#### Sample Response
<a name="API_DescribeFlowExecutionRecords_Example_1_Response"></a>

```
{
  "flowExecutionList": [
    {
      "executionId": "execution_id_value-delete",
      "executionMessage": "Request failed with Trendmicro Status Code 404: , RequestId: RequestId_value",
      "executionMetadata": {
        "bytesProcessed": 0,
        "bytesWritten": 0,
        "numFailures": 0,
        "numFilteredRecords": 0,
        "numPutFailures": 0,
        "reason": null,
        "recordsProcessed": 0,
        "terminateFlow": false
      },
      "executionResult": {
        "bytesProcessed": 0,
        "bytesWritten": 0,
        "errorInfo": {
          "executionMessage": "Request failed with Trendmicro Status Code 404: , RequestId: RequestId_value",
          "putFailuresCount": 0
        },
        "recordsProcessed": 0
      },
      "executionStartTime": "execution_start_time_value",
      "executionStatus": "Error",
      "lastUpdatedAt": "lastupdated_at_value",
      "lastUpdatedTime": "lastupdated_time_value",
      "startedAt": "started_at_value"
    }
  ],
  "nextToken": "next_token_value"
}
```

## See Also
<a name="API_DescribeFlowExecutionRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/DescribeFlowExecutionRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DescribeFlowExecutionRecords)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
