---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-roles.html
---

# Install the required IAM roles if needed
<a name="post-launch-action-settings-roles"></a>

To operate post-launch actions and allow SSM documents to run on launched instances, certain IAM roles must be installed. Usually these roles are installed into an AWS account when AWS DRS is initialized in the account for the first time in any region.

If you have already initialized Elastic Disaster Recovery in your account before September 13, 2023, it's possible that the required IAM roles were not installed in your account.

To verify the IAM roles are installed or install them if not installed (a one-time operation), go to **Settings → Default post-launch actions** and check **Post-launch actions settings**. If you see the message **Install the required IAM roles to allow using post-launch actions** select **Install post-launch IAM roles**. If the roles were installed successfully, the message to install the roles is not present in **Post-launch actions settings**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
