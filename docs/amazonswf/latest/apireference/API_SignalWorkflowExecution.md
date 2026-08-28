---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_SignalWorkflowExecution.html
---

# SignalWorkflowExecution
<a name="API_SignalWorkflowExecution"></a>

Records a `WorkflowExecutionSignaled` event in the workflow execution history and creates a decision task for the workflow execution identified by the given domain, workflowId and runId. The event is recorded with the specified user defined signalName and input (if provided).

**Note**
If a runId isn't specified, then the `WorkflowExecutionSignaled` event is recorded in the history of the current open workflow with the matching workflowId in the domain.

**Note**
If the specified workflow execution isn't open, this method fails with `UnknownResource`.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ You cannot use an IAM policy to constrain this action's parameters.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_SignalWorkflowExecution_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "input": "{{string}}",
   "runId": "{{string}}",
   "signalName": "{{string}}",
   "workflowId": "{{string}}"
}
```

## Request Parameters
<a name="API_SignalWorkflowExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_SignalWorkflowExecution_RequestSyntax) **   <a name="SWF-SignalWorkflowExecution-request-domain"></a>
The name of the domain containing the workflow execution to signal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [input](#API_SignalWorkflowExecution_RequestSyntax) **   <a name="SWF-SignalWorkflowExecution-request-input"></a>
Data to attach to the `WorkflowExecutionSignaled` event in the target workflow execution's history.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** [runId](#API_SignalWorkflowExecution_RequestSyntax) **   <a name="SWF-SignalWorkflowExecution-request-runId"></a>
The runId of the workflow execution to signal.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** [signalName](#API_SignalWorkflowExecution_RequestSyntax) **   <a name="SWF-SignalWorkflowExecution-request-signalName"></a>
The name of the signal. This name must be meaningful to the target workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [workflowId](#API_SignalWorkflowExecution_RequestSyntax) **   <a name="SWF-SignalWorkflowExecution-request-workflowId"></a>
The workflowId of the workflow execution to signal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Elements
<a name="API_SignalWorkflowExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SignalWorkflowExecution_Errors"></a>

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
<a name="API_SignalWorkflowExecution_Examples"></a>

### SignalWorkflowExecution Example
<a name="API_SignalWorkflowExecution_Example_1"></a>

This example illustrates one usage of SignalWorkflowExecution.

#### Sample Request
<a name="API_SignalWorkflowExecution_Example_1_Request"></a>

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
X-Amz-Date: Sun, 15 Jan 2012 00:06:18 GMT
X-Amz-Target: SimpleWorkflowService.SignalWorkflowExecution
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=lQpBZezK7JNQrXeWuJE+l7S0ZwjOEONCeRyImoyfX+E=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 162
Pragma: no-cache
Cache-Control: no-cache

{"domain": "867530901",
"workflowId": "20110927-T-1",
"runId": "f5ebbac6-941c-4342-ad69-dfd2f8be6689",
"signalName": "CancelOrder",
"input": "order 3553"}
```

#### Sample Response
<a name="API_SignalWorkflowExecution_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: bf78ae15-3f0c-11e1-9914-a356b6ea8bdf
```

## See Also
<a name="API_SignalWorkflowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/SignalWorkflowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/SignalWorkflowExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
