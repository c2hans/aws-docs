---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/allowed-domains.html
---

# Allowed Domains
<a name="allowed-domains"></a>

For WorkSpaces Pools users to access WorkSpaces, you must allow various domains on the network from which users initiate access to the WorkSpaces. For more information, see [IP address and port requirements for WorkSpaces Personal](workspaces-port-requirements.md). Note that the page specifies that it applies to WorkSpaces Personal but it also applies to WorkSpaces Pools.

**Note**
If your S3 bucket has a “.” character in the name, the domain used is `https://s3.{{<aws-region>}}.amazonaws.com`. If your S3 bucket does not have a “.” character in the name, the domain used is `https://{{<bucket-name>}}.s3.{{<aws-region>}}.amazonaws.com`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
