---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer.html
---

# Access container applications privately on Amazon ECS by using AWS PrivateLink and a Network Load Balancer
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer"></a>

*Kirankumar Chandrashekar, Amazon Web Services*

## Summary
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer-summary"></a>

This pattern describes how to privately host a Docker container application on Amazon Elastic Container Service (Amazon ECS) behind a Network Load Balancer, and access the application by using AWS PrivateLink. You can then use a private network to securely access services on the Amazon Web Services (AWS) Cloud. Amazon Relational Database Service (Amazon RDS) hosts the relational database for the application running on Amazon ECS with high availability (HA). Amazon Elastic File System (Amazon EFS) is used if the application requires persistent storage.

The Amazon ECS service running the Docker applications, with a Network Load Balancer at the front end, can be associated with a virtual private cloud (VPC) endpoint for access through AWS PrivateLink. This VPC endpoint service can then be shared with other VPCs by using their VPC endpoints.

You can also use [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) instead of an Amazon EC2 Auto Scaling group. For more information, see [Access container applications privately on Amazon ECS by using AWS Fargate, AWS PrivateLink, and a Network Load Balancer](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer.html?did=pg_card).

## Prerequisites and limitations
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ [AWS Command Line Interface (AWS CLI) version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), installed and configured on Linux, macOS, or Windows
+ [Docker](https://www.docker.com/), installed and configured on Linux, macOS, or Windows
+ An application running on Docker

## Architecture
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer-architecture"></a>

![Using AWS PrivateLink to access a container app on Amazon ECS behind a Network Load Balancer.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a316bf46-24db-4514-957d-abc60f8f6962/images/573951ed-74bb-4023-9d9c-43e77e4f8eda.png)

**Technology stack**
+ Amazon CloudWatch
+ Amazon Elastic Compute Cloud (Amazon EC2)
+ Amazon EC2 Auto Scaling
+ Amazon Elastic Container Registry (Amazon ECR)
+ Amazon ECS
+ Amazon RDS
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Lambda
+ AWS PrivateLink
+ AWS Secrets Manager
+ Application Load Balancer
+ Network Load Balancer
+ VPC

*Automation and scale*
+ You can use [AWS CloudFormation ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)to create this pattern by using [Infrastructure as Code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html).

## Tools
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer-tools"></a>
+ [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) – Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS Cloud.
+ [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) – Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application.
+ [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) – Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage containers on a cluster.
+ [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) – Amazon Elastic Container Registry (Amazon ECR) is a managed AWS container image registry service that is secure, scalable, and reliable.
+ [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) – Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – Lambda is a compute service for running code without provisioning or managing servers.
+ [Amazon RDS](https://docs.aws.amazon.com/rds/) – Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is storage for the internet. It is designed to make web-scale computing easier for developers.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) – Secrets Manager helps you replace hardcoded credentials in your code, including passwords, by providing an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) – Amazon Virtual Private Cloud (Amazon VPC) helps you launch AWS resources into a virtual network that you've defined.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) – Elastic Load Balancing distributes incoming application or network traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses, in multiple Availability Zones.
+ [Docker](https://www.docker.com/) – Docker helps developers to pack, ship, and run any application as a lightweight, portable, and self-sufficient container.

## Epics
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer-epics"></a>

### Create networking components
<a name="create-networking-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC. | 1. Sign in to the AWS Management Console and open the Amazon VPC console. Choose **Create VPC**, and choose **VPC and more**. <br />2. Enter a name for your VPC, and choose an appropriate CIDR block range. <br />3. Specify two Availability Zones, two public subnets, four private subnets. Two private subnets are for Amazon ECS tasks, and two private subnets are for Amazon RDS databases.<br />4. Specify one NAT gateway for each Availability Zone. <br />5. Choose **Create VPC**. | Cloud administrator |

### Create the load balancers
<a name="create-the-load-balancers"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Network Load Balancer.  | 1. Open the Amazon EC2 console and choose the AWS Region that contains your VPC. <br />2. Under **Load balancing**, choose **Load balancers**, and choose **Create load balancer**. <br />3. Choose **Network Load Balancer**, and choose **Create**. <br />4. On the **Configure load balancer** page, configure your Network Load Balancer and listener.** Important:** Make sure you choose your Network Load Balancer's scheme as **Internal**. <br />5. Choose the applicable security settings, configure a security group and a target group. Choose **Instance** or **IP** as the **Target type** in the **Configure routing** section. Make sure you do not register a target. <br />6. When you have configured all the settings, choose **Next: Review**, and then choose **Create**. | Cloud administrator |
| Create an Application Load Balancer. | 1. On the Amazon EC2 console, choose the same Region that contains your VPC.<br />2. Under **Load balancing**, choose **Load balancers**, and choose** Create load balancer**.<br />3. Choose **Application Load Balancer**, and choose **Create**. <br />4. Configure your Application Load Balancer and its listener. Make sure you choose your Application Load Balancer's scheme as **Internal**. <br />5. Choose the applicable security settings, configure a security group and a target group. Choose **Instance** or **IP** as the **Target type** in the **Configure routing** section. Make sure you do not register a target. <br />6. When you have configured all the settings, choose **Next: Review**, and then choose **Create**. | Cloud administrator |

### Create an Amazon EFS file system
<a name="create-an-amazon-efs-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EFS file system. | 1. Open the Amazon EFS console, and choose **Create file system**. <br />2. In the **Create file system** dialog box, enter a name for your file system, and choose your VPC. <br />3. Choose **Create** to create the file system. <br />4. Set up and configure your Amazon EFS file system. | Cloud administrator |
| Mount targets for the subnets. | 1. Return to the Amazon EFS console, and choose **File systems**. The **File systems** page shows the Amazon EFS file systems in your account. <br />2. Choose the file system that you created, and choose **Manage** to display the **Availability Zones**. To add a mount target, choose **Add mount target**, and add the four private subnets that you created. | Cloud administrator |
| Verify that the subnets are mounted as targets.  | 1. On the Amazon EFS console, choose **File systems**. <br />2. Choose **Network** to display the list of existing mount targets. Make sure that these include the four subnets that you created. | Cloud administrator |

### Create an S3 bucket
<a name="create-an-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket.  | Open the Amazon S3 console and create an S3 bucket to store your application’s static assets, if required. | Cloud administrator |

### Create a Secrets Manager secret
<a name="create-a-secrets-manager-secret"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS KMS key to encrypt the Secrets Manager secret. | Open the AWS Key Management Service (AWS KMS) console and create a KMS key. | Cloud administrator |
|  Create a Secrets Manager secret to store the Amazon RDS password. | 1. Open the AWS Secrets Manager console, and create a new secret by choosing **Store a new secret**. <br />2. Choose the KMS key that you created, and store your new secret. | Cloud Administrator  |

### Create an Amazon RDS instance
<a name="create-an-amazon-rds-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a DB subnet group.  | 1. Open the Amazon RDS console and choose **Subnet groups**. <br />2. Choose **Create DB subnet group**, and enter a name and description for your DB subnet group. <br />3. Choose the VPC that you created earlier, and choose the Availability Zones and subnets. Then choose **Create**. | Cloud administrator |
| Create an Amazon RDS instance. | Create and configure an Amazon RDS instance within the private subnets. Make sure that **Multi-AZ** is turned on for HA. | Cloud administrator |
| Load data to the Amazon RDS instance.  | Load the relational data required by your application into your Amazon RDS instance. This process will vary depending on your application's needs, as well as how your database schema is defined and designed. | Cloud administrator, DBA |

### Create the Amazon ECS components
<a name="create-the-amazon-ecs-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an ECS cluster. | 1. Open the Amazon ECS console, and choose **Clusters**.<br />2. Choose **Create clusters**, and set up an ECS cluster according to your required specifications. | Cloud administrator |
| Create the Docker images.  | Create the Docker images by following the instructions in the *Related resources* section. | Cloud administrator |
| Create Amazon ECR repositories. | 1. On the Amazon ECR console, choose **Repositories**. <br />2. Choose **Create repository**, and enter a unique name for your repository. <br />3. Configure the repository according to your specifications, including AWS KMS encryption if required. | Cloud administrator, DevOps engineer |
| Authenticate your Docker client for the Amazon ECR repository.  | To authenticate your Docker client for the Amazon ECR repository, run the "`aws ecr get-login-password` command in the AWS CLI. | Cloud administrator |
| Push the Docker images to the Amazon ECR repository.  | 1. Identify the Docker image you want to push, and run the `docker images` command in the AWS CLI. <br />2. Tag your image with the Amazon ECR registry, repository, and optional image tag name combination. <br />3. Push the Docker image by running the `docker push` command. <br />4. Repeat these steps for all required images. | Cloud administrator |
| Create an Amazon ECS task definition.  | A task definition is required to run Docker containers in Amazon ECS. 1. Return to the Amazon ECS console, choose **Task definitions**, and then choose **Create new task definition**. <br />2. On the **Select compatibilities** page, select the launch type that your task should use, and choose **Next step**.For help with setting up your task definition, see "Creating a task definition" in the *Related resources* section. Make sure you provide the Docker images that you pushed to Amazon ECR. | Cloud administrator |
| Create an Amazon ECS service.  | Create an Amazon ECS service by using the ECS cluster you created earlier. Make sure you choose Amazon EC2 as the launch type, and choose the task definition created in the previous step, as well as the target group of the Application Load Balancer. | Cloud administrator |

### Create an Amazon EC2 Auto Scaling group
<a name="create-an-amazon-ec2-auto-scaling-group"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a launch configuration. | Open the Amazon EC2 console, and create a launch configuration. Make sure that the user data has the code to allow the EC2 instances to join the desired ECS cluster. For an example of the code required, see the *Related resources* section. | Cloud administrator |
| Create an Amazon EC2 Auto Scaling group.  | Return to the Amazon EC2 console and under **Auto Scaling**, choose **Auto Scaling groups**. Set up an Amazon EC2 Auto Scaling group. Make sure you choose the private subnets and launch configuration that you created earlier. | Cloud administrator |

### Set up AWS PrivateLink
<a name="set-up-aws-privatelink"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the AWS PrivateLink endpoint. | 1. On the Amazon VPC console, create an AWS PrivateLink endpoint. <br />2. Associate this endpoint with the Network Load Balancer, which makes the application hosted on Amazon ECS available privately to customers. For more information, see the *Related resources* section. | Cloud administrator |

### Create a VPC endpoint
<a name="create-a-vpc-endpoint"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC endpoint. | Create a VPC endpoint for the AWS PrivateLink endpoint that you created earlier. The VPC endpoint Fully Qualified Domain Name (FQDN) will point to the AWS PrivateLink endpoint FQDN. This creates an elastic network interface to the VPC endpoint service that the DNS endpoints can access. | Cloud administrator |

### Create the Lambda function
<a name="create-the-lambda-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Lambda function. | On the AWS Lambda console, create a Lambda function to update the Application Load Balancer IP addresses as targets for the Network Load Balancer. For more information on this, see the [Using AWS Lambda to enable static IP addresses for Application Load Balancers](https://aws.amazon.com/blogs/networking-and-content-delivery/using-aws-lambda-to-enable-static-ip-addresses-for-application-load-balancers/) blog post. | App developer |

## Related resources
<a name="access-container-applications-privately-on-amazon-ecs-by-using-aws-privatelink-and-a-network-load-balancer-resources"></a>

**Create the load balancers:**
+ [Use a Network Load Balancer for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/nlb.html)
+ [Create a Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html)
+ [Use an Application Load Balancer for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb.html)
+ [Create an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html)

**Create an Amazon EFS file system:**
+ [Create an Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html)
+ [Create mount targets in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)

**Create an S3 bucket:**
+ [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket)

**Create a Secrets Manager secret:**
+ [Create keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html)
+ [Create a secret in AWS Secrets Manager ](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

**Create an Amazon RDS instance:**
+ [Create an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)

**Create the Amazon ECS components:**
+ [Create an Amazon ECS cluster ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-ec2-cluster-console-v2.html)
+ [Create a Docker image](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html)
+ [Create an Amazon ECR repository ](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html)
+ [Authenticate Docker with Amazon ECR repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth)
+ [Push an image to an Amazon ECR repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)
+ [Create Amazon ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)
+ [Create an Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html)

**Create an Amazon EC2 Auto Scaling group:**
+ [Create a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html)
+ [Create an Auto Scaling group using a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg.html)
+ [Bootstrap container instances with Amazon EC2 user data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bootstrap_container_instance.html)

**Set up AWS PrivateLink:**
+ [VPC endpoint services (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html)

**Create a VPC endpoint:**
+ [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html)

**Create the Lambda function:**
+ [Create a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)

**Other resources:**
+ [Using static IP addresses for Application Load Balancers](https://aws.amazon.com/blogs/networking-and-content-delivery/using-static-ip-addresses-for-application-load-balancers/)
+ [Securely accessing services over AWS PrivateLink](https://d1.awsstatic.com/whitepapers/aws-privatelink.pdf)
