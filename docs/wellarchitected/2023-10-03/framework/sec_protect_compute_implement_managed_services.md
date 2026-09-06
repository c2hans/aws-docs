---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_protect_compute_implement_managed_services.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC06-BP03 Implement managed services
<a name="sec_protect_compute_implement_managed_services"></a>

 Implement services that manage resources, such as Amazon Relational Database Service (Amazon RDS), AWS Lambda, and Amazon Elastic Container Service (Amazon ECS), to reduce your security maintenance tasks as part of the shared responsibility model. For example, Amazon RDS helps you set up, operate, and scale a relational database, automates administration tasks such as hardware provisioning, database setup, patching, and backups. This means you have more free time to focus on securing your application in other ways described in the AWS Well-Architected Framework. Lambda lets you run code without provisioning or managing servers, so you only need to focus on the connectivity, invocation, and security at the code level–not the infrastructure or operating system.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Explore available services: Explore, test, and implement services that manage resources, such as Amazon RDS, AWS Lambda, and Amazon ECS.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Website ](https://aws.amazon.com/)
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
+  [Replacing a Bastion Host with Amazon EC2 Systems Manager](https://aws.amazon.com/blogs/mt/replacing-a-bastion-host-with-amazon-ec2-systems-manager/)
+  [Security Overview of AWS Lambda](https://pages.awscloud.com/rs/112-TZM-766/images/Overview-AWS-Lambda-Security.pdf)

 **Related videos:**
+  [Running high-security workloads on Amazon EKS](https://youtu.be/OWRWDXszR-4)
+  [Securing Serverless and Container Services](https://youtu.be/kmSdyN9qiXY)
+  [Security best practices for the Amazon EC2 instance metadata service](https://youtu.be/2B5bhZzayjI)

 **Related examples:**
+ [Lab: AWS Certificate Manager Request Public Certificate ](https://wellarchitectedlabs.com/security/200_labs/200_certificate_manager_request_public_certificate/)
