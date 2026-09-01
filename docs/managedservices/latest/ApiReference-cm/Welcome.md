---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/Welcome.html
---

# Welcome
<a name="Welcome"></a>

The change management API provides operations to create and manage requests for change (RFCs). RFCs can be created, updated, submitted, approved (or rejected), and canceled.

 **Creating a Request for Change**

To create a request for change, begin by calling [CreateRfc](API_CreateRfc.md). After creating the basic RFC and before submitting it, you can add or update information (`Description`, `ExpectedOutcome`, `ImplementationPlan`, `RollbackPlan`, and `WorstCaseScenario`) by using the `UpdateRfc` operation ([UpdateRfc](API_UpdateRfc.md)).

When all necessary information has been added, use [SubmitRfc](API_SubmitRfc.md) to activate the RFC.

**Note**
Although only the change type (`ChangeTypeId` and `ChangeTypeVersion`) and `Title` are required to initially create an RFC, you must provide values for these fields (either in the original [CreateRfc](API_CreateRfc.md) call or by using the corresponding `UpdateRfc` ([UpdateRfc](API_UpdateRfc.md) operation) before calling [SubmitRfc](API_SubmitRfc.md):
 `RequestedStartTime` ([CreateRfc](API_CreateRfc.md) and `RequestedEndTime`, if you want to schedule the RFC. If scheduling is unimportant, leave off these values and execution begins as soon as the RFC is approved. This is part of a feature known as ASAP, or un-scheduled RFC.
 `ExecutionParameters` that comply with the JSON `ExecutionInputSchema` of the change type that is associated with the RFC ([CreateRfc](API_CreateRfc.md) or [UpdateRfc](API_UpdateRfc.md))

For more information and examples, see [Change Management](https://docs.aws.amazon.com/managedservices/latest/userguide/change-mgmt.html) in the *AWS Managed Services User Guide*.

 **Getting information about an RFC**

The [GetRfc](API_GetRfc.md) operation shows most of the information about an RFC, including the approval status and execution status.

If an RFC is rejected or canceled, the reason for the action appears in the `RfcReason`.

 **Service Endpoint**

The HTTP endpoint for the Change Management API is:
+ https://amscm.us-east-1.amazonaws.com

This document was last published on September 1, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
