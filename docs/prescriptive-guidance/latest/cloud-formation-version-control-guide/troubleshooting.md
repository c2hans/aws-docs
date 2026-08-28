---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-formation-version-control-guide/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

If a deployment fails, follow this resolution process:

1. Check Amazon CloudWatch Logs for specific error messages related to the failed stack operation.

1. Verify IAM permissions and role assignments for the deployment account.

1. Review the `deployment_map.json` configuration for correct version constraints, account IDs, and Region values.

1. Validate the CloudFormation template syntax by using the CloudFormation Linter (cfn-lint).

1. If the issue persists, roll back to the last known good version by updating the version constraint in `deployment_map.json` to the previous commit ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
