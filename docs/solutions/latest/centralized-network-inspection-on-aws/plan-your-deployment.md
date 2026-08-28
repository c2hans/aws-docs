---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

 This section describes the [cost](cost.md), [security](security.md), and [quota](quotas.md) considerations prior to deploying the guidance.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

 This guidance uses Network Firewall, which is not currently available in all AWS Regions. You must launch this guidance in an AWS Region where AWS Network Firewall is available. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

**Note**
 You can deploy this guidance multiple times in the same Region to allow users to set up a new network firewall and related resources for an existing transit gateway.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
