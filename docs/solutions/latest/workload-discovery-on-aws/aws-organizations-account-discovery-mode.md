---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/aws-organizations-account-discovery-mode.html
---

# AWS Organizations account discovery mode
<a name="aws-organizations-account-discovery-mode"></a>

When Workload Discovery on AWS is deployed in an AWS Organization, the discovery of accounts is no longer managed through the solution’s web UI. In this case, you don’t need to manage the deployment of CloudFormation templates to discover accounts.

Instead, the solution uses an AWS Organization-wide AWS Config aggregator to discover resources in all accounts in the organization that have AWS Config enabled.

For resource types that aren’t supported by AWS Config, the solution automatically deploys an IAM role in each account in the organization using AWS CloudFormation StackSets. This role allows the discovery process to make SDK calls in all the organization’s accounts to discover these supplementary resources.

This StackSet is configured to automatically deploy the role in any new accounts that are added to the organization and delete the role from any accounts removed from the organization.

**Note**
It is not possible for a StackSet to deploy stack instance to the Management account. If you want Workload Discovery to discover this account then you must deploy the global resources template using the standard AWS CloudFormation deployment method described in the [Deploy the stack to provision the Global resources using CloudFormation](import-a-region.md#deploy-the-stack-to-provision-the-global-resources-using-cloudformation) section.
