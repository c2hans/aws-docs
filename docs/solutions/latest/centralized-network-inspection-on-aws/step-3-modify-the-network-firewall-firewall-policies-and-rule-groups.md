---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/step-3-modify-the-network-firewall-firewall-policies-and-rule-groups.html
---

# Step 3. Modify the Network Firewall, firewall policies, and rule groups
<a name="step-3-modify-the-network-firewall-firewall-policies-and-rule-groups"></a>

 After successfully deploying the stack, CodePipeline initiates the CodeBuild stages. Each stage validates and deploys the Network Firewall components. After the deployment stage completes, you can view the AWS Network Firewall and firewall policy in the [AWS Network Firewall console](https://console.aws.amazon.com/vpc/home?#NetworkFirewalls:).

 To modify the default network firewall, firewall policy, and created rule groups, refer to [Configuring resources for Network Firewall](configuring-resources-for-network-firewall.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
