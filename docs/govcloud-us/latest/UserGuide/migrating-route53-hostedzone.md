---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/migrating-route53-hostedzone.html
---

# Migrating Route 53 public hosted zones from commercial AWS Region to AWS GovCloud (US)
<a name="migrating-route53-hostedzone"></a>

If you have created a public hosted zone in your commercial AWS account for AWS GovCloud (US) resources, we recommend you to migrate the hosted zone from the commercial AWS account to the AWS GovCloud (US) account. This migration offers two key benefits:
+ Streamlined operations by consolidating resources into a single account.
+ Addressing potential compliance requirements.

For instructions, see [Migrating a hosted zone to a different AWS account](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html).

Note the following:
+ Some Route 53 features are not yet available in AWS GovCloud (US). For more information, see [Amazon Route 53 in AWS GovCloud (US)](govcloud-r53.md).
+ Health checks can be created and managed directly within AWS GovCloud (US). While it’s possible to use health checks from commercial Regions with DNS records in AWS GovCloud (US), we recommend creating health checks in AWS GovCloud (US) for DNS failover operations. When migrating hosted zones to AWS GovCloud (US), consider migrating the associated health checks as well.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS GovCloud (US). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query govcloud-us` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
