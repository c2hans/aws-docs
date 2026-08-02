---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteWorkflowType.html
---

# DeleteWorkflowType
<a name="API_DeleteWorkflowType"></a>

Deletes the specified *workflow type*.

Note: Prior to deletion, workflow types must first be **deprecated**.

 After a workflow type has been deleted, you cannot create new executions of that type. Executions that started before the type was deleted will continue to run.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the following parameters by using a `Condition` element with the appropriate keys.
  +  `workflowType.name`: String constraint. The key is `swf:workflowType.name`.
  +  `workflowType.version`: String constraint. The key is `swf:workflowType.version`.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_DeleteWorkflowType_RequestSyntax"></a>

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
<a name="API_DeleteWorkflowType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_DeleteWorkflowType_RequestSyntax) **   <a name="SWF-DeleteWorkflowType-request-domain"></a>
The name of the domain in which the workflow type is registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [workflowType](#API_DeleteWorkflowType_RequestSyntax) **   <a name="SWF-DeleteWorkflowType-request-workflowType"></a>
The workflow type to delete.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

## Response Elements
<a name="API_DeleteWorkflowType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWorkflowType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** TypeNotDeprecatedFault **
Returned when the resource type has not been deprecated.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWorkflowType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/DeleteWorkflowType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DeleteWorkflowType)
