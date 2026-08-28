---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-5-add-tags.html
---

# Step 5: Add tags
<a name="step-5-add-tags"></a>

Follow the step-by-step instructions in this section to add tags to your VPCs and subnets to create or update transit gateway attachments to the VPC or to your transit gateway to create transit gateway peering attachments. Changing tag keys and values (if applicable) results in identifying the transit gateway route tables to create associations and enable propagations. Deleting the tags results in deleting the resources created when the tag was added.

For a real-world scenario on how to configure tag values with this solution, refer to [Implementing Serverless Transit Network Orchestrator (STNO) in AWS Control Tower](https://aws.amazon.com/blogs/mt/serverless-transit-network-orchestrator-stno-in-control-tower/). For information on using [Organizations tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) with this solution, refer to [Enforce compliance using AWS Organizations tag policies with Serverless Transit Network Orchestrator (STNO)](https://aws.amazon.com/blogs/mt/enforce-compliance-aws-organizations-tag-policies-with-serverless-transit-network-orchestrator-stno/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
