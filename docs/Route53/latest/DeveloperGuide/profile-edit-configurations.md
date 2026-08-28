---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-edit-configurations.html
---

# Edit Route 53 Profile configurations
<a name="profile-edit-configurations"></a>

After you associate resources to a Profile, you can edit the default VPC configurations to decide how they are applied to the VPCs.<a name="profile-edit-configurations-procedure"></a>

**To edit Profile configurations**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. On the navigation bar, choose the Region where you created the Profile.

1. In the navigation pane, choose **Profiles** and on the **Profiles** table, choose the linked name of the Profile you want to work with.

1. On the **<Profile name>** page, choose the **Configuration** tab and then **Edit**.

1. On the **Edit Configuration** page, choose one of the values for the VPC DNSSEC configuration, Resolver reverse DNS lookup configuration, and DNS Firewall failure mode configuration.

   For more information about the values, see [Configuration settings for Route 53 Profile](values-for-profile-configuration.md).

1. Choose **Update**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
