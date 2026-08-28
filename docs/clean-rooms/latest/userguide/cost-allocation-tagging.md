---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/cost-allocation-tagging.html
---

# Cost Allocation Tagging
<a name="cost-allocation-tagging"></a>

AWS Clean Rooms supports using Cost Allocation Tags to track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs and deliver a monthly cost allocation report to you. User-defined cost allocation tags can be applied to AWS Clean Rooms resources to help track and allocate costs across your collaboration.

## Taggable Resources for Cost Allocation
<a name="cost-allocation-tagging-resources"></a>

The following table lists the AWS Clean Rooms resources that incur charges and can be tagged with user-defined cost allocation tags for tracking and organizing costs.

| Billed Resource | Tagged resource |
| --- | --- |
| SQL Query | Membership |
| PySpark Job | Membership |
| ML Training Job | Membership |
| ML Inference Job | Membership |
| Synthetic Data Generation | Membership |
| Lookalike Model Training | Lookalike Model |
| Lookalike Segment Export | Lookalike Segment |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
