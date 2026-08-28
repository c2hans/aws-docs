---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-formation-version-control-guide/best-practices.html
---

# Best practices
<a name="best-practices"></a>

These are best practices for version control and tagging strategies. ** **
+ Use semantic versioning (MAJOR.MINOR.PATCH) consistently across all environments to maintain clear version tracking.
+ Use consistent version tagging conventions (for example, v1.0.0, v1.2.0) to maintain a clear deployment history.
+ Maintain the `deployment_map.json` file in the same repository as your CloudFormation templates to keep version mappings under source control.
+ Document all version changes and their impacts in commit messages and release notes.
+ Implement branching strategies that separate feature development from hotfix workflows.
+ Create hotfix branches from the current production version tag and use a dedicated naming convention (for example, v1.0.1-hotfix) to distinguish hotfixes from regular releases.
+ Configure error handling, logging, and retry mechanisms in your CI/CD pipeline by using the `buildspec.yml` file.
+ Use environment variables for sensitive information rather than hardcoding values in configuration files.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.
+ Configure IAM roles for cross-account access by using role assumption with least-privilege policies.
+ Monitor and audit cross-account access patterns by using AWS CloudTrail.
+ Rotate access credentials regularly and maintain separate security groups for different environments.
+ Maintain detailed deployment logs and historical configuration records for audit purposes.
+ Enable CloudTrail for API activity logging across all deployment accounts.
+ Implement approval workflows for production deployments to maintain change control.
+ Validate CloudFormation templates by using `cfn-lint` before committing to catch syntax errors early.
+ Conduct impact assessments before promoting version tags to production environments.
+ Establish communication plans for deployments that might cause service interruptions.
+ Maintain rollback procedures and contingency plans for each deployment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
