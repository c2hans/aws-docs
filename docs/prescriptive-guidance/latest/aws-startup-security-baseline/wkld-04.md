---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-04.html
---

# WKLD.04 Prevent application secrets from being exposed
<a name="wkld-04"></a>

During local development, application secrets can be stored in local configuration or code files and accidentally checked in to source code repositories. If a repository hosted on a public service provider is unsecured, unauthorized users can access it and discover exposed secrets. Use available tools to prevent secrets from being committed to your repository. During code reviews, check for hardcoded credentials, API keys, and other secrets before merging changes.

The following open-source tools can help prevent application secrets from being checked in to source code repositories:
+ [Gitleaks](https://github.com/zricethezav/gitleaks) on GitHub
+ [detect-secrets](https://github.com/Yelp/detect-secrets) on GitHub
+ [git-secrets](https://github.com/awslabs/git-secrets) on GitHub
+ [TruffleHog](https://github.com/trufflesecurity/truffleHog) on GitHub

**Note**
These tools are open source and available at no charge.

For guidance on detecting and remediating secrets that have already been exposed, see [WKLD.05 Detect and remediate when secrets are exposed](wkld-05.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
