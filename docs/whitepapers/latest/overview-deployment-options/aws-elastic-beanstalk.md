---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/aws-elastic-beanstalk.html
---

# AWS Elastic Beanstalk
<a name="aws-elastic-beanstalk"></a>

 [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, .NET Core, PHP, Node.js, Python, Ruby, Go, or Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. Elastic Beanstalk is a complete application management solution, and manages all infrastructure and platform tasks on your behalf.

 With Elastic Beanstalk, you can quickly deploy, manage, and scale applications without the operational burden of managing infrastructure. Elastic Beanstalk reduces management complexity for web applications, making it a good choice for organizations that are new to AWS or wish to deploy a web application as quickly as possible.

 When using Elastic Beanstalk as your deployment solution, simply upload your source code and Elastic Beanstalk will provision and operate all necessary infrastructure, including servers, databases, load balancers, networks, and auto scaling groups. Although these resources are created on your behalf, you retain full control of these resources, allowing developers to customize as needed. Elastic Beanstalk meets the criteria for ISO, PCI, SOC 1, SOC 2, and SOC 3 compliance along with the criteria for HIPAA eligibility. This means applications running on Elastic Beanstalk can process regulated financial data or protected health information (PHI).

* Table 2: AWS Elastic Beanstalk Deployment Features *

|  Capability  |  Description  |
| --- | --- |
|  Provision  |  Elastic Beanstalk will create all infrastructure components necessary to operate a web application or service that runs on one of its supported platforms. If you need additional infrastructure, this will have to be created outside of Elastic Beanstalk. <br /> Refer to [Elastic Beanstalk Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-all-platforms.html) for more details on the web application platforms supported by Elastic Beanstalk.  |
|  Configure  |  Elastic Beanstalk provides a wide range of options for customizing the resources in your environment. <br /> Refer to [Configuring Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers.html) environments for more information about customizing the resources that are created by Elastic Beanstalk.  |
|  Deploy  |  Elastic Beanstalk automatically handles application deployments, and creates an environment that runs a new version of your application without impacting existing users. <br /> Refer to [Deploying Applications to AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.deploy-existing-version.html) for more details on application deployments with Elastic Beanstalk.  |
|  Scale  |  Elastic Beanstalk uses Elastic Load Balancing and Auto Scaling to automatically scale your application in and out based on its specific needs. Multiple availability zones give you an option to improve application reliability and availability. <br /> Refer to [Auto Scaling Group for your Elastic Beanstalk Environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.as.html) for more details about auto scaling with Elastic Beanstalk.  |
|  Monitor  |  Elastic Beanstalk offers built-in environment monitoring for applications including deployment success/failures, environment health, resource performance, and application logs. <br /> Refer to [Monitoring an Environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-health.html) for more details on full-stack monitoring with Elastic Beanstalk.  |
|  Graviton support  |  AWS Graviton arm64-based processors deliver the best price performance for your cloud workloads running in Amazon EC2. With AWS Graviton on Elastic Beanstalk, you can select Amazon EC2 instance types to meet optimization needs of your workloads and benefit from improved price performance over a comparable x86-based processor.  |

 Elastic Beanstalk makes it easy for web applications to be quickly deployed and managed in AWS. The following example shows a general use case for Elastic Beanstalk as it is used to deploy a simple web application. All application infrastructure (including security groups, IAM roles, and CloudWatch alarms) is created and managed by Elastic Beanstalk. The Amazon EC2 instances are automatically provisioned with runtime environment and deployment packages. Elastic Beanstalk environments can integrate with resources like Amazon Relational Database Service (Amazon RDS) that are created outside of Elastic Beanstalk.

![Architecture diagram showing Elastic Beanstalk connecting to load balancer in public subnet and EC2 with RDS in private subnet.](http://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/images/image3.png)

* AWS Elastic Beanstalk use case *

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
