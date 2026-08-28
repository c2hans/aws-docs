---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

 This solution uses the best practices from the [*AWS Well-Architected Framework*](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

 This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

 **Operational excellence **

 This section describes how we architected this solution using the principles and best practices of the *[operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html)*.

 Secure Media Delivery at the Edge on AWS automatically creates a CloudWatch dashboard to monitor metrics and indicate if specific components in the solution operate as expected, and if there are any anomalies that must be investigated.

 **Security**

 This section describes how we architected this solution using the principles and best practices of the *[security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)*.

 This solution is specifically designed to protect your premium video content from unauthorized access when delivered through Amazon CloudFront. It creates IAM roles associated with resources that need to perform specific actions. The permissions defined in the policies created in the solution align with the principle of least privilege access, granting just those permissions that a specific component needs to fulfil its tasks fully.

 **Reliability **

 This section describes how we architected this solution using the principles and best practices of the *[reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)*.

 Secure Media Delivery at the Edge on AWS uses AWS serverless services wherever possible, (Lambda, API Gateway, Amazon S3 and DynamoDB) to ensure high availability and quick recovery from service failure.

 **Performance efficiency**

 This section describes how we architected this solution using the principles and best practices of the *[performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)*.

 Secure Media Delivery at the Edge on AWS uses serverless architecture throughout the solution, and it can be launched in any AWS Region of your choice in which regional resources will be created (Secrets Manager secrets, Step Functions workflows, Lambda functions, and Dynamo DB tables).

 This solution is automatically tested and reviewed by solutions architects and subject matter experts for areas to experiment and improve.

 **Cost optimization**

 This section describes how we architected this solution using the principles and best practices of the *[cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)*.

 The cost for running the solution varies based on a number of factors, including the duration of the streaming events and the number of concurrent viewers. We recommend creating a budget through AWS Cost Explorer to help manage costs, and customers can measure the efficiency of the workloads, and the costs associated with delivery, by using Application Manager.

 **Sustainability**

 This section describes how we architected this solution using the principles and best practices of the *[sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)*.

 Secure Media Delivery at the Edge on AWS uses managed and serverless services to minimize the environmental impact of the backend services. Customers can run this solution only during the duration of the event and delete the stack after the program ends, reducing the carbon footprint compared to the footprint of continually operating on-premises servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
