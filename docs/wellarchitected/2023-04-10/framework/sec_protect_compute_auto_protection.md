---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_protect_compute_auto_protection.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC06-BP04 Automate compute protection
<a name="sec_protect_compute_auto_protection"></a>

 Automate your protective compute mechanisms including vulnerability management, reduction in attack surface, and management of resources. The automation will help you invest time in securing other aspects of your workload, and reduce the risk of human error.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Automate configuration management: Enforce and validate secure configurations automatically by using a configuration management service or tool.
  +  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
  +  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
  +  [Lab: Automated deployment of VPC](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_VPC/README.html)
  +  [Lab: Automated deployment of EC2 web application](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_EC2_Web_Application/README.html)
+  Automate patching of Amazon Elastic Compute Cloud (Amazon EC2) instances: AWS Systems Manager Patch Manager automates the process of patching managed instances with both security-related and other types of updates. You can use Patch Manager to apply patches for both operating systems and applications.
  +  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
  +  [Centralized multi-account and multi-Region patching with AWS Systems Manager Automation](https://aws.amazon.com/blogs/mt/centralized-multi-account-and-multi-region-patching-with-aws-systems-manager-automation/)
+  Implement intrusion detection and prevention: Implement an intrusion detection and prevention tool to monitor and stop malicious activity on instances.
+  Consider AWS Partner solutions: AWS Partners offer hundreds of industry-leading products that are equivalent, identical to, or integrate with existing controls in your on-premises environments. These products complement the existing AWS services to allow you to deploy a comprehensive security architecture and a more seamless experience across your cloud and on-premises environments.
  +  [Infrastructure security](https://aws.amazon.com/security/partner-solutions/#infrastructure_security)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
+  [Centralized multi-account and multi-region patching with AWS Systems Manager Automation](https://aws.amazon.com/blogs/mt/centralized-multi-account-and-multi-region-patching-with-aws-systems-manager-automation/)
+  [Infrastructure security](https://aws.amazon.com/security/partner-solutions/#infrastructure_security)
+  [Replacing a Bastion Host with Amazon EC2 Systems Manager](https://aws.amazon.com/blogs/mt/replacing-a-bastion-host-with-amazon-ec2-systems-manager/)
+  [Security Overview of AWS Lambda](https://pages.awscloud.com/rs/112-TZM-766/images/Overview-AWS-Lambda-Security.pdf)

 **Related videos:**
+  [Running high-security workloads on Amazon EKS](https://youtu.be/OWRWDXszR-4)
+  [Securing Serverless and Container Services](https://youtu.be/kmSdyN9qiXY)
+  [Security best practices for the Amazon EC2 instance metadata service](https://youtu.be/2B5bhZzayjI)

 **Related examples:**
+  [Lab: Automated Deployment of Web Application Firewall](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_Web_Application_Firewall/README.html)
+  [Lab: Automated deployment of Amazon EC2 web application](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_EC2_Web_Application/README.html)
