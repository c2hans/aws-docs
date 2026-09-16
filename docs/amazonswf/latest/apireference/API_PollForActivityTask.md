---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForActivityTask.html
---

# PollForActivityTask
<a name="API_PollForActivityTask"></a>

Used by workers to get an [ActivityTask](API_ActivityTask.md) from the specified activity `taskList`. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available. The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns an empty result. An empty result, in this context, means that an ActivityTask is returned, but that the value of taskToken is an empty string. If a task is returned, the worker should use its type to identify and process it correctly.

**Important**
Workers should set their client side socket timeout to at least 70 seconds (10 seconds higher than the maximum time service may hold the poll request).

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the `taskList.name` parameter by using a `Condition` element with the `swf:taskList.name` key to allow the action to access only certain task lists.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_PollForActivityTask_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "identity": "{{string}}",
   "taskList": {
      "name": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_PollForActivityTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_PollForActivityTask_RequestSyntax) **   <a name="SWF-PollForActivityTask-request-domain"></a>
The name of the domain that contains the task lists being polled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [identity](#API_PollForActivityTask_RequestSyntax) **   <a name="SWF-PollForActivityTask-request-identity"></a>
Identity of the worker making the request, recorded in the `ActivityTaskStarted` event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [taskList](#API_PollForActivityTask_RequestSyntax) **   <a name="SWF-PollForActivityTask-request-taskList"></a>
Specifies the task list to poll for activity tasks.
The specified string must not start or end with whitespace. It must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: [TaskList](API_TaskList.md) object
Required: Yes

## Response Syntax
<a name="API_PollForActivityTask_ResponseSyntax"></a>

```
{
   "activityId": "string",
   "activityType": {
      "name": "string",
      "version": "string"
   },
   "input": "string",
   "startedEventId": number,
   "taskToken": "string",
   "workflowExecution": {
      "runId": "string",
      "workflowId": "string"
   }
}
```

## Response Elements
<a name="API_PollForActivityTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activityId](#API_PollForActivityTask_ResponseSyntax) **   <a name="SWF-PollForActivityTask-response-activityId"></a>
The unique ID of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [activityType](#API_PollForActivityTask_ResponseSyntax) **   <a name="SWF-PollForActivityTask-response-activityType"></a>
The type of this activity task.
Type: [ActivityType](API_ActivityType.md) object

 ** [input](#API_PollForActivityTask_ResponseSyntax) **   <a name="SWF-PollForActivityTask-response-input"></a>
The inputs provided when the activity task was scheduled. The form of the input is user defined and should be meaningful to the activity implementation.
Type: String
Length Constraints: Maximum length of 32768.

 ** [startedEventId](#API_PollForActivityTask_ResponseSyntax) **   <a name="SWF-PollForActivityTask-response-startedEventId"></a>
The ID of the `ActivityTaskStarted` event recorded in the history.
Type: Long

 ** [taskToken](#API_PollForActivityTask_ResponseSyntax) **   <a name="SWF-PollForActivityTask-response-taskToken"></a>
The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [workflowExecution](#API_PollForActivityTask_ResponseSyntax) **   <a name="SWF-PollForActivityTask-response-workflowExecution"></a>
The workflow execution that started this activity task.
Type: [WorkflowExecution](API_WorkflowExecution.md) object

## Errors
<a name="API_PollForActivityTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededFault **
Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

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
<a name="API_PollForActivityTask_Examples"></a>

### PollForActivityTask Example
<a name="API_PollForActivityTask_Example_1"></a>

This example illustrates one usage of PollForActivityTask.

#### Sample Request
<a name="API_PollForActivityTask_Example_1_Request"></a>

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
X-Amz-Date: Mon, 16 Jan 2012 03:53:52 GMT
X-Amz-Target: SimpleWorkflowService.PollForActivityTask
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=dv0H1RPYucoIcRckspWO0f8xG120MWZRKmj3O5/A4rY=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 108
Pragma: no-cache
Cache-Control: no-cache

{"domain": "867530901",
"taskList":
{"name": "mainTaskList"},
"identity": "VerifyCreditCardWorker01"}
```

#### Sample Response
<a name="API_PollForActivityTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 837
Content-Type: application/json
x-amzn-RequestId: b48fb6b5-3ff5-11e1-a23a-99d60383ae71

{"activityId": "verification-27",
"activityType":
{"name": "activityVerify",
"version": "1.0"},
"input": "5634-0056-4367-0923,12/12,437",
"startedEventId": 11,
"taskToken": "AAAAKgAAAAEAAAAAAAAAAX9p3pcp3857oLXFUuwdxRU5/zmn9f40XaMF7VohAH4jOtjXpZu7GdOzEi0b3cWYHbG5b5dpdcTXHUDPVMHXiUxCgr+Nc/wUW9016W4YxJGs/jmxzPln8qLftU+SW135Q0UuKp5XRGoRTJp3tbHn2pY1vC8gDB/K69J6q668U1pd4Cd9o43//lGgOIjN0/Ihg+DO+83HNcOuVEQMM28kNMXf7yePh31M4dMKJwQaQZG13huJXDwzJOoZQz+XFuqFly+lPnCE4XvsnhfAvTsh50EtNDEtQzPCFJoUeld9g64V/FS/39PHL3M93PBUuroPyHuCwHsNC6fZ7gM/XOKmW4kKnXPoQweEUkFV/J6E6+M1reBO7nJADTrLSnajg6MY/viWsEYmMw/DS5FlquFaDIhFkLhWUWN+V2KqiKS23GYwpzgZ7fgcWHQF2NLEY3zrjam4LW/UW5VLCyM3FpVD3erCTi9IvUgslPzyVGuWNAoTmgJEWvimgwiHxJMxxc9JBDR390iMmImxVl3eeSDUWx8reQltiviadPDjyRmVhYP8",
"workflowExecution":
{"runId": "cfa2bd33-31b0-4b75-b131-255bb0d97b3f",
"workflowId": "20110927-T-1"}
}
```

## See Also
<a name="API_PollForActivityTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/PollForActivityTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/PollForActivityTask)
