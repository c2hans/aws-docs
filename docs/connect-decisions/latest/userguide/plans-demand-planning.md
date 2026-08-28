---
source_url: https://docs.aws.amazon.com/connect-decisions/latest/userguide/plans-demand-planning.html
---

# Demand Planning
<a name="plans-demand-planning"></a>

A plan is created for a defined time horizon and refreshed periodically through rolling time windows (planning cycles). Each demand plan can contain multiple versions within a planning cycle to support refinement of plan for any incremental data received within a planning cycle.

## Prerequisites
<a name="demand-planning-prerequisites"></a>

Before creating your first demand plan in Amazon Connect Decisions, ensure that you have the following prerequisites in place:
+ Your Amazon Connect Decisions instance must be set up and configured.
+ Your user account must be assigned a Manager role.
+ Product or product-site data entities must be prepared and uploaded (see Data Entities for details).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
