---
source_url: https://docs.aws.amazon.com/vpc/latest/reachability/manage-role-deployments.html
---

# IAM role deployments in Reachability Analyzer
<a name="manage-role-deployments"></a>

When you enable trusted access, the following roles are deployed in your organization:
+ [AWSServiceRoleForReachabilityAnalyzer ](using-service-linked-roles.md#slr-permissions) – The service-linked role for Reachability Analyzer.
+ [IAMRoleForReachabilityAnalyzerCrossAccountResourceAccess](cross-account-access-roles.md) – The role for cross-account resource access for Reachability Analyzer.
+ [AWSServiceRoleForCloudFormationStackSetsOrgAdmin](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html) – The service-linked role for AWS CloudFormation StackSets for the management account.
+ [AWSServiceRoleForCloudFormationStackSetsOrgMember](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html) – The service-linked role for AWS CloudFormation StackSets for the member accounts.

The deployments can take several minutes to complete, depending on the number of member accounts in your organization. You can view the status of the role deployments as follows.

**To view IAM role deployments**

1. Sign in to the management account.

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home).

1. From the navigation pane, choose **Reachability Analyzer**, **Settings**.

1. Check **IAM role deployments status**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
