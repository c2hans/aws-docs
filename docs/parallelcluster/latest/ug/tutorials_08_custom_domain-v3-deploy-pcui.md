---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorials_08_custom_domain-v3-deploy-pcui.html
---

# Deploy PCUI
<a name="tutorials_08_custom_domain-v3-deploy-pcui"></a>

Complete the following steps to create, or update, your AWS ParallelCluster UI (PCUI) deployment so that it will use your custom domain.

In this example we assume that you want to deploy PCUI with a custom domain `xyz.example.com` and the Amazon Cognito interface with a custom domain `auth-xyz.example.com`.

**Note**
Please note that customizing the Amazon Cognito domain is not required and can be left with the default value. We include this customization for completeness.

**Note**
Custom domains for Amazon Cognito are not supported in the AWS GovCloud (US) Regions.

To accomplish this, deploy the PCUI stack with the following parameters:
+ **CustomDomain:** {{xyz.example.com}}.
+ **CustomDomainCertificateArn:** the ACM certificate Amazon Resource Name (ARN) for {{xyz.example.com}}.
+ **CognitoCustomDomain:** {{auth-xyz.example.com}}.
+ **CognitoCustomDomainCertificateArn** to the ACM certificate Amazon Resource Name (ARN) for {{xyz.example.com}}.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
