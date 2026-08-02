---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/services-for-bluegreen-deployments.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Services for blue/green deployments
<a name="services-for-bluegreen-deployments"></a>

 AWS provides a number of tools and services to help you automate and streamline your deployments and infrastructure.You can access these tools using the web console, [CLI tools, SDKs, and IDEs.](https://aws.amazon.com//tools/).

## Amazon Route 53
<a name="amazon-route-53"></a>

 [Amazon Route 53](https://aws.amazon.com/route53/) is a highly available and scalable authoritative DNS service that routes user requests for Internet-based resources to the appropriate destination. Amazon Route 53 runs on a global network of DNS servers providing customers with added features, such as routing based on health checks, geography, and latency. DNS is a classic approach to blue/green deployments, allowing administrators to direct traffic by simply updating DNS records in the hosted zone. Also, time to live (TTL) can be adjusted for resource records; this is important for an effective DNS pattern because a shorter TTL allows record changes to propagate faster to clients.

## Elastic Load Balancing
<a name="elastic-load-balancing"></a>

 Another common approach to routing traffic for a blue/green deployment is through the use of load balancing technologies. [Amazon Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) distributes incoming application traffic across designated [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instances. Elastic Load Balancing scales in response to incoming requests, performs health checking against Amazon EC2 resources, and naturally integrates with other services, such as Auto Scaling. This makes it a great option for customers who want to increase application fault tolerance.

## Auto Scaling
<a name="auto-scaling"></a>

 [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) helps maintain application availability and lets you scale EC2 capacity up or down automatically according to defined conditions. The templates used to launch EC2 instances in an Auto Scaling group are called *launch configurations*. You can attach different versions of launch configurations to an auto scaling group to enable blue/green deployment. You can also configure auto scaling for use with an ELB. In this configuration, the ELB balances the traffic across the EC2 instances running in an auto scaling group. You define termination policies in auto scaling groups to determine which EC2 instances to remove during a scaling action; auto scaling also allows instances to be placed in [Standby state](https://docs.aws.amazon.com//autoscaling/ec2/userguide/as-enter-exit-standby.html), instead of termination, which helps with quick rollback when required. Both auto scaling's termination policies and Standby state allow for blue/green deployment.

## AWS Elastic Beanstalk
<a name="aws-elastic-beanstalk"></a>

 [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk) is a fast and simple way to get an application up and running on AWS. It’s perfect for developers who want to deploy code without worrying about managing the underlying infrastructure. Elastic Beanstalk supports Auto Scaling and Elastic Load Balancing, both of which allow for blue/green deployment. Elastic Beanstalk helps you run multiple versions of your application and provides capabilities to swap the environment URLs, facilitating blue/green deployment.

## AWS OpsWorks
<a name="aws-opsworks"></a>

 [AWS OpsWorks](https://aws.amazon.com/opsworks/) is a configuration management service based on Chef that allows customers to deploy and manage application stacks on AWS. Customers can specify resource and application configuration, and deploy and monitor running resources. OpsWorks simplifies cloning entire stacks when you’re preparing blue/green environments.

## AWS CloudFormation
<a name="aws-cloudformation"></a>

 [AWS CloudFormation](https://aws.amazon.com/cloudformation/) provides customers with the ability to describe the AWS resources they need through JSON or YAML formatted templates. This service provides very powerful automation capabilities for provisioning blue/green environments and facilitating updates to switch traffic, whether through Route 53 DNS, ELB, or similar tools. The service can be used as part of a larger infrastructure as code strategy, where the infrastructure is provisioned and managed using code and software development techniques, such as version control and continuous integration, in a manner similar to how application code is treated.

## Amazon CloudWatch
<a name="amazon-cloudwatch"></a>

 [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is a monitoring service for AWS resources and applications. CloudWatch collects and visualizes metrics, ingests and monitors log files, and defines alarms. It provides system-wide visibility into resource utilization, application performance, and operational health, which are key to early detection of application health in blue/green deployments.

## AWS CodeDeploy
<a name="aws-codedeploy"></a>

 [AWS CodeDeploy](https://aws.amazon.com/codedeploy) is a deployment service that automates deployments to various compute types such as EC2 instances, on-premises instances, Lambda functions, or Amazon ECS services. Blue/Green deployment is a feature of CodeDeploy. CodeDeploy can also roll back deployment in case of failure. You can also use CloudWatch alarms to monitor the state of deployment and utilize CloudWatch Events to process the deployment or instance state change events.

## Amazon Elastic Container Service
<a name="elastic-container-service"></a>

 There are three ways traffic can be shifted during a deployment on [Amazon Elastic Container Service](https://aws.amazon.com/ecs) (Amazon ECS):
+ **Canary** – Traffic is shifted in two increments.
+ **Linear** – Traffic is shifted in equal increments.
+ **All-at-once** – All traffic is shifted to the updated tasks.

## AWS Lambda Hooks
<a name="aws-lambda-hooks"></a>

With AWS Lambda [hooks](https://docs.aws.amazon.com//codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html), CodeDeploy can call the Lambda function during the various lifecycle events including deployment of ECS, Lambda function deployment, and ECC2/On-premise deployment. The hooks are helpful in creating a deployment workflow for your apps.
