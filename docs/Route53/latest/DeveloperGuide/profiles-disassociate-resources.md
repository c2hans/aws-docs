---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles-disassociate-resources.html
---

# Disassociating a resource from an Amazon Route 53 Profile
<a name="profiles-disassociate-resources"></a>

Before you delete a Profile, you must dissociate all resources from it.<a name="profiles-disassociate-resources-procedure"></a>

**To disassociate a resource associated to a Route 53 Profile**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Profiles**.

1. On the navigation bar, choose the Region where the Profile from which you want to disassociate a resource was created.

1. Select the button next to the name of the Profile from which you want to disassociate a resource.

1. On the **Profile name** page choose the tab for the resource you want to delete, either , **DNS Firewall rule groups**, **Private hosted zones**, **Resolver query logging**, **Resolver rules** or **VPC endpoints**.

1. On the tab page for the resource, choose the resource you want to disassociate and then **Disassociate**.

1. In the **Disassociate resources** dialog, type in **confirm**, and then choose **Disassociate**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
