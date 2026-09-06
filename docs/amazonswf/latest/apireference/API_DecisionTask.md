---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DecisionTask.html
---

# DecisionTask
<a name="API_DecisionTask"></a>

A structure that represents a decision task. Decision tasks are sent to deciders in order for them to make decisions.

## Contents
<a name="API_DecisionTask_Contents"></a>

 ** events **   <a name="SWF-Type-DecisionTask-events"></a>
A paginated list of history events of the workflow execution. The decider uses this during the processing of the decision task.
Type: Array of [HistoryEvent](API_HistoryEvent.md) objects
Required: Yes

 ** startedEventId **   <a name="SWF-Type-DecisionTask-startedEventId"></a>
The ID of the `DecisionTaskStarted` event recorded in the history.
Type: Long
Required: Yes

 ** taskToken **   <a name="SWF-Type-DecisionTask-taskToken"></a>
The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** workflowExecution **   <a name="SWF-Type-DecisionTask-workflowExecution"></a>
The workflow execution for which this decision task was created.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: Yes

 ** workflowType **   <a name="SWF-Type-DecisionTask-workflowType"></a>
The type of the workflow execution for which this decision task was created.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

 ** nextPageToken **   <a name="SWF-Type-DecisionTask-nextPageToken"></a>
If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken`. Keep all other arguments unchanged.
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** previousStartedEventId **   <a name="SWF-Type-DecisionTask-previousStartedEventId"></a>
The ID of the DecisionTaskStarted event of the previous decision task of this workflow execution that was processed by the decider. This can be used to determine the events in the history new since the last decision task received by the decider.
Type: Long
Required: No

## See Also
<a name="API_DecisionTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DecisionTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DecisionTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DecisionTask)
