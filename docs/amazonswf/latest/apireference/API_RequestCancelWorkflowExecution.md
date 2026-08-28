---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelWorkflowExecution.html
---

# RequestCancelWorkflowExecution
<a name="API_RequestCancelWorkflowExecution"></a>

Records a `WorkflowExecutionCancelRequested` event in the currently running workflow execution identified by the given domain, workflowId, and runId. This logically requests the cancellation of the workflow execution as a whole. It is up to the decider to take appropriate actions when it receives an execution history with this event.

**Note**
If the runId isn't specified, the `WorkflowExecutionCancelRequested` event is recorded in the history of the current open workflow execution with the specified workflowId in the domain.

**Note**
Because this action allows the workflow to properly clean up and gracefully close, it should be used instead of [TerminateWorkflowExecution](API_TerminateWorkflowExecution.md) when possible.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ You cannot use an IAM policy to constrain this action's parameters.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_RequestCancelWorkflowExecution_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "runId": "{{string}}",
   "workflowId": "{{string}}"
}
```

## Request Parameters
<a name="API_RequestCancelWorkflowExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_RequestCancelWorkflowExecution_RequestSyntax) **   <a name="SWF-RequestCancelWorkflowExecution-request-domain"></a>
The name of the domain containing the workflow execution to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [runId](#API_RequestCancelWorkflowExecution_RequestSyntax) **   <a name="SWF-RequestCancelWorkflowExecution-request-runId"></a>
The runId of the workflow execution to cancel.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** [workflowId](#API_RequestCancelWorkflowExecution_RequestSyntax) **   <a name="SWF-RequestCancelWorkflowExecution-request-workflowId"></a>
The workflowId of the workflow execution to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Elements
<a name="API_RequestCancelWorkflowExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RequestCancelWorkflowExecution_Errors"></a>

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
<a name="API_RequestCancelWorkflowExecution_Examples"></a>

### RequestCancelWorkflowExecution Example
<a name="API_RequestCancelWorkflowExecution_Example_1"></a>

This example illustrates one usage of RequestCancelWorkflowExecution.

#### Sample Request
<a name="API_RequestCancelWorkflowExecution_Example_1_Request"></a>

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
X-Amz-Date: Mon, 16 Jan 2012 04:49:06 GMT
X-Amz-Target: SimpleWorkflowService.RequestCancelWorkflowExecution
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=xODwV3kbpJbWVa6bQiV2zQAw9euGI3uXI82urc+bVeo=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 106
Pragma: no-cache
Cache-Control: no-cache

{"domain": "867530901",
"workflowId": "20110927-T-1",
"runId": "94861fda-a714-4126-95d7-55ba847da8ab"}
```

#### Sample Response
<a name="API_RequestCancelWorkflowExecution_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: 6bd0627e-3ffd-11e1-9b11-7182192d0b57
```

## See Also
<a name="API_RequestCancelWorkflowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/RequestCancelWorkflowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/RequestCancelWorkflowExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
