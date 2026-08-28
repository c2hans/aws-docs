---
source_url: https://docs.aws.amazon.com/EDI/latest/eco-support-guide/eco-access-triggers.html
---

# EDI Cloud Operations customer account access reasons
<a name="eco-access-triggers"></a>

In certain circumstances ECO operators can access your account console and instances to manage your resources. You can view these access events in your AWS CloudTrail logs.

EDI customer account access activity is driven by triggers in response to CloudWatch alarms and events, and incident reports or service requests that you submit. The ECO operator might perform multiple service calls and host-level activities for each access.

Access justiﬁcation, the triggers, and the initiator of the trigger are listed in the following table.

| Access | Initiator | Trigger |
| --- | --- | --- |
| Internal problem investigation | ECO | Problem issue (an issue that has been identiﬁed as systemic) |
| Alert investigation and remediation | ECO | AWS Systems Manager operational work items (SSM OpsItems) |
| Incident investigation and remediation | You | Inbound support case (an incident or service request that you submit) |
| Inbound service request fulﬁllment | You | Inbound support case (an incident or service request that you submit) |

For information about how to review ECO operations and automation activity in your account, see [Tracking changes in your AMS Accelerate accounts](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-change-record.html), in the *AMS Accelerate User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Energy Data Insights on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query EDI` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
