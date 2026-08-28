---
source_url: https://docs.aws.amazon.com/partner-central/latest/getting-started/manage-account.html
---

# Managing your account settings
<a name="manage-account"></a>

From the navigation menu, partners have two settings: one for managing their AWS Partner Central account, and one for managing their Marketplace settings.

**Topics**
+ [AWS Partner Central settings](partner-central-settings.md)
+ [Associating domains for AWS Training and Certification tracking](associating-domains.md)
+ [Tags](#tags)
+ [Marketplace settings](marketplace-settings.md)

## Tags
<a name="tags"></a>

Tags allow partners to label specific resources (such as Opportunities or Fund Requests) and control access based on these tags. For example, partners can tag opportunities by Region or Sector and restrict individual user access in IAM to these specific segments of their AWS Partner Central data.

Each tag has a key and a value. For each resource, each tag key must be unique and can only have one value. Don't include sensitive information in tags.

### Create or update tags
<a name="create-update-tags"></a>

Choose the Tags tab for a summary of all existing tags. To create a new tag:

1. Choose the **Create AWS Partner Central tag** button in the top right-hand corner.

1. From the Manage Partner Tags page, you can remove existing tags by choosing **Remove** next to the associated tag or choose **Add new tag** to create new ones.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
