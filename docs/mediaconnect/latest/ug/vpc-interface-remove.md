---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/vpc-interface-remove.html
---

# Removing a VPC interface from a MediaConnect flow
<a name="vpc-interface-remove"></a>

You can remove a VPC interface from your flow if it isn't used as a source for the flow.

## Prerequisites
<a name="vpc-interface-remove-prerequisites"></a>
+ The flow must be in **Standby**.
+ If the flow has an error, you must resolve the error before you complete the following procedure.

## Procedure
<a name="vpc-interface-remove-procedure"></a>

**To remove a VPC interface from a flow (console)**

1. On the **Flows** page, choose the name of the flow that is associated with the VPC interface that you want to remove.

1. Choose **Stop**.

   The status of the flow changes to **Standby**. The flow stops immediately and is no longer viewable to customers who are accessing the output directly from your flow or through an entitlement.

1. Choose the **VPC interfaces** tab.

1. Choose the VPC interface that you want to remove, and then choose **Remove**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
