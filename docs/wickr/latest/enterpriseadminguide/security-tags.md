---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/security-tags.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Security tags
<a name="security-tags"></a>

Security tags are used to classify and organize users to prevent information leakage between classified and unclassified systems.

Admins can create network tags and override tags to create a hierarchy of information classification.

Complete the following procedure to enable security tags.

1. In the navigation pane of the Wickr Network Administrator Console, choose **Security Tags**.

1. On the **Security Tags** page, choose **\+ Override Tag**.

1. In the **Create override tag** dialog box that appears, enter a tag name, and then select a color.

1. Choose **Next**.

1. Select the security group you want to apply the tag.

1. Choose **Next**.

1. Review your settings, and then choose **Create**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
