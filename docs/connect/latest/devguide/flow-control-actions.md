---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-control-actions.html
---

# Flow control actions in the Connect Customer Flow language
<a name="flow-control-actions"></a>

These actions don't have any side effects and are only used to determine the path through a flow. Certain data may not be available (such as contact data, if the action is determining its path based on contact data). These actions generally work in every circumstance.

A flow control action is an action that:
+ Does not need a contact or a participant to succeed.
+ Controls the behavior of the flow, by either enabling or disabling flow behavior (such as logging) or by choosing a branch when the flow runs.

**Topics**
+ [CheckHoursOfOperation](flow-control-actions-checkhoursofoperation.md)
+ [CheckMetricData](flow-control-actions-checkmetricdata.md)
+ [CheckOutboundCallStatus](flow-control-actions-checkoutboundcallstatus.md)
+ [CheckVoiceId](flow-control-actions-checkvoiceid.md)
+ [Compare](flow-control-actions-compare.md)
+ [DistributeByPercentage](flow-control-actions-distributebypercentage.md)
+ [EndFlowExecution](flow-control-actions-endflowexecution.md)
+ [GetMetricData](flow-control-actions-getmetricdata.md)
+ [Loop](flow-control-actions-loop.md)
+ [StartVoiceIdStream](flow-control-actions-startvoiceidstream.md)
+ [TransferToFlow](flow-control-actions-transfertoflow.md)
+ [UpdateFlowAttributes](flow-control-actions-updateflowattributes.md)
+ [UpdateFlowLoggingBehavior](flow-control-actions-updateflowloggingbehavior.md)
+ [UpdateRoutingCriteria](flow-control-actions-updateroutingcriteria.md)
+ [Wait](flow-control-actions-wait.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
