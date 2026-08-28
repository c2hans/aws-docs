---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/optimize-the-remote-desktop-experience.html
---

# Optimize the remote desktop experience
<a name="optimize-the-remote-desktop-experience"></a>

Designers typically use terminal-based SSH sessions or graphical remote desktops to submit and visualize workflows. A remote desktop offers GUI-driven interactive tools (such as layout, place, and route) for tool engineers and chip designers to submit jobs. AWS offers [Amazon DCV](https://docs.aws.amazon.com/dcv/#nice-dcv), which is a high-performance remote display protocol that provides a robust user interface for engineering and physical design teams. Amazon DCV performs well over varying network conditions.

Amazon DCV streams pixels and not geometries in order to help protect data privacy. In addition, Amazon DCV uses TLS to secure pixels and end-user inputs.

Using a connection file, users can instantly connect to a Amazon DCV session. However, note that the connection file parameters use the `password` and `proxypassword` fields without encryption. For more information, see [Using a connection file](https://docs.aws.amazon.com/dcv/latest/userguide/using-connection-file.html). Amazon DCV establishes a TLS connection between the server and client. A validation policy in the connection file determines how the client responds when a certificate can't be verified as trustworthy. For more information, see [Set certificate validation policy](https://docs.aws.amazon.com/dcv/latest/userguide/set-certificate-validation-policy.html).

Other on-premises commercial solutions that provide remote desktop functionality include [NoMachine](https://www.nomachine.com/) or [OpenText Exceed TurboX](https://www.opentext.com/products-and-solutions/products/specialty-technologies/connectivity/opentext-exceed-turbox).

With any remote desktop solution, the underlying infrastructure is powered by Amazon Elastic Compute Cloud (Amazon EC2). According to the shared responsibility model, your responsibility includes the following areas to help secure remote desktop instances:
+ Controlling network access to your instances, such as by configuring your VPC and security groups. For more information, see [Controlling network traffic](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/infrastructure-security.html#control-network-traffic).
+ Managing the credentials used to connect to your instances.
+ Managing the guest operating system and software deployed to the guest operating system, including updates and security patches. For more information, see [Update management in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/update-management.html).
+ Configuring the IAM roles that are attached to the instance and the permissions associated with those roles. For more information, see [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
