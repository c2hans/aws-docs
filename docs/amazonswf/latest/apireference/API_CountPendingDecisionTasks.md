---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingDecisionTasks.html
---

# CountPendingDecisionTasks
<a name="API_CountPendingDecisionTasks"></a>

Returns the estimated number of decision tasks in the specified task list. The count returned is an approximation and isn't guaranteed to be exact. If you specify a task list that no decision task was ever scheduled in then `0` is returned.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the `taskList.name` parameter by using a `Condition` element with the `swf:taskList.name` key to allow the action to access only certain task lists.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_CountPendingDecisionTasks_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "taskList": {
      "name": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CountPendingDecisionTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_CountPendingDecisionTasks_RequestSyntax) **   <a name="SWF-CountPendingDecisionTasks-request-domain"></a>
The name of the domain that contains the task list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [taskList](#API_CountPendingDecisionTasks_RequestSyntax) **   <a name="SWF-CountPendingDecisionTasks-request-taskList"></a>
The name of the task list.
Type: [TaskList](API_TaskList.md) object
Required: Yes

## Response Syntax
<a name="API_CountPendingDecisionTasks_ResponseSyntax"></a>

```
{
   "count": number,
   "truncated": boolean
}
```

## Response Elements
<a name="API_CountPendingDecisionTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [count](#API_CountPendingDecisionTasks_ResponseSyntax) **   <a name="SWF-CountPendingDecisionTasks-response-count"></a>
The number of tasks in the task list.
Type: Integer
Valid Range: Minimum value of 0.

 ** [truncated](#API_CountPendingDecisionTasks_ResponseSyntax) **   <a name="SWF-CountPendingDecisionTasks-response-truncated"></a>
If set to true, indicates that the actual count was more than the maximum supported by this API and the count returned is the truncated value.
Type: Boolean

## Errors
<a name="API_CountPendingDecisionTasks_Errors"></a>

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
<a name="API_CountPendingDecisionTasks_Examples"></a>

### CountPendingDecisionTasks Example
<a name="API_CountPendingDecisionTasks_Example_1"></a>

This example illustrates one usage of CountPendingDecisionTasks.

#### Sample Request
<a name="API_CountPendingDecisionTasks_Example_1_Request"></a>

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
X-Amz-Date: Sun, 15 Jan 2012 23:25:57 GMT
X-Amz-Target: SimpleWorkflowService.CountPendingDecisionTasks
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=i9tUkWnZBLfn/T6BOymajCtwArAll6Stuh1x2C4dbsE=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 70
Pragma: no-cache
Cache-Control: no-cache

{"domain": "867530901",
"taskList":
{"name": "specialTaskList"}
}
```

#### Sample Response
<a name="API_CountPendingDecisionTasks_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 29
Content-Type: application/json
x-amzn-RequestId: 4718a364-3fd0-11e1-9914-a356b6ea8bdf

{"count": 2,
"truncated": false}
```

## See Also
<a name="API_CountPendingDecisionTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/CountPendingDecisionTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/CountPendingDecisionTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
