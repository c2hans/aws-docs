---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm.html
---

# Set up permissions to use AI-enhanced troubleshooting
<a name="support-interaction-perm"></a>

To access AI-enhanced troubleshooting capabilities in Support Center, you need specific AWS Identity and Access Management permissions. This section describes the necessary IAM permissions and explains how to configure them so that you can fully use these capabilities.

AI-enhanced troubleshooting requires permissions beyond traditional support case management. The required permissions fall into four categories:
+ **Support interaction permissions:** Enable the new interaction-based workflow in Support Center.
+ **AI-powered classification permissions:** Allow access to AI-powered issue classification features.
+ **Amazon Q integration permissions:** Enable conversation import from Amazon Q Developer.
+ **AWS DevOps Agent permissions:** Enable operations investigations by DevOps Agent during a support interaction.

 These permissions supplement your existing AWS Support permissions and don't replace them.

 You can set up permissions for AI-enhanced troubleshooting in two ways:

[Option 1: Use the AWS managed policy (recommended)](https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm-man-policy.html). Attach the `AWSSupportAccess` managed policy to your users or roles. This policy includes all required permissions and is automatically updated when new Support features are released.

[Option 2: Create a custom policy with minimum required permissions](https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm-custom-policy.html). This approach gives you more control but requires manual updates when new features are added.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
