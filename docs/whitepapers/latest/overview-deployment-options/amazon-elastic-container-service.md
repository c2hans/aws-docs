---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-container-service.html
---

# Amazon Elastic Container Service
<a name="amazon-elastic-container-service"></a>

 Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that supports Docker containers and allows you to easily run applications on a managed cluster. Amazon ECS eliminates the need to install, operate, and scale container management infrastructure, and simplifies the creation of environments with familiar AWS core features like [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html), [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), and [AWS Identity and Access Management](https://aws.amazon.com/iam/?nc=bc&pg=f-mr) (IAM).

 When running applications on Amazon ECS, you can choose to provide the underlying compute power for your containers with Amazon EC2 instances or with [AWS Fargate](https://aws.amazon.com/fargate/), a serverless compute engine for containers. In either case, Amazon ECS automatically places and scales your containers onto your cluster according to configurations defined by the user. Although Amazon ECS does not create infrastructure components such as Load Balancers or IAM roles on your behalf, the Amazon ECS service provides a number of APIs to simplify the creation and use of these resources in an Amazon ECS cluster.

 Amazon ECS allows developers to have direct, fine-grained control over all infrastructure components, allowing for the creation of custom application architectures. Additionally, Amazon ECS supports different deployment strategies to update your application container images.

* Table 4: Amazon ECS deployment features *

|  Capability  |  Description  |
| --- | --- |
|  Provision  |  Amazon ECS will provision new application container instances and compute resources based on scaling policies and Amazon ECS configurations. Infrastructure resources such as Load Balancers will need to be created outside of Amazon ECS. <br /> Refer to [Getting Started with Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_GetStarted.html) for more details on the types of resources that can be created with Amazon ECS.  |
|  Configure  |  Amazon ECS supports customization of the compute resources created to run a containerized application, as well as the runtime conditions of the application containers (for example, environment variables, exposed ports, reserved memory/CPU). Customization of underlying compute resources is only available if using Amazon EC2 instances. <br /> Refer to [Creating a Cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create_cluster.html) for more details on how to customize an Amazon ECS cluster to run containerized applications.  |
|  Deploy  |  Amazon ECS supports several deployment strategies for you containerized applications. <br /> Refer to [Amazon ECS Deployment Types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html) for more details on the types of deployment processes that are supported.  |
|  Scale  |  Amazon ECS can be used with auto scaling policies to automatically adjust the number of containers running in your Amazon ECS cluster. <br /> Refer to [Service Auto Scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) for more details on configuring auto scaling for your containerized applications on Amazon ECS.  |
|  Monitor  |  Amazon ECS supports monitoring compute resources and application containers with CloudWatch. <br /> Refer to [Monitoring Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_monitoring.html) for more details on the types of monitoring capabilities offered by Amazon ECS.  |

 The following diagram illustrates Amazon ECS being used to manage a simple containerized application. In this example, infrastructure components are created outside of Amazon ECS, and Amazon ECS is used to manage the deployment and operation of application containers on the cluster

![Users access containers in ECS through Application Load Balancer, with tasks pulling from ECR.](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/images/image5.png)

* Amazon ECS use case *

**Note**
Application infrastructure (including Amazon Elastic Container Registry (Amazon ECR) repositories, Amazon ECS configurations, and Load Balancers) is provisioned and managed outside of your Amazon ECS deployment.
 Amazon ECS manages the deployment of application containers running inside the Amazon ECS service as *tasks* that are sourced from a container registry like Amazon ECR.

 Amazon ECS supports multiple container instance types such as Linux and Windows, as well as external instance types such as an on-premises virtual machine (VM) with Amazon ECS Anywhere.

## Amazon ECS Anywhere
<a name="ecs-anywhere"></a>

 [Amazon ECS Anywhere](https://aws.amazon.com/ecs/anywhere/) allows you to run Amazon ECS tasks anywhere, whether it's on-premises or in other cloud environments. With Amazon ECS Anywhere, you can easily deploy and manage containerized applications across your hybrid infrastructure, while maintaining a consistent operational experience. The service works by extending the Amazon ECS platform to any environment, including on-premises data centers, remote offices, and other cloud environments. It enables you to use the same familiar Amazon ECS APIs and tooling to deploy and manage containers across all of your environments, without having to worry about the underlying infrastructure.

 Amazon ECS Anywhere uses the Amazon ECS agent to manage the deployment and lifecycle of containers, enabling you to use the same Amazon ECS task definitions and configuration files that you use in the AWS Cloud. This can help to simplify the process of deploying and managing containers across your hybrid infrastructure, and reduce the time and effort r equired for manual configuration and management.

 With Amazon ECS Anywhere, you can also leverage other AWS services, such as IAM, CloudFormation, and Amazon ECR, to manage your containerized applications. This can help to ensure that your applications are secure, compliant, and integrated with other AWS services.

![On-premises server with ECS Agent, SSM Agent, and containers connecting to Amazon ECS and Systems Manager.](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/images/image4-1.png)

## Amazon Elastic Container Service on AWS Outposts
<a name="ecs-on-outposts"></a>

 [Amazon ECS on AWS Outposts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-on-outposts.html) is a fully managed AWS service that enables you to run Amazon ECS tasks on-premises, using the same APIs and tooling that you use in the AWS Cloud. With Amazon ECS on AWS Outposts, you can deploy and manage containerized applications in a consistent and familiar way, whether you're running them on-premises or in the cloud. AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to your on-premises environments. With Amazon ECS on AWS Outposts, you can run Amazon ECS tasks on hardware that is dedicated to your organization, without having to worry about the underlying infrastructure. This can help to ensure that your applications are deployed in a secure and compliant manner, while also enabling you to take advantage of the flexibility and scalability of the cloud.

 Amazon ECS on AWS Outposts works by deploying a set of AWS services and APIs to your on-premises environment, which enables you to run Amazon ECS tasks on dedicated hardware. This includes the Amazon ECS agent, which manages the deployment and lifecycle of containers, and the AWS Outposts infrastructure, which provides a secure and compliant environment for running containerized applications. With Amazon ECS on AWS Outposts, you can use the same Amazon ECS APIs and tooling that you use in the AWS Cloud, making it easy to deploy and manage containerized applications in a consistent and familiar way. This can help to reduce the time and effort required for manual configuration and management, and improve consistency and reliability across your hybrid infrastructure. Amazon ECS on AWS Outposts also integrates with other AWS services, such as IAM, CloudFormation, and Amazon ECR, to manage your containerized applications. This can help to ensure that your applications are secure, compliant, and integrated with other AWS services.
