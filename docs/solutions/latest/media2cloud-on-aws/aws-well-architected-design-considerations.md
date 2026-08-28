---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

 This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

 This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

 This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

 The Media2Cloud on AWS solution pushes metrics to Amazon CloudWatch at various stages to provide observability into the infrastructure, such as Lambda functions, AI services, S3 buckets, and the rest of the [AWS services in this solution ](aws-services-in-this-solution.md).

## Security
<a name="security"></a>

 This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

 We highly recommends that customers encrypt sensitive data in transit and at rest. This solution automatically encrypts media files and metadata at rest with [Amazon S3 server-side encryption (SSE](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html)). The solution's Amazon SNS topics and DynamoDB tables are also encrypted at rest using SSE.

 Documents indexed to the OpenSearch Service cluster are encrypted at rest. Node-to-node communication within the cluster is also encrypted.

 Media2Cloud on AWS deploys a static website [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an S3 bucket. To help reduce latency and improve security, this solution includes a CloudFront distribution with an origin access identity, which is a special CloudFront user that helps restrict access to the solution's website bucket contents. For more information, refer to [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

## Reliability
<a name="reliability"></a>

 This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

 Media2Cloud on AWS uses AWS serverless services wherever possible (for example, Lambda, API Gateway, S3, and DynamoDB) to ensure high availability and quick recovery from service failure.

## Performance efficiency
<a name="performance-efficiency"></a>

 This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).

 Media2Cloud on AWS uses serverless architecture throughout the solution. You can launch in any AWS Region that [supports the AWS services](supported-aws-regions.md) used in the solution.

 This solution is automatically tested and reviewed by solution architects and subject matter experts for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

 This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

 Media2Cloud on AWS uses a serverless and event-driven architecture; therefore, customers are only charged for what they use. The solution's design allows users to configure and tailor their own media workflows, and use only the AWS services that they need.

## Sustainability
<a name="sustainability"></a>

 This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).

 Media2Cloud on AWS uses managed and serverless services to minimize the environmental impact of the backend services. A critical component for sustainability provided by the solution is maximizing the usage of the AWS AI services. The serverless design of Media2Cloud on AWS (using Lambda, API Gateway, Amazon S3, and DynamoDB) aims to reduce the carbon footprint compared to the footprint of continually operating operating on-premises servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
