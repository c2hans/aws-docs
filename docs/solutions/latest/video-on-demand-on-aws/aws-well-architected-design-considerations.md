---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

Video on Demand on AWS solution pushes metrics to CloudWatch at various stages to provide observability into the infrastructure; Lambda functions, MediaConvert, MediaPackage, AWS S3 buckets, and the rest of the solution components.

## Security
<a name="security"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. Video on Demand on AWS creates several IAM roles, including a role that grants MediaConvert access to Amazon API Gateway and Amazon Simple Storage Service. This role is necessary to allow the services to operate in your account. The Amazon S3 buckets for MediaConvert output includes a policy that allows access from Amazon CloudFront. Because the CloudFront endpoints are publicly accessible, the MediaConvert output bucket is also publicly accessible. For information on how to secure CloudFront, refer to [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

Video on Demand on AWS uses AWS serverless services wherever possible (ex Lambda, S3 and DynamoDB) to ensure high availability and quick recovery from service failure.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).

Video on Demand on AWS, as mentioned earlier, uses serverless architecture throughout the solution. It can be launched in any region that supports the AWS services used in the solution such as: AWS Lambda, AWS S3, MediaConvert, and (optional) MediaPackage.

This solution is automatically tested and reviewed by solutions architects and subject matter experts for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

The cost for running Video on Demand on AWS varies based on several factors, including the size of the videos, the number of outputs created, and the number of views the published content receives through CloudFront. MediaConvert is the majority of the cost, and we recommend creating a budget through AWS Cost Explorer.

Customers can measure the efficiency of the workloads, and the costs associated with delivery, by using Application Manager.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).

Video on Demand on AWS uses managed and serverless services to minimize the environmental impact of the backend services. Customers can choose to run this solution during specific events and delete the stack after the program ends, reducing the carbon footprint compared to the footprint of continually operating on-premises servers.
