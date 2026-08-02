---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ Resources defined as IaC using CloudFormation.
+ All actions and audit logging sent to Amazon CloudWatch, allowing for automated responses to be deployed.

## Security
<a name="security1"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ IAM used for authentication and authorization.
+ Role permissions scoped to be as narrow as possible, though in many cases this solution requires wildcard permissions to be able to act on any resources.
+ Optional use of WAF to further secure the solution.
+ Amazon Cognito and optional ability to federate with external IDPs.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ Serverless services allow the solution to provide a fault tolerant architecture.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ Serverless services allow the solution to scale as needed.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ Serverless services allow you to pay for only what you use.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ Serverless services allow you to scale up or down as needed.
