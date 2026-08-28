---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorials_08_custom_domain-v3.html
---

# Configure a custom domain
<a name="tutorials_08_custom_domain-v3"></a>

Learn how to configure a custom domain for the AWS ParallelCluster UI (PCUI). The UI is hosted on Amazon API Gateway in your AWS account. You can configure a custom domain in the API Gateway console.

**Prerequisites:**
+ You have an AWS account.
+ You own a domain.
+ The domain root is resolvable. For example, if you want to use `xyz.example.com` as your custom domain, then the root domain `example.com` must be resolvable. This means that you must have at least an A record for `example.com` pointing to an IP. If you don't have such record, add a dummy record pointing to 0.0.0.0.
+ You have created or imported the custom domain certificate for Cognito into AWS Certificate Manager (ACM) in us-east-1.
+ You have the necessary permissions to change the Domain Name System (DNS) settings.

**Topics**
+ [Deploy PCUI](tutorials_08_custom_domain-v3-deploy-pcui.md)
+ [Configure DNS](tutorials_08_custom_domain-v3-config-dns.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
