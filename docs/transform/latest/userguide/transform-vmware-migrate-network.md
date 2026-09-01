---
source_url: https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network.html
---

# Migrate network
<a name="transform-vmware-migrate-network"></a>

With AWS Transform, you can migrate your network to AWS in a fraction of the time it takes to design and deploy manually. AWS Transform uses an AI-powered agent to translate your source environment configuration into production-ready AWS network resources. You review and modify the generated configuration through a conversational interface before deployment.

AWS Transform supports two approaches to network migration. Choose the one that matches how much of your target network already exists in AWS:
+ [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md) – AWS Transform builds a complete target network from your source configuration, creating new VPCs, subnets, security groups, and connectivity. Choose this approach when you are provisioning your AWS network as part of the migration.
+ [Apply security posture to existing VPCs](transform-vmware-apply-security-posture.md) – AWS Transform applies your source security groups and rules to VPCs that you have already provisioned in AWS, and leaves the rest of your network untouched. Choose this approach when your target VPCs and subnets already exist and you only need to bring over your security posture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transform` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
