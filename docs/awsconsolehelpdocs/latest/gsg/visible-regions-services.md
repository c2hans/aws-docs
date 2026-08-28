---
source_url: https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/visible-regions-services.html
---

# Configuring visible Regions and services in the AWS Management Console
<a name="visible-regions-services"></a>

Account administrators can control which AWS Regions and AWS services are visible in the AWS Management Console navigation. These account-level settings are available on the **Account settings** tab of the Unified Settings page. When you hide a Region, it is removed from the Region selector for all users in the account. When you hide a service, it appears as unavailable in a separate section of the Services menu for all users in the account. Hidden services are also grayed out in Unified Search results and in the Recently Visited and Favorites widgets on Console Home.

If a user navigates directly to a hidden Region or service through a URL, they see an overlay that informs them the Region or service is hidden at the account level.

**Note**
Navigation to the Unified Settings page is always available, so administrators can't lock themselves out of these settings. If a user doesn't have the required permissions, or if the AWS User Experience Customization service is unavailable, all Regions and services are visible by default.

**Topics**
+ [Prerequisites for configuring visible Regions and services](visible-regions-services-prereqs.md)
+ [Configuring visible Regions in the AWS Management Console](configure-visible-regions.md)
+ [Configuring visible services in the AWS Management Console](configure-visible-services.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Management Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsconsolehelpdocs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
