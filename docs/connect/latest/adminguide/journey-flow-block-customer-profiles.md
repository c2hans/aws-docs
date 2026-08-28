---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/journey-flow-block-customer-profiles.html
---

# Customer profiles
<a name="journey-flow-block-customer-profiles"></a>

## Description
<a name="journey-flow-block-customer-profiles-description"></a>

Use this block to determine whether a profile belongs to a particular segment or meets specific profile criteria.

## How to configure this block
<a name="journey-flow-block-customer-profiles-configure"></a>

You can configure the **Customer profiles** block in the admin website or using the CheckSegmentMembership action.

### Common properties
<a name="journey-flow-block-customer-profiles-common-properties"></a>

| Property | Description |
| --- | --- |
| Action | Select check segment membership action |
| Segment name | Select the segment to check. |

**Example**

Proceed only for customers in the "Loyalty Gold" segment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
