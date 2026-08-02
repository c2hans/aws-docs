---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/applying-e8-framework.html
---

# Reinterpreting the Essential Eight strategies
<a name="applying-e8-framework"></a>

The following are the original Essential Eight mitigation strategies that were designed for Microsoft-based internet-connected networks:
+ Application control
+ Patch applications
+ Configure Microsoft Office macro settings
+ User application hardening
+ Restrict administrative privileges
+ Patch operating systems
+ Multi-factor authentication
+ Regular backups

It is important to reiterate that the Essential Eight framework is not designed for cloud environments. However, the underlying principles are applicable, and there is overlap between the Essential Eight strategies and AWS Well-Architected Framework best practices.

Various cloud-native approaches can improve security and dramatically reduce your compliance burden. In on-premises environments, you are responsible for all aspects of security, and there are no inherited controls. When running workloads in the cloud, AWS is responsible for protecting the infrastructure that runs our services. You can also reduce your compliance burden by using automation and managed services. *Managed services*, also known as *abstracted services*, are AWS services for which AWS operates the infrastructure layer, the operating system, and platforms, and you access the endpoints to store and retrieve data. Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB are examples of managed services. For more information, see the [Theme 1: Use managed services](theme-1.md) section in this guide.

Therefore, some reinterpretation is required to make the Essential Eight strategies appropriate for workloads on AWS. This guide converts the Essential Eight strategies into AWS *themes*.

## Using the themes
<a name="using-themes"></a>

This guide is divided into eight themes. Each Essential Eight strategy is mapped to one or more of the following themes, and each theme is mapped to one or more best practices in the AWS Well-Architected Framework:
+ [Theme 1: Use managed services](theme-1.md)
+ [Theme 2: Manage immutable infrastructure through secure pipelines](theme-2.md)
+ [Theme 3: Manage mutable infrastructure with automation](theme-3.md)
+ [Theme 4: Manage identities](theme-4.md)
+ [Theme 5: Establish a data perimeter](theme-5.md)
+ [Theme 6: Automate backups](theme-6.md)
+ [Theme 7: Centralise logging and monitoring](theme-7.md)
+ [Theme 8: Implement mechanisms for manual processes](theme-8.md)

Each theme includes an overview of the topic, related AWS Well-Architected Framework best practices, and instructions for how to achieve Essential Eight maturity and monitor compliance. The instructions provide manual steps or help you configure automations by using [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html). Manual steps require mechanisms to make sure that findings are addressed. For more information, see [Theme 8: Implement mechanisms for manual processes](theme-8.md). AWS Config rules require similar oversight or automation in order to [remediate noncompliant resources](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html). By following the guidance aligned with these themes, you can reach Essential Eight maturity with an approach that also maximises cloud benefits.

## Reinterpreting the Essential Eight strategies for the cloud
<a name="reinterpreting-e8-strategies"></a>

Because the Essential Eight framework is not designed for cloud environments, it is essential to take a cloud-native approach when addressing the underlying principles of each Essential Eight strategy. The approach varies depending on two key questions.

### Which services are you using?
<a name="which-services-are-you-using-.ba80ebf7-a2f1-5b22-ae12-dd86260549d8"></a>

The [AWS shared responsibility model](australian-sec-compliance.md#shared-model) can help relieve your compliance and operational burdens. Managed services shift more responsibility to AWS for maintaining the availability, performance, and security optimisation of the deployed service. Managed services also remove the operational and administrative burden of maintaining a service, providing more time to focus on innovation.

Managed services include serverless services, such as [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), and [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html). A database on [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) requires less operational responsibility than a database on [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/?icmpid=docs_homepage_compute).

For example, if you're adapting the *Patch operating systems* Essential Eight strategy for the cloud, you need consider which services you are using and whether you're responsible for patching those resources. AWS is responsible for patching fully managed services, such as Lambda and DynamoDB. For other services, such as Amazon RDS or [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html), you might need to manage patches during maintenance windows.

### What deployment model are you using?
<a name="what-deployment-model-are-you-using-.bff79cf8-1bc9-5cb6-9f4a-6f1770fb0712"></a>

Is your organization using a mutable or immutable infrastructure approach?

The *mutable infrastructure* model updates and modifies the existing infrastructure for production workloads.** **This was the standard deployment method before the cloud, when replacing server infrastructure was so costly and time-consuming that the most practical approach was to apply changes to servers already in production. An example of a mutable approach in the cloud is deploying application changes directly onto running EC2 instances, either manually or by using a software deployment service, such as [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) or [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html).

The *immutable infrastructure* model deploys new infrastructure for production workloads instead of updating, patching, or modifying the existing infrastructure. An example of an immutable approach is defining an application stack in [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html). You can use these services to deploy an application stack through continuous integration and continuous delivery (CI/CD) pipelines. This approach uses [deployment methods](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html) such as *rolling* or *blue/green*. For more information about this approach, see the [Deploy using immutable infrastructure](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.html) best practice in the AWS Well-Architected Framework.

For example, if you're adapting the *Patch operating systems* Essential Eight strategy for the cloud, you need consider how patching applies to the deployment model. For mutable infrastructure, you can manually patch resources or could improve operational efficiency through automation. If you're using immutable infrastructure, then you'd use a CI/CD pipeline to deploy new infrastructure with the latest version of the operating system. In fact, the term *patching* is a misnomer under this model because the infrastructure would be replaced rather than patched.
