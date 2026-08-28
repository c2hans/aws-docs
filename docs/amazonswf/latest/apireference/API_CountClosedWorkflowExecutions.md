---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountClosedWorkflowExecutions.html
---

# CountClosedWorkflowExecutions
<a name="API_CountClosedWorkflowExecutions"></a>

Returns the number of closed workflow executions within the given domain that meet the specified filtering criteria.

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
<a name="API_CountClosedWorkflowExecutions_RequestSyntax"></a>

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
<a name="API_CountClosedWorkflowExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [closeStatusFilter](#API_CountClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-request-closeStatusFilter"></a>
If specified, only workflow executions that match this close status are counted. This filter has an affect only if `executionStatus` is specified as `CLOSED`.
 `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.
Type: [CloseStatusFilter](API_CloseStatusFilter.md) object
Required: No

 ** [closeTimeFilter](#API_CountClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-request-closeTimeFilter"></a>
If specified, only workflow executions that meet the close time criteria of the filter are counted.
 `startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must specify one of these in a request but not both.
Type: [ExecutionTimeFilter](API_ExecutionTimeFilter.md) object
Required: No

 ** [domain](#API_CountClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-request-domain"></a>
The name of the domain containing the workflow executions to count.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [executionFilter](#API_CountClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-request-executionFilter"></a>
If specified, only workflow executions matching the `WorkflowId` in the filter are counted.
 `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.
Type: [WorkflowExecutionFilter](API_WorkflowExecutionFilter.md) object
Required: No

 ** [startTimeFilter](#API_CountClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-request-startTimeFilter"></a>
If specified, only workflow executions that meet the start time criteria of the filter are counted.
 `startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must specify one of these in a request but not both.
Type: [ExecutionTimeFilter](API_ExecutionTimeFilter.md) object
Required: No

 ** [tagFilter](#API_CountClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-request-tagFilter"></a>
If specified, only executions that have a tag that matches the filter are counted.
 `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.
Type: [TagFilter](API_TagFilter.md) object
Required: No

 ** [typeFilter](#API_CountClosedWorkflowExecutions_RequestSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-request-typeFilter"></a>
If specified, indicates the type of the workflow executions to be counted.
 `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.
Type: [WorkflowTypeFilter](API_WorkflowTypeFilter.md) object
Required: No

## Response Syntax
<a name="API_CountClosedWorkflowExecutions_ResponseSyntax"></a>

```
{
   "count": number,
   "truncated": boolean
}
```

## Response Elements
<a name="API_CountClosedWorkflowExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [count](#API_CountClosedWorkflowExecutions_ResponseSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-response-count"></a>
The number of workflow executions.
Type: Integer
Valid Range: Minimum value of 0.

 ** [truncated](#API_CountClosedWorkflowExecutions_ResponseSyntax) **   <a name="SWF-CountClosedWorkflowExecutions-response-truncated"></a>
If set to true, indicates that the actual count was more than the maximum supported by this API and the count returned is the truncated value.
Type: Boolean

## Errors
<a name="API_CountClosedWorkflowExecutions_Errors"></a>

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
<a name="API_CountClosedWorkflowExecutions_Examples"></a>

### CountClosedWorkflowExecutions Example
<a name="API_CountClosedWorkflowExecutions_Example_1"></a>

This example illustrates one usage of CountClosedWorkflowExecutions.

#### Sample Request
<a name="API_CountClosedWorkflowExecutions_Example_1_Request"></a>

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
X-Amz-Date: Sun, 15 Jan 2012 02:42:47 GMT
X-Amz-Target: SimpleWorkflowService.CountClosedWorkflowExecutions
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=jFS74utjeATV7vj72CWdLToPCKW0RQse6OEDkafB+SA=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 157
Pragma: no-cache
Cache-Control: no-cache

{
  "domain": "867530901",
  "activityType": {
  "version": "1.0",
  "name": "activityVerify"
  }
}
```

#### Sample Response
<a name="API_CountClosedWorkflowExecutions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 29
Content-Type: application/json
x-amzn-RequestId: 9bfad387-3f22-11e1-9914-a356b6ea8bdf

{ "count":3, "truncated":false }
```

## See Also
<a name="API_CountClosedWorkflowExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/CountClosedWorkflowExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/CountClosedWorkflowExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
