---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_parallelcluster.html
---

# How AWS ParallelCluster uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_parallelcluster"></a>

AWS ParallelCluster is an open source cluster management tool that you can use to deploy and manage high performance computing (HPC) clusters in the AWS Cloud. You can create a multiple user environment that includes an AWS ParallelCluster that's integrated with an AWS Managed Microsoft AD (Active Directory). The AWS ParallelCluster uses a Secrets Manager secret for validating logins to Active Directory. For more information, see [Integrating Active Directory](https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorials_05_multi-user-ad.html) in the *AWS ParallelCluster User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
