---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListClosedWorkflowExecutions.html
---

# ListClosedWorkflowExecutions
<a name="API_ListClosedWorkflowExecutions"></a>

Returns a list of closed workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.

**Note**
This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the following parameters by using a `Condition` element with the appropriate keys.
  +  `tagFilter.tag`: String constraint. The key is `swf:tagFilter.tag`.
  +  `typeFilter.name`: String constraint. The key is `swf:typeFilter.name`.
  +  `typeFilter.version`: String constraint. The key is `swf:typeFilter.version`.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_ListClosedWorkflowExecutions_RequestSyntax"></a>

```
{
   "closeStatusFilter": {
      "status": "{{string}}"
   },
   "closeTimeFilter": {
      "latestDate": {{number}},
      "oldestDate": {{number}}
   },
   "domain": "{{string}}",
   "executionFilter": {
      "workflowId": "{{string}}"
   },
   "maximumPageSize": {{number}},
   "nextPageToken": "{{string}}",
   "reverseOrder": {{boolean}},
   "startTimeFilter": {
      "latestDate": {{number}},
      "oldestDate": {{number}}
   },
   "tagFilter": {
      "tag": "{{string}}"
   },
   "typeFilter": {
      "name": "{{string}}",
      "version": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListClosedWorkflowExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [closeStatusFilter](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-closeStatusFilter"></a>
If specified, only workflow executions that match this *close status* are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.
 `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.
Type: [CloseStatusFilter](API_CloseStatusFilter.md) object
Required: No

 ** [closeTimeFilter](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-closeTimeFilter"></a>
If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.
 `startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must specify one of these in a request but not both.
Type: [ExecutionTimeFilter](API_ExecutionTimeFilter.md) object
Required: No

 ** [domain](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-domain"></a>
The name of the domain that contains the workflow executions to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [executionFilter](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-executionFilter"></a>
If specified, only workflow executions matching the workflow ID specified in the filter are returned.
 `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.
Type: [WorkflowExecutionFilter](API_WorkflowExecutionFilter.md) object
Required: No

 ** [maximumPageSize](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-maximumPageSize"></a>
The maximum number of results that are returned per call. Use `nextPageToken` to obtain further pages of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [nextPageToken](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-nextPageToken"></a>
If `NextPageToken` is returned there are more results available. The value of `NextPageToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a `400` error: "`Specified token has exceeded its maximum lifetime`".
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [reverseOrder](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-reverseOrder"></a>
When set to `true`, returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.
Type: Boolean
Required: No

 ** [startTimeFilter](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-startTimeFilter"></a>
If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.
 `startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must specify one of these in a request but not both.
Type: [ExecutionTimeFilter](API_ExecutionTimeFilter.md) object
Required: No

 ** [tagFilter](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-tagFilter"></a>
If specified, only executions that have the matching tag are listed.
 `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.
Type: [TagFilter](API_TagFilter.md) object
Required: No

 ** [typeFilter](#API_ListClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-request-typeFilter"></a>
If specified, only executions of the type specified in the filter are returned.
 `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.
Type: [WorkflowTypeFilter](API_WorkflowTypeFilter.md) object
Required: No

## Response Syntax
<a name="API_ListClosedWorkflowExecutions_ResponseSyntax"></a>

```
{
   "executionInfos": [
      {
         "cancelRequested": boolean,
         "closeStatus": "string",
         "closeTimestamp": number,
         "execution": {
            "runId": "string",
            "workflowId": "string"
         },
         "executionStatus": "string",
         "parent": {
            "runId": "string",
            "workflowId": "string"
         },
         "startTimestamp": number,
         "tagList": [ "string" ],
         "workflowType": {
            "name": "string",
            "version": "string"
         }
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_ListClosedWorkflowExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionInfos](#API_ListClosedWorkflowExecutions_ResponseSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-response-executionInfos"></a>
The list of workflow information structures.
Type: Array of [WorkflowExecutionInfo](API_WorkflowExecutionInfo.md) objects

 ** [nextPageToken](#API_ListClosedWorkflowExecutions_ResponseSyntax) **   <a name="SWF-ListClosedWorkflowExecutions-response-nextPageToken"></a>
If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken`. Keep all other arguments unchanged.
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.

## Errors
<a name="API_ListClosedWorkflowExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_ListClosedWorkflowExecutions_Examples"></a>

### ListClosedWorkflowExecutions Example
<a name="API_ListClosedWorkflowExecutions_Example_1"></a>

This example illustrates one usage of ListClosedWorkflowExecutions.

#### Sample Request
<a name="API_ListClosedWorkflowExecutions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: swf.us-east-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25 ( .NET CLR 3.5.30729; .NET4.0E)
Accept: application/json, text/javascript, */*
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
Content-Type: application/x-amz-json-1.0
X-Requested-With: XMLHttpRequest
X-Amz-Date: Sun, 15 Jan 2012 02:51:01 GMT
X-Amz-Target: SimpleWorkflowService.ListClosedWorkflowExecutions
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=WY9jGbf5E3F9smGJHANhEXz9VL+1oGVgNL0/o7cBxQw=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 150
Pragma: no-cache
Cache-Control: no-cache

{"domain": "867530901",
"closeTimeFilter":
{"oldestDate": 1325376070,
"latestDate": 1356998399},
"tagFilter":
{"tag": "ricoh-the-dog"}
}
```

#### Sample Response
<a name="API_ListClosedWorkflowExecutions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 1084
Content-Type: application/json
x-amzn-RequestId: c28b4df4-3f23-11e1-9e8f-57bb03e21482

{"executionInfos":
[
{"cancelRequested": false,
"closeStatus": "TIMED_OUT",
"closeTimestamp": 1326590754.654,
"execution":
{"runId": "c724e07a-b966-441f-a1c0-4831acbda1cd",
"workflowId": "20110927-T-1"},
"executionStatus": "CLOSED",
"startTimestamp": 1326587154.626,
"tagList":
["music purchase", "digital", "ricoh-the-dog"],
"workflowType":
{"name": "customerOrderWorkflow",
"version": "1.0"}
},
{"cancelRequested": false,
"closeStatus": "TIMED_OUT",
"closeTimestamp": 1326586831.628,
"execution":
{"runId": "f5ebbac6-941c-4342-ad69-dfd2f8be6689",
"workflowId": "20110927-T-1"},
"executionStatus": "CLOSED",
"startTimestamp": 1326585031.619,
"tagList":
["music purchase", "digital", "ricoh-the-dog"],
"workflowType":
{"name": "customerOrderWorkflow",
"version": "1.0"}
},
{"cancelRequested": false,
"closeStatus": "TIMED_OUT",
"closeTimestamp": 1326582914.031,
"execution":
{"runId": "1e536162-f1ea-48b0-85f3-aade88eef2f7",
"workflowId": "20110927-T-1"},
"executionStatus": "CLOSED",
"startTimestamp": 1326581114.02,
"tagList":
["music purchase", "digital", "ricoh-the-dog"],
"workflowType":
{"name": "customerOrderWorkflow",
"version": "1.0"}
}
]
}
```

## See Also
<a name="API_ListClosedWorkflowExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/ListClosedWorkflowExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ListClosedWorkflowExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
