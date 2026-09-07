---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer.html
---

# Access container applications privately on Amazon ECS by using AWS Fargate, AWS PrivateLink, and a Network Load Balancer
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer"></a>

*Kirankumar Chandrashekar, Amazon Web Services*

## Summary
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer-summary"></a>

This pattern describes how to privately host a Docker container application on the Amazon Web Services (AWS) Cloud by using Amazon Elastic Container Service (Amazon ECS) with an AWS Fargate launch type, behind a Network Load Balancer, and access the application by using AWS PrivateLink. Amazon Relational Database Service (Amazon RDS) hosts the relational database for the application running on Amazon ECS with high availability (HA). You can use Amazon Elastic File System (Amazon EFS) if the application requires persistent storage.

This pattern uses a [Fargate launch type](https://docs.aws.amazon.com/AmazonECS/latest/userguide/launch_types.html) for the Amazon ECS service running the Docker applications, with a Network Load Balancer at the front end. It can then be associated with a virtual private cloud (VPC) endpoint for access through AWS PrivateLink. This VPC endpoint service can then be shared with other VPCs by using their VPC endpoints.

You can use Fargate with Amazon ECS to run containers without having to manage servers or clusters of Amazon Elastic Compute Cloud (Amazon EC2) instances. You can also use an Amazon EC2 Auto Scaling group instead of Fargate. For more information, see [Access container applications privately on Amazon ECS by using AWS PrivateLink and a Network Load Balancer](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer.html?did=pg_card&trk=pg_card).

## Prerequisites and limitations
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ [AWS Command Line Interface (AWS CLI) version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), installed and configured on Linux, macOS, or Windows
+ [Docker](https://www.docker.com/), installed and configured on Linux, macOS, or Windows
+ An application running on Docker

## Architecture
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer-architecture"></a>

![Using PrivateLink to access a container app on Amazon ECS with an AWS Fargate launch type.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/31cca5e2-8d8b-45ec-b872-a06b0dd97007/images/57cc9995-45f4-4039-a0bf-2d2b3d6a05de.png)

**Technology stack**
+ Amazon CloudWatch
+ Amazon Elastic Container Registry (Amazon ECR)
+ Amazon ECS
+ Amazon EFS
+ Amazon RDS
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Fargate
+ AWS PrivateLink
+ AWS Secrets Manager
+ Application Load Balancer
+ Network Load Balancer
+ VPC

**Automation and scale**
+ You can use [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to create this pattern by using [Infrastructure as Code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html).

## Tools
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer-tools"></a>

**AWS services**
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed AWS container image registry service that is secure, scalable, and reliable.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage containers on a cluster.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources.
+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/rds/index.html) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is storage for the internet. It is designed to make web-scale computing easier for developers.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you've defined.
+ [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in multiple Availability Zones.

**Other tools**
+ [Docker](https://www.docker.com/) helps developers to easily pack, ship, and run any application as a lightweight, portable, and self-sufficient container.

## Epics
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer-epics"></a>

### Create networking components
<a name="create-networking-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC. | 1. Sign in to the AWS Management Console, and open the Amazon VPC console. Choose **Create VPC**, and choose **VPC and more**. <br />2. Enter a name for your VPC, and choose an appropriate CIDR block range.<br />3. Specify two Availability Zones, two public subnets, four private subnets. Two private subnets are for Amazon ECS tasks, and two private subnets are for Amazon RDS databases.<br />4. Specify one NAT gateway for each Availability Zone.<br />5. Choose Create **VPC**. | Cloud administrator |

### Create the load balancers
<a name="create-the-load-balancers"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Network Load Balancer.  | 1. Open the Amazon EC2 console, and choose the AWS Region that contains your VPC. <br />2. Under **Load balancing**, choose **Load balancers**, and choose **Create load balancer**. <br />3. Choose **Network Load Balancer**, and choose **Create**. <br />4. On the **Configure load balancer** page, configure your Network Load Balancer and listener. **Important:** Make sure you choose your Network Load Balancer's scheme as **Internal**. <br />5. Choose the applicable security settings, configure a security group and a target group. Choose **IP** as the **Target type** in the **Configure routing** section. Make sure you do not register a target. <br />6. When you have configured all the settings, choose **Next: Review**, and then choose **Create**.For help with this and other stories, see the *Related resources* section. | Cloud administrator |
| Create an Application Load Balancer. | 1. On the Amazon EC2 console, choose the same Region that contains your VPC. <br />2. Under **Load balancing**, choose **Load balancers**, and choose **Create load balancer**. <br />3. Choose **Application Load Balancer**, and choose **Create**. <br />4. Configure your Application Load Balancer and its listener. Make sure you choose your Application Load Balancer's scheme as **Internal**. <br />5. Choose the applicable security settings, configure a security group and a target group. Choose **IP** as the **Target type** in the **Configure routing** section. Make sure you do not register a target. <br />6. When you have configured all the settings, choose **Next: Review**, and then choose **Create**. | Cloud administrator |

### Create an Amazon EFS file system
<a name="create-an-amazon-efs-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EFS file system. | 1. Open the Amazon EFS console, and choose **Create file system**. <br />2. In the **Create file system** dialog box, enter a name for your file system, and choose your VPC. <br />3. Choose **Create** to create the file system. <br />4. Set up and configure your Amazon EFS file system. | Cloud administrator |
| Mount targets for the subnets. | 1. Return to the Amazon EFS console, and choose **File systems**. The **File systems** page shows the Amazon EFS file systems in your account. <br />2. Choose the file system that you created, and choose **Manage** to display the **Availability Zone**. <br />3. To add a mount target, choose **Add mount target**, and add the four private subnets that you created. | Cloud administrator |
| Verify that the subnets are mounted as targets.  | 1. On the Amazon EFS console, choose **File systems**. <br />2. Choose **Network** to display the list of existing mount targets. Make sure that these include the four subnets that you created. | Cloud administrator |

### Create an S3 bucket
<a name="create-an-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | Open the Amazon S3 console and [create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket) to store your application’s static assets, if required. | Cloud administrator |

### Create a Secrets Manager secret
<a name="create-a-secrets-manager-secret"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Create an AWS KMS key to encrypt the Secrets Manager secret. | Open the AWS Key Management Service (AWS KMS) console and create a KMS key. | Cloud administrator |
|  Create a Secrets Manager secret to store the Amazon RDS password. | 1. Open the AWS Secrets Manager console, and create a new secret by choosing **Store a new secret**. <br />2. Choose the KMS key that you created, and store your new secret. | Cloud administrator |

### Create an Amazon RDS instance
<a name="create-an-amazon-rds-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a DB subnet group.  | 1. Open the Amazon RDS console, and choose **Subnet groups**. <br />2. Choose **Create DB subnet group**, and enter a name and description for your DB subnet group. <br />3. Choose the VPC that you created earlier, and choose the Availability Zones and subnets. Then choose **Create**. | Cloud administrator |
| Create an Amazon RDS instance. | Create and configure an Amazon RDS instance within the private subnets. Make sure that **Multi-AZ** is turned on for high availability (HA). | Cloud administrator |
| Load data to the Amazon RDS instance.  | Load the relational data required by your application into your Amazon RDS instance. This process will vary depending on your application's needs, as well as how your database schema is defined and designed. | DBA |

### Create the Amazon ECS components
<a name="create-the-amazon-ecs-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an ECS cluster. | 1. Open the Amazon ECS console, and choose **Clusters**. <br />2. Choose **Create clusters**, and set up an ECS cluster according to your required specifications. | Cloud administrator |
| Create the Docker images. | Create the Docker images by following the instructions in the [AWS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html). | Cloud administrator |
| Create an Amazon ECR repository. | 1. Open the Amazon ECR console, and choose **Repositories**. <br />2. Choose **Create repository**, and enter a unique name for your repository. <br />3. Configure the repository according to your specifications, including AWS KMS encryption if required. | Cloud administrator, DevOps engineer |
| Push the Docker images to the Amazon ECR repository.  | 1. Identify the Docker image you want to push, and run the `docker images` command in AWS CLI. <br />2. Tag your image with the Amazon ECR registry, repository, and optional image tag name combination. <br />3. Push the Docker image by running the `docker push` command. <br />4. Repeat these steps for all required images. | Cloud administrator |
| Create an Amazon ECS task definition.  | A task definition is required to run Docker containers in Amazon ECS. 1. Return to the Amazon ECS console, choose **Task definitions**, and then choose **Create new task definition**. <br />2. On the **Select compatibilities** page, select the launch type that your task should use, and choose **Next step**.For help with setting up your task definition, see "Creating a task definition" in the *Related resources* section. Make sure you provide the Docker images that you pushed to Amazon ECR. | Cloud administrator |
| Create an ECS service and choose Fargate as the launch type. | 1. [Create an Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html) by using the ECS cluster you created earlier. Make sure you choose **Fargate** as the launch type.<br />2. Choose the task definition created in the previous step, and choose the target group of the Application Load Balancer. | Cloud administrator |

### Set up AWS PrivateLink
<a name="set-up-aws-privatelink"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the AWS PrivateLink endpoint. | 1. Open the Amazon VPC console, and [create an AWS PrivateLink endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html). <br />2. Associate this endpoint with the Network Load Balancer, which makes the application hosted on Amazon ECS available privately to customers.  | Cloud administrator |

### Create a VPC endpoint
<a name="create-a-vpc-endpoint"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC endpoint. | [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) for the AWS PrivateLink endpoint that you created earlier. The VPC endpoint Fully Qualified Domain Name (FQDN) will point to the AWS PrivateLink endpoint FQDN. This creates an elastic network interface to the VPC endpoint service that the Domain Name Service endpoints can access. | Cloud administrator |

### Set the target
<a name="set-the-target"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add the Application Load Balancer as a target. | To add the Application Load Balancer as a target for the Network Load Balancer, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/application-load-balancer-target.html). | App developer |

## Related resources
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer-resources"></a>

**Create the load balancers:**
+ [Use a Network Load Balancer for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/nlb.html)
+ [Create a Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html)
+ [Use an Application Load Balancer for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb.html)
+ [Create an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html)

**Create an Amazon EFS file system:**
+ [Create an Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html)
+ [Create mount targets in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)

**Create a Secrets Manager secret:**
+ [Create keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html)
+ [Create a secret in AWS Secrets Manager ](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html)

**Create an Amazon RDS instance:**
+ [Create an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)

**Create the Amazon ECS components**
+ [Create an Amazon ECR repository ](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html)
+ [Authenticate Docker with Amazon ECR repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth)
+ [Push an image to an Amazon ECR repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)
+ [Create Amazon ECS task definition ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)
+ [Create an Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html)

**Other resources:**
+ [Securely accessing services over AWS PrivateLink](https://d1.awsstatic.com/whitepapers/aws-privatelink.pdf)
