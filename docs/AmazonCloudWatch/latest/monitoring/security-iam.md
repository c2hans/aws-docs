---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security-iam.html
---

# Identity and Access Management for Internet Monitor
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Internet Monitor resources. IAM is an AWS service that you can use with no additional charge.

**Important**
**Internet Monitor resource changes on July 8, 2024**
If you created IAM policies that included Internet Monitor resources before July 8, 2024, be aware of the following change to Internet Monitor resources and resource types:
Resource-level permissions for the **GetHealthEvent** action are now supported only on the **Monitor** resource type. The permissions are not supported on the **HealthEvent** resource.
To see more information about the actions, resources, and condition keys that you can specify in policies to manage access to AWS resources in Internet Monitor, see [Actions, resources, and condition keys for Internet Monitor](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchinternetmonitor.html).

**Topics**
+ [Upgrade IAM policies to IPv6](security_iam_cwim_security-ipv6-upgrade.md)
+ [How Internet Monitor works with IAM](security_iam_service-with-iam-cwim.md)
+ [Confused deputy prevention](security-iam-cwim-confused-deputy.md)
+ [AWS managed policies](CloudWatch-IM-permissions.md)
+ [Service-linked role](using-service-linked-roles-CWIM.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
