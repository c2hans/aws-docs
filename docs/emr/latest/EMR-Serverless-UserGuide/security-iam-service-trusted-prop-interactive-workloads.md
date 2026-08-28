---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop-interactive-workloads.html
---

# Trusted Identity Propagation for interactive workloads
<a name="security-iam-service-trusted-prop-interactive-workloads"></a>

The steps to propagate identity to interactive workloads through an Apache Livy endpoint depend on whether your users interact with AWS managed development environment like Amazon SageMaker AI or your own self-hosted Notebook environment as client-facing application.

![EMR Serverless flowchart.](http://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/images/PEZ-SMAI.png)

## AWS managed development environment
<a name="security-iam-service-trusted-prop-aws-managed-development"></a>

The following AWS managed client-facing application supports trusted identity propagation with EMR-Serverless Apache Livy endpoint:
+ [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)

## Customer managed self-hosted Notebook environment
<a name="security-iam-service-trusted-prop-self-hosted-notebook"></a>

To enable trusted identity propagation for users of custom-developed applications, see to [Access AWS services programmatically using trusted identity propagation](https://aws.amazon.com/blogs/security/access-aws-services-programmatically-using-trusted-identity-propagation/) in the *AWS Security Blog*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
