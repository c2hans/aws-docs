---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-04.html
---

# WKLD.04 Prevent application secrets from being exposed
<a name="wkld-04"></a>

During local development, you might store application secrets in local configuration or code files and accidentally check them in to source code repositories. If a repository hosted on a public service provider doesn't have access controls, unauthorized users can access it and discover exposed secrets. Use secret-scanning tools to prevent your team from committing secrets to your repository. During code reviews, check for hardcoded credentials, API keys, and other secrets before you merge changes.

The following open-source tools can help you prevent checking in application secrets to source code repositories:
+ [Gitleaks](https://github.com/zricethezav/gitleaks) on GitHub
+ [detect-secrets](https://github.com/Yelp/detect-secrets) on GitHub
+ [git-secrets](https://github.com/awslabs/git-secrets) on GitHub
+ [TruffleHog](https://github.com/trufflesecurity/truffleHog) on GitHub

**Note**
These tools are open source and available at no charge.

For guidance on detecting and remediating exposed secrets, see [WKLD.05 Detect and remediate when secrets are exposed](wkld-05.md).
