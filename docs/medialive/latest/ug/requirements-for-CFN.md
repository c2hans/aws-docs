---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-CFN.html
---

# Requirements for CloudFormation
<a name="requirements-for-CFN"></a>

MediaLive includes a workflow wizard. Creation of a workflow always includes automatic creation of an CloudFormation stack. Therefore, to use the workflow wizard, users need permissions in CloudFormation.

| Permissions | Service name in IAM | Actions |
| --- | --- | --- |
| Work with the workflow wizard | CloudFormation | `ListStacks`<br />`DescribeStacks`<br />`DescribeStackResources`<br />`CreateStack`<br />`DeleteStack` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
