---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/cost-optimization.html
---

# Cost optimization
<a name="cost-optimization"></a>

 For serverless API cost optimization, [Serverless Application Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) covers cost optimization best practices such as cost-effective resources, matching supply and demand, expenditure awareness, and optimizing over time in [Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/cost-optimization-pillar.html) section.

 For REST and HTTP API pricing, see [Amazon API Gateway pricing](https://aws.amazon.com/api-gateway/pricing/). You might incur additional charges if you use API Gateway in conjunction with other AWS services, or transfer data out of AWS.

* Table 4 – REST and HTTP API pricing *

|  Endpoint type  |  Pricing  |
| --- | --- |
|  REST  |  Free tier: one million API calls per month for up to 12 months. <br /> API calls: [See the AWS documentation website for more details](http://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/cost-optimization.html)<br /> Caching: Billed per hour based on the cache memory size (not eligible for free tier)  |
|  HTTP  |  Free tier: one million API calls per month for up to 12 months. <br /> API calls (us-east-1); [See the AWS documentation website for more details](http://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/cost-optimization.html)<br /> HTTP APIs are metered in 512 KB increments.  |

 For private integration with REST APIs, the original approach required a Network Load Balancer (VPC link V1). With VPC links V2, you can now use either an ALB or an NLB. The NLB cost is billed per hour, so while a VPC link remains active, you pay for the NLB. The ALB cost is billed per ALB running per hour and per Load Balancer Capacity Units (LCU) used per hour. For a use case where requests to a REST API are made infrequently, such as five requests per day, a VPC-enabled Lambda function can be a more cost-effective option. VPC-enabled Lambda functions can access VPC resources. Because Lambda bills per request and code execution duration, using a VPC-enabled Lambda function can cost less. See [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/) and [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

 *Table 5 – Private integration vs. Lambda pricing *

|  Integration/Lambda  |  Cost  |  Use cases  |
| --- | --- | --- |
|  Private integration (NLB)  |  Billed per NLB running per hour and Network Load Balancer Capacity Units (NLCU) used per hour.  |  If there is a backend service hosted in ECS or other target such as EC2 instances that can be directly integrated with NLB, using an NLB to route traffic simplifies the architecture.  |
|  Private integration (ALB)  |  Billed per ALB running per hour and Load Balancer Capacity Units (LCU) used per hour.  |  If there is a backend service hosted in ECS or other target such as EC2 instances that can be directly integrated with ALB according to the architecture patterns.  |
|  VPC-enabled Lambda  |  Lambda pricing is billed on-demand, so if a Lambda function is not used, there is no charge.  |  If there is any private resource like RDS which cannot be directly accessed by NLB, using a VPC-enabled Lambda function is a good alternative.  |
