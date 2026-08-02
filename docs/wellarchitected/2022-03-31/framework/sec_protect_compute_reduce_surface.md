---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_compute_reduce_surface.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC06-BP02 Reduce attack surface
<a name="sec_protect_compute_reduce_surface"></a>

 Reduce your exposure to unintended access by hardening operating systems and minimizing the components, libraries, and externally consumable services in use. Start by reducing unused components, whether they are operating system packages or applications, for Amazon Elastic Compute Cloud (Amazon EC2)-based workloads, or external software modules in your code, for all workloads. You can find many hardening and security configuration guides for common operating systems and server software. For example, you can start with the [Center for Internet Security](https://www.cisecurity.org/) and iterate.

 In Amazon EC2, you can create your own Amazon Machine Images (AMIs), which you have patched and hardened, to help you meet the specific security requirements for your organization. The patches and other security controls you apply on the AMI are effective at the point in time in which they were created—they are not dynamic unless you modify after launching, for example, with AWS Systems Manager.

 You can simplify the process of building secure AMIs with EC2 Image Builder. EC2 Image Builder significantly reduces the effort required to create and maintain golden images without writing and maintaining automation. When software updates become available, Image Builder automatically produces a new image without requiring users to manually initiate image builds. EC2 Image Builder allows you to easily validate the functionality and security of your images before using them in production with AWS-provided tests and your own tests. You can also apply AWS-provided security settings to further secure your images to meet internal security criteria. For example, you can produce images that conform to the Security Technical Implementation Guide (STIG) standard using AWS-provided templates.

 Using third-party static code analysis tools, you can identify common security issues such as unchecked function input bounds, as well as applicable common vulnerabilities and exposures (CVEs). You can use [Amazon CodeGuru](https://aws.amazon.com/codeguru/) for supported languages. Dependency checking tools can also be used to determine whether libraries your code links against are the latest versions, are themselves free of CVEs, and have licensing conditions that meet your software policy requirements.

 Using Amazon Inspector, you can perform configuration assessments against your instances for known CVEs, assess against security benchmarks, and automate the notification of defects. Amazon Inspector runs on production instances or in a build pipeline, and it notifies developers and engineers when findings are present. You can access findings programmatically and direct your team to backlogs and bug-tracking systems. [EC2 Image Builder](https://aws.amazon.com/image-builder/) can be used to maintain server images (AMIs) with automated patching, AWS-provided security policy enforcement, and other customizations. When using containers implement [ECR Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in your build pipeline and on a regular basis against your image repository to look for CVEs in your containers.

 While Amazon Inspector and other tools are effective at identifying configurations and any CVEs that are present, other methods are required to test your workload at the application level. [Fuzzing](https://owasp.org/www-community/Fuzzing) is a well-known method of finding bugs using automation to inject malformed data into input fields and other areas of your application.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Harden operating system: Configure operating systems to meet best practices.
  +  [Securing Amazon Linux](https://www.cisecurity.org/benchmark/amazon_linux/)
  +  [Securing Microsoft Windows Server](https://www.cisecurity.org/benchmark/microsoft_windows_server/)
+  Harden containerized resources: Configure containerized resources to meet security best practices.
+  Implement AWS Lambda best practices.
  +  [AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
+  [Replacing a Bastion Host with Amazon EC2 Systems Manager](https://aws.amazon.com/blogs/mt/replacing-a-bastion-host-with-amazon-ec2-systems-manager/)
+  [Security Overview of AWS Lambda](https://pages.awscloud.com/rs/112-TZM-766/images/Overview-AWS-Lambda-Security.pdf)

 **Related videos:**
+  [Running high-security workloads on Amazon EKS](https://youtu.be/OWRWDXszR-4)
+  [Securing Serverless and Container Services](https://youtu.be/kmSdyN9qiXY)
+  [Security best practices for the Amazon EC2 instance metadata service](https://youtu.be/2B5bhZzayjI)

 **Related examples:**
+  [Lab: Automated Deployment of Web Application Firewall](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_Web_Application_Firewall/README.html)
