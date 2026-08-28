---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/features-benefits.html
---

# Features and benefits
<a name="features-benefits"></a>

 **Automate the creation of a sandbox environment**

Transforms the sandbox setup process with automated deployment of organizational unit (OU) structures that adhere to best practices for workload isolation.

 **Accelerate environment setup with blueprints**

Deploys pre-configured infrastructure to sandbox accounts automatically through CloudFormation StackSets, allowing users to get started with ready-to-use resources.

 **Enable team collaboration with shared leases**

Shares a single sandbox account with multiple IAM Identity Center users and groups, so teams can collaborate in the same environment without provisioning separate accounts.

 **Enhanced operational efficiency**

Reduces administrative overhead by implementing standardized policies, guardrails, and security controls across sandbox accounts automatically, ensuring consistent governance while saving valuable cloud administration time.

 **Establish cost governance**

Maintains better cost control and takes necessary action to reduce unnecessary spend; monitors spend patterns, sends automated alerts at defined thresholds, and restricts access or clean up resources when budget thresholds are approached.

 **Gain visibility into sandbox usage**

Centrally monitors all sandbox accounts, tracks sandbox usage metrics, and makes informed decisions with detailed visibility of sandbox environments using the web User Interface (UI).

 **Analyze sandbox costs natively in AWS Billing**

Use account cost allocation tags to filter, group, and analyze sandbox spend by lease, user, cost report group, and lease template directly in AWS Cost Explorer, AWS Budgets, and Cost and Usage Reports. The solution applies these tags automatically throughout the lease lifecycle.

 **Recycle and reuse AWS accounts**

Efficiently reuses AWS accounts using a cleanup mechanism that is automatically initiated when the spend or time period reaches predefined limits. This systematic approach is designed to recycle sandbox environments and prepare them for new experiments, while minimizing administrative overheads.

 **Manage solution settings from the web UI**

As an administrator, you manage global solution settings directly from the **Settings** page in the web UI, without using the AWS Management Console. These settings include lease policies, account cleanup behavior, maintenance mode, terms of service, and cost reporting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
