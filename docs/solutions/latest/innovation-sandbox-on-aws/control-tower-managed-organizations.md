---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/control-tower-managed-organizations.html
---

# Control Tower managed organizations
<a name="control-tower-managed-organizations"></a>

The Innovation Sandbox on AWS solution creates an account pool organizational unit (default: InnovationSandboxAccountPool) when you deploy the Account Pool Stack. This OU is created through AWS Organizations and is not managed by Control Tower. This OU and all nested OUs do not need to be registered with Control Tower.

If you choose to register the OU within Control Tower, or deploy the OU as a nested OU in an already Control Tower-managed OU, the parent OU (InnovationSandboxAccountPool OU), nested OUs, and accounts will appear in a drifted state in the Control Tower console. This is expected behavior because the solution moves accounts between the nested OUs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
