---
source_url: https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-console-links.html
---

# Pivoting from a profile panel to another console
<a name="profile-panel-console-links"></a>

For EC2 instances, IAM users, and IAM roles, you can navigate directly from the details profile panel to the corresponding console. The information available from the console can provide additional input for your security investigation.

On the **EC2 instance details** profile panel, the EC2 instance identifier is linked to the Amazon EC2 console.

On the **User details** profile panel, the user name is linked to the IAM console.

On the **Role details** profile panel, the role name is linked to the IAM console.

## Pivoting from a profile panel to another entity profile
<a name="profile-panel-pivot"></a>

When a profile panel contains an identifier of a different entity, it is usually a link to that entity profile. The exceptions are the links to the Amazon EC2 and IAM consoles on the EC2 instance, IAM users, and IAM roles profiles. See [Pivoting from a profile panel to another console](#profile-panel-console-links).

For example, from a list of IP addresses, you might be able to display the profile for a specific IP address. That way you can see if there is any other information available to help you to complete your investigation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
