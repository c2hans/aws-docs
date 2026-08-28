---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ETSI-NFVO-compliant-orchestration-in-kubernetes/solution-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Solution architecture
<a name="solution-architecture"></a>

 Due to the different approaches in cloud-native operations versus virtualized application operations, the day -1 to day 2 operations also look different in the two. In this section, we will go over typical day -1 to day 2 operations, and explore how a cloud native orchestration can be built using those requirements. The following diagram represents a grouping of relevant AWS services for implementation of a cloud-native network orchestrator. To maintain ease of reading, we have ignored some of the operational requirements such as reliability, security and recovery from the following diagram, however in a real implementation, it is important to consider those requirements as well.

![A diagram depciting AWS constructs for a cloud-native CNF and infrastructure orchestrator.](http://docs.aws.amazon.com/whitepapers/latest/ETSI-NFVO-compliant-orchestration-in-kubernetes/images/cloud-native-cns.png)

 Motivation and tasks of each service in the preceding figure will become clear as the operational requirements are examined in detail in the following. Some guidelines to develop automation steps that are scalable while taking advantage of AWS and EKS native constructs for maximum flexibility is also presented.

## Day -1: Planning
<a name="day--1-planning"></a>

 Common tasks during this phase are:
+  Creation of account structure
+  Planning IP/subnets
+  Working with ISVs and CSP to populate Customer Information Questionnaire (CIQ) and artifacts
+  Ordering [AWS Outposts](https://aws.amazon.com/outposts/) if needed
+  Defining naming conventions, metadata and tags
+  Creating [AWS Identity and Access Management](https://aws.amazon.com/iam/) (AWS IAM) accounts and roles in the account structure
+  Creating service and CNF catalog
+  Giving appropriate permissions and set policies
+  Creating infrastructure — Deploy AWS constructs such as [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/?), [AWS Direct Connect](https://aws.amazon.com/directconnect/), and subnets.

 Most of these activities are covered by proper landing zone design, discussions with ISVs and network teams to create well-structured accounts and permissions, naming conventions and network design. AWS services such as [AWS Organizations](https://aws.amazon.com/organizations/) and [AWS Control Tower](https://aws.amazon.com/controltower/) can be quite useful to develop proper account structure and management, such as new account creation. With (AWS IAM), you can specify who or what can access services and resources in AWS, centrally manage fine-grained permissions, and analyze access and refine permissions across AWS. [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) helps create, manage, and control cryptographic keys across applications and more than 100 AWS services, and helps with secure access and management.

 [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) gives you full control over virtual networking environment, including resource placement, connectivity, and security. One of more VPCs might be required depending on VPC design and scale. [AWS Direct Connect](https://aws.amazon.com/directconnect/) links the CSP internal network to a Direct Connect location over a standard ethernet fiber-optic cable. [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) connects Amazon VPCs and on-premises networks through a central routing hub. This simplifies the network and puts an end to complex peering relationships as each new connection is only made once. [Amazon Route 53](https://aws.amazon.com/route53/) is a highly-available and scalable domain name system (DNS) web service. Route 53 connects user requests to internet applications running on AWS or on-premises.

 [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR) is an AWS-managed, Open Container Initiative (OCI)-compliant container image registry service that is secure, scalable, and reliable. Amazon ECR supports private repositories with resource-based permissions using AWS IAM. This ensures that only specified users or Amazon EC2 instances can access container repositories and images, thereby allowing separation across vendors. Customers can use the familiar Docker CLI, or their preferred client, to push, pull, and manage Docker images, OCI images, and OCI-compatible artifacts.

 Significant engineering effort and consideration should be given at this stage, as this lays the foundation of future automation and operations. Although proper planning needs human decisions, implementation of these design choices can often be automated.

## Day 0: Topology development
<a name="day-0-topology-development"></a>

 Some of the tasks in this phase of deployment are as follows:
+  Activate hardware, such as AWS Outposts instance, if it is deployed.
+  Develop a service/CNF catalog — This catalog contains services that upper layers can call.
+  Deploy platforms such as EKS clusters, Container Network Interfaces (CNIs), Container Storage Interfaces (CSIs), vRouters, and observability infrastructure such as probes and clients.
+  Boot up infrastructure such as node groups.

 Some of the well-developed robotic automation tools or customized process automation tools can be developed to activate AWS Outposts. Services such as [Service Catalog](https://aws.amazon.com/servicecatalog/) can be useful in creating the catalog and customizing it for the particular CSP and ISVs. Care should be taken to properly abstract configuration parameters to avoid bloating the catalog size.

 [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) constructs are flexible and functionally rich tools to deploy infrastructure and many of the platform components such as EKS clusters, CNIs, CSIs, and so on. The invocation of AWS CloudFormation/AWS CDK templates can be further customized using [AWS CodePipeline](https://aws.amazon.com/codepipeline/) with tools such as [AWS CodeCommit](https://aws.amazon.com/codecommit/) and [AWS CodeDeploy](https://aws.amazon.com/codedeploy/). Some of the functions can also be automated using a purpose-built automation workflow using [AWS Lambda](https://aws.amazon.com/lambda/) and [AWS Step Functions](https://aws.amazon.com/step-functions/).

 Increased agility and resilience can be achieved using Amazon EKS, an AWS managed Kubernetes service that makes it easy to run Kubernetes on AWS. The Kubernetes control plane managed by EKS runs inside an EKS-managed VPC, running components such as the Kubernetes API server nodes and [etcd cluster](https://etcd.io/docs/v3.4/op-guide/clustering/). Kubernetes API server nodes run the API server, scheduler, kube-controller-manager, and so on. in an EC2 Auto Scaling group, allowing it to scale based on demand. API server nodes run in a minimum configuration of two in distinct Availability Zones (AZs), while the [etcd](https://etcd.io/) server nodes run in an auto-scaling group that spans three Availability Zones. This architecture ensures that an event in a single Availability Zone doesn’t affect the EKS cluster's availability. The control plane backup (such as etcd backup) is periodically performed by AWS. Having a unified, managed Kubernetes control plane helps with operational agility and automation.

 For on-premises infrastructure not managed by AWS, Amazon EKS Anywhere is a new deployment option that allows customers to create and operate Kubernetes clusters. Amazon EKS Anywhere helps simplify the creation and operation of on-premises Kubernetes clusters with default component configurations while providing tools for automating cluster management. While not as feature-rich as EKS, it gives customers option to view all of their Kubernetes clusters in one dashboard.

## Day 1: Instantiation
<a name="day-1-instantiation"></a>

 This phase of deployment deals with the following tasks:
+  Instantiate CNFs
+  Update route tables

 Most of these functions can be automated if properly designed. CloudFormation and AWS CDKs are good constructs for this part. An automation pipeline can be build using AWS-provided continuous integration/continuous development ([CI/CD](https://en.wikipedia.org/wiki/CI/CD)) tools such as AWS CodeCommit and AWS CodeDeploy, or custom workflows can be created using AWS Lambda and AWS Step Functions that invoke appropriate AWS CloudFormation and CDK templates. Again, care should be taken to develop pipelines with appropriate parameterization so as to not bloat the number of pipelines or custom workflows. Some beneficial approaches in this part of the deployment are constructs such as [Amazon EKS blueprints](https://aws-quickstart.github.io/cdk-eks-blueprints/).

 You must also create proper databases to handle the vast and different types of data that is generated by network functions, and to ensure proper mapping between services, functions and their instantiation. Graph database such as [Amazon Neptune](https://aws.amazon.com/neptune/) can be useful in this regard. Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications. [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools. [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) is a managed relational database service for MySQL, PostgreSQL, MariaDB, Oracle BYOL, or SQL Server. Some AWS partner solutions, such as [Portworx PX-Enterprise](https://aws.amazon.com/quickstart/architecture/portworx-px-enterprise/), can be useful in architecting CNFs for high availability.

## Day 2: Operation and management
<a name="day-2-operation-and-management"></a>

 This is arguably the hardest part of the automation lifecycle, and deals with day-to-day operation of the network. This phase deals with the following tasks:
+  Update and scale CNFs
+  Update and scale network services
+  Update EKS version
+  Update configuration
+  Allow creation of new services
+  Monitor and manage
+  End service/CNFs when not needed

 New infrastructure, network and functions can also be deployed in this part to address increased network demand. Hence, it is important not to view this phase in isolation of earlier phases but think of it this phase as invoking all the earlier phases as and when needed.

 This phase is also the one that is most difficult to handle with traditional CI/CD. However, the new [GitOps](https://en.wikipedia.org/wiki/DevOps#GitOps)-based approaches can be particularly beneficial in this context. GitOps enables configuration as code and, if properly implemented, can take care of drift management from the desired configuration. This model is often utilized as an efficient strategy for provisioning cloud provider-specific managed resources, such as [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket and Amazon RDS instance, on which application workloads depends. Furthermore, AWS constructs such as [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) can provide a cost-effective way to manage utilization and allow for traffic adaptation. Combining this approach with an application configuration provides a useful method to manage the operational configuration.

 Monitoring, observability, and logging alarm for the Day 2 operations can be achieved using services such as Amazon CloudWatch, AWS CloudTrail, and AWS-provided managed services such as [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) and [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/). AWS CloudWatch collects monitoring and operational data in the form of logs, metrics, and events so that the operation teams can get a unified view of operational health and gain complete visibility of AWS resources, applications, and services running on AWS and on-premises. You can use CloudWatch to detect anomalous behavior in CSP environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep network running smoothly.

Because network functions continuously emit performance data and Key Performance Indicators (KPIs), you'll need a way to process this streaming data. [Amazon Kinesis](https://aws.amazon.com/kinesis/) makes it easy to collect, process, and analyze near real-time, streaming data to get timely insights and react quickly to new information. [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) helps prepare, build, train, and deploy high-quality machine learning (ML) models quickly by bringing together a broad set of capabilities purpose-built for ML. This makes it easy to get insights on the deployment and operations.

 With the previous described AWS constructs, one possible implementation on AWS is be as follows:

![Example implementation architecture of a cloud-native CNF and infrastructure orchestrator.](http://docs.aws.amazon.com/whitepapers/latest/ETSI-NFVO-compliant-orchestration-in-kubernetes/images/cloud-native-cns2.png)

 This diagram represents VPC constructs, EKS clusters, load-balancers and repositories, network connections, and so on in the context of Region, Availability Zones, and on-premises data centers. For ease of representation, we haven’t depicted some of the functionalities such as account and user administration, the creation of a landing zone, security, and DNS that were part of the earlier architecture, because many of those features will run in their own VPCs within control of cross-account permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
