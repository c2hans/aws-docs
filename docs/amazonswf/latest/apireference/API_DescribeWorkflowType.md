---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowType.html
---

# DescribeWorkflowType
<a name="API_DescribeWorkflowType"></a>

Returns information about the specified *workflow type*. This includes configuration settings specified when the type was registered and other information such as creation date, current status, etc.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the following parameters by using a `Condition` element with the appropriate keys.
  +  `workflowType.name`: String constraint. The key is `swf:workflowType.name`.
  +  `workflowType.version`: String constraint. The key is `swf:workflowType.version`.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_DescribeWorkflowType_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "workflowType": {
      "name": "{{string}}",
      "version": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_DescribeWorkflowType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_DescribeWorkflowType_RequestSyntax) **   <a name="SWF-DescribeWorkflowType-request-domain"></a>
The name of the domain in which this workflow type is registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [workflowType](#API_DescribeWorkflowType_RequestSyntax) **   <a name="SWF-DescribeWorkflowType-request-workflowType"></a>
The workflow type to describe.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

## Response Syntax
<a name="API_DescribeWorkflowType_ResponseSyntax"></a>

```
{
   "configuration": {
      "defaultChildPolicy": "string",
      "defaultExecutionStartToCloseTimeout": "string",
      "defaultLambdaRole": "string",
      "defaultTaskList": {
         "name": "string"
      },
      "defaultTaskPriority": "string",
      "defaultTaskStartToCloseTimeout": "string"
   },
   "typeInfo": {
      "creationDate": number,
      "deprecationDate": number,
      "description": "string",
      "status": "string",
      "workflowType": {
         "name": "string",
         "version": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeWorkflowType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_DescribeWorkflowType_ResponseSyntax) **   <a name="SWF-DescribeWorkflowType-response-configuration"></a>
Configuration settings of the workflow type registered through [RegisterWorkflowType](API_RegisterWorkflowType.md)
Type: [WorkflowTypeConfiguration](API_WorkflowTypeConfiguration.md) object

 ** [typeInfo](#API_DescribeWorkflowType_ResponseSyntax) **   <a name="SWF-DescribeWorkflowType-response-typeInfo"></a>
General information about the workflow type.
The status of the workflow type (returned in the WorkflowTypeInfo structure) can be one of the following.
+  `REGISTERED` – The type is registered and available. Workers supporting this type should be running.
+  `DEPRECATED` – The type was deprecated using [DeprecateWorkflowType](API_DeprecateWorkflowType.md), but is still in use. You should keep workers supporting this type running. You cannot create new workflow executions of this type.
Type: [WorkflowTypeInfo](API_WorkflowTypeInfo.md) object

## Errors
<a name="API_DescribeWorkflowType_Errors"></a>

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
<a name="API_DescribeWorkflowType_Examples"></a>

### DescribeWorkflowType Example
<a name="API_DescribeWorkflowType_Example_1"></a>

This example illustrates one usage of DescribeWorkflowType.

#### Sample Request
<a name="API_DescribeWorkflowType_Example_1_Request"></a>

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
X-Amz-Date: Sun, 15 Jan 2012 22:40:40 GMT
X-Amz-Target: SimpleWorkflowService.DescribeWorkflowType
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=iGt8t83OmrURqu0pKYbcW6mNdjXbFomevCBPUPQEbaM=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 102
Pragma: no-cache
Cache-Control: no-cache

{
  "domain": "867530901",
  "workflowType": {
  "version": "1.0",
  "name": "customerOrderWorkflow"
  }
}
```

#### Sample Response
<a name="API_DescribeWorkflowType_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 348
Content-Type: application/json
x-amzn-RequestId: f35a8e7f-3fc9-11e1-a23a-99d60383ae71

{
  "configuration": {
  "defaultExecutionStartToCloseTimeout": "3600",
  "defaultTaskStartToCloseTimeout": "600",
  "defaultTaskList": {"name": "mainTaskList"},
  "defaultTaskPriority": "10"
  "defaultChildPolicy": "TERMINATE"
  },
  "typeInfo": {
  "status": "REGISTERED",
  "creationDate": 1326481174.027,
  "description": "Handle customer orders",
  "workflowType": {
    "version": "1.0",
    "name": "customerOrderWorkflow"
  }
  }
}
```

## See Also
<a name="API_DescribeWorkflowType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/DescribeWorkflowType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DescribeWorkflowType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
