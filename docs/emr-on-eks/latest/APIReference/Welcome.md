---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

Amazon EMR on EKS provides a deployment option for Amazon EMR that allows you to run open-source big data frameworks on Amazon Elastic Kubernetes Service (Amazon EKS). With this deployment option, you can focus on running analytics workloads while Amazon EMR on EKS builds, configures, and manages containers for open-source applications. For more information about Amazon EMR on EKS concepts and tasks, see [What is Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html).

 *Amazon EMR containers* is the API name for Amazon EMR on EKS. The `emr-containers` prefix is used in the following scenarios:
+ It is the prefix in the CLI commands for Amazon EMR on EKS. For example, `aws emr-containers start-job-run`.
+ It is the prefix before IAM policy actions for Amazon EMR on EKS. For example, `"Action": [ "emr-containers:StartJobRun"]`. For more information, see [Policy actions for Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-actions).
+ It is the prefix used in Amazon EMR on EKS service endpoints. For example, `emr-containers.us-east-2.amazonaws.com`. For more information, see [Amazon EMR on EKSService Endpoints](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/service-quotas.html#service-endpoints).

This document was last published on September 1, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
