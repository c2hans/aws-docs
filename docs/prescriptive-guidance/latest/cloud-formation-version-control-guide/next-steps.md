---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-formation-version-control-guide/next-steps.html
---

# Next steps
<a name="next-steps"></a>

This guide described how commit ID-based tagging provides version control for CloudFormation deployments by using CodePipeline and CodeBuild. To build upon this foundation focus on these key areas:

1. **Evaluate environment needs** — Review your environment configurations and assess version mapping requirements across development, staging, and production environments. Consider cross-account deployment needs and plan for scaling infrastructure deployments as your organization grows.

1. **Implement monitoring and logging** — Establish comprehensive monitoring for your deployment pipelines by using CloudWatch. Configure appropriate alerts and notifications to maintain visibility into your infrastructure changes.

1. **Review security and compliance** — Regularly audit your IAM roles, cross-account access configurations, and security group settings. Ensure your implementation adheres to organizational compliance standards and security best practices.

1. **Enable team adoption** — Create clear documentation and conduct team training to ensure successful adoption of these practices. Establish standardized deployment workflows and approval processes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
