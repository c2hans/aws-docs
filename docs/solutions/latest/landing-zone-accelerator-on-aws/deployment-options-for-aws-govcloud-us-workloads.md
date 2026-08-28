---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/deployment-options-for-aws-govcloud-us-workloads.html
---

# Deployment options for AWS GovCloud (US) workloads
<a name="deployment-options-for-aws-govcloud-us-workloads"></a>

We base the following options on amount of access type of workloads:
+  [Option 1](option-1-deploy-to-new-standard-and-aws-govcloud-us-accounts.md) - Deploy to new standard and AWS GovCloud (US) accounts. This is recommended for customers who are planning to host workloads in both standard and AWS GovCloud (US) Regions. Both Region types will have a Landing Zone Accelerator on AWS.
+  [Option 2](option-2-deploy-on-new-aws-govcloud-us-accounts.md) - Deploy on new AWS GovCloud (US) accounts. This environment has access to both standard and AWS GovCloud (US) Regions. To create new AWS GovCloud (US) accounts, you can use the `CreateGovCloudAccount` API with [Service Catalog](https://aws.amazon.com/servicecatalog/) to create new accounts in the standard Region and add these new accounts into the solution in the AWS GovCloud (US) Region. You only use the standard Region to vend new accounts; no workloads are present in the standard Region.
+  [Option 3](option-3.-deploy-on-existing-govcloud-accounts.md) - Deploy on existing AWS GovCloud (US) accounts. In this option, users have access to AWS GovCloud (US) only and can’t create their own AWS GovCloud (US) accounts. In this situation, AWS GovCloud (US) accounts are provided by third-party providers such as partners or resellers. If AWS Organizations is activated in the management account with [administrative permissions](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/design-considerations.html#administrative-role), then you can deploy the solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
