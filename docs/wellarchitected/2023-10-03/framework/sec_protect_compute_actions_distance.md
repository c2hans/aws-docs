---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_protect_compute_actions_distance.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC06-BP05 Enable people to perform actions at a distance
<a name="sec_protect_compute_actions_distance"></a>

 Removing the ability for interactive access reduces the risk of human error, and the potential for manual configuration or management. For example, use a change management workflow to deploy Amazon Elastic Compute Cloud (Amazon EC2) instances using infrastructure-as-code, then manage Amazon EC2 instances using tools such as AWS Systems Manager instead of allowing direct access or through a bastion host. AWS Systems Manager can automate a variety of maintenance and deployment tasks, using features including [automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) [workflows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html), [documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) (playbooks), and the [run command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html). AWS CloudFormation stacks build from pipelines and can automate your infrastructure deployment and management tasks without using the AWS Management Console or APIs directly.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Replace console access: Replace console access (SSH or RDP) to instances with AWS Systems Manager Run Command to automate management tasks.
+  [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
+  [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html)
+  [Replacing a Bastion Host with Amazon EC2 Systems Manager](https://aws.amazon.com/blogs/mt/replacing-a-bastion-host-with-amazon-ec2-systems-manager/)
+  [Security Overview of AWS Lambda](https://pages.awscloud.com/rs/112-TZM-766/images/Overview-AWS-Lambda-Security.pdf)

 **Related videos:**
+  [Running high-security workloads on Amazon EKS](https://youtu.be/OWRWDXszR-4)
+  [Securing Serverless and Container Services](https://youtu.be/kmSdyN9qiXY)
+  [Security best practices for the Amazon EC2 instance metadata service](https://youtu.be/2B5bhZzayjI)

 **Related examples:**
+  [Lab: Automated Deployment of Web Application Firewall](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_Web_Application_Firewall/README.html)
