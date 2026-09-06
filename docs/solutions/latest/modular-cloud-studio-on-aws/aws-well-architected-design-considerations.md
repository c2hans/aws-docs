---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ This solution automates the deployment and configuration of your cloud environment by using AWS services and AWS Partner integrations.
+ MCS tracks the assets that are deployed with CloudWatch and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/). It also tracks logs from [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2), [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/), and [AWS Directory Service](https://aws.amazon.com/directoryservice/) to provide observability into the infrastructure and solution components.

## Security
<a name="security"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ AWS resources that are deployed by the solution, such as Amazon EC2 instances and networking components installed in modules, are deployed within a VPC with limited access.
+ Upon deployment, the solution automatically creates a default administrator in the Amazon Cognito user pools. This user is part of the administrator group, which assumes the MCS Administrator IAM role. This role grants administrator permissions such as installing modules and viewing stored secrets within the account.
+ The solution securely stores sensitive data classified as confidential, such as administrator username and password used in the [Managed Active Directory module](identity-modules.md#managed-active-directory-module), in Secrets Manager.
+ The MCS web interface is publicly available via CloudFront, and the traffic travels through HTTPS protocol.
+ Users must authenticate via Amazon Cognito to use the MCS web console. The solution only allows authorized requests, whether the MCS API is accessed through the provided web interface or through a custom client. The MCS API is provided through [Amazon API Gateway](https://aws.amazon.com/api-gateway/) by using an Amazon Cognito authorizer.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ MCS simplifies the deployment of the workloads required to build a studio in the cloud, automates the configuration and integration of modules, which helps to avoid misconfigurations.
+ Optionally, you can configure the solution to use FSx for Windows File Server, which sets up and provisions file servers and storage volumes, replicates data, manages failover and failback, and eliminates much of the administrative overhead.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The solution helps users to launch a global studio in the cloud within hours.
+ The solution supports the deployment of MCS modules across multiple AWS Regions. This provides lower latency and a better experience for editors, content creators, and other production users.
+ The MCS management layer is entirely serverless and event-driven, removing the need to run and maintain physical servers. Data is stored in Amazon S3 and DynamoDB, and static web assets are served through CloudFront. The API is provided through API Gateway and Lambda.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ The cost for running MCS varies, based on how it is configured to deploy and how it is subsequently used over time. Some examples that influence cost include the following:
  + Number of Amazon EC2 workstations
  + How long your Amazon EC2 workstations run daily
  + How much data you transfer into MCS storage resources

See [Cost](cost.md) for more detail.
+ You can measure the efficiency of the workloads, and the costs associated with delivery, by using AWS Service Catalog AppRegistry or AWS [myApplications](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/aws-myApplications.html). See [Monitoring the solution with AWS Service Catalog AppRegistry](monitoring-the-solution-with-aws-service-catalog-appregistry.md) for more detail.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ The solution uses managed and serverless services where possible to minimize the environmental impact of the backend services.
+ Travel and transportation is a significant source of carbon emissions in media and entertainment workflows. MCS helps video editors and other post-production team members to work on remote cloud-based virtual desktops to lessen the need to travel to a facility to perform their work.
+ Customers can deploy MCS in one of the supported Regions (hub), and optionally enable additional Regions (spoke), based on both business requirements and sustainability goals to optimize performance, cost, and carbon footprint.
+ You can deploy your MCS studio close to end users, resulting in reduced latency, reduced distance that network traffic must travel, and fewer total network resources required to support your workload.
+ MCS can help you optimize team member resources for the activities performed by using virtual desktops to limit upgrade and device requirements.
+ You can use shared file systems or storage such as Amazon FSx for Windows File Server to access common data, avoid data duplication, and allow for more efficient infrastructure for your workloads.
+ The modular design of MCS helps you to size cloud resources to match the needs of a specific project, lower a workload’s environmental impact, reduce costs, and maintain performance benchmarks.
+ Using managed services supported in MCS shifts the responsibility to AWS, which has insights across millions of customers that can help drive new innovations and efficiencies. Managed services also distribute the environmental impact of the service across many users because of the multi-tenet control planes.
