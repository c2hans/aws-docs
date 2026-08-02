---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-az-failover-spark-emr-clusters-arc.html
---

# Manage Multi-AZ failover for EMR clusters by using Application Recovery Controller
<a name="multi-az-failover-spark-emr-clusters-arc"></a>

*Aarti Rajput, Ashish Bhatt, Neeti Mishra, and Nidhi Sharma, Amazon Web Services*

## Summary
<a name="multi-az-failover-spark-emr-clusters-arc-summary"></a>

This pattern offers an efficient disaster recovery strategy for Amazon EMR workloads to help ensure high availability and data consistency across multiple Availability Zones within a single AWS Region. The design uses [Amazon Application Recovery Controller](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) and an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) to manage failover operations and traffic distribution for an Apache Spark-based EMR cluster.

Under standard conditions, the primary Availability Zone hosts an active EMR cluster and application with full read/write functionality. If an Availability Zone fails unexpectedly, traffic is automatically redirected to the secondary Availability Zone, where a new EMR cluster is launched. Both Availability Zones access a shared Amazon Simple Storage Service (Amazon S3) bucket through dedicated [gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html), which ensure consistent data management. This approach minimizes downtime and enables rapid recovery for critical big data workloads during Availability Zone failures. The solution is useful in industries such as finance or retail, where real-time analytics are crucial.

## Prerequisites and limitations
<a name="multi-az-failover-spark-emr-clusters-arc-prereqs"></a>

**Prerequisites**
+ An active [AWS account](https://aws.amazon.com/resources/create-account/)
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) on Amazon Elastic Compute Cloud (Amazon EC2)
+ Access from the master node of the EMR cluster to Amazon S3.
+ AWS Multi-AZ infrastructure

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

**Product versions**
+ [Amazon EMR 6.x and later releases](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html)

## Architecture
<a name="multi-az-failover-spark-emr-clusters-arc-architecture"></a>

**Target technology stack**
+ Amazon EMR cluster
+ Amazon Application Recovery Controller
+ Application Load Balancer
+ Amazon S3 bucket
+ Gateway endpoints for Amazon S3

**Target architecture**

![Architecture for an automated recovery mechanism with Application Recovery Cotnroller.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e5ecdb66-0eef-4a6a-8367-982a55104748/images/e982d580-13db-4bdd-9f6b-6400d7c31c01.png)

This architecture provides application resilience by using multiple Availability Zones and implementing an automated recovery mechanism through the Application Recovery Controller.

1. The Application Load Balancer routes traffic to the active Amazon EMR environment, which is typically the primary EMR cluster in the primary Availability Zone.

1. The active EMR cluster processes the application requests and connects to Amazon S3 through its dedicated Amazon S3 gateway endpoint for read and write operations.

1. Amazon S3 serves as a central data repository and is potentially used as a checkpoint or as shared storage between EMR clusters. EMR clusters maintain data consistency when they write directly to Amazon S3 through the `s3://` protocol and the [EMR File System (EMRFS)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-fs.html).

1. Application Recovery Controller continuously monitors the health of the primary Availability Zone and automatically manages failover operations when necessary.

1. If the Application Recovery Controller detects a failure in the primary EMR cluster, it takes these actions:
   + Initiates the failover process to the secondary EMR cluster in Availability Zone 2.
   + Updates routing configurations to direct traffic to the secondary cluster.

## Tools
<a name="multi-az-failover-spark-emr-clusters-arc-tools"></a>

**AWS services**
+ [Amazon Application Recovery Controller](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html)** **helps you manage and coordinate the recovery of your applications across AWS Regions and Availability Zones. This service simplifies the process and improves the reliability of application recovery by reducing the manual steps required by traditional tools and processes.
+ [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) operates at the application layer, which is the seventh layer of the Open Systems Interconnection (OSI) model. It distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. This increases the availability of your application.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command line shell.
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) is a big data platform that provides data processing, interactive analysis, and machine learning for open source frameworks such as Apache Spark, Apache Hive, and Presto.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) provides a simple web service interface that you can use to store and retrieve any amount of data, at any time, from anywhere. Using this service, you can easily build applications that make use of cloud native storage.
+ [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) are gateways that you specify in your route table to access Amazon S3 from your virtual private cloud (VPC) over the AWS network.

## Best practices
<a name="multi-az-failover-spark-emr-clusters-arc-best-practices"></a>
+ Follow [AWS best practices for security, identity, and compliance](https://aws.amazon.com/architecture/security-identity-compliance/?cards-all.sort-by=%5b…%5d.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all) to ensure a robust and secure architecture.
+ Align the architecture with the [AWS Well-Architected Framework.](https://aws.amazon.com/architecture/well-architected/)
+ Use Amazon S3 Access Grants to manage access from your Spark-based EMR cluster to Amazon S3. For details, see the blog post [Use Amazon EMR with S3 Access Grants to Scale Spark access to Amazon S3](https://aws.amazon.com/blogs/big-data/use-amazon-emr-with-s3-access-grants-to-scale-spark-access-to-amazon-s3/).
+ [Improve Spark performance with Amazon S3](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-s3-performance.html).

## Epics
<a name="multi-az-failover-spark-emr-clusters-arc-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Sign in to the AWS Management Console. | Sign in to the [AWS Management Console](https://console.aws.amazon.com/) as an IAM user. For instructions, see the [AWS documentation](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-iam-user-sign-in-tutorial.html). | AWS DevOps |
| Configure the AWS CLI.** ** | Install the AWS CLI or update it to the latest version so you can interact with AWS services in the AWS Management Console. For instructions, see the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). | AWS DevOps |

### Deploy a Spark application on your EMR cluster
<a name="deploy-a-spark-application-on-your-emr-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-az-failover-spark-emr-clusters-arc.html) | AWS DevOps |
| Create an EMR cluster. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-az-failover-spark-emr-clusters-arc.html) | AWS DevOps |
| Configure security settings for the EMR cluster. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-az-failover-spark-emr-clusters-arc.html) | AWS DevOps |
| Connect to the EMR cluster. | Connect to the master node of the EMR cluster through SSH by using the provided key pair.<br />Ensure that the key pair file is present in the same directory as your application.<br />Run the following commands to set the correct permissions for the key pair and to establish the SSH connection:<pre>chmod 400 <key-pair-name><br />ssh -i ./<key-pair-name> hadoop@<master-node-public-dns></pre> | AWS DevOps |
| Deploy the Spark application. | After you establish the SSH connection, you will be in the Hadoop console.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-az-failover-spark-emr-clusters-arc.html) | AWS DevOps |
| Monitor the Spark application. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-az-failover-spark-emr-clusters-arc.html) | AWS DevOps |

### Shift traffic to another Availability Zone
<a name="shift-traffic-to-another-availability-zone"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Application Load Balancer. | Set up the target group that routes traffic between Amazon EMR master nodes that are deployed across two Availability Zones within an AWS Region.<br />For instructions, see [Create a target group for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html) in the Elastic Load Balancing documentation. | AWS DevOps |
| Configure zonal shift in Application Recovery Controller. | In this step, you'll use the [zonal shift feature](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html) in Application Recovery Controller to shift traffic to another Availability Zone.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-az-failover-spark-emr-clusters-arc.html)<br />To use the AWS CLI, see [Examples of using the AWS CLI with zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonalshift.html) in the Application Recovery Controller documentation. | AWS DevOps |
| Verify zonal shift configuration and progress. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/multi-az-failover-spark-emr-clusters-arc.html) | AWS DevOps |

## Related resources
<a name="multi-az-failover-spark-emr-clusters-arc-resources"></a>
+ AWS CLI commands:
  + [create-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html)
  + [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-cluster.html)
  + [arc-zonal-shift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/index.html)
+ [Configuring Amazon EMR cluster instance types and best practices for Spot instances](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html) (Amazon EMR documentation)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation)
+ [Use instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) (IAM documentation)
+ [Use zonal shift and zonal autoshift to recovery applications in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/multi-az.html) (Application Recovery Controller documentation)
