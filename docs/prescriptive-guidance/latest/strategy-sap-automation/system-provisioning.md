---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/system-provisioning.html
---

# Example: Automating system provisioning
<a name="system-provisioning"></a>

*System provisioning* is the process of setting up infrastructure in the cloud, including establishing user, system, and service access to the applications, data, and cloud resources. The benefits of automatic system provisioning are:
+ Reduced human errors during the deployment
+ Consistent, reproducible, and auditable provisioning
+ Scalability of infrastructure
+ Reduced time and cost of provisioning

There are number of approaches for automating system provisioning. This guide dives deeper into two options, AWS Launch Wizard and infrastructure as code (IaC).

## Launch Wizard
<a name="launch-wizard"></a>

Using Launch Wizard to automatically provision systems reduces the amount of time it takes to deploy SAP applications in the cloud. You input your application requirements on the service console, including SAP HANA settings, SAP landscape settings, and deployment details. Launch Wizard identifies the appropriate AWS resources to support the application and estimates the cost of deployment. You can modify the resources and instantly view the updated, estimated cost. You can also deploy the resources to operate your SAP application directly from Launch Wizard. For more information, see [AWS Launch Wizard for SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap.html).

The following image and process explains, at a high level, how you use Launch Wizard to identify, estimate, and launch the AWS resources needed to support your SAP application:

1. In Launch Wizard, from a catalog of applications, you choose which to deploy.

1. You enter the application specifications.

1. Launch Wizard recommends the AWS resources for the application and provides a cost estimate.

1. When you approve, Launch Wizard provisions the selected resources on AWS.

1. Launch Wizard configures the high availability solution and creates code templates for future use.

1. Launch Wizard creates a ready-to-use application that is integrated with AWS management and monitoring services.

![Process diagram explaining the high-level steps of how to use AWS Launch Wizard.](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/images/guide-img/029e7e61-9fe5-41b5-83f4-177d03384b91/images/b9f69ada-a04d-4dfa-9b49-2fa5968e3dc6.png)

## Infrastructure as code
<a name="iac"></a>

Another way to automatically provision systems and reduce the time required to deploy SAP applications is to use infrastructure as code. *Infrastructure as code* is a practice in which you use code and software development techniques, such as version control and continuous integration, to provision and manage infrastructure. The AWS Cloud offers an application programming interface (API)-driven model that enables developers and system administrators to interact with infrastructure programmatically at scale, instead of manually setting up and configuring resources. Because the resources and services are defined as code, you can quickly use standardized patterns to deploy infrastructure and servers with the latest patches and versions, and you can duplicate resources in repeatable ways. For more information, see the blog post [Terraform your SAP Infrastructure on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/).
