---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/understanding-the-security-scope.html
---

# Understanding the security scope
<a name="understanding-the-security-scope"></a>

The AWS shared responsibility model defines how you share responsibility with AWS for security and compliance in the cloud. AWS secures the infrastructure that runs all of the services offered in the AWS Cloud, and you are responsible for securing your use of those services, such as your data and applications.

This shared model can help relieve your compliance and operational burden because AWS operates, manages, and controls many components, from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. Managed services help you reduce your security and compliance obligations by allowing AWS to manage some security tasks, such as patching and vulnerability management. Using managed services is a best practice in the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a4.html). In general, as infrastructure is modernized, more responsibility is shifted onto the service provider.

The following are three different service examples to help you understand how your security scope changes based on which services you choose:
+ [Infrastructure services](#infrastructure-services)
+ [Container services](#container-services)
+ [Serverless services](#serverless-services)

Your responsibility for security is not static, and it changes with the type of architecture that you select. Your time, effort, and costs are affected by the cloud architecture you choose.

## Infrastructure services
<a name="infrastructure-services"></a>

For infrastructure services, AWS focuses on securing the underlying infrastructure. Within infrastructure services, the scope is larger for the customer because they need to address platform security, OS patching, and application management, as compared to the other models. Amazon Elastic Compute Cloud (Amazon EC2) is an example of a common infrastructure service.

![AWS shared responsibility model for infrastructure services.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/4162f88e-cb6f-4190-8eb3-5e4d55aa6ea8.png)

## Container services
<a name="container-services"></a>

As the infrastructure becomes more abstracted and modernized, the footprint becomes smaller. Your scope shrinks because responsibility for some security elements shifts to AWS. Container services is an example which some of the backend responsibilities shift back to AWS. For example, AWS becomes responsible for the operating system (OS) configuration, network configuration, platform management, and application management. Examples of common container services include Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Container Registry (Amazon ECR), Amazon Elastic Container Service (Amazon ECS), and AWS Fargate.

![AWS shared responsibility model for container services.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/8501bac7-1e8e-4865-acd4-34d04583573b.png)

## Serverless services
<a name="serverless-services"></a>

When using serverless services, nearly all of the responsibility for security belongs to AWS. The scope of your responsibility is minimal. For example, a managed serverless database (DB) eliminates the need for you to secure the network, hardware, and operating system. All OS and DB patching is covered by AWS. Your only concern is securing access to the data through encryption and authentication.

![AWS shared responsibility model for serverless services.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/32ec276a-3f72-4233-bdf9-e7f6eeae201d.png)
