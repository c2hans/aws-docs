---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteMatchingWorkflow.html
---

# DeleteMatchingWorkflow
<a name="API_DeleteMatchingWorkflow"></a>

Deletes the `MatchingWorkflow` with a given name. This operation returns a `ResourceNotFoundException` if a workflow with the given name does not exist.

## Request Syntax
<a name="API_DeleteMatchingWorkflow_RequestSyntax"></a>

```
DELETE /matchingworkflows/{{workflowName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMatchingWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowName](#API_DeleteMatchingWorkflow_RequestSyntax) **   <a name="API-DeleteMatchingWorkflow-request-uri-workflowName"></a>
The name of the workflow to be retrieved.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_DeleteMatchingWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMatchingWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "message": "string"
}
```

## Response Elements
<a name="API_DeleteMatchingWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [message](#API_DeleteMatchingWorkflow_ResponseSyntax) **   <a name="API-DeleteMatchingWorkflow-response-message"></a>
A successful operation message.
Type: String

## Errors
<a name="API_DeleteMatchingWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_DeleteMatchingWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/DeleteMatchingWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/DeleteMatchingWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
