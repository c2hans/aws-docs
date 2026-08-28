---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/delete-m2m-clients.html
---

# Delete machine-to-machine client stacks
<a name="delete-m2m-clients"></a>

If you deployed any machine-to-machine (M2M) client stacks to grant programmatic API access, delete them before uninstalling the solution stacks. Each M2M client stack is a separate AWS CloudFormation stack that creates a dedicated IAM role trusted by an external principal. If you leave these stacks in place, they orphan IAM roles that reference the removed API.

Delete each M2M client stack using the same tool you used to deploy it — the `scripts/m2m` tooling described in [Programmatic access (machine-to-machine)](m2m-access.md), or the AWS CloudFormation console. To identify all M2M client stacks, use the M2M client listing script or filter CloudFormation stacks by the `aws-solutions:isb-stack-type=M2mClient` tag.

**Note**
If you disabled a client role using a revocation policy, remove that policy before deleting the stack; otherwise the stack deletion fails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
