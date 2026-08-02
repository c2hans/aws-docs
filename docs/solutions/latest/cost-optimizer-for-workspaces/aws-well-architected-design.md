---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/aws-well-architected-design.html
---

# AWS Well-Architected design framework
<a name="aws-well-architected-design"></a>

We designed this solution with best practices from the AWS Well-Architected Framework, which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how we applied the design principles and best practices of the Well-Architected Framework when building this solution.

 **Operational excellence**

This section describes how we applied the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) when designing this solution.
+ The solution pushes metrics to [Amazon CloudWatch](http://aws.amazon.com/cloudwatch/) to provide observability into the infrastructure, AWS Lambda functions, Amazon S3 buckets, and the rest of the solution components.
+ The solution updates the daily report to indicate if the WorkSpace was skipped due to an application programming interface (API) failure.
+ The solution provides a way to incrementally onboard spoke accounts when new WorkSpace workloads are added to the account.

 **Security**

This section describes how we applied the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) when designing this solution.
+ All inter-service communications use IAM roles.
+ All multi-account communications use IAM roles.
+ All roles used by the solution follow least-privilege access. In other words, they only contain minimum permissions required so that the service can function properly.
+ All data storage, including Amazon S3 buckets and DynamoDB tables, have encryption at rest.

 **Reliability**

This section describes how we applied the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) when designing this solution.
+ The solution uses serverless AWS services wherever possible (such as Lambda, Amazon S3, and AWS Fargate) to ensure high availability and recovery from service failure.
+ Data processing uses Lambda functions. The solution stores data in DynamoDB and Amazon S3, so it persists in multiple Availability Zones by default.

 **Performance efficiency**

This section describes how we applied the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) when designing this solution.
+ All inter-service communications use IAM roles.
+ The solution uses serverless AWS services wherever possible (such as Lambda, Amazon S3, and Fargate).
+ The solution provides the ability to launch in any AWS Region that supports the AWS services used in this solution, such as AWS Lambda and Amazon S3.
+ Automatically tested and deployed daily. This solution is reviewed by solution architects and subject matter experts for areas to experiment and improve.

 **Cost optimization**

This section describes how we applied the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) when designing this solution.
+ The solution uses serverless architecture, and customers pay only for what they use.
+ The solution uses a lifecycle policy for the Amazon S3 bucket to delete objects after a year to help reduce the storage cost.
+ The solution provides a feature to terminate unused WorkSpaces to help you save costs by reducing the operating workloads.

 **Sustainability**

This section describes how we applied the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) when designing this solution.
+ The solution uses managed and serverless services to minimize the environmental impact of the backend services.
+ The solution’s serverless design is aimed at reducing the carbon footprint compared to the footprint of continually operating on-premises servers.
+ Solution provides a feature to terminate unused WorkSpaces to help minimize the carbon footprint further.
