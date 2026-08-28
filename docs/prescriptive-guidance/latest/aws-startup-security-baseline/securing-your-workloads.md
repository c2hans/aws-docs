---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/securing-your-workloads.html
---

# Securing your workloads
<a name="securing-your-workloads"></a>

A workload is a collection of resources and code that delivers business value, such as a customer-facing application or a backend process. As you build and deploy workloads on AWS, the controls in this section help you protect your data, limit exposure of sensitive resources, and establish secure defaults. The controls cover managing application secrets, restricting access scope, minimizing access routes to private resources, and encrypting data in transit and at rest.

**This section contains the following topics:**
+ [WKLD.01 Use IAM roles for compute environment permissions](wkld-01.md)
+ [WKLD.02 Restrict credential usage scope with resource-based policies](wkld-02.md)
+ [WKLD.03 Use ephemeral secrets or a secrets management service](wkld-03.md)
+ [WKLD.04 Prevent application secrets from being exposed](wkld-04.md)
+ [WKLD.05 Detect and remediate when secrets are exposed](wkld-05.md)
+ [WKLD.06 Use AWS Systems Manager instead of SSH or RDP](wkld-06.md)
+ [WKLD.07 Enable CloudTrail data events for Amazon S3 buckets with sensitive data](wkld-07.md)
+ [WKLD.08 Encrypt Amazon EBS volumes](wkld-08.md)
+ [WKLD.09 Encrypt Amazon RDS databases](wkld-09.md)
+ [WKLD.10 Deploy private resources into private subnets](wkld-10.md)
+ [WKLD.11 Restrict network access with security groups](wkld-11.md)
+ [WKLD.12 Use VPC endpoints to access supported AWS and external services](wkld-12.md)
+ [WKLD.13 Require HTTPS for public web endpoints](wkld-13.md)
+ [WKLD.14 Use edge protection services for public endpoints](wkld-14.md)
+ [WKLD.15 Define security controls in templates and deploy them by using CI/CD practices](wkld-15.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
