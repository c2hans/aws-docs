---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CancelFlowExecutions.html
---

# CancelFlowExecutions
<a name="API_CancelFlowExecutions"></a>

Cancels active runs for a flow.

You can cancel all of the active runs for a flow, or you can cancel specific runs by providing their IDs.

You can cancel a flow run only when the run is in progress. You can't cancel a run that has already completed or failed. You also can't cancel a run that's scheduled to occur but hasn't started yet. To prevent a scheduled run, you can deactivate the flow with the `StopFlow` action.

You cannot resume a run after you cancel it.

When you send your request, the status for each run becomes `CancelStarted`. When the cancellation completes, the status becomes `Canceled`.

**Note**
When you cancel a run, you still incur charges for any data that the run already processed before the cancellation. If the run had already written some data to the flow destination, then that data remains in the destination. If you configured the flow to use a batch API (such as the Salesforce Bulk API 2.0), then the run will finish reading or writing its entire batch of data after the cancellation. For these operations, the data processing charges for Amazon AppFlow apply. For the pricing information, see [Amazon AppFlow pricing](http://aws.amazon.com/appflow/pricing/).

## Request Syntax
<a name="API_CancelFlowExecutions_RequestSyntax"></a>

```
POST /cancel-flow-executions HTTP/1.1
Content-type: application/json

{
   "executionIds": [ "{{string}}" ],
   "flowName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelFlowExecutions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CancelFlowExecutions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [executionIds](#API_CancelFlowExecutions_RequestSyntax) **   <a name="appflow-CancelFlowExecutions-request-executionIds"></a>
The ID of each active run to cancel. These runs must belong to the flow you specify in your request.
If you omit this parameter, your request ends all active runs that belong to the flow.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** [flowName](#API_CancelFlowExecutions_RequestSyntax) **   <a name="appflow-CancelFlowExecutions-request-flowName"></a>
The name of a flow with active runs that you want to cancel.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: Yes

## Response Syntax
<a name="API_CancelFlowExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "invalidExecutions": [ "string" ]
}
```

## Response Elements
<a name="API_CancelFlowExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [invalidExecutions](#API_CancelFlowExecutions_ResponseSyntax) **   <a name="appflow-CancelFlowExecutions-response-invalidExecutions"></a>
The IDs of runs that Amazon AppFlow couldn't cancel. These runs might be ineligible for canceling because they haven't started yet or have already completed.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Maximum length of 256.
Pattern: `\S+`

## Errors
<a name="API_CancelFlowExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
AppFlow/Requester has invalid or missing permissions.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** ThrottlingException **
API calls have exceeded the maximum allowed API request rate per account and per Region.
HTTP Status Code: 429

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_CancelFlowExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/CancelFlowExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/CancelFlowExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
