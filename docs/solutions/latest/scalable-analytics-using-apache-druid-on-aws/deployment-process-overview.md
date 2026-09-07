---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/deployment-process-overview.html
---

# Deployment process overview
<a name="deployment-process-overview"></a>

Follow the step-by-step instructions in this section to configure and deploy the guidance into your account. Before you launch the guidance, review the [cost](cost.md), [architecture](architecture-overview.md), [network security](security-1.md), and other considerations discussed earlier in this guide.

 **Time to deploy:** Approximately 40 minutes

## Choose deployment option
<a name="choose-deployment-option"></a>

You can deploy Druid with one of the following compute options:
+ Amazon EC2 (default option)
+ EKS with EC2 hosting
+ EKS with Fargate hosting

You can have multiple deployments/clusters in the same Region/account, and choose different compute options across the deployments.

## Choose Druid configuration
<a name="choose-druid-configuration"></a>

You can use one of the three pre-configured Druid settings: **small, medium**, or **large**. If your use case matches any of these settings, use the source/quickstart/ folders (small, medium, or large) to deploy Apache Druid in your AWS account with these settings pre-configured.

Small usage profile (profile assumptions: ingestion throughput at 30,000 records per second, query throughput at 25 queries per second)

| AWS service | Dimensions |
| --- | --- |
| Amazon EC2 | \* Druid master: 3 x t4g.medium \* Druid query: 3 x t4g.medium \* Druid data: 3 x (t4g.medium \+ 100GB EBS GP2 volume) \* ZooKeeper: 3 x t4g.small |
| Amazon ELB | 1 x ALB, 5 GB/h processed bytes (EC2 Instances and IP addresses as targets) |
| Amazon Aurora | 3 x db.t4g.medium |
| Amazon S3 | 1 TB standard storage \+ 1,000,000 requests per month |
| AWS Key Management Service | 7 x customer managed key |
| AWS Secrets Manager | 4 x secrets |
| Amazon CloudWatch | 50 GB standard logs ingested per month, 200 custom metrics \+ 1,000,000 metric requests per month |

Medium usage profile (profile assumptions: ingestion throughput at 120,000 records per second, query throughput at 100 queries per second)

| AWS service | Dimensions |
| --- | --- |
| Amazon EC2 | \* Druid master: 3 x m6g.xlarge \* Druid query: 3 x m6g.xlarge \* Druid data: 3 x (m6g.2xlarge \+ 500 GB EBS GP2 volume) \* ZooKeeper: 3 x t4g.medium |
| Amazon ELB | 1 x ALB, 20 GB/h processed bytes (EC2 Instances and IP addresses as targets) |
| Amazon Aurora | 3 x db.t4g.medium |
| Amazon S3 | 5 TB standard storage \+ 5,000,000 requests per month |
| AWS Key Management Service | 7 x customer managed key |
| AWS Secrets Manager | 4 x secrets |
| Amazon CloudWatch | 100 GB standard logs ingested per month, 200 custom metrics \+ 1,000,000 metric requests per month |

Large usage profile (profile assumptions: ingestion throughput at 1.4 million records per second, query throughput at 1,200 queries per second)

| AWS service | Dimensions |
| --- | --- |
| Amazon EC2 | \* Druid master: 3 x m6g.4xlarge \* Druid query: 3 x m6g.4xlarge \* Druid data: 3 x (m6g.16xlarge \+ 5 TB EBS GP2 volume) \* ZooKeeper: 3 x m5.2xlarge |
| Amazon ELB | 1 x ALB, 200 GB/h processed bytes (EC2 Instances and IP addresses as targets) |
| Amazon Aurora | 3 x db.t3.large |
| Amazon S3 | 50 TB standard storage \+ 10,000,000 requests per month |
| AWS Key Management Service | 7 x customer managed key |
| AWS Secrets Manager | 4 x secrets |
| Amazon CloudWatch | 1,000 GB standard logs ingested per month, 200 custom metrics \+ 1,000,000 metric requests per month |

## Build and deploy
<a name="build-and-deploy"></a>
+ From the guidance [GitHub repository](https://github.com/aws-solutions/scalable-analytics-using-apache-druid-on-aws), download the source files for this guidance The Scalable Analytics using Apache Druid on AWS templates are generated using the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/).
+ Open the terminal and navigate to the source directory: `cd source/`
+ Using `cdk.json`, configure the guidance for your requirements.
**Note**
We recommend using the `cdk.json` example in the `source/quickstart` folder, and making changes to suit your use cases accordingly. Refer to the [Configure the guidance](configure-the-solution.md) section for more information.
+ To install the guidance dependencies, type `npm install`.
+ To build the code, type `npm run build`.
+ To deploy the guidance, type `npm run cdk deploy`.

## Post-deployment
<a name="post-deployment"></a>

Once you have configured/customized and deployed the guidance, you can log into the AWS Management Console, and verify the stacks installed as part of the deployment.

AWS CDK will deploy a stack with the specified name and provisioned resources for the guidance that will show up shortly after this stack is completed on deployment. The main stack of the guidance is named DruidOptionStack-CustomName and contains the relevant guidance resources.
+ Sign into your [AWS Management console](https://console.aws.amazon.com/), and navigate to **CloudFormation > Stacks**. Make sure you select the Region where this guidance has been deployed.
+ Select the stack name to view the provisioned resources.

   **guidance provisioned resources**
![image3](https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/image3.png)
