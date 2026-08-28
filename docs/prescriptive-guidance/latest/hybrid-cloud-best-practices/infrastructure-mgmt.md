---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/infrastructure-mgmt.html
---

# Edge infrastructure management
<a name="infrastructure-mgmt"></a>

AWS provides fully managed services that extend AWS infrastructure, services, APIs, and tools closer to your end users and data centers. The services that are available in Outposts and Local Zones are the same as those available in AWS Regions, so you can manage those services by using the same AWS console, AWS CLI, or AWS APIs. For supported services, see the [AWS Outposts feature comparison](https://aws.amazon.com/outposts/) table and [AWS Local Zones features](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/).

## Deploying services at the edge
<a name="deploying-services"></a>

You can configure the available services in Local Zones and Outposts in the same way you configure them in AWS Regions: by using the AWS console, AWS CLI, or AWS APIs. The primary difference between Regional and edge deployments is the subnets where resources will be provisioned. The [Networking at the edge](networking.md) section described how subnets are deployed in Outposts and Local Zones. After you identify the edge subnets, you use the edge subnet ID as a parameter to deploy the service in Outposts or Local Zones. The following sections provide examples of deploying edge services.

### Amazon EC2 at the edge
<a name="9999999999999999ec2--at-the-edge.8f7e69d6-1f74-5da1-9d42-622aff52c909"></a>

The following `run-instances` example launches a single instance of type `m5.2xlarge` into the edge subnet for the current Region. The key pair is optional if you do not plan to connect to your instance by using SSH on Linux or remote desktop protocol (RDP) on Windows.

```
aws ec2 run-instances \
    --image-id ami-id \
    --instance-type m5.2xlarge \
    --subnet-id <subnet-edge-id> \
    --key-name MyKeyPair
```

### Application Load Balancers at the edge
<a name="9999999999999999albs--at-the-edge.f69939ac-b00a-5c9a-966c-d9bad6519812"></a>

The following `create-load-balancer` example creates an internal Application Load Balancer and enables the Local Zones or Outposts for the specified subnets.

```
aws elbv2 create-load-balancer \
    --name my-internal-load-balancer \
    --scheme internal \
    --subnets <subnet-edge-id>
```

To deploy an internet-facing Application Load Balancer to a subnet on an Outpost, you set the `internet-facing` flag in the `--scheme` option and provide a [CoIP pool ID](https://docs.aws.amazon.com/outposts/latest/userguide/local-rack.html#local-gateway-subnet), as shown in this example:

```
aws elbv2 create-load-balancer \
    --name my-internal-load-balancer \
    --scheme internet-facing \
    --customer-owned-ipv4-pool <coip-pool-id>
    --subnets <subnet-edge-id>
```

For information about deploying other services at the edge, follow these links:

|
|
| Service | AWS Outposts | AWS Local Zones |
| --- |--- |--- |
| Amazon EKS | [Deploy Amazon EKS on-premises with AWS Outposts](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts.html) | [Launch low-latency EKS clusters with AWS Local Zones](https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html) |
| Amazon ECS | [Amazon ECS on AWS Outposts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-on-outposts.html) | [Amazon ECS applications in shared subnets, Local Zones, and Wavelength Zones](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html) |
| Amazon RDS | [Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) | Select the Local Zone subnet |
| Amazon S3 | [Getting started with Amazon S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsGS.html) | Not available |
| Amazon ElastiCache | [Using Outposts with ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ElastiCache-Outposts.html) | [Using Local Zones with ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/Local_zones.html) |
| Amazon EMR | [EMR clusters on AWS Outposts](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-outposts.html) | [EMR clusters on AWS Local Zones](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-localzones.html) |
| Amazon FSx | Not available | Select the Local Zone subnet |
| AWS Elastic Disaster Recovery | [Working with AWS DRS and AWS Outposts](https://docs.aws.amazon.com/drs/latest/userguide/outposts.html) | Not available |
| AWS Transform MGN | Not available | Select the Local Zone subnet as the staging subnet |

## Outposts-specific CLI and SDK
<a name="cli-sdk"></a>

AWS Outposts has two groups of commands and APIs for creating a service order or manipulating the routing tables between the local gateway and your local network.

### Outposts ordering process
<a name="outposts-ordering-process.564dd313-73ac-5d48-8753-2362136fdd63"></a>

You can use the [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/index.html) or the [Outposts APIs](https://docs.aws.amazon.com/outposts/latest/APIReference/API_Operations.html) to create an Outposts site, to create an Outpost, and to create an Outposts order. We recommend that you work with a hybrid cloud specialist during your AWS Outposts ordering process to ensure proper selection of resource IDs and optimal configuration for your implementation needs. For a complete resource ID list, see the [AWS Outposts racks pricing](https://aws.amazon.com/outposts/rack/pricing/) page.

### Local gateway management
<a name="local-gateway-management.2d735836-e8b0-541d-9032-4d917c05e182"></a>

The management and operation of the local gateway (LGW) in Outposts requires knowledge of the AWS CLI and SDK commands available for this task. You can use the AWS CLI and AWS SDKs to create and modify LGW routes, among other tasks. For more information about managing the LGW, see these resources:
+ [AWS CLI for Amazon EC2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html)
+ EC2.Client in the [AWS SDK for Python (Boto)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html)
+ Ec2Client in the [AWS SDK for Java](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html)

### CloudWatch metrics and logs
<a name="9999999999999999cw--metrics-and-logs.752653df-641a-54a3-b722-04931915bf1e"></a>

For AWS services that are available in both Outposts and Local Zones, metrics and logs are managed in the same way as in Regions. Amazon CloudWatch provides metrics that are dedicated to monitoring Outposts in the following dimensions:

|
|
| Dimension | Description |
| --- |--- |
| `Account` | The account or service using the capacity |
| `InstanceFamily` | The instance family |
| `InstanceType` | The instance type |
| `OutpostId` | The ID of the Outpost |
| `VolumeType` | The EBS volume type |
| `VirtualInterfaceId` | The ID of the local gateway or service link virtual interface (VIF) |
| `VirtualInterfaceGroupId` | The ID of the VIF group for the local gateway VIF |

For more information, see [CloudWatch metrics for Outposts racks](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) in the Outposts documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
