---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/reoccurring-addf-deployments.html
---

# Reoccurring ADDF deployments
<a name="reoccurring-addf-deployments"></a>

Deploy ADDF and its modules as described in the [ADDF Deployment Guide](https://github.com/awslabs/autonomous-driving-data-framework/blob/main/docs/deployment_guide.md) (GitHub). To support reoccurring ADDF deployments that add, update, or remove resources in your target accounts, SeedFarmer uses MD5 hashes, stored in the Parameter Store of your toolchain and target acccounts, to compare the currently deployed infrastructure against the infrastructure defined in the manifest files in your local code base.

This approach follows the GitOps paradigm, where your source repository (the local code base where you operate SeedFarmer) is the source of truth, and the infrastructure declared explicitly in it is the desired outcome of your deployment. For more information about GitOps, see [What is GitOps](https://about.gitlab.com/topics/gitops/) (GitLab website).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
