---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/production-environment.html
---

# Production environment
<a name="production-environment"></a>

The *production environment* supports the released product, handling real data by real clients. This is a protected environment that is assigned access by least privilege and elevated access should only be allowed through an audited exception process for a limited period of time.

## Access
<a name="access"></a>

In the production environment, developers should have limited, read-only access in the AWS Management Console. For example, developers should be able to access log data for day-to-day operations. All releases to production should be gated by an approval step prior to deployment.

## Build steps
<a name="build-steps"></a>

None. The same artifacts that were used in the testing and staging environments are reused in the production environment.

## Deployment steps
<a name="deployment-steps"></a>

Automatically initiate deployment of the `release` branch (Gitflow) or the `main` branch (Trunk or GitHub Flow) in the production environment after approval and deployment in the staging environment. The following are the deployment steps in the production environment:

1. Deploy the `release` branch (Gitflow) or `main` branch (Trunk or GitHub Flow) in the production environment

1. Pause for manual approval by designated personnel

1. Download published artifacts

1. Perform database versioning

1. Perform IaC deployment

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
