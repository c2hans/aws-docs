---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

 This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

 This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

 This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

 This solution pushes metrics to CloudWatch at various stages to provide observability into the infrastructure, Lambda functions, MediaConvert, S3 buckets, and the rest of the solution components.

## Security
<a name="security"></a>

 This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

 This solution uses [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles to allow customers to assign granular access policies and permissions to services and users in the AWS Cloud.

## Reliability
<a name="reliability"></a>

 This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

 This solution uses AWS serverless services wherever possible (for example, Lambda and Amazon S3) to ensure high availability and quick recovery from service failure.

## Performance efficiency
<a name="performance-efficiency"></a>

 This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).

 This solution uses serverless architecture. It can be launched in any AWS Region that supports the AWS services used in the solution, such as Lambda, Amazon S3, and MediaConvert.

 This solution is automatically tested and reviewed by solutions architects and subject matter experts for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

 This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

 You can measure the efficiency of the workloads, and the costs associated with delivery, by using Application Manager.

## Sustainability
<a name="sustainability"></a>

 This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).

 This solution uses managed and serverless services to minimize the environmental impact of the backend services. If desired, you can run this solution only during specific events and then delete the stack after the program ends. This approach helps reduce the carbon footprint compared to the footprint of continually operating on-premises servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
