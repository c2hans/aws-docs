---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/reoccurring-addf-deployments.html
---

# Reoccurring ADDF deployments
<a name="reoccurring-addf-deployments"></a>

Deploy ADDF and its modules as described in the [ADDF Deployment Guide](https://github.com/awslabs/autonomous-driving-data-framework/blob/main/docs/deployment_guide.md) (GitHub). To support reoccurring ADDF deployments that add, update, or remove resources in your target accounts, SeedFarmer uses MD5 hashes, stored in the Parameter Store of your toolchain and target acccounts, to compare the currently deployed infrastructure against the infrastructure defined in the manifest files in your local code base.

This approach follows the GitOps paradigm, where your source repository (the local code base where you operate SeedFarmer) is the source of truth, and the infrastructure declared explicitly in it is the desired outcome of your deployment. For more information about GitOps, see [What is GitOps](https://about.gitlab.com/topics/gitops/) (GitLab website).
