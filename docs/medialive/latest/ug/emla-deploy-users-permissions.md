---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-users-permissions.html
---

# Create users and assign permissions
<a name="emla-deploy-users-permissions"></a>

If you haven't set up users who will run channels on on-premises hardware, you should do that now. If your organization is a current user of MediaLive and you are now deploying MediaLive Anywhere, you must modify the permissions for your existing users. See [Identity and Access Management for AWS Elemental MediaLive](security-iam.md) and [Setting up IAM permissions for users](setting-up-for-production.md).

In both scenarios, there are two guidelines:
+ When you create or modify your users, you might want to create a role and policies that are designed specifically for using MediaLive Anywhere.
+ You must include permissions that the users need to work with MediaLive Anywhere. See [Requirements for MediaLive Anywhere](requirements-for-emla.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
