---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/well-architected.html
---

# AWS Well-Architected design considerations
<a name="well-architected"></a>

This solution was designed with best practices from the AWS Well-Architected Framework which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud. This section describes how the design principles and best practices of the Well-Architected Framework were applied when building this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ Resources defined as IaC using CloudFormation.
+ Remediations implemented with the following characteristics, where possible:
  + Idempotency
  + Error handling and reporting
  + Logging
  + Restoring resources to a known state on failure

## Security
<a name="security-wa"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ IAM used for authentication and authorization.
+ Role permissions scoped to be as narrow as possible, though in many cases this solution requires wildcard permissions to be able to act on any resources.
+ For security purposes, all IAM roles deployed by this solution use least-privilege permissions scoped to the specific resources they manage.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ Security Hub continues to create findings if the underlying cause of the finding is not resolved by the remediation.
+ Serverless services allow the solution to scale as needed.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ This solution was designed to be a platform for you to extend without having to implement orchestration and permissions yourself.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ Serverless services allow you to pay for only what you use.
+ Use the free tier for SSM automation in every account

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ Serverless services allow you to scale up or down as needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
