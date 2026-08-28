---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/privatelink-troubleshooting.html
---

# Troubleshooting
<a name="privatelink-troubleshooting"></a>

If your calls to the Amazon WorkSpaces Secure Browser APIs are hanging, there is likely a misconfiguration in your VPC Endpoint Service security group or IAM role setup. To resolve this, try the following:
+ While creating your interface VPC endpoint, it might have automatically attached to your AWS account’s default security group. Try using a different security group, and make sure the inbound and outbound permissions allow you to transfer your data appropriately.
+ Make sure you are using an IAM role that allows you to call Amazon WorkSpaces Secure Browser APIs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
